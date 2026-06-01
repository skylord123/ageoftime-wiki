# DSO Decompiler

Much of the *Age of Time* client and server ships as compiled **`.dso`** files
— TorqueScript that has been pre-compiled to bytecode, so the original `.cs`
source is not included. `dsodecomp.py` is a community decompiler that
reconstructs readable `.cs` source from those `.dso` files.

[:material-github: View the gist on GitHub](https://gist.github.com/skylord123/6fa28f1ce6633213fea0d45d75cda4ba){ .md-button }

## Try it in your browser

Pick a `.dso` file below to decompile it right here. The same `dsodecomp.py`
runs locally in your browser (via [Pyodide](https://pyodide.org/)) — **your
file is never uploaded anywhere**.

<div id="dso-tool" class="dso-tool">
  <div class="dso-controls">
    <label class="md-button md-button--primary dso-file-label">
      Choose a .dso file…
      <input type="file" id="dso-file" accept=".dso,.dso.cs,application/octet-stream" hidden>
    </label>
    <label class="dso-opt"><input type="checkbox" id="dso-disasm"> Raw disassembly</label>
    <button id="dso-download" class="md-button" type="button" hidden>Download result</button>
  </div>
  <div id="dso-status" class="dso-status">Select a <code>.dso</code> file to decompile it locally in your browser.</div>
  <div class="highlight"><pre><code id="dso-output" class="dso-output"></code></pre></div>
</div>

!!! note "First run downloads the Python runtime"
    The first time you decompile, the page fetches the Pyodide runtime
    (a few MB) from a CDN. After that it's cached. Everything — the runtime,
    the decompiler, and your file — stays in your browser.

## What it does

The decompiler reads the **DSO version 33** format used by *Age of Time*'s
custom TGE 1.x fork and reconstructs equivalent, recompilable TorqueScript:

- Recovers control flow — `if`/`else`, `while`, `for`, `do`/`while`,
  ternaries, and logical operators.
- Reconstructs string building, function calls, and method calls.
- Handles `new` and `datablock` object declarations.

It is written in **Python 3** and has **no third-party dependencies** — only
the standard library.

The gist also includes `DSO-FORMAT.md`, a reverse-engineered specification of
the bytecode format, and a `README.md`.

## Usage

```text
python3 dsodecomp.py path/to/FILE.cs.dso          # Write FILE.cs next to it
python3 dsodecomp.py FILE.cs.dso -o /tmp/out.cs   # Specify the output path
python3 dsodecomp.py FILE.cs.dso --stdout         # Print to the terminal
python3 dsodecomp.py FILE.cs.dso --disasm         # Raw bytecode disassembly
python3 dsodecomp.py ../directory                 # Recurse a directory
```

## See also

- [Torque Script](index.md) — other notes on the TorqueScript runtime.
- [Datablocks](datablocks.md) — datablock declarations the decompiler can
  recover.
