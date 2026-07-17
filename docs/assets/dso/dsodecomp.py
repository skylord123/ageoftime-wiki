#!/usr/bin/env python3
"""
dsodecomp.py - decompiler for Age of Time / Torque Game Engine ".dso" files.

A .dso is the compiled bytecode the TGE console (TorqueScript) VM executes. This
tool reads a .dso, disassembles its bytecode, and reconstructs a ".cs" source
file that compiles back to equivalent bytecode and behaves the same as the .dso.

Age of Time uses DSO bytecode **version 33** (a custom TGE 1.x fork). See
DSO-FORMAT.md for the reverse-engineered container + opcode spec.

Usage:
    python3 dsodecomp.py FILE.cs.dso              # write FILE.cs next to the dso
    python3 dsodecomp.py FILE.cs.dso -o OUT.cs    # write to a specific path
    python3 dsodecomp.py FILE.cs.dso --stdout     # print source to the terminal
    python3 dsodecomp.py FILE.cs.dso --disasm     # print raw disassembly (debug)
    python3 dsodecomp.py DIR                       # recurse, decompile every *.dso

No third-party dependencies - standard library only. The logic is kept simple
and dependency-free so it can later be ported to JavaScript for an in-browser
decompiler on the wiki.
"""

import argparse
import os
import struct
import sys

DSO_VERSION = 33
STRING_TAG_PREFIX_BYTE = 0x01

# ---------------------------------------------------------------------------
# Opcodes (TorqueScript VM). Order == numeric value.
#
# This is AoT's DSO v33 layout, which differs from stock TGE 1.4 (v36): three
# extra opcodes (never emitted by the script compiler) are present, so every
# stock opcode is shifted up. They were located empirically: an enum that puts
# them at values 2, 3 and 72 disassembles all 184 shipped .dso files cleanly
# (every StringTableEntry operand lands on an ident-table entry, every jump
# lands on an instruction boundary). Stock opcode N maps to: N (N<=1),
# N+2 (2<=N<=69), N+3 (N>=70). See DSO-FORMAT.md.
# ---------------------------------------------------------------------------
OPCODES = [
    "OP_FUNC_DECL",
    "OP_CREATE_OBJECT",
    "OP_UNUSED_2",            # custom AoT opcode, never emitted by the compiler
    "OP_UNUSED_3",            # custom AoT opcode, never emitted by the compiler
    "OP_ADD_OBJECT",
    "OP_END_OBJECT",
    "OP_JMPIFFNOT",
    "OP_JMPIFNOT",
    "OP_JMPIFF",
    "OP_JMPIF",
    "OP_JMPIFNOT_NP",
    "OP_JMPIF_NP",
    "OP_JMP",
    "OP_RETURN",
    "OP_CMPEQ",
    "OP_CMPGR",
    "OP_CMPGE",
    "OP_CMPLT",
    "OP_CMPLE",
    "OP_CMPNE",
    "OP_XOR",
    "OP_MOD",
    "OP_BITAND",
    "OP_BITOR",
    "OP_NOT",
    "OP_NOTF",
    "OP_ONESCOMPLEMENT",
    "OP_SHR",
    "OP_SHL",
    "OP_AND",
    "OP_OR",
    "OP_ADD",
    "OP_SUB",
    "OP_MUL",
    "OP_DIV",
    "OP_NEG",
    "OP_SETCURVAR",
    "OP_SETCURVAR_CREATE",
    "OP_SETCURVAR_ARRAY",
    "OP_SETCURVAR_ARRAY_CREATE",
    "OP_LOADVAR_UINT",
    "OP_LOADVAR_FLT",
    "OP_LOADVAR_STR",
    "OP_SAVEVAR_UINT",
    "OP_SAVEVAR_FLT",
    "OP_SAVEVAR_STR",
    "OP_SETCUROBJECT",
    "OP_SETCUROBJECT_NEW",
    "OP_SETCURFIELD",
    "OP_SETCURFIELD_ARRAY",
    "OP_LOADFIELD_UINT",
    "OP_LOADFIELD_FLT",
    "OP_LOADFIELD_STR",
    "OP_SAVEFIELD_UINT",
    "OP_SAVEFIELD_FLT",
    "OP_SAVEFIELD_STR",
    "OP_STR_TO_UINT",
    "OP_STR_TO_FLT",
    "OP_STR_TO_NONE",
    "OP_FLT_TO_UINT",
    "OP_FLT_TO_STR",
    "OP_FLT_TO_NONE",
    "OP_UINT_TO_FLT",
    "OP_UINT_TO_STR",
    "OP_UINT_TO_NONE",
    "OP_LOADIMMED_UINT",
    "OP_LOADIMMED_FLT",
    "OP_TAG_TO_STR",
    "OP_LOADIMMED_STR",
    "OP_LOADIMMED_IDENT",
    "OP_CALLFUNC_RESOLVE",
    "OP_CALLFUNC",
    "OP_UNUSED_72",           # custom AoT opcode, never emitted by the compiler
    "OP_ADVANCE_STR",
    "OP_ADVANCE_STR_APPENDCHAR",
    "OP_ADVANCE_STR_COMMA",
    "OP_ADVANCE_STR_NUL",
    "OP_REWIND_STR",
    "OP_TERMINATE_REWIND_STR",
    "OP_COMPARE_STR",
    "OP_PUSH",
    "OP_PUSH_FRAME",
    "OP_BREAK",
    "OP_INVALID",
]
OP = {name: i for i, name in enumerate(OPCODES)}

# Number of fixed code words consumed AFTER the opcode word. OP_FUNC_DECL is
# variable-length (6 + argc) and handled specially in the disassembler.
FIXED_OPERANDS = {
    "OP_CREATE_OBJECT": 3,
    "OP_ADD_OBJECT": 1,
    "OP_END_OBJECT": 1,
    "OP_JMPIFFNOT": 1, "OP_JMPIFNOT": 1, "OP_JMPIFF": 1, "OP_JMPIF": 1,
    "OP_JMPIFNOT_NP": 1, "OP_JMPIF_NP": 1, "OP_JMP": 1,
    "OP_SETCURVAR": 1, "OP_SETCURVAR_CREATE": 1,
    "OP_SETCURFIELD": 1,
    "OP_LOADIMMED_UINT": 1, "OP_LOADIMMED_FLT": 1,
    "OP_TAG_TO_STR": 1, "OP_LOADIMMED_STR": 1, "OP_LOADIMMED_IDENT": 1,
    "OP_CALLFUNC_RESOLVE": 3, "OP_CALLFUNC": 3,
    "OP_ADVANCE_STR_APPENDCHAR": 1,
}

# Which operand words are StringTableEntry references (resolved through the
# ident table, not the inline string table). Index is the operand position
# AFTER the opcode word.
STE_OPERANDS = {
    "OP_CREATE_OBJECT": [0],          # parent object name
    "OP_SETCURVAR": [0],
    "OP_SETCURVAR_CREATE": [0],
    "OP_SETCURFIELD": [0],
    "OP_LOADIMMED_IDENT": [0],
    "OP_CALLFUNC": [0, 1],            # funcName, namespace
    "OP_CALLFUNC_RESOLVE": [0, 1],
}

CALL_FUNCTION = 0
CALL_METHOD = 1
CALL_PARENT = 2


# ---------------------------------------------------------------------------
# Binary stream reader
# ---------------------------------------------------------------------------
class Reader:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def u8(self):
        v = self.data[self.pos]
        self.pos += 1
        return v

    def u32(self):
        v = struct.unpack_from("<I", self.data, self.pos)[0]
        self.pos += 4
        return v

    def f64(self):
        v = struct.unpack_from("<d", self.data, self.pos)[0]
        self.pos += 8
        return v

    def bytes(self, n):
        v = self.data[self.pos:self.pos + n]
        self.pos += n
        return v


# ---------------------------------------------------------------------------
# DSO container
# ---------------------------------------------------------------------------
class StringTable:
    """A packed blob of NUL-terminated strings, indexed by byte offset."""
    def __init__(self, blob):
        self.blob = blob

    def get(self, offset):
        end = self.blob.find(b"\x00", offset)
        if end < 0:
            end = len(self.blob)
        return self.blob[offset:end]

    def get_str(self, offset):
        return self.get(offset).decode("latin-1")


class CodeBlock:
    def __init__(self):
        self.version = 0
        self.global_strings = StringTable(b"")
        self.function_strings = StringTable(b"")
        self.global_floats = []
        self.function_floats = []
        self.code = []            # list of U32
        self.code_size = 0
        self.line_break_pairs = []
        # ip -> StringTableEntry (decoded string) from the ident table
        self.idents = {}

    @classmethod
    def load(cls, data):
        cb = cls()
        r = Reader(data)
        cb.version = r.u32()

        # NOTE: v33 groups the tables global-then-function:
        #   globalStrings, globalFloats, functionStrings, functionFloats
        # (TGE 1.4 / v36 instead interleaves them str,str,flt,flt.)
        size = r.u32()
        global_size = size
        cb.global_strings = StringTable(r.bytes(size) if size else b"")

        size = r.u32()
        cb.global_floats = [r.f64() for _ in range(size)]

        size = r.u32()
        cb.function_strings = StringTable(r.bytes(size) if size else b"")

        size = r.u32()
        cb.function_floats = [r.f64() for _ in range(size)]

        code_size = r.u32()
        line_break_pair_count = r.u32()
        cb.code_size = code_size

        code = [0] * (code_size + line_break_pair_count * 2)
        for i in range(code_size):
            b = r.u8()
            code[i] = r.u32() if b == 0xFF else b
        for i in range(code_size, code_size + line_break_pair_count * 2):
            code[i] = r.u32()
        cb.code = code
        cb.line_break_pairs = code[code_size:]

        # Ident table: patch in StringTableEntry references.
        ident_count = r.u32()
        for _ in range(ident_count):
            offset = r.u32()
            ste = (cb.global_strings.get_str(offset)
                   if offset < global_size else "")
            count = r.u32()
            for _ in range(count):
                ip = r.u32()
                cb.idents[ip] = ste

        cb.trailing = len(data) - r.pos
        return cb


# ---------------------------------------------------------------------------
# Disassembler
# ---------------------------------------------------------------------------
class Instr:
    __slots__ = ("ip", "op", "operands")

    def __init__(self, ip, op, operands):
        self.ip = ip          # code index of the opcode word
        self.op = op          # opcode name
        self.operands = operands  # list of raw U32 operand words

    def __repr__(self):
        return "%-6d %-26s %s" % (self.ip, self.op, self.operands)


def disassemble(cb):
    """Return (instrs, by_ip) for the executable code region."""
    instrs = []
    by_ip = {}
    code = cb.code
    ip = 0
    n = cb.code_size
    while ip < n:
        opcode = code[ip]
        if opcode >= len(OPCODES):
            raise ValueError("bad opcode %d at ip %d" % (opcode, ip))
        name = OPCODES[opcode]
        start = ip
        ip += 1
        if name == "OP_FUNC_DECL":
            # name, ns, package, hasBody, endip, argc, then argc arg-name STEs
            fixed = code[ip:ip + 6]
            argc = code[ip + 5]
            operands = code[ip:ip + 6 + argc]
            ip += 6 + argc
        else:
            k = FIXED_OPERANDS.get(name, 0)
            operands = code[ip:ip + k]
            ip += k
        instr = Instr(start, name, operands)
        instrs.append(instr)
        by_ip[start] = instr
    return instrs, by_ip


# ---------------------------------------------------------------------------
# Disassembly pretty-printer (debug aid)
# ---------------------------------------------------------------------------
def format_disasm(cb):
    instrs, _ = disassemble(cb)
    # figure out which code region (global vs function) each ip is in
    fn_ranges = []
    for ins in instrs:
        if ins.op == "OP_FUNC_DECL":
            end = ins.operands[4]
            fn_ranges.append((ins.ip, end))

    def in_fn(ip):
        return any(a <= ip < b for a, b in fn_ranges)

    lines = []
    lines.append("; DSO version %d, code_size=%d, %d global strings bytes, "
                 "%d func string bytes, %d/%d floats"
                 % (cb.version, cb.code_size, len(cb.global_strings.blob),
                    len(cb.function_strings.blob),
                    len(cb.global_floats), len(cb.function_floats)))
    for ins in instrs:
        ann = annotate(cb, ins, in_fn(ins.ip))
        lines.append("%-7d %-26s %-22s %s"
                     % (ins.ip, ins.op,
                        " ".join(str(o) for o in ins.operands), ann))
    return "\n".join(lines)


def annotate(cb, ins, in_fn):
    strings = cb.function_strings if in_fn else cb.global_strings
    floats = cb.function_floats if in_fn else cb.global_floats
    op = ins.op
    o = ins.operands
    if op in ("OP_SETCURVAR", "OP_SETCURVAR_CREATE", "OP_SETCURFIELD",
              "OP_LOADIMMED_IDENT", "OP_CREATE_OBJECT"):
        return "; %r" % cb.idents.get(ins.ip + 1, "")
    if op in ("OP_CALLFUNC", "OP_CALLFUNC_RESOLVE"):
        fn = cb.idents.get(ins.ip + 1, "")
        ns = cb.idents.get(ins.ip + 2, "")
        ct = {0: "func", 1: "method", 2: "parent"}.get(o[2], o[2])
        return "; %s%s%s [%s]" % (ns, "::" if ns else "", fn, ct)
    if op in ("OP_LOADIMMED_STR", "OP_TAG_TO_STR"):
        return "; %r" % strings.get_str(o[0])
    if op == "OP_LOADIMMED_FLT":
        return "; %s" % (floats[o[0]] if o[0] < len(floats) else "?")
    if op == "OP_ADVANCE_STR_APPENDCHAR":
        return "; %r" % chr(o[0])
    if op == "OP_FUNC_DECL":
        fn = cb.idents.get(ins.ip + 1, "")
        ns = cb.idents.get(ins.ip + 2, "")
        args = [cb.idents.get(ins.ip + 7 + i, "") for i in range(o[5])]
        return "; %s%s%s(%s) end=%d body=%d" % (
            ns, "::" if ns else "", fn, ", ".join(args), o[4], o[3])
    return ""


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def default_output_path(path, disasm):
    if disasm:
        return path + ".disasm"
    # strip the trailing .dso: foo.cs.dso -> foo.cs
    return path[:-4] if path.lower().endswith(".dso") else path + ".cs"


def decompile_file(path, out=None, to_stdout=False, disasm=False, quiet=False,
                   force=False):
    with open(path, "rb") as fh:
        data = fh.read()
    cb = CodeBlock.load(data)
    if cb.version != DSO_VERSION and not quiet:
        print("warning: %s is DSO version %d (expected %d)"
              % (path, cb.version, DSO_VERSION), file=sys.stderr)

    text = format_disasm(cb) if disasm else decompile(cb)

    if to_stdout:
        print(text)
        return
    if out is None:
        out = default_output_path(path, disasm)
    # Don't silently clobber an existing file (e.g. the original .cs source
    # sitting next to a foo.cs.dso) unless asked to.
    if os.path.exists(out) and not force:
        raise RuntimeError("refusing to overwrite existing %s (use --force, "
                           "-o OTHER, or --stdout)" % out)
    with open(out, "w") as fh:
        fh.write(text + "\n")
    if not quiet:
        print("wrote %s" % out)


# ===========================================================================
# Decompiler
#
# TorqueScript's VM is a stack machine. We reconstruct source by symbolically
# executing the bytecode over expression "stacks" (mirroring the engine's
# string / numeric stacks), and by recovering control flow from the jump
# targets. The compiler's exact emission patterns (engine astNodes.cc) are the
# inverse map we invert here.
# ===========================================================================

# Source-operator precedence (higher binds tighter). Used to add parens.
P_ATOM = 100
P_UNARY = 90
P_MULT = 80      # * / %
P_ADD = 70       # + -
P_SHIFT = 60     # << >>
P_REL = 50       # < > <= >=
P_EQ = 45        # == != $= !$=
P_BAND = 42; P_BXOR = 40; P_BOR = 38
P_AND = 30       # &&
P_OR = 25        # ||
P_TERNARY = 20   # ?:
P_CAT = 15       # @ SPC TAB NL
P_ASSIGN = 12    # = += ...
P_COMMA = 8      # , (array comma-cat)


class Expr:
    __slots__ = ("t", "p", "ident", "array")

    def __init__(self, text, prec=P_ATOM, ident=False, array=None):
        self.t = text
        self.p = prec
        self.ident = ident      # produced by OP_LOADIMMED_IDENT (bareword)
        self.array = array      # (base_text, index_expr) when this is an array var

    def paren(self, min_prec):
        return self.t if self.p >= min_prec else "(" + self.t + ")"

    def __repr__(self):
        return "Expr(%r)" % self.t


def fmt_float(v):
    if v == int(v) and abs(v) < 1e15:
        return str(int(v))
    return repr(v)


def quote_str(s):
    out = ['"']
    for ch in s:
        if ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\t":
            out.append("\\t")
        elif ch == "\r":
            out.append("\\r")
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def quote_tagged(s):
    return "'" + s.replace("'", "\\'") + "'"


class Scope:
    """Decompiles one code region (top-level or a single function body)."""

    def __init__(self, cb, instrs, idx_of_ip, lo, hi, in_function):
        self.cb = cb
        self.I = instrs
        self.idx_of_ip = idx_of_ip
        self.lo = lo
        self.hi = hi               # exclusive instruction index
        self.strings = cb.function_strings if in_function else cb.global_strings
        self.floats = cb.function_floats if in_function else cb.global_floats
        # symbolic stacks
        self.nstack = []           # numeric (uint+float unified)
        self.cur = None            # current string value (Expr or None)
        self.saved = []            # [(Expr_or_None, sep)] string start stack
        self.frames = []           # [[arg Expr,...]] open call frames
        self.cur_var = None
        self.cur_obj = None        # Expr or "NEW"
        self.cur_field = None
        self.cur_field_array = None
        # control flow
        self.loops = {}            # guard/do-head idx -> loop info
        self.do_heads = {}
        self.break_ip = []         # stack of loop break ips
        self.continue_ip = []
        self._find_loops()

    # -- helpers ----------------------------------------------------------
    def ste(self, ip):
        return self.cb.idents.get(ip, "")

    def target_idx(self, ins):
        return self.idx_of_ip[ins.operands[0]]

    def _find_loops(self):
        I = self.I
        for j in range(self.lo, self.hi):
            ins = I[j]
            if ins.op in ("OP_JMPIF", "OP_JMPIFF"):
                tgt = ins.operands[0]
                if tgt < ins.ip:               # backward => loop bottom
                    top_idx = self.idx_of_ip.get(tgt)
                    if top_idx is None:
                        continue
                    break_ip = ins.ip + 2
                    guard_idx = top_idx - 1
                    info = {"bottom": j, "L": top_idx, "break_ip": break_ip}
                    if (guard_idx >= self.lo
                            and I[guard_idx].op in ("OP_JMPIFNOT", "OP_JMPIFFNOT")
                            and I[guard_idx].operands[0] == break_ip):
                        info["kind"] = "while"
                        self.loops[guard_idx] = info
                    else:
                        info["kind"] = "do"
                        self.do_heads[top_idx] = info

    # -- statement emission ----------------------------------------------
    def decompile(self, base_indent=0):
        lines = []
        self._block(self.lo, self.hi, lines, base_indent)
        return lines

    def _emit(self, lines, indent, text):
        lines.append("    " * indent + text)

    def at_boundary(self):
        return (not self.nstack and self.cur is None and not self.saved
                and not self.frames)

    def pop_value(self):
        """Pop the single pending value (numeric or string)."""
        if self.cur is not None:
            v = self.cur
            self.cur = None
            return v
        if self.nstack:
            return self.nstack.pop()
        return Expr("")

    # -- core block walker ------------------------------------------------
    def _block(self, lo, hi, lines, indent):
        i = lo
        while i < hi:
            ins = self.I[i]
            op = ins.op

            # implicit trailing RETURN of the whole scope: drop it
            if op == "OP_RETURN" and i == self.hi - 1 and self.at_boundary():
                i += 1
                continue

            if i in self.loops:                      # while / for head
                i = self._do_while_loop(i, lines, indent)
                continue
            if i in self.do_heads:                   # do { } while
                i = self._do_do_loop(i, lines, indent)
                continue

            if op in ("OP_JMPIFNOT", "OP_JMPIFFNOT"):
                i = self._do_if(i, lines, indent)
                continue

            if op == "OP_JMP":
                tgt = ins.operands[0]
                if self.break_ip and tgt == self.break_ip[-1]:
                    self._emit(lines, indent, "break;")
                elif self.continue_ip and tgt == self.continue_ip[-1]:
                    self._emit(lines, indent, "continue;")
                # else: an internal jump we don't model; ignore
                i += 1
                continue

            if op == "OP_RETURN":
                val = self.pop_value()
                if val is not None and val.t != "":
                    self._emit(lines, indent, "return %s;" % val.t)
                else:
                    self._emit(lines, indent, "return;")
                i += 1
                continue

            # otherwise a normal value/statement instruction
            i = self._step(i, lines, indent)
        return i

    def _do_if(self, i, lines, indent):
        ins = self.I[i]
        cond = self.pop_value()
        tdx = self.target_idx(ins)
        # else?  instruction just before the target is JMP -> E (E > target).
        # But a trailing JMP that targets an enclosing loop's break/continue
        # point is a break/continue inside the if-block, not an else-skip.
        prev = self.I[tdx - 1]
        loop_targets = set(self.break_ip) | set(self.continue_ip)
        if (prev.op == "OP_JMP" and prev.operands[0] > ins.operands[0]
                and prev.operands[0] not in loop_targets):
            edx = self.idx_of_ip[prev.operands[0]]
            true_lo, true_hi = i + 1, tdx - 1
            false_lo, false_hi = tdx, edx
            # ternary?  true branch yields a value (no statements)
            sub = []
            save = self._snapshot()
            self._block(true_lo, true_hi, sub, indent + 1)
            if not sub and not self.at_boundary():
                # ternary expression; the branch value lives in the string
                # register (cur) or on the numeric stack - keep it there.
                string_typed = self.cur is not None
                tval = self.pop_value()
                self._block(false_lo, false_hi, [], indent + 1)
                fval = self.pop_value()
                self._restore(save)
                tern = Expr("%s ? %s : %s" % (cond.paren(P_TERNARY + 1),
                                              tval.paren(P_TERNARY + 1),
                                              fval.paren(P_TERNARY)), P_TERNARY)
                if string_typed:
                    self.cur = tern
                else:
                    self.nstack.append(tern)
                return edx
            # if / else statement
            self._emit(lines, indent, "if (%s)" % cond.t)
            self._emit(lines, indent, "{")
            lines.extend(sub)
            self._emit(lines, indent, "}")
            self._emit(lines, indent, "else")
            self._emit(lines, indent, "{")
            self._block(false_lo, false_hi, lines, indent + 1)
            self._emit(lines, indent, "}")
            return edx
        else:
            # plain if (no else); could still be ternary w/o else (rare) -> treat as if
            sub = []
            self._block(i + 1, tdx, sub, indent + 1)
            self._emit(lines, indent, "if (%s)" % cond.t)
            self._emit(lines, indent, "{")
            lines.extend(sub)
            self._emit(lines, indent, "}")
            return tdx

    def _do_while_loop(self, i, lines, indent):
        info = self.loops[i]
        cond = self.pop_value()
        L = info["L"]
        bottom = info["bottom"]
        break_ip = info["break_ip"]
        # The continue point is where the re-test (a byte-for-byte copy of the
        # loop test) begins; for a `for` loop the increment sits just before
        # it. Find it by matching the test opcodes backward from the guard and
        # from the bottom jump.
        j1, j2 = i - 1, bottom - 1
        while j1 >= L and j2 >= L and self.I[j1].op == self.I[j2].op:
            j1 -= 1
            j2 -= 1
        cont_ip = self.I[j2 + 1].ip if j2 + 1 <= bottom else self.I[bottom].ip
        self.break_ip.append(break_ip)
        self.continue_ip.append(cont_ip)
        body = []
        self._block(L, bottom, body, indent + 1)
        # the bottom retest leaves a dangling value; discard it
        self.pop_value()
        self.break_ip.pop()
        self.continue_ip.pop()
        self._emit(lines, indent, "while (%s)" % cond.t)
        self._emit(lines, indent, "{")
        lines.extend(body)
        self._emit(lines, indent, "}")
        return self.idx_of_ip[break_ip]

    def _do_do_loop(self, i, lines, indent):
        info = self.do_heads[i]
        bottom = info["bottom"]
        break_ip = info["break_ip"]
        self.break_ip.append(break_ip)
        self.continue_ip.append(self.I[i].ip)
        body = []
        self._block(i, bottom, body, indent + 1)
        cond = self.pop_value()   # trailing retest value == loop condition
        self.break_ip.pop()
        self.continue_ip.pop()
        self._emit(lines, indent, "do")
        self._emit(lines, indent, "{")
        lines.extend(body)
        self._emit(lines, indent, "} while (%s);" % cond.t)
        return self.idx_of_ip[break_ip]

    def _snapshot(self):
        return (list(self.nstack), self.cur, list(self.saved),
                [list(f) for f in self.frames])

    def _restore(self, snap):
        self.nstack, self.cur, self.saved, self.frames = (
            list(snap[0]), snap[1], list(snap[2]), [list(f) for f in snap[3]])

    # -- single-instruction symbolic execution ---------------------------
    def _step(self, i, lines, indent):
        ins = self.I[i]
        op = ins.op
        o = ins.operands

        if op == "OP_LOADIMMED_UINT":
            self.nstack.append(Expr(str(o[0])))
        elif op == "OP_LOADIMMED_FLT":
            self.nstack.append(Expr(fmt_float(self.floats[o[0]])))
        elif op == "OP_LOADIMMED_STR":
            self.cur = Expr(quote_str(self.strings.get_str(o[0])))
        elif op == "OP_TAG_TO_STR":
            self.cur = Expr(quote_tagged(self.strings.get_str(o[0])))
        elif op == "OP_LOADIMMED_IDENT":
            self.cur = Expr(self.ste(ins.ip + 1), ident=True)

        elif op == "OP_SETCURVAR" or op == "OP_SETCURVAR_CREATE":
            self.cur_var = Expr(self.ste(ins.ip + 1))
        elif op in ("OP_SETCURVAR_ARRAY", "OP_SETCURVAR_ARRAY_CREATE"):
            self.cur_var = self._array_var(self.cur)
            self.cur = None      # the index string was consumed into the var name
        elif op in ("OP_LOADVAR_UINT", "OP_LOADVAR_FLT"):
            self.nstack.append(self.cur_var)
        elif op == "OP_LOADVAR_STR":
            self.cur = self.cur_var
        elif op in ("OP_SAVEVAR_UINT", "OP_SAVEVAR_FLT"):
            rhs = self.nstack[-1] if self.nstack else Expr("")
            self.nstack[-1:] = [Expr("%s = %s" % (self.cur_var.t,
                                rhs.paren(P_ASSIGN)), P_ASSIGN)]
        elif op == "OP_SAVEVAR_STR":
            rhs = self.cur if self.cur is not None else Expr("")
            self.cur = Expr("%s = %s" % (self.cur_var.t, rhs.paren(P_ASSIGN)),
                            P_ASSIGN)

        elif op == "OP_SETCUROBJECT":
            # The engine moves the string register into the object register;
            # the value is consumed, so clear `cur`. Failing to clear it left a
            # stale bare-object expr that hijacked the next conditional/loop test
            # (the P1/P2/P3 defects), pushing the real `obj.field` comparison out
            # as a stray trailing statement.
            self.cur_obj = self.cur
            self.cur = None
        elif op == "OP_SETCUROBJECT_NEW":
            self.cur_obj = "NEW"
        elif op == "OP_SETCURFIELD":
            self.cur_field = self.ste(ins.ip + 1)
            self.cur_field_array = None
        elif op == "OP_SETCURFIELD_ARRAY":
            self.cur_field_array = self.cur
            self.cur = None      # the index string was consumed into the field
        elif op in ("OP_LOADFIELD_UINT", "OP_LOADFIELD_FLT"):
            self.nstack.append(self._field_expr())
        elif op == "OP_LOADFIELD_STR":
            self.cur = self._field_expr()
        elif op in ("OP_SAVEFIELD_UINT", "OP_SAVEFIELD_FLT"):
            rhs = self.nstack[-1] if self.nstack else Expr("")
            self.nstack[-1:] = [Expr("%s = %s" % (self._field_expr().t,
                                rhs.paren(P_ASSIGN)), P_ASSIGN)]
        elif op == "OP_SAVEFIELD_STR":
            rhs = self.cur if self.cur is not None else Expr("")
            self.cur = Expr("%s = %s" % (self._field_expr().t,
                            rhs.paren(P_ASSIGN)), P_ASSIGN)

        # conversions: source text unchanged; just move between stacks
        elif op in ("OP_STR_TO_UINT", "OP_STR_TO_FLT"):
            self.nstack.append(self.cur if self.cur is not None else Expr(""))
            self.cur = None
        elif op in ("OP_UINT_TO_STR", "OP_FLT_TO_STR"):
            self.cur = self.nstack.pop() if self.nstack else Expr("")
        elif op in ("OP_UINT_TO_FLT", "OP_FLT_TO_UINT"):
            pass
        elif op == "OP_STR_TO_NONE":
            self._emit_stmt(lines, indent, self.cur)
            self.cur = None
        elif op in ("OP_UINT_TO_NONE", "OP_FLT_TO_NONE"):
            self._emit_stmt(lines, indent, self.nstack.pop() if self.nstack
                            else None)

        # arithmetic / comparison / logic (binary; left was compiled last = top)
        elif op == "OP_ADD":
            self._binop("+", P_ADD)
        elif op == "OP_SUB":
            self._binop("-", P_ADD)
        elif op == "OP_MUL":
            self._binop("*", P_MULT)
        elif op == "OP_DIV":
            self._binop("/", P_MULT)
        elif op == "OP_MOD":
            self._binop("%", P_MULT)
        elif op == "OP_CMPEQ":
            self._binop("==", P_EQ)
        elif op == "OP_CMPNE":
            self._binop("!=", P_EQ)
        elif op == "OP_CMPGR":
            self._binop(">", P_REL)
        elif op == "OP_CMPGE":
            self._binop(">=", P_REL)
        elif op == "OP_CMPLT":
            self._binop("<", P_REL)
        elif op == "OP_CMPLE":
            self._binop("<=", P_REL)
        elif op == "OP_BITAND":
            self._binop("&", P_BAND)
        elif op == "OP_BITOR":
            self._binop("|", P_BOR)
        elif op == "OP_XOR":
            self._binop("^", P_BXOR)
        elif op == "OP_SHL":
            self._binop("<<", P_SHIFT)
        elif op == "OP_SHR":
            self._binop(">>", P_SHIFT)
        elif op == "OP_AND":
            self._binop("&&", P_AND)
        elif op == "OP_OR":
            self._binop("||", P_OR)
        elif op == "OP_NEG":
            a = self.nstack.pop() if self.nstack else Expr("")
            self.nstack.append(Expr("-" + a.paren(P_UNARY), P_UNARY))
        elif op == "OP_NOT" or op == "OP_NOTF":
            a = self.nstack.pop() if self.nstack else Expr("")
            self.nstack.append(Expr("!" + a.paren(P_UNARY), P_UNARY))
        elif op == "OP_ONESCOMPLEMENT":
            a = self.nstack.pop() if self.nstack else Expr("")
            self.nstack.append(Expr("~" + a.paren(P_UNARY), P_UNARY))

        # short-circuit && / || via NP jumps
        elif op in ("OP_JMPIF_NP", "OP_JMPIFNOT_NP"):
            return self._logical(i)

        # string building
        elif op == "OP_ADVANCE_STR":
            self.saved.append((self.cur, "@"))
            self.cur = None
        elif op == "OP_ADVANCE_STR_APPENDCHAR":
            sep = {" ": "SPC", "\t": "TAB", "\n": "NL"}.get(chr(o[0]), "@")
            self.saved.append((self.cur, sep))
            self.cur = None
        elif op == "OP_ADVANCE_STR_COMMA":
            self.saved.append((self.cur, "COMMA"))
            self.cur = None
        elif op == "OP_ADVANCE_STR_NUL":
            self.saved.append((self.cur, "NUL"))
            self.cur = None
        elif op == "OP_REWIND_STR":
            saved, sep = self.saved.pop()
            self.cur = self._combine(saved, sep, self.cur)
        elif op == "OP_TERMINATE_REWIND_STR":
            saved, sep = self.saved.pop()
            self.cur = saved                    # discard current, restore saved
        elif op == "OP_COMPARE_STR":
            saved, sep = self.saved.pop()
            left = saved if saved is not None else Expr("")
            right = self.cur if self.cur is not None else Expr("")
            self.cur = None
            self.nstack.append(Expr("%s $= %s" % (left.paren(P_EQ + 1),
                               right.paren(P_EQ + 1)), P_EQ))

        # calls
        elif op == "OP_PUSH_FRAME":
            self.frames.append([])
        elif op == "OP_PUSH":
            self.frames[-1].append(self.cur if self.cur is not None else Expr(""))
            self.cur = None
        elif op in ("OP_CALLFUNC", "OP_CALLFUNC_RESOLVE"):
            self._call(ins)

        # object creation
        elif op == "OP_CREATE_OBJECT":
            return self._object(i, lines, indent)
        elif op in ("OP_ADD_OBJECT", "OP_END_OBJECT"):
            pass

        elif op in ("OP_UNUSED_2", "OP_UNUSED_3", "OP_UNUSED_72", "OP_BREAK"):
            pass
        else:
            self._emit(lines, indent, "// ?? unhandled %s" % op)
        return i + 1

    # -- expression helpers ----------------------------------------------
    def _binop(self, sym, prec):
        a = self.nstack.pop() if self.nstack else Expr("")   # left (top)
        b = self.nstack.pop() if self.nstack else Expr("")   # right
        self.nstack.append(Expr("%s %s %s" % (a.paren(prec), sym,
                           b.paren(prec + 1)), prec))

    def _combine(self, left, sep, right):
        left = left if left is not None else Expr("")
        right = right if right is not None else Expr("")
        if sep == "COMMA":
            return Expr("%s, %s" % (left.paren(P_COMMA + 1),
                        right.paren(P_COMMA + 1)), P_COMMA)
        sym = {"@": "@", "SPC": "SPC", "TAB": "TAB", "NL": "NL"}.get(sep, "@")
        e = Expr("%s %s %s" % (left.paren(P_CAT), sym, right.paren(P_CAT + 1)),
                 P_CAT)
        if left.ident:
            e.array = (left.t, right)
        return e

    def _array_var(self, e):
        if e is not None and e.array is not None:
            base, idx = e.array
            return Expr("%s[%s]" % (base, idx.t))
        # fallback
        return Expr((e.t if e else ""))

    def _field_expr(self):
        fld = self.cur_field
        if self.cur_field_array is not None:
            fld = "%s[%s]" % (fld, self.cur_field_array.t)
        if self.cur_obj == "NEW" or self.cur_obj is None:
            return Expr(fld)
        return Expr("%s.%s" % (self.cur_obj.paren(P_ATOM), fld))

    def _logical(self, i):
        ins = self.I[i]
        sym = "||" if ins.op == "OP_JMPIF_NP" else "&&"
        prec = P_OR if sym == "||" else P_AND
        left = self.nstack.pop() if self.nstack else Expr("")
        tdx = self.target_idx(ins)
        self._block(i + 1, tdx, [], 0)         # evaluate right operand
        right = self.nstack.pop() if self.nstack else Expr("")
        self.nstack.append(Expr("%s %s %s" % (left.paren(prec),
                           sym, right.paren(prec + 1)), prec))
        return tdx

    def _call(self, ins):
        fn = self.ste(ins.ip + 1)
        ns = self.ste(ins.ip + 2)
        call_type = ins.operands[2]
        args = self.frames.pop() if self.frames else []
        argtxt = [a.t for a in args]
        if call_type == CALL_METHOD:
            obj = argtxt[0] if argtxt else ""
            rest = ", ".join(argtxt[1:])
            self.cur = Expr("%s.%s(%s)" % (obj, fn, rest))
        elif call_type == CALL_PARENT:
            self.cur = Expr("Parent::%s(%s)" % (fn, ", ".join(argtxt)))
        else:
            name = "%s::%s" % (ns, fn) if ns else fn
            self.cur = Expr("%s(%s)" % (name, ", ".join(argtxt)))

    def _emit_stmt(self, lines, indent, val):
        if val is not None and val.t != "":
            self._emit(lines, indent, val.t + ";")

    # -- object declarations ---------------------------------------------
    def _object(self, i, lines, indent):
        """Parse a root OP_CREATE_OBJECT .. OP_END_OBJECT into `new`/`datablock`."""
        text, end_idx = self._object_text(i, indent)
        # A root object decl is preceded by `OP_LOADIMMED_UINT 0` (the group id
        # placeholder); OP_ADD_OBJECT overwrites it with the new object's id.
        if self.nstack and self.nstack[-1].t == "0":
            self.nstack.pop()
        self.nstack.append(Expr(text, P_ATOM))
        return end_idx

    def _object_text(self, i, indent):
        ins = self.I[i]
        parent = self.ste(ins.ip + 1)
        is_db = ins.operands[1]
        frame = self.frames.pop() if self.frames else []
        argtxt = [a.t for a in frame]
        class_name = argtxt[0] if argtxt else ""
        obj_name = argtxt[1] if len(argtxt) > 1 else ""
        ctor = argtxt[2:]
        kw = "datablock" if is_db else "new"
        name_part = "" if obj_name in ("", '""') else obj_name
        decl = name_part
        if parent:
            decl = "%s : %s" % (name_part, parent) if name_part else ": " + parent
        if ctor:
            decl = (decl + ", " if decl else "") + ", ".join(ctor)
        header = "%s %s(%s)" % (kw, class_name, decl)

        # find this object's OP_ADD_OBJECT (depth 0; a field value could itself
        # create a nested object, which would have its own ADD/END pair)
        j = i + 1
        depth = 0
        while j < self.hi:
            op = self.I[j].op
            if op == "OP_CREATE_OBJECT":
                depth += 1
            elif op == "OP_END_OBJECT":
                depth -= 1
            elif op == "OP_ADD_OBJECT" and depth == 0:
                break
            j += 1
        add_idx = j
        # field assignments may contain ternary/logical expressions, so run the
        # full control-flow-aware walker over the field region.
        field_lines = []
        child_texts = []
        self._block(i + 1, add_idx, field_lines, 0)
        if j < self.hi and self.I[j].op == "OP_ADD_OBJECT":
            j += 1
        # sub-objects: each is a full nested decl whose preamble (PUSH_FRAME,
        # class/name/arg pushes) must be simulated before its CREATE_OBJECT.
        throwaway = []
        while j < self.hi and self.I[j].op != "OP_END_OBJECT":
            if self.I[j].op == "OP_CREATE_OBJECT":
                ctext, j = self._object_text(j, indent + 1)
                child_texts.append(ctext)
            else:
                j = self._step(j, throwaway, 0)
        # OP_END_OBJECT for this object
        if j < self.hi and self.I[j].op == "OP_END_OBJECT":
            j += 1

        ind = "    " * indent
        body = ""
        inner = "    " * (indent + 1)
        parts = []
        for fl in field_lines:
            parts.append(inner + fl)
        if child_texts:
            if parts:
                parts.append("")
            for ct in child_texts:
                parts.append(inner + ct + ";")
        if parts:
            body = "\n%s{\n%s\n%s}" % (ind, "\n".join(parts), ind)
        else:
            body = ""
        return header + body, j


def function_ranges(instrs, idx_of_ip):
    """Return list of (decl_instr_idx, body_lo_idx, body_hi_idx)."""
    ranges = []
    for k, ins in enumerate(instrs):
        if ins.op == "OP_FUNC_DECL":
            argc = ins.operands[5]
            end_ip = ins.operands[4]
            body_lo = k + 1
            body_hi = idx_of_ip[end_ip]
            ranges.append((k, body_lo, body_hi))
    return ranges


def decompile(cb):
    instrs, by_ip = disassemble(cb)
    idx_of_ip = {ins.ip: k for k, ins in enumerate(instrs)}
    # also map code_size (one past end) for jump targets to the end
    idx_of_ip[cb.code_size] = len(instrs)

    fns = function_ranges(instrs, idx_of_ip)
    fn_body = set()
    fn_decl_idx = {}
    for decl, lo, hi in fns:
        fn_decl_idx[decl] = (lo, hi)
        for k in range(decl, hi):
            fn_body.add(k)

    out = []
    out.append("// Decompiled from DSO (TorqueScript v%d) by dsodecomp.py"
               % cb.version)
    out.append("")

    # Walk top-level instructions in order; when we hit a FUNC_DECL, emit the
    # function (using the function string/float tables); otherwise accumulate
    # top-level statements and flush them as a group.
    i = 0
    n = len(instrs)
    top_chunk_lo = None

    def flush_top(lo, hi):
        if lo is None or lo >= hi:
            return
        scope = Scope(cb, instrs, idx_of_ip, lo, hi, in_function=False)
        for line in scope.decompile():
            out.append(line)

    while i < n:
        ins = instrs[i]
        if ins.op == "OP_FUNC_DECL":
            flush_top(top_chunk_lo, i)
            top_chunk_lo = None
            lo, hi = fn_decl_idx[i]
            name = cb.idents.get(ins.ip + 1, "")
            ns = cb.idents.get(ins.ip + 2, "")
            pkg = cb.idents.get(ins.ip + 3, "")
            argc = ins.operands[5]
            args = []
            for a in range(argc):
                nm = cb.idents.get(ins.ip + 7 + a, "").lstrip("%")
                args.append("%" + nm if nm else "%%junk%d" % a)
            full = "%s::%s" % (ns, name) if ns else name
            if pkg:
                out.append("// package: %s" % pkg)
            out.append("function %s(%s)" % (full, ", ".join(args)))
            out.append("{")
            scope = Scope(cb, instrs, idx_of_ip, lo, hi, in_function=True)
            for line in scope.decompile(base_indent=1):
                out.append(line)
            out.append("}")
            out.append("")
            i = hi
        else:
            if top_chunk_lo is None:
                top_chunk_lo = i
            i += 1
    flush_top(top_chunk_lo, n)

    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Decompile Torque/AoT .dso files.")
    ap.add_argument("path", help="a .dso file, or a directory to recurse")
    ap.add_argument("-o", "--output", help="output path (single file only)")
    ap.add_argument("--stdout", action="store_true",
                    help="print result to the terminal instead of a file")
    ap.add_argument("--disasm", action="store_true",
                    help="emit raw disassembly instead of reconstructed source")
    ap.add_argument("-f", "--force", action="store_true",
                    help="overwrite the output file if it already exists")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if os.path.isdir(args.path):
        targets = []
        for root, _dirs, files in os.walk(args.path):
            for f in files:
                if f.lower().endswith(".dso"):
                    targets.append(os.path.join(root, f))
        for t in sorted(targets):
            try:
                decompile_file(t, disasm=args.disasm, quiet=args.quiet,
                               force=args.force)
            except Exception as exc:  # noqa: BLE001
                print("ERROR %s: %s" % (t, exc), file=sys.stderr)
        return 0

    decompile_file(args.path, out=args.output, to_stdout=args.stdout,
                   disasm=args.disasm, quiet=args.quiet, force=args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())
