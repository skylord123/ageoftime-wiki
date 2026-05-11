# Dye Recipe Finder

Interactive recipe search for *Age of Time* dyes.

Enter a target RGB color or choose a named dye, and this tool searches for a
shortest recipe using named dyes. The share link below the result preserves
the current target color only.

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
      white-space: pre-wrap;
      background: rgba(255,255,255,0.55);
      border: 1px solid var(--aot-border);
      border-radius: 12px;
      padding: 12px;
      min-height: 70px;
      font-size: 0.9rem;
      overflow-x: auto;
    }
    @media (prefers-color-scheme: dark) {
      #aot-dye-recipe-finder .aot-result-box { background: rgba(10,8,6,0.58); }
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
  <p class="aot-subtitle">Search for a shortest named-dye recipe for a target color. If the target is itself a named dye, the direct dye is excluded so the tool finds how to make it from other dyes.</p>

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

    <div class="aot-result-box" id="aot-recipe-result" style="margin-top: 12px;">Enter a target color, then click Find Shortest Recipe.</div>

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
      const MAX_RECIPE_STATES = 500000;
      const MAX_RECIPE_DEPTH = 24;
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
      function buildRecipeFromReverseSearch(startKey, targetKey, parents, baseRecipeByKey) {
        let currentKey = startKey;
        let recipe = baseRecipeByKey.get(startKey);
        while (currentKey !== targetKey) {
          const parent = parents.get(currentKey);
          if (!parent) return null;
          recipe = { type: "mix", rgb: parent.nextRgb, left: recipe, right: parent.ingredientRecipe };
          currentKey = parent.nextKey;
        }
        return recipe;
      }
      function findShortestRecipe(targetRgb) {
        const target = normalizeRgb(targetRgb);
        const targetKey = rgbKey(target);
        const exactTargetDye = findNamedDyeByRgb(target);
        const excludedName = exactTargetDye ? exactTargetDye.name : null;
        const baseRecipes = NAMED_DYES.filter(function (dye) {
          return dye.name !== excludedName;
        }).map(function (dye) {
          return { type: "base", name: dye.name, rgb: normalizeRgb(dye.rgb) };
        });
        const baseRecipeByKey = new Map();
        baseRecipes.forEach(function (recipe) {
          const key = rgbKey(recipe.rgb);
          if (!baseRecipeByKey.has(key)) baseRecipeByKey.set(key, recipe);
        });
        if (!excludedName && baseRecipeByKey.has(targetKey)) {
          return { recipe: baseRecipeByKey.get(targetKey), exact: true, excludedName: excludedName, searchedStates: 1 };
        }
        const queue = [{ rgb: target, depth: 0 }];
        const parents = new Map();
        const seen = new Set([targetKey]);
        let bestBaseKey = null;
        let bestBaseDistance = Infinity;
        let stoppedEarly = false;
        for (let index = 0; index < queue.length; index++) {
          const current = queue[index];
          const currentKey = rgbKey(current.rgb);
          if (baseRecipeByKey.has(currentKey)) {
            const recipe = buildRecipeFromReverseSearch(currentKey, targetKey, parents, baseRecipeByKey);
            return { recipe: recipe, exact: true, excludedName: excludedName, searchedStates: seen.size };
          }
          baseRecipeByKey.forEach(function (baseRecipe, baseKey) {
            const distance = colorDistance(current.rgb, baseRecipe.rgb);
            if (distance < bestBaseDistance) { bestBaseDistance = distance; bestBaseKey = baseKey; }
          });
          if (current.depth >= MAX_RECIPE_DEPTH) continue;
          for (const ingredientRecipe of baseRecipes) {
            const previousColors = inverseMixCandidates(current.rgb, ingredientRecipe.rgb);
            for (const previousRgb of previousColors) {
              const previousKey = rgbKey(previousRgb);
              if (seen.has(previousKey)) continue;
              seen.add(previousKey);
              parents.set(previousKey, { nextKey: currentKey, nextRgb: current.rgb, ingredientRecipe: ingredientRecipe });
              queue.push({ rgb: previousRgb, depth: current.depth + 1 });
              if (seen.size >= MAX_RECIPE_STATES) {
                stoppedEarly = true;
                index = queue.length;
                break;
              }
            }
            if (stoppedEarly) break;
          }
        }
        if (bestBaseKey && baseRecipeByKey.has(bestBaseKey)) {
          return {
            recipe: baseRecipeByKey.get(bestBaseKey),
            exact: false,
            excludedName: excludedName,
            searchedStates: seen.size,
            stoppedEarly: stoppedEarly,
            distance: bestBaseDistance
          };
        }
        return { recipe: null, exact: false, excludedName: excludedName, searchedStates: seen.size, stoppedEarly: stoppedEarly };
      }

      document.getElementById("aot-find-recipe").addEventListener("click", function () {
        const target = getTargetRgb();
        recipeResult.textContent = "Searching...";
        window.setTimeout(function () {
          const result = findShortestRecipe(target);
          if (!result.recipe) {
            recipeResult.innerHTML = "<span class=\"aot-warning\">No exact recipe found.</span>\n" +
              "Target: " + rgbText(target) + "\n" +
              "Searched states: " + result.searchedStates + "\n" +
              (result.stoppedEarly ? "Stopped early at the configured search limit of " + MAX_RECIPE_STATES + " states.\n" : "") +
              "Tip: some RGB values may not be reachable exactly from the named dyes using floor-average mixing.";
            return;
          }
          const lines = [];
          const namedMatch = findNamedDyeByRgb(target);
          lines.push("Target: " + rgbText(target) + (namedMatch ? " (" + namedMatch.name + ")" : ""));
          if (result.excludedName) lines.push("Excluded direct ingredient: " + result.excludedName);
          lines.push("Mix count: " + recipeDepth(result.recipe));
          lines.push("Named dye ingredients used: " + recipeIngredientCount(result.recipe));
          lines.push("Searched states: " + result.searchedStates);
          lines.push("");
          lines.push("Ingredients needed:");
          ingredientSummaryLines(result.recipe).forEach(function (line) { lines.push("- " + line); });
          lines.push("");
          lines.push("Mix flow:");
          recipeFlowLines(result.recipe).forEach(function (line) { lines.push(line); });
          lines.push("");
          lines.push("Step-by-step:");
          const stepLines = simplifiedRecipeSteps(result.recipe);
          if (stepLines.length === 0) {
            lines.push("Use " + recipeExpression(result.recipe) + " directly.");
          } else {
            stepLines.forEach(function (step, index) {
              lines.push((index + 1) + ". Mix " + step.inputLabel + " (" + rgbText(step.inputRgb) + ") with " + step.ingredientLabel + " (" + rgbText(step.ingredientRgb) + ")");
              lines.push("   = " + step.resultLabel + " (" + rgbText(step.resultRgb) + ")");
            });
          }
          recipeResult.textContent = lines.join("\n");
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
        recipeResult.textContent = "Enter a target color, then click Find Shortest Recipe.";
        persistShareState();
        updateShareUi("Defaults restored.", "aot-success");
      });

      const initialState = loadStateFromUrl();
      setTargetRgb(initialState.t, true);
      persistShareState();
    })();
  </script>
</div>
