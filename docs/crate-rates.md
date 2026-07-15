# Crate Rates

![Crate](assets/items/Crate.png){ width=100 loading=lazy }

[Crates](world-objects.md) are the main source of [Gold](gold.md) and
[Dyes](items/dyes.md) in *Age of Time*. This page documents measured crate
counts, respawn times, and drop rates for every crate-bearing area.

The numbers below come from logging **561,853 crate breaks** (~2.9 million
gold) across all six main crate zones. Every crate break was recorded with its
exact gold piles, item drop, and dynamite, so the percentages are tight — the
biggest zones have 190k+ samples.

!!! warning "Data still being gathered"
    - [Level 1](world/locations/level-1.md) also contains crates, but **no
      drop data has been logged there yet**.
    - [Volcano](world/locations/volcano.md),
      [Swamp](world/locations/swamp.md),
      [Blue Hill](world/locations/blue-hill.md), and the
      [Woods](world/locations/woods.md) have smaller sample sizes (26k–50k
      crates) and need more data to fully hone their rates.

    This page will be updated as more data is collected.

## Crate counts & respawn times

| Zone | Crates | Respawn time (per crate) |
|---|---:|---|
| [Auric Fields](world/locations/auric-fields.md) | 20 | 1 second |
| [Red Crater](world/locations/red-crater.md) | 8 | 30 seconds |
| [Volcano](world/locations/volcano.md) | 5 ⚠️ | 20 seconds |
| [Woods](world/locations/woods.md) | 26 | 1 second |
| [Swamp](world/locations/swamp.md) | 10 | 1 second |
| [Blue Hill](world/locations/blue-hill.md) | 10 | 1 second |

**How respawns work:** each crate respawns on its own individual timer,
measured from the moment *that* crate was broken. Crates do not respawn
together as a group — if you break crate A, then crate B 5 seconds later,
each one respawns its own respawn-time after *its* break.

!!! bug "Volcano bug — crates can permanently disappear"
    Volcano starts with 5 crates, but in some edge case a broken crate never
    respawns. After a few days of farming there, no crates were left at all.
    Treat the 5 as a starting/max count that degrades over time.

## The standard loot table

Four zones — **Auric Fields, Blue Hill, Swamp, and the Woods** — share the
exact same loot table. Every crate rolls one of these outcomes:

| Outcome | Gold piles | Chance | Item? |
|:--------|:-----------|-------:|:------|
| 3 gold | 1+1+1 | ~50% | never |
| 7 gold | 1+1+5 | ~40% | never |
| 11 gold | 1+10 | ~9% | **almost always the zone's dye** |
| 100 gold (jackpot) | single 100 pile | ~1% | never |

Mean is about **6.2–6.35 gold per crate** in all four zones.

**Dyes ride the 11-gold crate.** In every standard zone, dyes drop *only*
from the 11-gold (1+10) crate, and that crate almost always includes one
(93–98% of the time). The split is roughly **2:1 normal vs bright**:

| Zone | Normal dye | Bright dye | Any dye (per crate) |
|:-----|:-----------|:-----------|--------------------:|
| [Auric Fields](world/locations/auric-fields.md) | Yellow — 6.2% | Bright Yellow — 3.7% | 9.9% |
| [Blue Hill](world/locations/blue-hill.md) | Blue — 5.6% | Bright Blue — 2.7% | 8.3% |
| [Swamp](world/locations/swamp.md) | Cyan — 5.7% | Bright Cyan — 2.9% | 8.6% |
| [Woods](world/locations/woods.md) | Green — 5.7% | Bright Green — 2.9% | 8.6% |

**Dynamite is Auric Fields only.** 0.90% of Auric crates (~1 in 111) spawn
lit dynamite and drop nothing else. In half a million crate breaks, no other
zone ever produced dynamite.

## Red Crater — a completely different table

[Red Crater](world/locations/red-crater.md) doesn't use the standard table at
all (193,348 crates logged):

| Outcome | Chance |
|:--------|-------:|
| 3 gold (1+1+1) | 52.6% |
| 1 gold (single pile) | 42.1% |
| 0 gold + **Red Dye** | 1.6% |
| 0 gold + **Bright Red Dye** | 1.6% |
| 0 gold, completely empty | 1.1% |
| 100 gold (jackpot) | 1.0% |

- There is **no 7 or 11 gold tier** — mean is only **~3.0 gold/crate**, less
  than half of any other zone.
- **Dyes come in gold-less crates** instead of riding a gold tier, and the
  Red/Bright Red split is ~50/50 rather than 2:1.
- It's the only zone with truly **empty crates** (~1%).

## Volcano — no jackpot, three dyes

[Volcano](world/locations/volcano.md) is standard-ish but with two twists
(26,287 crates logged):

| Outcome | Chance |
|:--------|-------:|
| 3 gold (1+1+1) | 50.0% |
| 7 gold (1+1+5) | 40.0% |
| 11 gold + **Black Dye** | 5.2% |
| 11 gold + **Magenta Dye** | 2.7% |
| 11 gold, no item | 0.9% |
| 0 gold + **Pitch Black Dye** | 0.8% |
| 0 gold, empty | 0.3% |

- **The 100-gold jackpot does not exist in Volcano** — zero in 26k+ breaks.
  Mean is 5.27 gold/crate.
- It's the only zone with **three dye types**: Black and Magenta on the
  11-gold crate, plus rare **Pitch Black Dye** in its own gold-less crate
  (~1 in 123 crates — the rarest dye per crate in the game).

!!! note "What about Orange Dye?"
    **Orange Dye does not drop from Volcano crates**, despite being
    historically credited to them — it did not appear once in 26k+ logged
    breaks. Where it actually comes from is unknown; the unlogged
    [Level 1](world/locations/level-1.md) crates are one possibility, but
    there is no data for that yet.

## Per-zone sample sizes

| Zone | Crates logged | Mean gold/crate | Jackpot rate |
|:-----|--------------:|----------------:|-------------:|
| [Auric Fields](world/locations/auric-fields.md) | 226,290 | 6.35 | 1.00% |
| [Red Crater](world/locations/red-crater.md) | 193,348 | 3.04 | 1.04% |
| [Swamp](world/locations/swamp.md) | 50,087 | 6.19 | 0.92% |
| [Blue Hill](world/locations/blue-hill.md) | 38,374 | 6.33 | 1.05% |
| [Woods](world/locations/woods.md) | 27,467 | 6.23 | 0.95% |
| [Volcano](world/locations/volcano.md) | 26,287 | 5.27 | none |

## TL;DR for farmers

- Gold per crate is basically identical everywhere (~6.3) except Volcano
  (5.27, no jackpot) and Red Crater (3.0). **Where you farm is about crate
  count and respawn speed, not the loot table.**
- Best gold: **[Auric Fields](world/locations/auric-fields.md)** and
  **[the Woods](world/locations/woods.md)** — 20–26 crates on 1-second
  individual respawns.