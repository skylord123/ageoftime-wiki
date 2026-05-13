# Blacksmith

<div markdown="1" style="display: flex; align-items: flex-start; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">

![Blacksmith](../assets/npcs/aot_blacksmith.png){ width=100 loading=lazy }

<div markdown="1" style="flex: 1; min-width: 240px;">

The Blacksmith is located in [Port Town](../world/locations/port-town.md) and is the
only NPC who can craft weapons, shields, clothing, cloth, and refined metals
from raw materials. Almost every piece of player-made gear in *Age of Time*
passes through the Blacksmith at some point.

</div>
</div>

## Using the Blacksmith

Talk to the Blacksmith and choose one of four crafting menus: **Weapons**,
**Clothing**, **Cloth**, or **Metal**. Each menu lists recipes with their gold
cost and material requirements; selecting a recipe consumes the materials and
gold from your inventory and produces the listed item.

!!! note "Source data"
    The tables below are transcribed from the live server's craft
    definitions, served from the *Age of Time* master server:

    - <https://master.ageoftime.com/craft/weapons.craft>
    - <https://master.ageoftime.com/craft/clothing.craft>
    - <https://master.ageoftime.com/craft/cloth.craft>
    - <https://master.ageoftime.com/craft/metal.craft>

    Local copies are mirrored in this wiki for posterity (archived
    **2026-05-07**):

    - [`weapons.txt`](../assets/archive/weapons.txt)
    - [`clothing.txt`](../assets/archive/clothing.txt)
    - [`cloth.txt`](../assets/archive/cloth.txt)
    - [`metal.txt`](../assets/archive/metal.txt)

## Weapons

| Item | Cost | Produces | Requirements |
|---|---:|---|---|
| [Crossbow](../items/weapons.md#crossbow) | 500 gold | Crossbow ×1 | 5 Wood, 2 Metal, 1 Metal |
| [Broadsword](../items/weapons.md#sword) | 900 gold | Broadsword ×1 | 5 Metal, 2 Metal, 1 Wood |
| [Shield](../items/weapons.md#shield) | 500 gold | Shield ×1 | 10 Metal, 2 Metal, 1 Metal |

Material choice matters differently by item type:

- [Swords](../items/weapons.md#sword) always deal the same damage and do not gain
  special metal effects.
- [Shields](../items/weapons.md#shield) can trigger special effects based on their
  body metal.
- Crossbow metal behavior remains only partially documented by the community.

## Clothing

All clothing recipes are free (0 gold). Multiple cloth slots let you mix
different colors and patterns; the visual result depends on which Cloth you
feed into each slot. For the full clothing list, recipes, shop locations, and
screenshots, see [Clothing](../items/clothing.md).

## Cloth

All Cloth recipes are free (0 gold) and produce **ClothItem ×5**. Each recipe
combines raw Fiber with one or more dyes to produce a distinct cloth pattern.
The texture list and full recipe table can be found on the [Cloth](../items/cloth.md)
page.

## Metal

Refines raw [Ores](../items/ores.md) into ingots. Steel is the standard
crafting metal; Plutonium is the strongest available. The full metal list,
images, and recipe table can be found on the [Metals](../items/metals.md)
page.

## Shield metal effects

Shield effects are community-reported and not officially documented.

- They trigger from **monster contact damage** or from **a player hitting the
  shield user with a sword**.
- Only the shield's **body** metal appears to matter. The crest and trim are
  believed to be cosmetic only.

| Metal | Reported shield effect |
|---|---|
| Copper | Freezes monsters for about 1 second and makes them lose their target. |
| Zinc | Spins monsters around and makes them lose their target. |
| Gold | Makes players drop 1 gold; makes monsters spawn 1 gold. |
| Iron | Spawns a couple of low-damage sparks. |
| Steel | Spawns more sparks. |
| Lead | Knocks the attacker back a few feet. |
| Plutonium | No confirmed effect. |
| Rust | No confirmed effect. |
| Brass | No confirmed effect. |

!!! note
    These reports only cover shield behavior. Sword damage/effects do not
    appear to change with metal.
