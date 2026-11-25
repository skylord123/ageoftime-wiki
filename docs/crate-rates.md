# Crates

![Crate](assets/items/Crate.png){ width=100 loading=lazy }

[Crates](world-objects.md) are the main source of [Gold](gold.md) and
[Dyes](items/dyes.md) in *Age of Time*. This page explains how crate farms
spawn and respawn, followed by measured [drop rates](#crate-rates) for every
main crate-bearing area.

## Spawning logic

Each crate farm has a fixed number of crates. When one is broken, **only that
crate** starts its respawn timer: crates do not respawn together as a group.
For example, breaking two crates five seconds apart makes them return five
seconds apart.

| Zone | Crates | Respawn time (per crate) |
|---|---:|---|
| [Auric Fields](world/locations/auric-fields.md) | 20 | 1 second |
| [Red Crater](world/locations/red-crater.md) | 8 | 30 seconds |
| [Volcano](world/locations/volcano.md) | 5 ⚠️ | 20 seconds |
| [Woods](world/locations/woods.md) | 30 ⚠️ | 1 second |
| [Swamp](world/locations/swamp.md) | 10 | 1 second |
| [Blue Hill](world/locations/blue-hill.md) | 10 | 1 second |

!!! bug "Crates can permanently disappear"
    A crate can fail to be placed when the server starts or when a broken
    crate tries to respawn. The spawner makes about **100 placement attempts**
    and then gives up; that crate is gone until the next server restart, so an
    area's crate count can only go down between restarts. Every spawner works
    this way, but it only matters where most spots are unusable: the **Woods**,
    the **Volcano** and the **Level 1** dungeon (about 0.7% of Level 1 respawns
    fail, so after a couple of thousand breaks only one crate was left). Treat
    the listed counts as starting/max counts rather than a guarantee of how
    many crates are currently available.

### Where a crate can appear

Each farm has a single spawner that places crates in a horizontal circle around
it. The radius below is the configured placement radius.

| Zone | Spawn radius | Grid spacing | Farming note |
|---|---:|---:|---|
| Auric Fields | 100 | 2.0 | Large, mostly flat area |
| Swamp | 100 | 2.0 | Large, mostly flat area |
| Blue Hill | 50 | 1.0 | Flat, compact area |
| Red Crater | 50 | 1.0 | Flat, compact area |
| Woods | 65 | 1.3 | Maze layout changes at restart, so usable spots change too |
| Volcano | 10 | 0.2 | Very tight peak; crates often recur in the same places |

Crate positions are **not continuously random**. Each spawner uses a fixed
101 × 101 grid centred on itself, with the cells outside its circular radius
excluded. It selects a valid grid cell and places the crate there; crates do
not use physics or slide after spawning. If a cell is invalid, it tries another
one (up to 100 attempts). The grid spacing is always:

```
spawn radius / 50
```

Crates never spawn on perfectly flat ground. The spawner looks straight down
from just above its own height and only accepts a surface that is at least a
little sloped, so in the Volcano every crate sits on the steep faces at the edge
of the plateau, and in Level 1 only on the sloped floor pieces of some rooms.
The same goes for flattened terrain: the flat area in the middle of Auric Fields
never gets a crate. Crates can still stack, because the top of a crate isn't
perfectly flat.

Whether crates can spawn under water depends on the farm. Blue Hill's crates are
all under water and the Swamp's often are, but Auric Fields and Red Crater never
put a crate under water.

Crates can land **outside** the radius. When a picked spot is inside a
building or wall (anything within 2 units above the spawner), the spawner
doesn't start over from its centre: it adds another random offset to the
spot it just rejected. In the open farms this almost never happens, so their
crates stay inside the circle. In the Volcano about 4% of crates land outside
it (up to 1.5 × the radius), in the Woods about 6%, and in Level 1 over a
third (up to about twice the radius).

Terrain and objects can make a grid cell unusable. This matters most in the
Woods and Volcano. Volcano has a small, stable set of usable cells, so crates
often pile up in the same footprints. The Woods maze changes every server
restart, so its usable cells—and therefore its repeated crate spots—are
dynamic; a percentage of valid spawn points from a multi-restart log would not
describe any one server. The flatter farms can use almost their entire grid, so
their crates are distributed much more widely.

## Breaking a crate

Crates have **30 health**. A sword hit (30 damage) breaks one in a single
swing, while a Ball spell (15 per hit) takes two hits, often from the same ball
bouncing off it. A broken crate disappears at once, with a small burst of tan dust,
six wooden chunks that bounce one to three times before vanishing, and a short
explosion sound you can hear up to about 100 m away.

Everything it drops starts exactly where the crate stood and is tossed up and
out in a random direction. Each drop gets its own throw: it rises 0.4 to 2 m
and lands up to about 2.6 m from the crate on flat ground. The throw has nothing to do with where you're standing.

## Crate Rates

The numbers below come from logging **1,853,882 crate breaks** (~9.7 million
gold) across all six main crate zones. Every crate break was recorded with its
exact gold piles, item drop, and dynamite, so the percentages are tight — the
biggest zones have 528k+ samples.

!!! warning "Data still being gathered"
    - [Level 1](world/locations/level-1.md) has only about 1,500 logged crates
      so far, so its rare outcomes are still rough.
    - [Volcano](world/locations/volcano.md) and the
      [Woods](world/locations/woods.md) have smaller sample sizes (50k–57k
      crates) and need more data to fully hone their rates.

    This page will be updated as more data is collected.

### The standard loot table

Four zones — **Auric Fields, Blue Hill, Swamp, and the Woods** — share the
exact same loot table. Every crate rolls one of these outcomes:

| Outcome | Gold piles | Chance | Item? |
|:--------|:-----------|-------:|:------|
| 3 gold | 1+1+1 | ~50% | never |
| 7 gold | 1+1+5 | ~40% | never |
| 11 gold | 1+10 | ~9% | **almost always the zone's dye** |
| 100 gold (jackpot) | single 100 pile | ~1% | never |

Mean is about **6.25–6.35 gold per crate** in all four zones.

**Dyes ride the 11-gold crate.** In every standard zone, dyes drop *only*
from the 11-gold (1+10) crate, and that crate almost always includes one
(92–98% of the time). The split is roughly **2:1 normal vs bright**:

| Zone | Normal dye | Bright dye | Any dye (per crate) |
|:-----|:-----------|:-----------|--------------------:|
| [Auric Fields](world/locations/auric-fields.md) | Yellow — 6.2% | Bright Yellow — 3.6% | 9.8% |
| [Blue Hill](world/locations/blue-hill.md) | Blue — 5.2% | Bright Blue — 2.6% | 7.8% |
| [Swamp](world/locations/swamp.md) | Cyan — 5.7% | Bright Cyan — 2.8% | 8.6% |
| [Woods](world/locations/woods.md) | Green — 5.7% | Bright Green — 2.8% | 8.5% |

**Dynamite is Auric Fields only.** 0.93% of Auric crates (~1 in 107) spawn
lit dynamite and drop nothing else. In 1.85 million crate breaks, no other
zone ever produced dynamite.

### Red Crater — a completely different table

[Red Crater](world/locations/red-crater.md) doesn't use the standard table at
all (590,687 crates logged):

| Outcome | Chance |
|:--------|-------:|
| 3 gold (1+1+1) | 52.6% |
| 1 gold (single pile) | 42.1% |
| 0 gold + **Red Dye** | 2.1% |
| 0 gold + **Bright Red Dye** | 2.1% |
| 100 gold (jackpot) | 1.1% |

- There is **no 7 or 11 gold tier** — mean is only **~3.1 gold/crate**, less
  than half of any other zone.
- **Dyes come in gold-less crates** instead of riding a gold tier, and the
  Red/Bright Red split is ~50/50 rather than 2:1.
- Crates are **never empty**. The farmer's logs showed ~1% empty crates here,
  but watching over 1,000 breaks directly showed every crate dropping
  something: the "empty" ones were dye crates whose only drop, the dye, the
  bot didn't pick up. They're counted as dye crates in the table above.

### Volcano — no jackpot, three dyes

[Volcano](world/locations/volcano.md) is standard-ish but with two twists
(50,062 crates logged):

| Outcome | Chance |
|:--------|-------:|
| 3 gold (1+1+1) | 50.3% |
| 7 gold (1+1+5) | 40.3% |
| 11 gold + **Black Dye** | 5.1% |
| 11 gold + **Magenta Dye** | 2.7% |
| 0 gold + **Pitch Black Dye** | 0.8% |
| 11 gold, no item | 0.8% |

- **The 100-gold jackpot does not exist in Volcano** — zero in 50k+ breaks.
  Mean is 5.27 gold/crate.
- It's the only zone with **three dye types**: Black and Magenta on the
  11-gold crate, plus rare **Pitch Black Dye** in its own gold-less crate
  (~1 in 125 crates — the rarest dye per crate in the game).

!!! note "What about Orange Dye?"
    **Orange Dye does not drop from Volcano crates**, despite being
    historically credited to them — it did not appear once in 50k+ logged
    breaks. It comes from [Level 1](#level-1) crates instead.

### Level 1

[Level 1](world/locations/level-1.md) crates use the standard gold tiers but,
like the Volcano, have **no 100-gold jackpot**, and its 11-gold crate carries a
**Blue Vial** or **Brown Dye** instead of a dye pair. It is also where
**Orange Dye** comes from: a rare gold-less crate with two Blue Vials and an
Orange Dye.

| Outcome | Chance |
|:--------|-------:|
| 3 gold (1,1,1) | 50.1% |
| 7 gold (1,1,5) | 39.0% |
| 11 gold (1,10) + Blue Vial | 6.3% |
| 11 gold (1,10) + Brown Dye | 3.2% |
| 0 gold + 2 Blue Vials + Orange Dye | 1.2% |

Based on 1,516 crates logged 2026-11-22 and 23. Mean is about 5.3 gold per
crate.

### Per-zone sample sizes

| Zone | Crates logged | Mean gold/crate | Jackpot rate |
|:-----|--------------:|----------------:|-------------:|
| [Red Crater](world/locations/red-crater.md) | 590,687 | 3.07 | 1.07% |
| [Auric Fields](world/locations/auric-fields.md) | 528,177 | 6.34 | 0.99% |
| [Swamp](world/locations/swamp.md) | 316,224 | 6.26 | 0.97% |
| [Blue Hill](world/locations/blue-hill.md) | 311,864 | 6.25 | 1.00% |
| [Woods](world/locations/woods.md) | 56,868 | 6.28 | 1.00% |
| [Volcano](world/locations/volcano.md) | 50,062 | 5.27 | none |
| [Level 1](world/locations/level-1.md) | 1,516 | 5.29 | none |

### TL;DR for farmers

- Gold per crate is basically identical everywhere (~6.3) except Volcano
  (5.26, no jackpot) and Red Crater (3.1). **Where you farm is about crate
  count and respawn speed, not the loot table.**
- Best gold: **[Auric Fields](world/locations/auric-fields.md)** and
  **[the Woods](world/locations/woods.md)** — 20–30 crates on 1-second
  individual respawns.
