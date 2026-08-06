# Fiber & Fiber Plants

![Fiber](../assets/items/Fibers.png){ width=96 loading=lazy }

**Fiber** is a raw material used to make [Cloth](cloth.md). It is obtained
from [shrubs](../world-objects.md#resource-nodes-and-breakables), but can also
be grown into more Fiber: throw a Fiber onto the ground to plant a Fiber plant.

## At a glance

| | |
|---|---|
| Seed | Throw **1 Fiber** onto a surface |
| Time to maturity | **30–31 minutes** in real time |
| Harvest | Destroy a fully grown plant |
| Yield | **2–3 Fiber** |
| Net result | **+1 to +2 Fiber** per successful crop |
| Regrowth | None — harvest removes the plant; replant to start again |

!!! warning "Do not harvest early"
    An immature Fiber plant drops **nothing** when destroyed, including the
    Fiber used to plant it. Wait until it is fully grown before harvesting.

## Growing Fiber

1. Equip a Fiber and throw it onto a suitable surface.
2. A small Fiber plant appears and starts growing immediately.
3. Leave it for about **31 minutes**. Plants continue growing while no one is
   nearby.
4. When the plant is fully grown, destroy it to receive **2–3 Fiber**.
5. Replant one of the harvested Fiber to begin the next crop.

Each plant is single-use. Harvesting removes it completely; it will not grow
back in the same spot on its own.

## How to tell when it is ready

A ripe plant has both of these signs:

- Its size has reached its full scale (`1 1 1`).
- Its stalks have changed from green to **brown**.

The change is discrete, not gradual at the end: a plant one growth step short
of full size is still unripe and yields nothing. If you can inspect its scale,
only `1 1 1` is safe to harvest; do not rely on an almost-full appearance.

## Timing and growth stages

Fiber plants grow one stage at a time on a shared server-wide growth tick. The
tick is designed to run every server minute, which was measured as about
**62.4 seconds of real time**. A plant becomes ripe on the 30th tick after it
is planted.

Because planting can happen anywhere between ticks, a new plant takes about
**30.16 to 31.20 minutes** to mature (about **30.7 minutes on average**).
Plants planted at different times can therefore finish together when the next
shared tick arrives.

| Visible scale | What it means | Approx. time remaining |
|---:|---|---:|
| `0.1` | New plant; the first few stages look identical | 28.1–31.2 min |
| `0.5` | About halfway through growth | 15.6 min |
| `0.9` | Nearly ready | 3.1 min |
| `1 1 1` | Fully grown and harvestable | Ready now |

!!! tip "Planning a Fiber farm"
    Since every plant uses the same tick, seeing *any* plant advance a stage
    tells you when the next stage will occur for the whole farm. Outside the
    initial `0.1` stage, a plant's scale maps directly to its progress in
    1/30 increments.

## Farming strategy

Replanting one Fiber from each harvest turns every successful crop into a net
gain of 1–2 Fiber. In practice, expanding the farm is limited by the room and
time needed to plant and harvest, rather than by a per-plant respawn timer.

For example, reinvesting every harvested Fiber produces roughly 2–3 times as
many plants per ~31-minute cycle. Once the farm is large enough, staggered
planting makes regular harvests easier to manage.

## Technical details

The Fiber plant is a `StaticShape` using
`base/data/shapes/rock/bush1.dts`. Its growth scale is quantised to 30 stages:
after the initial display clamp, each tick adds `1/30` to the displayed scale.
The initial `0.1` scale covers several early stages, which is why it cannot
give an exact remaining-time estimate. Fully grown plants remain ripe until
they are harvested.

The 62.4-second real-time tick and the maturity window above were measured
from 54 observed growth ticks over about 75 minutes. The exact probability of
a 2-Fiber versus 3-Fiber harvest has not yet been measured.

## See also

- [Cloth](cloth.md) — Fiber recipes and cloth patterns.
- [World Objects](../world-objects.md#resource-nodes-and-breakables) — shrubs
  and other harvestable world objects.
