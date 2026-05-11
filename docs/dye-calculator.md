# Dye Calculator

Interactive mixer for *Age of Time* dyes.

This tool mixes two colors using floor averaging per RGB channel:
<code>floor((A + B) / 2)</code>. The share link below the result preserves the
current two inputs.

<div id="aot-dye-calculator">
  <style>
    #aot-dye-calculator {
      --aot-bg: linear-gradient(180deg, #f4efe5 0%, #ece1cf 100%);
      --aot-panel: rgba(255, 250, 242, 0.92);
      --aot-panel-2: #fffdf8;
      --aot-border: #c7b293;
      --aot-text: #2f2418;
      --aot-muted: #6f6254;
      --aot-accent: #7a3f16;
      --aot-accent-2: #9f5a20;
      --aot-button-text: #fff7eb;
      --aot-danger: #9d2f2f;
      --aot-success: #1f6b46;
      font-family: "Trebuchet MS", "Segoe UI", Tahoma, sans-serif;
      color: var(--aot-text);
      background:
        radial-gradient(circle at top right, rgba(181, 118, 53, 0.18), transparent 30%),
        radial-gradient(circle at bottom left, rgba(114, 76, 47, 0.14), transparent 34%),
        var(--aot-bg);
      border: 1px solid var(--aot-border);
      border-radius: 16px;
      padding: 18px;
      max-width: 1040px;
      box-sizing: border-box;
      box-shadow: 0 18px 40px rgba(64, 38, 12, 0.12);
    }
    @media (prefers-color-scheme: dark) {
      #aot-dye-calculator {
        --aot-bg: linear-gradient(180deg, #21180f 0%, #18110c 100%);
        --aot-panel: rgba(47, 33, 23, 0.92);
        --aot-panel-2: #38281d;
        --aot-border: #735339;
        --aot-text: #f5eadb;
        --aot-muted: #c1ab95;
        --aot-accent: #df9156;
        --aot-accent-2: #f0ad73;
        --aot-button-text: #21150d;
        --aot-danger: #ff9898;
        --aot-success: #8be0aa;
        box-shadow: 0 20px 48px rgba(0, 0, 0, 0.28);
      }
    }
    #aot-dye-calculator * { box-sizing: border-box; }
    #aot-dye-calculator h2, #aot-dye-calculator h3, #aot-dye-calculator p { margin-top: 0; }
    #aot-dye-calculator .aot-subtitle { color: var(--aot-muted); font-size: 0.94rem; max-width: 72ch; }
    #aot-dye-calculator .aot-section {
      background: var(--aot-panel);
      border: 1px solid var(--aot-border);
      border-radius: 14px;
      padding: 14px;
      margin-top: 14px;
      backdrop-filter: blur(2px);
    }
    #aot-dye-calculator .aot-grid { display: grid; gap: 12px; }
    #aot-dye-calculator .aot-grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    @media (max-width: 760px) {
      #aot-dye-calculator .aot-grid-2,
      #aot-dye-calculator .aot-button-row,
      #aot-dye-calculator .aot-share-row { grid-template-columns: 1fr; }
    }
    #aot-dye-calculator .aot-card {
      background: var(--aot-panel-2);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 12px;
    }
    #aot-dye-calculator label { display: block; font-weight: 650; font-size: 0.85rem; margin-bottom: 5px; }
    #aot-dye-calculator select,
    #aot-dye-calculator input,
    #aot-dye-calculator button {
      width: 100%;
      border-radius: 9px;
      border: 1px solid var(--aot-border);
      padding: 8px 10px;
      background: rgba(255,255,255,0.85);
      color: var(--aot-text);
      font: inherit;
    }
    @media (prefers-color-scheme: dark) {
      #aot-dye-calculator select, #aot-dye-calculator input, #aot-dye-calculator button {
        background: rgba(17,12,8,0.82);
      }
    }
    #aot-dye-calculator input[type="number"] { appearance: textfield; }
    #aot-dye-calculator input[type="number"]::-webkit-outer-spin-button,
    #aot-dye-calculator input[type="number"]::-webkit-inner-spin-button { appearance: none; margin: 0; }
    #aot-dye-calculator button {
      cursor: pointer;
      background: linear-gradient(180deg, var(--aot-accent-2), var(--aot-accent));
      color: var(--aot-button-text);
      border-color: rgba(78, 37, 10, 0.45);
      font-weight: 650;
    }
    #aot-dye-calculator button:hover { filter: brightness(1.05); }
    #aot-dye-calculator button.aot-secondary {
      background: transparent;
      color: var(--aot-text);
      border-color: var(--aot-border);
    }
    #aot-dye-calculator .aot-color-row {
      display: grid;
      grid-template-columns: 76px 1fr;
      gap: 10px;
      align-items: center;
      margin-bottom: 10px;
    }
    #aot-dye-calculator .aot-swatch {
      width: 76px;
      height: 76px;
      border-radius: 12px;
      border: 1px solid rgba(255,255,255,0.45);
      background: rgb(0,0,0);
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.08);
    }
    #aot-dye-calculator .aot-rgb-inputs {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    #aot-dye-calculator .aot-output-rgb,
    #aot-dye-calculator .aot-share-url {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
    #aot-dye-calculator .aot-output-rgb { font-size: 1.1rem; margin: 6px 0 10px; }
    #aot-dye-calculator .aot-button-row,
    #aot-dye-calculator .aot-share-row {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
    }
    #aot-dye-calculator .aot-inline-note { margin-top: 8px; font-size: 0.85rem; color: var(--aot-muted); }
    #aot-dye-calculator .aot-share-status { min-height: 1.2em; margin-top: 8px; font-size: 0.88rem; }
    #aot-dye-calculator .aot-share-url { font-size: 0.82rem; }
    #aot-dye-calculator .aot-warning { color: var(--aot-danger); font-weight: 650; }
    #aot-dye-calculator .aot-success { color: var(--aot-success); font-weight: 650; }
  </style>

  <h2>Age of Time Dye Calculator</h2>
  <p class="aot-subtitle">Choose named dyes or enter RGB values directly to test a two-input mix.</p>

  <div class="aot-section" aria-labelledby="aot-mixer-title">
    <h3 id="aot-mixer-title">Dye Mixer</h3>
    <div class="aot-grid aot-grid-2">
      <div class="aot-card" data-aot-input="1">
        <h3>Input 1</h3>
        <div class="aot-color-row">
          <div class="aot-swatch" data-role="swatch"></div>
          <div>
            <label>Named dye</label>
            <select data-role="named-select"></select>
          </div>
        </div>
        <div class="aot-rgb-inputs">
          <div><label>R</label><input type="number" min="0" max="255" step="1" data-role="r" /></div>
          <div><label>G</label><input type="number" min="0" max="255" step="1" data-role="g" /></div>
          <div><label>B</label><input type="number" min="0" max="255" step="1" data-role="b" /></div>
        </div>
      </div>

      <div class="aot-card" data-aot-input="2">
        <h3>Input 2</h3>
        <div class="aot-color-row">
          <div class="aot-swatch" data-role="swatch"></div>
          <div>
            <label>Named dye</label>
            <select data-role="named-select"></select>
          </div>
        </div>
        <div class="aot-rgb-inputs">
          <div><label>R</label><input type="number" min="0" max="255" step="1" data-role="r" /></div>
          <div><label>G</label><input type="number" min="0" max="255" step="1" data-role="g" /></div>
          <div><label>B</label><input type="number" min="0" max="255" step="1" data-role="b" /></div>
        </div>
      </div>
    </div>

    <div class="aot-card" style="margin-top: 12px;">
      <h3>Result</h3>
      <div class="aot-color-row">
        <div class="aot-swatch" id="aot-mix-output-swatch"></div>
        <div>
          <div class="aot-output-rgb" id="aot-mix-output-rgb">0 0 0</div>
          <div class="aot-button-row">
            <button type="button" id="aot-output-to-input-1">Set Input 1 to Result</button>
            <button type="button" id="aot-output-to-input-2">Set Input 2 to Result</button>
          </div>
        </div>
      </div>
      <div class="aot-inline-note" id="aot-mix-output-name"></div>
    </div>

    <div class="aot-card" style="margin-top: 12px;">
      <h3>Share State</h3>
      <div class="aot-share-row">
        <button type="button" id="aot-copy-share-link">Copy Share Link</button>
        <button type="button" class="aot-secondary" id="aot-reset-share-state">Reset to Defaults</button>
      </div>
      <div class="aot-inline-note">Anyone opening the shared link will load the same two calculator inputs.</div>
      <div class="aot-share-status" id="aot-share-status"></div>
      <input class="aot-share-url" id="aot-share-url" type="text" readonly aria-label="Shareable dye calculator link" />
    </div>
  </div>

  <script>
    (function () {
      "use strict";
      const NAMED_DYES = [
        { name: "Orange Dye", rgb: [255, 127, 0] },
        { name: "Bright Cyan Dye", rgb: [0, 255, 255] },
        { name: "Cyan Dye", rgb: [0, 127, 127] },
        { name: "Dark Cyan Dye", rgb: [0, 63, 63] },
        { name: "Magenta Dye", rgb: [255, 0, 255] },
        { name: "Bright Green Dye", rgb: [0, 255, 0] },
        { name: "Green Dye", rgb: [0, 127, 0] },
        { name: "Dark Green Dye", rgb: [0, 63, 0] },
        { name: "Black Dye", rgb: [31.0001, 31.0001, 31.0001] },
        { name: "Bright Blue Dye", rgb: [0, 0, 255] },
        { name: "Dark Blue Dye", rgb: [0, 0, 63] },
        { name: "Midnight Blue Dye", rgb: [0, 0, 31] },
        { name: "Bright Yellow Dye", rgb: [255, 255, 0] },
        { name: "Yellow Dye", rgb: [127, 127, 0] },
        { name: "Bright Red Dye", rgb: [255, 0, 0] },
        { name: "Dark Red Dye", rgb: [63, 0, 0] },
        { name: "Brown Dye", rgb: [79, 61.0001, 23] },
        { name: "Ocre Dye", rgb: [63, 63, 0] },
        { name: "Bleach", rgb: [255, 255, 255] },
        { name: "Pitch Black Dye", rgb: [0, 0, 0] },
        { name: "Red Dye", rgb: [127, 0, 0] },
        { name: "Pink Dye", rgb: [255, 127, 127] },
        { name: "Lavender Dye", rgb: [255, 127, 255] },
        { name: "Light Gray Dye", rgb: [191, 191, 191] },
        { name: "Gray Dye", rgb: [127, 127, 127] },
        { name: "Dark Gray Dye", rgb: [63, 63, 63] },
        { name: "Blue Dye", rgb: [0, 0, 127] },
        { name: "Purple Dye", rgb: [127, 0, 127] },
        { name: "Dark Purple Dye", rgb: [63, 0, 63] },
        { name: "Light Pink Dye", rgb: [255, 192, 192] }
      ];
      const OTHER_VALUE = "__other__";
      const SHARE_PARAM = "state";
      const shareStatus = document.getElementById("aot-share-status");
      const shareUrlField = document.getElementById("aot-share-url");

      function clamp(value, min, max) { return Math.min(max, Math.max(min, value)); }
      function normalizeRgb(rgb) {
        return rgb.map(function (value) {
          const number = Number(value);
          if (!Number.isFinite(number)) return 0;
          return clamp(Math.floor(number), 0, 255);
        });
      }
      function rgbKey(rgb) { const n = normalizeRgb(rgb); return n[0] + "," + n[1] + "," + n[2]; }
      function rgbText(rgb) { const n = normalizeRgb(rgb); return n[0] + " " + n[1] + " " + n[2]; }
      function rgbCss(rgb) { const n = normalizeRgb(rgb); return "rgb(" + n[0] + ", " + n[1] + ", " + n[2] + ")"; }
      function mixRgb(a, b) {
        return [
          Math.floor((Number(a[0]) + Number(b[0])) / 2),
          Math.floor((Number(a[1]) + Number(b[1])) / 2),
          Math.floor((Number(a[2]) + Number(b[2])) / 2)
        ];
      }
      function findNamedDyeByRgb(rgb) {
        const key = rgbKey(rgb);
        return NAMED_DYES.find(function (dye) { return rgbKey(dye.rgb) === key; }) || null;
      }
      function findNamedDyeByName(name) {
        return NAMED_DYES.find(function (dye) { return dye.name === name; }) || null;
      }
      function fillDyeSelect(select, includeOther) {
        select.innerHTML = "";
        if (includeOther) {
          const other = document.createElement("option");
          other.value = OTHER_VALUE;
          other.textContent = "Other";
          select.appendChild(other);
        }
        NAMED_DYES.forEach(function (dye) {
          const option = document.createElement("option");
          option.value = dye.name;
          option.textContent = dye.name + " (" + rgbText(dye.rgb) + ")";
          select.appendChild(option);
        });
      }
      function encodeShareState(state) {
        const json = JSON.stringify(state);
        return btoa(unescape(encodeURIComponent(json))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
      }
      function decodeShareState(value) {
        const padded = value.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((value.length + 3) % 4);
        const json = decodeURIComponent(escape(atob(padded)));
        return JSON.parse(json);
      }
      function getDefaultState() { return { i1: [255, 255, 255], i2: [0, 0, 0] }; }
      function buildShareUrl() {
        const url = new URL(window.location.href);
        url.searchParams.set(SHARE_PARAM, encodeShareState({ i1: input1.getRgb(), i2: input2.getRgb() }));
        url.hash = "";
        return url.toString();
      }
      function updateShareUi(statusText, statusClass) {
        shareUrlField.value = buildShareUrl();
        shareStatus.textContent = statusText || "";
        shareStatus.className = "aot-share-status" + (statusClass ? " " + statusClass : "");
      }
      function persistShareState() {
        window.history.replaceState({}, "", buildShareUrl());
        updateShareUi();
      }
      function loadStateFromUrl() {
        const raw = new URLSearchParams(window.location.search).get(SHARE_PARAM);
        if (!raw) return getDefaultState();
        try {
          const parsed = decodeShareState(raw);
          return { i1: normalizeRgb(parsed.i1 || getDefaultState().i1), i2: normalizeRgb(parsed.i2 || getDefaultState().i2) };
        } catch (error) {
          updateShareUi("Share link could not be parsed. Defaults loaded instead.", "aot-warning");
          return getDefaultState();
        }
      }
      function createDyeInput(card, onChange) {
        const select = card.querySelector('[data-role="named-select"]');
        const r = card.querySelector('[data-role="r"]');
        const g = card.querySelector('[data-role="g"]');
        const b = card.querySelector('[data-role="b"]');
        const swatch = card.querySelector('[data-role="swatch"]');
        fillDyeSelect(select, true);
        function getRgb() { return normalizeRgb([r.value, g.value, b.value]); }
        function syncSelectFromRgb() {
          const match = findNamedDyeByRgb(getRgb());
          select.value = match ? match.name : OTHER_VALUE;
        }
        function updateSwatch() { swatch.style.background = rgbCss(getRgb()); }
        function setRgb(rgb, silent) {
          const normalized = normalizeRgb(rgb);
          r.value = normalized[0]; g.value = normalized[1]; b.value = normalized[2];
          syncSelectFromRgb(); updateSwatch(); updateMixerOutput();
          if (!silent) onChange();
        }
        function applyChange() { syncSelectFromRgb(); updateSwatch(); updateMixerOutput(); onChange(); }
        select.addEventListener("change", function () {
          if (select.value === OTHER_VALUE) { applyChange(); return; }
          const dye = findNamedDyeByName(select.value);
          if (dye) setRgb(dye.rgb);
        });
        [r, g, b].forEach(function (input) {
          input.addEventListener("input", function () {
            input.value = clamp(Math.floor(Number(input.value || 0)), 0, 255);
            applyChange();
          });
        });
        return { getRgb: getRgb, setRgb: setRgb };
      }

      const mixOutputSwatch = document.getElementById("aot-mix-output-swatch");
      const mixOutputRgb = document.getElementById("aot-mix-output-rgb");
      const mixOutputName = document.getElementById("aot-mix-output-name");
      function getMixedOutputRgb() { return mixRgb(input1.getRgb(), input2.getRgb()); }
      function updateMixerOutput() {
        const output = getMixedOutputRgb();
        const match = findNamedDyeByRgb(output);
        mixOutputSwatch.style.background = rgbCss(output);
        mixOutputRgb.textContent = rgbText(output);
        mixOutputName.textContent = match ? "Matches named dye: " + match.name : "No named dye match.";
      }
      function handleStateChange() { persistShareState(); }
      const input1 = createDyeInput(document.querySelector('[data-aot-input="1"]'), handleStateChange);
      const input2 = createDyeInput(document.querySelector('[data-aot-input="2"]'), handleStateChange);

      document.getElementById("aot-output-to-input-1").addEventListener("click", function () { input1.setRgb(getMixedOutputRgb()); });
      document.getElementById("aot-output-to-input-2").addEventListener("click", function () { input2.setRgb(getMixedOutputRgb()); });
      document.getElementById("aot-copy-share-link").addEventListener("click", function () {
        const url = buildShareUrl();
        shareUrlField.value = url;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(function () {
            updateShareUi("Share link copied.", "aot-success");
          }).catch(function () {
            updateShareUi("Clipboard copy failed. The share link is still shown below.", "aot-warning");
            shareUrlField.focus(); shareUrlField.select();
          });
          return;
        }
        updateShareUi("Clipboard access is unavailable here. Copy the link from the field below.", "aot-warning");
        shareUrlField.focus(); shareUrlField.select();
      });
      document.getElementById("aot-reset-share-state").addEventListener("click", function () {
        const defaults = getDefaultState();
        input1.setRgb(defaults.i1, true);
        input2.setRgb(defaults.i2, true);
        persistShareState();
        updateShareUi("Defaults restored.", "aot-success");
      });

      const initialState = loadStateFromUrl();
      input1.setRgb(initialState.i1, true);
      input2.setRgb(initialState.i2, true);
      updateMixerOutput();
      persistShareState();
    })();
  </script>
</div>
