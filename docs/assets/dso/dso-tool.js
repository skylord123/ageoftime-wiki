/* In-browser DSO decompiler.
 *
 * Runs the real dsodecomp.py (the same script linked in the gist) unmodified
 * via Pyodide, entirely client-side — the selected .dso file never leaves the
 * browser. TorqueScript syntax highlighting is a lightweight regex tokenizer
 * whose token model mirrors the IDEA-TorqueScriptLanguage flex lexer.
 */
(function () {
  "use strict";

  var PYODIDE_VERSION = "0.26.2";
  var PYODIDE_INDEX = "https://cdn.jsdelivr.net/pyodide/v" + PYODIDE_VERSION + "/full/";

  // ---- TorqueScript highlighter -------------------------------------------

  var KEYWORDS = new Set([
    "new", "if", "else", "switch", "switch$", "do", "while", "for",
    "foreach", "foreach$", "in", "case", "or", "default", "break", "continue",
    "assert", "return", "function", "datablock", "singleton", "package",
    "namespace", "true", "false", "Parent"
  ]);
  // String-concatenation keyword-operators.
  var OPWORDS = new Set(["SPC", "TAB", "NL"]);

  var TS_RE = new RegExp([
    "\\/\\*[\\s\\S]*?\\*\\/",                  // block / doc comment
    "\\/\\/[^\\n]*",                           // line comment
    "\"(?:\\\\.|[^\"\\\\])*\"",                // string
    "'(?:\\\\.|[^'\\\\])*'",                   // tagged string
    "\\$[A-Za-z_][\\w:]*",                     // $global var
    "%[A-Za-z_][\\w:]*",                       // %local var
    "\\b0[xX][0-9a-fA-F]+\\b",                 // hex
    "\\b\\d+\\.\\d+(?:[eE][+-]?\\d+)?\\b",     // float
    "\\b\\d+\\b",                              // integer
    "switch\\$|foreach\\$",                    // $-suffixed keywords
    "[A-Za-z_]\\w*"                            // identifier / keyword
  ].join("|"), "g");

  function esc(s) {
    return s.replace(/[&<>]/g, function (c) {
      return c === "&" ? "&amp;" : c === "<" ? "&lt;" : "&gt;";
    });
  }

  function highlight(code) {
    var out = "", last = 0, m;
    TS_RE.lastIndex = 0;
    while ((m = TS_RE.exec(code)) !== null) {
      if (m.index > last) out += esc(code.slice(last, m.index));
      var t = m[0], cls = null;
      var c0 = t.charAt(0);
      if (t.indexOf("/*") === 0 || t.indexOf("//") === 0) cls = "tsc";
      else if (c0 === '"') cls = "tss";
      else if (c0 === "'") cls = "tst";
      else if (c0 === "$") cls = "tsv";
      else if (c0 === "%") cls = "tsl";
      else if (c0 >= "0" && c0 <= "9") cls = "tsn";
      else if (KEYWORDS.has(t) || OPWORDS.has(t)) cls = "tsk";
      else {
        // function name: next non-space char is '('
        var j = TS_RE.lastIndex;
        while (j < code.length && (code[j] === " " || code[j] === "\t")) j++;
        if (code[j] === "(") cls = "tsf";
      }
      out += cls ? '<span class="' + cls + '">' + esc(t) + "</span>" : esc(t);
      last = TS_RE.lastIndex;
    }
    out += esc(code.slice(last));
    return out;
  }

  // ---- asset / pyodide loading --------------------------------------------

  // Resolve the bundled dsodecomp.py relative to the site root, independent of
  // the deployment base path (e.g. GitHub Pages' /ageoftime-wiki/).
  function assetUrl(rel) {
    var p = location.pathname;
    var marker = "reference/torque-script/dso-decompiler";
    var i = p.indexOf(marker);
    var base = i >= 0 ? p.slice(0, i) : p.replace(/[^/]*$/, "");
    return location.origin + base + rel;
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("failed to load " + src)); };
      document.head.appendChild(s);
    });
  }

  var pyodidePromise = null;
  function getPyodide(onProgress) {
    if (pyodidePromise) return pyodidePromise;
    pyodidePromise = (async function () {
      if (typeof loadPyodide === "undefined") {
        onProgress && onProgress("Loading Python runtime (first time only)…");
        await loadScript(PYODIDE_INDEX + "pyodide.js");
      }
      var py = await loadPyodide({ indexURL: PYODIDE_INDEX });
      onProgress && onProgress("Loading decompiler…");
      var resp = await fetch(assetUrl("assets/dso/dsodecomp.py"));
      if (!resp.ok) throw new Error("could not fetch dsodecomp.py");
      var src = await resp.text();
      // Drop the CLI entry point so importing the module doesn't run argparse.
      src = src.replace(/\nif __name__ == ["']__main__["']:[\s\S]*$/, "\n");
      py.runPython(src);
      return py;
    })();
    return pyodidePromise;
  }

  // ---- widget -------------------------------------------------------------

  function initTool(root) {
    var fileInput = root.querySelector("#dso-file");
    var disasm = root.querySelector("#dso-disasm");
    var status = root.querySelector("#dso-status");
    var output = root.querySelector("#dso-output");
    var download = root.querySelector("#dso-download");

    var lastBytes = null;
    var lastName = "decompiled";
    var lastText = "";

    function setStatus(msg, kind) {
      status.textContent = msg || "";
      status.classList.toggle("dso-error", kind === "error");
      status.classList.toggle("dso-busy", kind === "busy");
    }

    async function run() {
      if (!lastBytes) return;
      try {
        setStatus("Decompiling…", "busy");
        var py = await getPyodide(function (m) { setStatus(m, "busy"); });
        py.FS.writeFile("/tmp/input.dso", lastBytes);
        py.runPython("_cb = CodeBlock.load(open('/tmp/input.dso','rb').read())");
        var version = py.runPython("_cb.version");
        lastText = py.runPython(
          disasm.checked ? "format_disasm(_cb)" : "decompile(_cb)"
        );
        output.innerHTML = highlight(lastText);
        root.classList.add("dso-has-output");
        download.hidden = false;
        var note = version !== 33 ? " (DSO v" + version + " — expected 33)" : "";
        setStatus("Decompiled " + lastName + note + ". Processed locally in your browser.");
      } catch (e) {
        root.classList.remove("dso-has-output");
        download.hidden = true;
        setStatus("Could not decompile this file: " + (e && e.message ? e.message : e), "error");
      }
    }

    fileInput.addEventListener("change", async function () {
      var f = fileInput.files && fileInput.files[0];
      if (!f) return;
      lastName = f.name.replace(/\.dso$/i, "");
      if (!/\.cs$/i.test(lastName)) lastName += ".cs";
      lastBytes = new Uint8Array(await f.arrayBuffer());
      run();
    });

    disasm.addEventListener("change", function () { if (lastBytes) run(); });

    download.addEventListener("click", function () {
      if (!lastText) return;
      var blob = new Blob([lastText + "\n"], { type: "text/plain" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = disasm.checked ? lastName + ".disasm.txt" : lastName;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(a.href);
    });
  }

  function boot() {
    var root = document.getElementById("dso-tool");
    if (!root || root.dataset.init) return;
    root.dataset.init = "1";
    initTool(root);
  }

  // Material's instant navigation re-runs this via document$; also handle a
  // direct (non-instant) page load.
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(boot);
  } else if (document.readyState !== "loading") {
    boot();
  } else {
    document.addEventListener("DOMContentLoaded", boot);
  }
})();
