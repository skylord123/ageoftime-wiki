# 3D Model Viewer

An interactive, in-browser viewer for *Age of Time*'s 3D assets. It renders the
game's own converted shapes and interiors, so you can see exactly what a player,
an item, or a building looks like without launching the game.

The viewer has four modes, picked from its **Display** panel:

- **Player** — the female character, dressed through a full clothing and
  appearance UI (equip items into slots, pick fabrics per material, set dye
  colors, hair, face, skin tone, posture, and body scale) that mirrors the
  in-game clothing logic.
- **Clothing** — a single standalone garment (bikini, skirt, shirt, …) with
  material and dye controls. Good for "how does this item look" previews.
- **Other** — any converted Torque shape (weapons, trees, crates, gems,
  campfires, …) with material/IFL selectors, per-node visibility toggles, and
  scale controls.
- **Interiors** — any converted `.dif` building or dungeon, rendered with its
  in-game baked lightmaps.

Drag to orbit, scroll to zoom, and use the sidebar to configure whatever you're
looking at.

[:material-arrow-expand-all: Open the full viewer](../model-viewer/index.html){ .md-button .md-button--primary }

<iframe src="../../model-viewer/" title="Age of Time 3D model viewer"
        loading="lazy" allowfullscreen
        style="width: 100%; height: 80vh; min-height: 640px; border: 1px solid
               var(--md-default-fg-color--lightest); border-radius: 6px;">
</iframe>

!!! tip "Share a configured view"

    Every setting the viewer offers is stored in the page URL, so any look you
    build can be shared as a link. The full viewer's **Embed** panel also builds
    a compact, chrome-less link (`?embed=1`) suitable for dropping into an
    `<iframe>` on another page.
