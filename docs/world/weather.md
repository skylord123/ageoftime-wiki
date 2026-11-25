# Weather

It rains, and now and then snows, across the whole world at once: every player
sees the same storm at the same time. Nothing announces it; it just starts.

The numbers on this page were measured on the official server from a
**17-hour recording on two clients** (24–25 November 2026): 107 storms, 81 of
them recorded from start to finish. They will be refined as more are recorded.

!!! tip "Can't see the rain?"
    Precipitation can be turned off in the graphics options. If it is off, you
    won't see storms even while other players do.

## How a storm works

The weather changes only on a **world-wide tick about once a minute** (every
62.4 seconds of real time). Between ticks nothing changes.

- **Strength:** a storm starts with a random strength, its number of drops,
  anywhere up to about **3,100**. Values over the whole range were seen, with no
  clear favourite.
- **Fading:** on each tick, a storm usually (**3 times in 4**) gets **1,000
  drops lighter**. Otherwise it stays as it is for another tick. When it would
  drop to zero or below, it stops.
- **Length:** a storm therefore lasts as many steps as it has thousands of
  drops, rounded up. A 2,400-drop storm goes 2,400 → 1,400 → 400 and then ends.
  The pauses can stretch any storm, though: a 164-drop drizzle was seen lasting
  four minutes.
- **Typical length:** about 2 to 3 minutes. The longest seen lasted about 7
  minutes.

| Start strength | Steps | Usual length |
|---|---|---|
| under 1,000 drops | 1 | 1–2 minutes |
| 1,000–1,999 | 2 | 2–3 minutes |
| 2,000–2,999 | 3 | 3–4 minutes |
| 3,000 or more | 4 | 4–5 minutes |

## How often

- **Gap:** after a storm ends there is at least one dry minute. Then each tick
  has about an **11% chance** of starting a new storm.
- **Dry spells:** average about **9–10 minutes** (median about 7). The longest
  seen was 35 minutes.
- **Rate:** that works out to roughly **5 storms an hour**, and it rains (or
  snows) about a fifth of the time.

## Rain or snow

About **1 storm in 13 is snow** (8 of 107 recorded); the rest are rain. Snow
follows exactly the same rules as rain. It just falls more slowly and drifts
in the wind.
