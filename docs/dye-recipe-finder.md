# Dye Recipe Finder

Interactive recipe search for *Age of Time* dyes.

Enter a target RGB color or choose a named dye, and this tool searches for a
shortest recipe using named dyes. The share link below the result preserves
the current target color only.

For dye sources, named dye RGB values, and mixing guidance, see
[Dyes](items/dyes.md).

<div id="aot-dye-recipe-finder">
  <style>
    #aot-dye-recipe-finder {
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
      #aot-dye-recipe-finder {
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
    #aot-dye-recipe-finder * { box-sizing: border-box; }
    #aot-dye-recipe-finder h2, #aot-dye-recipe-finder h3, #aot-dye-recipe-finder p { margin-top: 0; }
    #aot-dye-recipe-finder .aot-subtitle { color: var(--aot-muted); font-size: 0.94rem; max-width: 72ch; }
    #aot-dye-recipe-finder .aot-section {
      background: var(--aot-panel);
      border: 1px solid var(--aot-border);
      border-radius: 14px;
      padding: 14px;
      margin-top: 14px;
      backdrop-filter: blur(2px);
    }
    #aot-dye-recipe-finder .aot-card {
      background: var(--aot-panel-2);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 12px;
    }
    #aot-dye-recipe-finder label { display: block; font-weight: 650; font-size: 0.85rem; margin-bottom: 5px; }
    #aot-dye-recipe-finder select,
    #aot-dye-recipe-finder input,
    #aot-dye-recipe-finder button {
      width: 100%;
      border-radius: 9px;
      border: 1px solid var(--aot-border);
      padding: 8px 10px;
      background: rgba(255,255,255,0.85);
      color: var(--aot-text);
      font: inherit;
    }
    @media (prefers-color-scheme: dark) {
      #aot-dye-recipe-finder select, #aot-dye-recipe-finder input, #aot-dye-recipe-finder button {
        background: rgba(17,12,8,0.82);
      }
    }
    #aot-dye-recipe-finder input[type="number"] { appearance: textfield; }
    #aot-dye-recipe-finder input[type="number"]::-webkit-outer-spin-button,
    #aot-dye-recipe-finder input[type="number"]::-webkit-inner-spin-button { appearance: none; margin: 0; }
    #aot-dye-recipe-finder button {
      cursor: pointer;
      background: linear-gradient(180deg, var(--aot-accent-2), var(--aot-accent));
      color: var(--aot-button-text);
      border-color: rgba(78, 37, 10, 0.45);
      font-weight: 650;
    }
    #aot-dye-recipe-finder button:hover { filter: brightness(1.05); }
    #aot-dye-recipe-finder button.aot-secondary {
      background: transparent;
      color: var(--aot-text);
      border-color: var(--aot-border);
    }
    #aot-dye-recipe-finder .aot-color-row {
      display: grid;
      grid-template-columns: 76px 1fr;
      gap: 10px;
      align-items: center;
      margin-bottom: 10px;
    }
    #aot-dye-recipe-finder .aot-swatch {
      width: 76px;
      height: 76px;
      border-radius: 12px;
      border: 1px solid rgba(255,255,255,0.45);
      background: rgb(0,0,0);
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.08);
    }
    #aot-dye-recipe-finder .aot-rgb-inputs {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    #aot-dye-recipe-finder .aot-result-box,
    #aot-dye-recipe-finder .aot-share-url {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
    #aot-dye-recipe-finder .aot-result-box {
      background: rgba(255,255,255,0.55);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 12px;
      min-height: 70px;
      font-size: 0.9rem;
      overflow-x: auto;
    }
    #aot-dye-recipe-finder .aot-result-box .aot-empty-state {
      white-space: pre-wrap;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
    @media (prefers-color-scheme: dark) {
      #aot-dye-recipe-finder .aot-result-box { background: rgba(10,8,6,0.58); }
    }
    #aot-dye-recipe-finder .aot-results-summary {
      background: var(--aot-panel-2);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 10px 14px;
      display: grid;
      gap: 4px;
      font-size: 0.92rem;
    }
    #aot-dye-recipe-finder .aot-results-summary .aot-summary-meta {
      color: var(--aot-muted);
      font-size: 0.82rem;
    }
    #aot-dye-recipe-finder .aot-recipe-card {
      background: var(--aot-panel-2);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 12px 14px;
      margin-top: 12px;
    }
    #aot-dye-recipe-finder .aot-recipe-card-header {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1px solid var(--aot-border);
      padding-bottom: 8px;
      margin-bottom: 10px;
    }
    #aot-dye-recipe-finder .aot-recipe-card-header h4 { margin: 0; font-size: 1rem; }
    #aot-dye-recipe-finder .aot-recipe-card-header .aot-recipe-meta { color: var(--aot-muted); font-size: 0.85rem; }
    #aot-dye-recipe-finder .aot-recipe-section { margin-bottom: 12px; }
    #aot-dye-recipe-finder .aot-recipe-section:last-child { margin-bottom: 0; }
    #aot-dye-recipe-finder .aot-recipe-section-head {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 6px;
    }
    #aot-dye-recipe-finder .aot-recipe-section-head .aot-tree-hint { color: var(--aot-muted); font-size: 0.78rem; }
    #aot-dye-recipe-finder .aot-recipe-section > strong:first-child { display: block; margin-bottom: 6px; }
    #aot-dye-recipe-finder .aot-recipe-ingredients,
    #aot-dye-recipe-finder .aot-recipe-steps {
      margin: 0;
      padding-left: 22px;
    }
    #aot-dye-recipe-finder .aot-recipe-ingredients li,
    #aot-dye-recipe-finder .aot-recipe-steps li {
      margin-bottom: 4px;
      font-size: 0.9rem;
    }
    #aot-dye-recipe-finder .aot-swatch-inline {
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 3px;
      margin-right: 6px;
      vertical-align: -1px;
      border: 1px solid rgba(0,0,0,0.18);
    }
    #aot-dye-recipe-finder .aot-tree-wrapper {
      position: relative;
      margin-top: 6px;
    }
    #aot-dye-recipe-finder .aot-tree-viewport {
      position: relative;
      overflow: hidden;
      width: 100%;
      height: 520px;
      max-height: 70vh;
      border: 1px solid var(--aot-border);
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.45);
      touch-action: none;
      cursor: grab;
      user-select: none;
    }
    @media (max-width: 720px) {
      #aot-dye-recipe-finder .aot-tree-viewport { height: 360px; }
    }
    #aot-dye-recipe-finder .aot-tree-viewport:active { cursor: grabbing; }
    @media (prefers-color-scheme: dark) {
      #aot-dye-recipe-finder .aot-tree-viewport { background: rgba(10, 8, 6, 0.5); }
    }
    #aot-dye-recipe-finder .aot-tree-stage {
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      will-change: transform;
    }
    #aot-dye-recipe-finder .aot-tree-stage svg {
      display: block;
      max-width: none;
      max-height: none;
    }
    #aot-dye-recipe-finder .aot-tree-link {
      fill: none;
      stroke: var(--aot-muted);
      stroke-width: 2;
      opacity: 0.75;
    }
    #aot-dye-recipe-finder .aot-tree-node-rect {
      stroke: rgba(0, 0, 0, 0.28);
      stroke-width: 1;
    }
    #aot-dye-recipe-finder .aot-tree-node-text-primary {
      font-family: "Trebuchet MS", "Segoe UI", Tahoma, sans-serif;
      font-size: 12px;
      font-weight: 650;
      pointer-events: none;
    }
    #aot-dye-recipe-finder .aot-tree-node-text-secondary {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10px;
      pointer-events: none;
    }
    #aot-dye-recipe-finder .aot-tree-controls {
      position: absolute;
      top: 8px;
      right: 8px;
      display: flex;
      gap: 4px;
      z-index: 2;
    }
    #aot-dye-recipe-finder .aot-tree-btn {
      width: auto;
      min-width: 32px;
      padding: 4px 10px;
      font-size: 0.85rem;
      border-radius: 8px;
      line-height: 1;
    }
    #aot-dye-recipe-finder .aot-truncate-note,
    #aot-dye-recipe-finder .aot-fallback-note {
      color: var(--aot-muted);
      font-size: 0.85rem;
      margin-top: 8px;
    }
    .aot-tree-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(20, 14, 8, 0.62);
      backdrop-filter: blur(3px);
      z-index: 9999;
      display: flex;
      align-items: stretch;
      justify-content: center;
      padding: 24px;
      font-family: "Trebuchet MS", "Segoe UI", Tahoma, sans-serif;
      color: #2f2418;
    }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-overlay { background: rgba(0, 0, 0, 0.7); color: #f5eadb; }
    }
    .aot-tree-modal {
      background: linear-gradient(180deg, #f4efe5 0%, #ece1cf 100%);
      border: 1px solid #c7b293;
      border-radius: 14px;
      width: 100%;
      max-width: 1600px;
      max-height: 100%;
      display: flex;
      flex-direction: column;
      box-shadow: 0 24px 56px rgba(0, 0, 0, 0.35);
      overflow: hidden;
    }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal {
        background: linear-gradient(180deg, #21180f 0%, #18110c 100%);
        border-color: #735339;
      }
    }
    .aot-tree-modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
      border-bottom: 1px solid #c7b293;
    }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-header { border-bottom-color: #735339; }
    }
    .aot-tree-modal-header h3 {
      margin: 0;
      font-size: 1.05rem;
    }
    .aot-tree-modal-meta {
      color: #6f6254;
      font-size: 0.85rem;
      margin-left: 12px;
    }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-meta { color: #c1ab95; }
    }
    .aot-tree-modal-close {
      cursor: pointer;
      background: transparent;
      border: 1px solid #c7b293;
      color: inherit;
      padding: 6px 12px;
      border-radius: 8px;
      font: inherit;
      font-weight: 650;
    }
    .aot-tree-modal-close:hover { background: rgba(0,0,0,0.06); }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-close { border-color: #735339; }
      .aot-tree-modal-close:hover { background: rgba(255,255,255,0.06); }
    }
    .aot-tree-modal-body {
      position: relative;
      flex: 1;
      min-height: 0;
      display: flex;
    }
    .aot-tree-modal-viewport {
      position: relative;
      flex: 1;
      overflow: hidden;
      background: rgba(255,255,255,0.55);
      touch-action: none;
      cursor: grab;
      user-select: none;
    }
    .aot-tree-modal-viewport:active { cursor: grabbing; }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-viewport { background: rgba(10, 8, 6, 0.5); }
    }
    .aot-tree-modal-viewport .aot-tree-stage {
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      will-change: transform;
    }
    .aot-tree-modal-viewport .aot-tree-stage svg {
      display: block;
      max-width: none;
      max-height: none;
    }
    .aot-tree-modal-viewport .aot-tree-link {
      fill: none;
      stroke: #6f6254;
      stroke-width: 2;
      opacity: 0.75;
    }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-viewport .aot-tree-link { stroke: #c1ab95; }
    }
    .aot-tree-modal-viewport .aot-tree-node-rect {
      stroke: rgba(0, 0, 0, 0.28);
      stroke-width: 1;
    }
    .aot-tree-modal-viewport .aot-tree-node-text-primary {
      font-family: "Trebuchet MS", "Segoe UI", Tahoma, sans-serif;
      font-size: 12px;
      font-weight: 650;
      pointer-events: none;
    }
    .aot-tree-modal-viewport .aot-tree-node-text-secondary {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 10px;
      pointer-events: none;
    }
    .aot-tree-modal-controls {
      position: absolute;
      top: 12px;
      right: 12px;
      display: flex;
      gap: 4px;
      z-index: 2;
    }
    .aot-tree-modal-btn {
      cursor: pointer;
      background: linear-gradient(180deg, #9f5a20, #7a3f16);
      color: #fff7eb;
      border: 1px solid rgba(78, 37, 10, 0.45);
      padding: 6px 12px;
      border-radius: 8px;
      font: inherit;
      font-weight: 650;
      line-height: 1;
    }
    .aot-tree-modal-btn:hover { filter: brightness(1.05); }
    @media (prefers-color-scheme: dark) {
      .aot-tree-modal-btn {
        background: linear-gradient(180deg, #f0ad73, #df9156);
        color: #21150d;
        border-color: rgba(78, 37, 10, 0.55);
      }
    }
    #aot-dye-recipe-finder .aot-share-row {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
    }
    @media (max-width: 760px) {
      #aot-dye-recipe-finder .aot-share-row { grid-template-columns: 1fr; }
    }
    #aot-dye-recipe-finder .aot-inline-note { margin-top: 8px; font-size: 0.85rem; color: var(--aot-muted); }
    #aot-dye-recipe-finder .aot-share-status { min-height: 1.2em; margin-top: 8px; font-size: 0.88rem; }
    #aot-dye-recipe-finder .aot-share-url { font-size: 0.82rem; }
    #aot-dye-recipe-finder .aot-warning { color: var(--aot-danger); font-weight: 650; }
    #aot-dye-recipe-finder .aot-success { color: var(--aot-success); font-weight: 650; }
  </style>

  <h2>Age of Time Dye Recipe Finder</h2>
  <p class="aot-subtitle">Search for a shortest exact named-dye recipe for a target color. If the target is itself a named dye, the direct dye is excluded so the tool finds how to make it from other dyes instead of just returning the dye itself.</p>

  <div class="aot-section" aria-labelledby="aot-path-title">
    <h3 id="aot-path-title">Recipe Finder</h3>
    <div class="aot-card">
      <div class="aot-color-row">
        <div class="aot-swatch" id="aot-target-swatch"></div>
        <div>
          <label>Target named dye</label>
          <select id="aot-target-select"></select>
        </div>
      </div>
      <div class="aot-rgb-inputs">
        <div><label>Target R</label><input type="number" min="0" max="255" step="1" id="aot-target-r" /></div>
        <div><label>Target G</label><input type="number" min="0" max="255" step="1" id="aot-target-g" /></div>
        <div><label>Target B</label><input type="number" min="0" max="255" step="1" id="aot-target-b" /></div>
      </div>
      <div style="margin-top: 10px;">
        <button type="button" id="aot-find-recipe">Find Shortest Recipe</button>
      </div>
    </div>

    <div class="aot-result-box" id="aot-recipe-result" style="margin-top: 12px;"><div class="aot-empty-state">Enter a target color, then click Find Shortest Recipe.</div></div>

    <div class="aot-card" style="margin-top: 12px;">
      <h3>Share State</h3>
      <div class="aot-share-row">
        <button type="button" id="aot-copy-share-link">Copy Share Link</button>
        <button type="button" class="aot-secondary" id="aot-reset-share-state">Reset to Defaults</button>
      </div>
      <div class="aot-inline-note">Anyone opening the shared link will load the same recipe target.</div>
      <div class="aot-share-status" id="aot-share-status"></div>
      <input class="aot-share-url" id="aot-share-url" type="text" readonly aria-label="Shareable dye recipe finder link" />
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
      const ACQUISITION_ONLY_NAMES = new Set(["Bleach", "Pitch Black Dye"]);
      // Maximum total mix depth the tool will search for ANY recipe. Bump if
      // you want to find very deep recipes (memory cost grows with depth).
      const MAX_MIX_DEPTH = 30;
      // Bidirectional split. Forward search builds chain recipes from the
      // base dyes, backward search builds parent links from the target.
      // Forward memory cost grows fastest, so keep it modest.
      const FORWARD_SEARCH_DEPTH = 6;
      const BACKWARD_SEARCH_DEPTH = Math.max(0, MAX_MIX_DEPTH - FORWARD_SEARCH_DEPTH);
      const MAX_TOTAL_MIXES = FORWARD_SEARCH_DEPTH + BACKWARD_SEARCH_DEPTH;
      // Safety cap when building bidirectional layers; once a layer grows
      // past this, we stop building deeper layers from that side.
      const MAX_LAYER_SIZE = 600000;
      // Maximum number of unique alternative recipes to display at the
      // minimum found depth.
      const MAX_ALTERNATIVES = 30;
      // Time budget (ms) for the alternative enumeration. The search bails
      // out once this elapses so very deep targets stay responsive.
      const ENUMERATION_TIME_BUDGET_MS = 1500;
      const SHARE_PARAM = "state";
      const shareStatus = document.getElementById("aot-share-status");
      const shareUrlField = document.getElementById("aot-share-url");
      const targetSelect = document.getElementById("aot-target-select");
      const targetR = document.getElementById("aot-target-r");
      const targetG = document.getElementById("aot-target-g");
      const targetB = document.getElementById("aot-target-b");
      const targetSwatch = document.getElementById("aot-target-swatch");
      const recipeResult = document.getElementById("aot-recipe-result");

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
      function getDefaultState() { return { t: [127, 127, 127] }; }
      function buildShareUrl() {
        const url = new URL(window.location.href);
        url.searchParams.set(SHARE_PARAM, encodeShareState({ t: getTargetRgb() }));
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
          return { t: normalizeRgb(parsed.t || getDefaultState().t) };
        } catch (error) {
          updateShareUi("Share link could not be parsed. Defaults loaded instead.", "aot-warning");
          return getDefaultState();
        }
      }
      function getTargetRgb() { return normalizeRgb([targetR.value, targetG.value, targetB.value]); }
      function syncTargetSelectFromRgb() {
        const match = findNamedDyeByRgb(getTargetRgb());
        targetSelect.value = match ? match.name : OTHER_VALUE;
      }
      function updateTargetSwatch() { targetSwatch.style.background = rgbCss(getTargetRgb()); }
      function setTargetRgb(rgb, silent) {
        const normalized = normalizeRgb(rgb);
        targetR.value = normalized[0];
        targetG.value = normalized[1];
        targetB.value = normalized[2];
        syncTargetSelectFromRgb();
        updateTargetSwatch();
        if (!silent) persistShareState();
      }
      fillDyeSelect(targetSelect, true);
      targetSelect.addEventListener("change", function () {
        if (targetSelect.value === OTHER_VALUE) {
          syncTargetSelectFromRgb();
          updateTargetSwatch();
          persistShareState();
          return;
        }
        const dye = findNamedDyeByName(targetSelect.value);
        if (dye) setTargetRgb(dye.rgb);
      });
      [targetR, targetG, targetB].forEach(function (input) {
        input.addEventListener("input", function () {
          input.value = clamp(Math.floor(Number(input.value || 0)), 0, 255);
          syncTargetSelectFromRgb();
          updateTargetSwatch();
          persistShareState();
        });
      });

      function recipeExpression(recipe) {
        if (recipe.type === "base") return recipe.name;
        return "(" + recipeExpression(recipe.left) + " + " + recipeExpression(recipe.right) + ")";
      }
      function flattenRecipeChain(recipe, steps) {
        steps = steps || [];
        if (recipe.type === "base") return { label: recipe.name, rgb: recipe.rgb, steps: steps };
        const left = flattenRecipeChain(recipe.left, steps);
        const rightLabel = recipeExpression(recipe.right);
        const stepNumber = steps.length + 1;
        const resultLabel = "Result " + stepNumber;
        steps.push({
          inputLabel: left.label,
          inputRgb: left.rgb,
          ingredientLabel: rightLabel,
          ingredientRgb: recipe.right.rgb,
          resultLabel: resultLabel,
          resultRgb: recipe.rgb
        });
        return { label: resultLabel, rgb: recipe.rgb, steps: steps };
      }
      function simplifiedRecipeSteps(recipe) { return flattenRecipeChain(recipe).steps; }
      function ingredientCounts(recipe, counts) {
        counts = counts || new Map();
        if (recipe.type === "base") {
          const current = counts.get(recipe.name) || { count: 0, rgb: recipe.rgb };
          current.count += 1;
          counts.set(recipe.name, current);
          return counts;
        }
        ingredientCounts(recipe.left, counts);
        ingredientCounts(recipe.right, counts);
        return counts;
      }
      function recipeFlowLines(recipe) {
        const steps = simplifiedRecipeSteps(recipe);
        if (steps.length === 0) return [recipeExpression(recipe) + " (" + rgbText(recipe.rgb) + ")"];
        const lines = [];
        const first = steps[0];
        lines.push("Start with: " + first.inputLabel + " (" + rgbText(first.inputRgb) + ")");
        steps.forEach(function (step, index) {
          lines.push("  + " + step.ingredientLabel + " (" + rgbText(step.ingredientRgb) + ")");
          lines.push("  = " + (index === steps.length - 1 ? "Final" : step.resultLabel) + " (" + rgbText(step.resultRgb) + ")");
        });
        return lines;
      }
      function ingredientSummaryLines(recipe) {
        const counts = Array.from(ingredientCounts(recipe).entries());
        counts.sort(function (a, b) { return b[1].count - a[1].count || a[0].localeCompare(b[0]); });
        return counts.map(function (entry) {
          const name = entry[0];
          const data = entry[1];
          return data.count + "x " + name + " (" + rgbText(data.rgb) + ")";
        });
      }
      function recipeDepth(recipe) {
        if (recipe.type === "base") return 0;
        return 1 + Math.max(recipeDepth(recipe.left), recipeDepth(recipe.right));
      }
      function recipeIngredientCount(recipe) {
        if (recipe.type === "base") return 1;
        return recipeIngredientCount(recipe.left) + recipeIngredientCount(recipe.right);
      }
      function inverseCandidates(targetChannel, ingredientChannel) {
        const low = (2 * targetChannel) - ingredientChannel;
        const high = (2 * targetChannel) + 1 - ingredientChannel;
        const values = [];
        for (let value = low; value <= high; value++) {
          if (value >= 0 && value <= 255) values.push(value);
        }
        return values;
      }
      function inverseMixCandidates(targetRgb, ingredientRgb) {
        const target = normalizeRgb(targetRgb);
        const ingredient = normalizeRgb(ingredientRgb);
        const rValues = inverseCandidates(target[0], ingredient[0]);
        const gValues = inverseCandidates(target[1], ingredient[1]);
        const bValues = inverseCandidates(target[2], ingredient[2]);
        if (!rValues.length || !gValues.length || !bValues.length) return [];
        const results = [];
        rValues.forEach(function (r) {
          gValues.forEach(function (g) {
            bValues.forEach(function (b) { results.push([r, g, b]); });
          });
        });
        return results;
      }
      function colorDistance(a, b) {
        const aa = normalizeRgb(a);
        const bb = normalizeRgb(b);
        return Math.abs(aa[0] - bb[0]) + Math.abs(aa[1] - bb[1]) + Math.abs(aa[2] - bb[2]);
      }
      function precomputeForwardLevels(baseRecipes, maxDepth) {
        const levels = [new Map()];
        baseRecipes.forEach(function (recipe) {
          const key = rgbKey(recipe.rgb);
          if (!levels[0].has(key)) levels[0].set(key, recipe);
        });
        for (let depth = 1; depth <= maxDepth; depth++) {
          const level = new Map();
          let abort = false;
          levels[depth - 1].forEach(function (previousRecipe) {
            if (abort) return;
            baseRecipes.forEach(function (ingredientRecipe) {
              if (abort) return;
              const mixed = mixRgb(previousRecipe.rgb, ingredientRecipe.rgb);
              const key = rgbKey(mixed);
              if (level.has(key)) return;
              level.set(key, {
                type: "mix",
                rgb: mixed,
                left: previousRecipe,
                right: ingredientRecipe
              });
              if (level.size >= MAX_LAYER_SIZE) abort = true;
            });
          });
          levels.push(level);
          if (level.size === 0 || abort) break;
        }
        return levels;
      }
      function precomputeBackwardLevels(targetRgb, baseRecipes, maxDepth) {
        const target = normalizeRgb(targetRgb);
        const levels = [new Map([[rgbKey(target), { rgb: target }]])];
        const parents = [new Map()];
        for (let depth = 1; depth <= maxDepth; depth++) {
          const previousLevel = levels[depth - 1];
          const level = new Map();
          const parentMap = new Map();
          let abort = false;
          previousLevel.forEach(function (state) {
            if (abort) return;
            baseRecipes.forEach(function (ingredientRecipe) {
              if (abort) return;
              inverseMixCandidates(state.rgb, ingredientRecipe.rgb).forEach(function (previousRgb) {
                if (abort) return;
                const key = rgbKey(previousRgb);
                if (level.has(key)) return;
                level.set(key, { rgb: previousRgb });
                parentMap.set(key, {
                  nextRgb: state.rgb,
                  ingredientRecipe: ingredientRecipe
                });
                if (level.size >= MAX_LAYER_SIZE) abort = true;
              });
            });
          });
          levels.push(level);
          parents.push(parentMap);
          if (level.size === 0 || abort) break;
        }
        return { levels: levels, parents: parents };
      }
      function buildRecipeFromMeetingPoint(startRgb, backwardDepth, parents, forwardRecipe) {
        let recipe = forwardRecipe;
        let currentKey = rgbKey(startRgb);
        for (let depth = backwardDepth; depth >= 1; depth--) {
          const parent = parents[depth].get(currentKey);
          if (!parent) return null;
          recipe = {
            type: "mix",
            rgb: normalizeRgb(parent.nextRgb),
            left: recipe,
            right: parent.ingredientRecipe
          };
          currentKey = rgbKey(parent.nextRgb);
        }
        return recipe;
      }
      function countLevelStates(levels) {
        return levels.reduce(function (sum, level) { return sum + level.size; }, 0);
      }
      function findShortestRecipe(targetRgb) {
        const target = normalizeRgb(targetRgb);
        const targetKey = rgbKey(target);
        const exactTargetDye = findNamedDyeByRgb(target);
        const excludedName = exactTargetDye ? exactTargetDye.name : null;
        if (exactTargetDye && ACQUISITION_ONLY_NAMES.has(exactTargetDye.name)) {
          return {
            recipe: null,
            exact: false,
            excludedName: excludedName,
            searchedStates: 0,
            acquisitionOnly: true
          };
        }
        const baseRecipes = NAMED_DYES.filter(function (dye) {
          return dye.name !== excludedName;
        }).map(function (dye) {
          return { type: "base", name: dye.name, rgb: normalizeRgb(dye.rgb) };
        });
        const forwardLevels = precomputeForwardLevels(baseRecipes, FORWARD_SEARCH_DEPTH);
        const backward = precomputeBackwardLevels(target, baseRecipes, BACKWARD_SEARCH_DEPTH);
        const builtForwardDepth = forwardLevels.length - 1;
        const builtBackwardDepth = backward.levels.length - 1;
        const searchedStates = countLevelStates(forwardLevels) + countLevelStates(backward.levels);

        for (let totalDepth = 0; totalDepth <= MAX_TOTAL_MIXES; totalDepth++) {
          const minForwardDepth = Math.max(0, totalDepth - builtBackwardDepth);
          const maxForwardDepth = Math.min(builtForwardDepth, totalDepth);
          for (let forwardDepth = minForwardDepth; forwardDepth <= maxForwardDepth; forwardDepth++) {
            const backwardDepth = totalDepth - forwardDepth;
            const forwardLevel = forwardLevels[forwardDepth];
            const backwardLevel = backward.levels[backwardDepth];
            if (!forwardLevel || !backwardLevel) continue;
            const iterateForward = forwardLevel.size <= backwardLevel.size;
            const source = iterateForward ? forwardLevel : backwardLevel;
            for (const entry of source) {
              const currentKey = entry[0];
              if (!(iterateForward ? backwardLevel.has(currentKey) : forwardLevel.has(currentKey))) continue;
              const forwardRecipe = iterateForward ? entry[1] : forwardLevel.get(currentKey);
              const joinRgb = normalizeRgb(forwardRecipe.rgb);
              const recipe = buildRecipeFromMeetingPoint(joinRgb, backwardDepth, backward.parents, forwardRecipe);
              if (recipe) {
                return {
                  recipe: recipe,
                  exact: true,
                  excludedName: excludedName,
                  searchedStates: searchedStates,
                  forwardLevels: forwardLevels,
                  backward: backward,
                  baseRecipes: baseRecipes
                };
              }
            }
          }
        }
        return {
          recipe: null,
          exact: false,
          excludedName: excludedName,
          searchedStates: searchedStates,
          maxMixDepth: MAX_TOTAL_MIXES
        };
      }

      function chainSignature(recipe) {
        if (recipe.type === "base") return "B|" + recipe.name;
        const rightPath = [];
        let cur = recipe;
        while (cur.type === "mix" && cur.left.type === "mix") {
          rightPath.push(cur.right.name);
          cur = cur.left;
        }
        if (cur.type !== "mix") return "B|" + cur.name;
        const innerNames = [cur.left.name, cur.right.name].sort().join("&");
        return rightPath.join("|") + "||" + innerNames;
      }

      function enumerateChainsAtDepth(target, depth, baseRecipes, out, limit, deadline) {
        if (out.length >= limit) return;
        if (Date.now() > deadline) return;
        const normTarget = normalizeRgb(target);
        if (depth === 0) {
          const targetKey = rgbKey(normTarget);
          for (let i = 0; i < baseRecipes.length; i++) {
            if (out.length >= limit) return;
            const base = baseRecipes[i];
            if (rgbKey(base.rgb) === targetKey) {
              out.push({ type: "base", name: base.name, rgb: normalizeRgb(base.rgb) });
            }
          }
          return;
        }
        for (let i = 0; i < baseRecipes.length; i++) {
          if (out.length >= limit) return;
          if (Date.now() > deadline) return;
          const base = baseRecipes[i];
          const baseRecipe = { type: "base", name: base.name, rgb: normalizeRgb(base.rgb) };
          const candidates = inverseMixCandidates(normTarget, base.rgb);
          for (let c = 0; c < candidates.length; c++) {
            if (out.length >= limit) return;
            if (Date.now() > deadline) return;
            const prevRgb = candidates[c];
            const sub = [];
            const subLimit = (limit - out.length) * 2 + 4;
            enumerateChainsAtDepth(prevRgb, depth - 1, baseRecipes, sub, subLimit, deadline);
            for (let s = 0; s < sub.length; s++) {
              if (out.length >= limit) return;
              out.push({
                type: "mix",
                rgb: normTarget,
                left: sub[s],
                right: baseRecipe
              });
            }
          }
        }
      }

      function findAllShortestRecipes(targetRgb) {
        const single = findShortestRecipe(targetRgb);
        if (!single.recipe) {
          return {
            recipes: [],
            excludedName: single.excludedName,
            searchedStates: single.searchedStates,
            acquisitionOnly: single.acquisitionOnly,
            maxMixDepth: single.maxMixDepth,
            enumerated: false,
            minDepth: -1
          };
        }
        const minDepth = recipeDepth(single.recipe);
        const baseRecipes = single.baseRecipes;
        const deadline = Date.now() + ENUMERATION_TIME_BUDGET_MS;

        const seen = new Set();
        const unique = [];
        const singleSig = chainSignature(single.recipe);
        seen.add(singleSig);
        unique.push(single.recipe);

        const rawCap = Math.min(MAX_ALTERNATIVES * 50, 5000);
        const raw = [];
        let enumeratedFully = true;
        try {
          enumerateChainsAtDepth(normalizeRgb(targetRgb), minDepth, baseRecipes, raw, rawCap, deadline);
          if (Date.now() > deadline || raw.length >= rawCap) enumeratedFully = false;
        } catch (err) {
          enumeratedFully = false;
        }

        for (let i = 0; i < raw.length; i++) {
          if (unique.length >= MAX_ALTERNATIVES) break;
          const sig = chainSignature(raw[i]);
          if (seen.has(sig)) continue;
          seen.add(sig);
          unique.push(raw[i]);
        }

        return {
          recipes: unique,
          excludedName: single.excludedName,
          searchedStates: single.searchedStates,
          minDepth: minDepth,
          enumerated: true,
          truncated: !enumeratedFully || unique.length >= MAX_ALTERNATIVES
        };
      }

      function escapeHtml(value) {
        return String(value)
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#39;");
      }

      function textColorFor(rgb) {
        const n = normalizeRgb(rgb);
        const brightness = 0.299 * n[0] + 0.587 * n[1] + 0.114 * n[2];
        return brightness > 140 ? "#1a1a1a" : "#ffffff";
      }

      function assignTreeLayout(recipe) {
        function assignLevel(node) {
          if (node.type === "base") { node.level = 0; return 0; }
          const l = assignLevel(node.left);
          const r = assignLevel(node.right);
          node.level = Math.max(l, r) + 1;
          return node.level;
        }
        assignLevel(recipe);

        // Bracket layout: place each leaf at parent.level - 1 so siblings
        // share a column rather than stacking all leaves at the deepest
        // column. This turns a chain into a readable bracket on its side.
        function adjustLeafColumns(node) {
          if (node.type !== "mix") return;
          if (node.left.type === "base") {
            node.left.level = Math.max(0, node.level - 1);
          } else {
            adjustLeafColumns(node.left);
          }
          if (node.right.type === "base") {
            node.right.level = Math.max(0, node.level - 1);
          } else {
            adjustLeafColumns(node.right);
          }
        }
        adjustLeafColumns(recipe);

        let leafCounter = 0;
        function assignY(node) {
          if (node.type === "base") { node.yIndex = leafCounter++; return; }
          assignY(node.left);
          assignY(node.right);
          node.yIndex = (node.left.yIndex + node.right.yIndex) / 2;
        }
        assignY(recipe);

        let stepCounter = 1;
        function assignStep(node) {
          if (node.type === "base") return;
          assignStep(node.left);
          assignStep(node.right);
          node.step = stepCounter++;
        }
        assignStep(recipe);

        let sumLevel = 0;
        let sumYIndex = 0;
        let nodeCount = 0;
        function accumulate(node) {
          sumLevel += node.level;
          sumYIndex += node.yIndex;
          nodeCount += 1;
          if (node.type === "mix") {
            accumulate(node.left);
            accumulate(node.right);
          }
        }
        accumulate(recipe);
        const avgLevel = nodeCount > 0 ? sumLevel / nodeCount : 0;
        const avgYIndex = nodeCount > 0 ? sumYIndex / nodeCount : 0;

        return {
          totalLeaves: leafCounter,
          totalSteps: stepCounter - 1,
          maxLevel: recipe.level,
          avgLevel: avgLevel,
          avgYIndex: avgYIndex
        };
      }

      function buildTreeSvg(recipe) {
        const cloned = JSON.parse(JSON.stringify(recipe));
        const layout = assignTreeLayout(cloned);
        const COL_WIDTH = 200;
        const ROW_HEIGHT = 58;
        const NODE_WIDTH = 170;
        const NODE_HEIGHT = 42;
        const PADDING = 22;
        const width = PADDING * 2 + layout.maxLevel * COL_WIDTH + NODE_WIDTH;
        const height = PADDING * 2 + Math.max(0, layout.totalLeaves - 1) * ROW_HEIGHT + NODE_HEIGHT;

        function nodeX(node) { return PADDING + node.level * COL_WIDTH; }
        function nodeY(node) { return PADDING + node.yIndex * ROW_HEIGHT; }

        const NS = "http://www.w3.org/2000/svg";
        const svg = document.createElementNS(NS, "svg");
        svg.setAttribute("xmlns", NS);
        svg.setAttribute("width", String(width));
        svg.setAttribute("height", String(height));
        svg.setAttribute("viewBox", "0 0 " + width + " " + height);

        const linksGroup = document.createElementNS(NS, "g");
        const nodesGroup = document.createElementNS(NS, "g");

        function nodeLabels(node) {
          if (node.type === "base") return { primary: node.name, secondary: rgbText(node.rgb) };
          if (node === cloned) return { primary: "Final", secondary: rgbText(node.rgb) };
          return { primary: "Result " + node.step, secondary: rgbText(node.rgb) };
        }

        function walk(node, parent) {
          if (parent) {
            const x1 = nodeX(node) + NODE_WIDTH;
            const y1 = nodeY(node) + NODE_HEIGHT / 2;
            const x2 = nodeX(parent);
            const y2 = nodeY(parent) + NODE_HEIGHT / 2;
            const midX = (x1 + x2) / 2;
            const path = document.createElementNS(NS, "path");
            path.setAttribute("d", "M " + x1 + " " + y1 + " H " + midX + " V " + y2 + " H " + x2);
            path.setAttribute("class", "aot-tree-link");
            linksGroup.appendChild(path);
          }
          const labels = nodeLabels(node);
          const fill = rgbCss(node.rgb);
          const textColor = textColorFor(node.rgb);
          const g = document.createElementNS(NS, "g");
          g.setAttribute("transform", "translate(" + nodeX(node) + ", " + nodeY(node) + ")");
          const rect = document.createElementNS(NS, "rect");
          rect.setAttribute("width", String(NODE_WIDTH));
          rect.setAttribute("height", String(NODE_HEIGHT));
          rect.setAttribute("rx", "8");
          rect.setAttribute("fill", fill);
          rect.setAttribute("class", "aot-tree-node-rect");
          g.appendChild(rect);
          const title = document.createElementNS(NS, "title");
          title.textContent = labels.primary + " (" + labels.secondary + ")";
          g.appendChild(title);
          const primary = document.createElementNS(NS, "text");
          primary.setAttribute("x", String(NODE_WIDTH / 2));
          primary.setAttribute("y", "17");
          primary.setAttribute("text-anchor", "middle");
          primary.setAttribute("fill", textColor);
          primary.setAttribute("class", "aot-tree-node-text-primary");
          primary.textContent = labels.primary;
          g.appendChild(primary);
          const secondary = document.createElementNS(NS, "text");
          secondary.setAttribute("x", String(NODE_WIDTH / 2));
          secondary.setAttribute("y", "32");
          secondary.setAttribute("text-anchor", "middle");
          secondary.setAttribute("fill", textColor);
          secondary.setAttribute("class", "aot-tree-node-text-secondary");
          secondary.textContent = labels.secondary;
          g.appendChild(secondary);
          nodesGroup.appendChild(g);
          if (node.type === "mix") {
            walk(node.left, node);
            walk(node.right, node);
          }
        }
        walk(cloned, null);
        svg.appendChild(linksGroup);
        svg.appendChild(nodesGroup);
        const centerX = PADDING + layout.avgLevel * COL_WIDTH + NODE_WIDTH / 2;
        const centerY = PADDING + layout.avgYIndex * ROW_HEIGHT + NODE_HEIGHT / 2;
        return { svg: svg, width: width, height: height, centerX: centerX, centerY: centerY };
      }

      function attachPanZoom(viewport, stage, contentWidth, contentHeight, centerX, centerY) {
        const svg = stage.querySelector("svg");
        const focusX = (typeof centerX === "number" && isFinite(centerX)) ? centerX : contentWidth / 2;
        const focusY = (typeof centerY === "number" && isFinite(centerY)) ? centerY : contentHeight / 2;
        let scale = 1;
        let tx = 0;
        let ty = 0;
        function apply() {
          if (svg) {
            const w = contentWidth * scale;
            const h = contentHeight * scale;
            svg.style.width = w + "px";
            svg.style.height = h + "px";
            svg.setAttribute("width", String(w));
            svg.setAttribute("height", String(h));
          }
          stage.style.transform = "translate(" + tx + "px, " + ty + "px)";
        }
        function fit() {
          const rect = viewport.getBoundingClientRect();
          if (rect.width === 0 || rect.height === 0) {
            requestAnimationFrame(fit);
            return;
          }
          const fitScale = Math.min(rect.width / contentWidth, rect.height / contentHeight);
          scale = Math.min(fitScale * 0.95, 2);
          if (!isFinite(scale) || scale <= 0) scale = 1;
          tx = rect.width / 2 - focusX * scale;
          ty = rect.height / 2 - focusY * scale;
          apply();
        }
        function zoomAtPoint(factor, px, py) {
          const newScale = Math.min(Math.max(scale * factor, 0.05), 20);
          tx = px - (px - tx) * (newScale / scale);
          ty = py - (py - ty) * (newScale / scale);
          scale = newScale;
          apply();
        }
        function zoomCentered(factor) {
          const rect = viewport.getBoundingClientRect();
          zoomAtPoint(factor, rect.width / 2, rect.height / 2);
        }
        viewport.addEventListener("wheel", function (event) {
          event.preventDefault();
          const factor = Math.exp(-event.deltaY * 0.0015);
          const rect = viewport.getBoundingClientRect();
          zoomAtPoint(factor, event.clientX - rect.left, event.clientY - rect.top);
        }, { passive: false });
        const pointers = new Map();
        let dragging = false;
        let lastX = 0;
        let lastY = 0;
        let pinchStartDist = 0;
        let pinchStartScale = 1;
        viewport.addEventListener("pointerdown", function (event) {
          viewport.setPointerCapture(event.pointerId);
          pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
          if (pointers.size === 1) {
            dragging = true;
            lastX = event.clientX;
            lastY = event.clientY;
          } else if (pointers.size === 2) {
            const pts = Array.from(pointers.values());
            pinchStartDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y) || 1;
            pinchStartScale = scale;
            dragging = false;
          }
        });
        viewport.addEventListener("pointermove", function (event) {
          if (!pointers.has(event.pointerId)) return;
          pointers.set(event.pointerId, { x: event.clientX, y: event.clientY });
          if (pointers.size === 1 && dragging) {
            tx += event.clientX - lastX;
            ty += event.clientY - lastY;
            lastX = event.clientX;
            lastY = event.clientY;
            apply();
          } else if (pointers.size === 2) {
            const pts = Array.from(pointers.values());
            const dist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y) || 1;
            const factor = dist / pinchStartDist;
            const newScale = Math.min(Math.max(pinchStartScale * factor, 0.05), 20);
            const rect = viewport.getBoundingClientRect();
            const cx = (pts[0].x + pts[1].x) / 2 - rect.left;
            const cy = (pts[0].y + pts[1].y) / 2 - rect.top;
            tx = cx - (cx - tx) * (newScale / scale);
            ty = cy - (cy - ty) * (newScale / scale);
            scale = newScale;
            apply();
          }
        });
        function endPointer(event) {
          pointers.delete(event.pointerId);
          if (pointers.size === 0) {
            dragging = false;
          } else if (pointers.size === 1) {
            const remaining = Array.from(pointers.values())[0];
            dragging = true;
            lastX = remaining.x;
            lastY = remaining.y;
          }
        }
        viewport.addEventListener("pointerup", endPointer);
        viewport.addEventListener("pointercancel", endPointer);
        viewport.addEventListener("pointerleave", endPointer);
        return { fit: fit, zoomIn: function () { zoomCentered(1.25); }, zoomOut: function () { zoomCentered(0.8); } };
      }

      function renderTreeIntoContainer(container, recipe, recipeLabel) {
        const built = buildTreeSvg(recipe);
        const stage = document.createElement("div");
        stage.className = "aot-tree-stage";
        stage.appendChild(built.svg);
        const viewport = container.querySelector(".aot-tree-viewport");
        viewport.innerHTML = "";
        viewport.appendChild(stage);
        const controls = attachPanZoom(viewport, stage, built.width, built.height, built.centerX, built.centerY);
        const buttons = container.querySelectorAll(".aot-tree-btn");
        buttons.forEach(function (btn) {
          btn.addEventListener("click", function () {
            const action = btn.getAttribute("data-action");
            if (action === "zoom-in") controls.zoomIn();
            else if (action === "zoom-out") controls.zoomOut();
            else if (action === "fit") controls.fit();
            else if (action === "expand") openTreeModal(recipe, recipeLabel);
          });
        });
        requestAnimationFrame(controls.fit);
      }

      let modalKeyHandler = null;
      function openTreeModal(recipe, recipeLabel) {
        closeTreeModal();
        const overlay = document.createElement("div");
        overlay.className = "aot-tree-modal-overlay";
        const modal = document.createElement("div");
        modal.className = "aot-tree-modal";

        const header = document.createElement("div");
        header.className = "aot-tree-modal-header";
        const titleWrap = document.createElement("div");
        const title = document.createElement("h3");
        title.textContent = "Tree view";
        titleWrap.appendChild(title);
        if (recipeLabel) {
          const meta = document.createElement("span");
          meta.className = "aot-tree-modal-meta";
          meta.textContent = recipeLabel;
          title.appendChild(document.createTextNode(" "));
          title.appendChild(meta);
        }
        const closeBtn = document.createElement("button");
        closeBtn.type = "button";
        closeBtn.className = "aot-tree-modal-close";
        closeBtn.textContent = "Close";
        closeBtn.setAttribute("aria-label", "Close tree view");
        header.appendChild(titleWrap);
        header.appendChild(closeBtn);

        const body = document.createElement("div");
        body.className = "aot-tree-modal-body";
        const viewport = document.createElement("div");
        viewport.className = "aot-tree-modal-viewport";
        const controlsEl = document.createElement("div");
        controlsEl.className = "aot-tree-modal-controls";
        controlsEl.innerHTML =
          "<button type=\"button\" class=\"aot-tree-modal-btn\" data-action=\"zoom-out\" aria-label=\"Zoom out\">&minus;</button>" +
          "<button type=\"button\" class=\"aot-tree-modal-btn\" data-action=\"zoom-in\" aria-label=\"Zoom in\">+</button>" +
          "<button type=\"button\" class=\"aot-tree-modal-btn\" data-action=\"fit\" aria-label=\"Fit to view\">Fit</button>";
        body.appendChild(viewport);
        body.appendChild(controlsEl);

        modal.appendChild(header);
        modal.appendChild(body);
        overlay.appendChild(modal);
        document.body.appendChild(overlay);

        const built = buildTreeSvg(recipe);
        const stage = document.createElement("div");
        stage.className = "aot-tree-stage";
        stage.appendChild(built.svg);
        viewport.appendChild(stage);

        const controls = attachPanZoom(viewport, stage, built.width, built.height, built.centerX, built.centerY);
        controlsEl.querySelectorAll(".aot-tree-modal-btn").forEach(function (btn) {
          btn.addEventListener("click", function () {
            const action = btn.getAttribute("data-action");
            if (action === "zoom-in") controls.zoomIn();
            else if (action === "zoom-out") controls.zoomOut();
            else if (action === "fit") controls.fit();
          });
        });
        requestAnimationFrame(controls.fit);

        closeBtn.addEventListener("click", closeTreeModal);
        overlay.addEventListener("click", function (event) {
          if (event.target === overlay) closeTreeModal();
        });
        modalKeyHandler = function (event) {
          if (event.key === "Escape") closeTreeModal();
        };
        document.addEventListener("keydown", modalKeyHandler);
      }

      function closeTreeModal() {
        if (modalKeyHandler) {
          document.removeEventListener("keydown", modalKeyHandler);
          modalKeyHandler = null;
        }
        const existing = document.querySelector(".aot-tree-modal-overlay");
        if (existing) existing.remove();
      }

      function buildIngredientItem(line, rgb) {
        const swatch = "<span class=\"aot-swatch-inline\" style=\"background: " + rgbCss(rgb) + ";\"></span>";
        return "<li>" + swatch + escapeHtml(line) + "</li>";
      }

      function renderRecipeCard(recipe, index, total, treeIdAttr) {
        const depth = recipeDepth(recipe);
        const ingredients = ingredientSummaryLines(recipe);
        const ingredientEntries = Array.from(ingredientCounts(recipe).entries()).sort(function (a, b) {
          return b[1].count - a[1].count || a[0].localeCompare(b[0]);
        });
        const steps = simplifiedRecipeSteps(recipe);

        let html = "<div class=\"aot-recipe-card\">";
        html += "<div class=\"aot-recipe-card-header\">";
        html += "<h4>Recipe " + (index + 1) + " of " + total + "</h4>";
        html += "<span class=\"aot-recipe-meta\">" + recipeIngredientCount(recipe) + " dye" + (recipeIngredientCount(recipe) === 1 ? "" : "s") + ", " + depth + " mix" + (depth === 1 ? "" : "es") + "</span>";
        html += "</div>";

        html += "<div class=\"aot-recipe-section\">";
        html += "<strong>Ingredients</strong>";
        html += "<ul class=\"aot-recipe-ingredients\">";
        for (let i = 0; i < ingredientEntries.length; i++) {
          const entry = ingredientEntries[i];
          const line = ingredients[i] || (entry[1].count + "x " + entry[0]);
          html += buildIngredientItem(line, entry[1].rgb);
        }
        html += "</ul>";
        html += "</div>";

        html += "<div class=\"aot-recipe-section\">";
        html += "<strong>Mix steps</strong>";
        if (steps.length === 0) {
          html += "<p>Use " + escapeHtml(recipeExpression(recipe)) + " directly.</p>";
        } else {
          html += "<ol class=\"aot-recipe-steps\">";
          steps.forEach(function (step, idx) {
            const resultName = idx === steps.length - 1 ? "Final" : step.resultLabel;
            html += "<li>Mix <strong>" + escapeHtml(step.inputLabel) + "</strong> (" + escapeHtml(rgbText(step.inputRgb)) + ") with <strong>" + escapeHtml(step.ingredientLabel) + "</strong> (" + escapeHtml(rgbText(step.ingredientRgb)) + ") &rarr; " + escapeHtml(resultName) + " (" + escapeHtml(rgbText(step.resultRgb)) + ")</li>";
          });
          html += "</ol>";
        }
        html += "</div>";

        html += "<div class=\"aot-recipe-section\">";
        html += "<div class=\"aot-recipe-section-head\"><strong>Tree view</strong><span class=\"aot-tree-hint\">drag to pan, scroll to zoom</span></div>";
        html += "<div class=\"aot-tree-wrapper\" data-tree-id=\"" + treeIdAttr + "\">";
        html += "<div class=\"aot-tree-viewport\"></div>";
        html += "<div class=\"aot-tree-controls\">";
        html += "<button type=\"button\" class=\"aot-tree-btn\" data-action=\"zoom-out\" aria-label=\"Zoom out\">&minus;</button>";
        html += "<button type=\"button\" class=\"aot-tree-btn\" data-action=\"zoom-in\" aria-label=\"Zoom in\">+</button>";
        html += "<button type=\"button\" class=\"aot-tree-btn\" data-action=\"fit\" aria-label=\"Fit to view\">Fit</button>";
        html += "<button type=\"button\" class=\"aot-tree-btn\" data-action=\"expand\" aria-label=\"Open in larger view\" title=\"Open in larger view\">&#x26F6;</button>";
        html += "</div>";
        html += "</div>";
        html += "</div>";

        html += "</div>";
        return html;
      }

      function renderRecipeResults(target, result) {
        if (result.recipes.length === 0) {
          let message = "<div class=\"aot-empty-state\"><span class=\"aot-warning\">No exact recipe found.</span>\n" +
            "Target: " + escapeHtml(rgbText(target)) + "\n" +
            "Searched states: " + result.searchedStates + "\n";
          if (result.acquisitionOnly) {
            message += "This dye is treated as acquisition-only in the tool, rather than something you can make by mixing.\n";
          } else if (result.maxMixDepth) {
            message += "No exact result was found within " + result.maxMixDepth + " mixes.";
          }
          message += "</div>";
          recipeResult.innerHTML = message;
          return;
        }
        const namedMatch = findNamedDyeByRgb(target);
        const recipes = result.recipes;
        let html = "<div class=\"aot-results-summary\">";
        html += "<div><strong>Target:</strong> " + escapeHtml(rgbText(target)) + (namedMatch ? " (" + escapeHtml(namedMatch.name) + ")" : "") + "</div>";
        if (result.excludedName) {
          html += "<div><strong>Excluded direct ingredient:</strong> " + escapeHtml(result.excludedName) + "</div>";
        }
        html += "<div><strong>Mix count:</strong> " + result.minDepth + "</div>";
        html += "<div><strong>Recipes shown:</strong> " + recipes.length;
        if (result.truncated) {
          html += " <span class=\"aot-summary-meta\">(more may exist; showing up to " + MAX_ALTERNATIVES + ")</span>";
        }
        html += "</div>";
        html += "<div class=\"aot-summary-meta\">Searched states: " + result.searchedStates + "</div>";
        html += "</div>";

        const treeIds = [];
        for (let i = 0; i < recipes.length; i++) {
          const treeId = "tree-" + Date.now() + "-" + i + "-" + Math.floor(Math.random() * 100000);
          treeIds.push(treeId);
          html += renderRecipeCard(recipes[i], i, recipes.length, treeId);
        }

        recipeResult.innerHTML = html;
        for (let i = 0; i < recipes.length; i++) {
          const wrapper = recipeResult.querySelector(".aot-tree-wrapper[data-tree-id=\"" + treeIds[i] + "\"]");
          if (wrapper) {
            const recipeLabel = "Recipe " + (i + 1) + " of " + recipes.length;
            renderTreeIntoContainer(wrapper, recipes[i], recipeLabel);
          }
        }
      }

      document.getElementById("aot-find-recipe").addEventListener("click", function () {
        const target = getTargetRgb();
        recipeResult.innerHTML = "<div class=\"aot-empty-state\">Searching...</div>";
        window.setTimeout(function () {
          const result = findAllShortestRecipes(target);
          renderRecipeResults(target, result);
        }, 0);
      });
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
        setTargetRgb(defaults.t, true);
        recipeResult.innerHTML = "<div class=\"aot-empty-state\">Enter a target color, then click Find Shortest Recipe.</div>";
        persistShareState();
        updateShareUi("Defaults restored.", "aot-success");
      });

      const initialState = loadStateFromUrl();
      setTargetRgb(initialState.t, true);
      persistShareState();
    })();
  </script>
</div>
