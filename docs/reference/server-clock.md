# Server Clock

The Age of Time server keeps its own game clock, and that clock runs **a little
slower than real time**. Everything the server times (stuns, fuses, jail
sentences, crime timers, plant growth, your play time) is counted on this
clock. So in practice everything takes about **4% longer** than its
"designed" length.

That's why many timings on this wiki look slightly odd: a stun that's meant to
last 10 seconds lasts about 10.4 seconds on your watch.

## How slow is it?

Measured on 2026-11-20 by sending `/playtime` four times a second and timing
each minute tick against a real clock:

| | |
|---|---|
| One server minute | **62.4 seconds** of real time |
| Server clock speed | **96.15%** of real time |
| Everything takes | about **4% longer** than designed |

The rate depends on how the server machine is set up (see
[Why it happens](#why-it-happens)), so it could change if the server moves.

## What it means for timings

The game was designed with round numbers; you experience them about 4% longer:

| What | Designed (game time) | What you actually see |
|---|---|---|
| A jail sentence of 60 demerits | 60 s (1 s per demerit) | about 62.4 s |
| Fiber plant growth tick | 1 minute | about 62.4 s |
| Dynamite fuse | 5 s | about 5.2 s |
| Baton: longest stun from one hit | 35 s | about 36.5 s |
| Baton: longest stun in total | 45 s | about 47 s |
| Baton: stun cap on innocents and monsters | 10 s | about 10.4 s |
| Baton: full charge | 2 s | about 2.1 s |
| Public Nudity repeat charge | 45 s | about 47 s |
| Spamming window (same message) | 4 s | about 4.2 s |
| `/playtime` hour needed to join the police | 1 hour | about 62.4 minutes |

Unless a page says otherwise, the timings on this wiki are **what you
actually see** (real time), because that's what matters when you're playing.

## `/playtime` is close, but not exact

`/playtime` counts on the server's clock too, so it **under-reports** your real
play time by about 4%: when it says *1:00:00* you've really been playing about
**1 hour 2½ minutes**, and 10 hours shown is about 10 hours 24 minutes real.
It's close enough for everyday use, and it's what the game itself uses (for
example the 1 hour you need before you can
[join the police](../npcs/police.md#becoming-a-police-officer)), but don't
rely on it as an exact real-time measure.

## Why it happens

The server runs on the Torque Game Engine, which moves its game clock forward
once per pass of its main loop, by however much time has passed. On Windows the
engine measures that time and **rounds it down to a whole millisecond**, and the
leftover fraction is simply thrown away.

A server with no game window rests between passes, and on Windows a rest lasts
one scheduler tick: about **15.6 ms**. The engine counts that as **15 ms**, so
it loses about 0.6 ms on every pass. That's 4% of game time, and matches the
96% we measured. The official game client loses time the same way (about 4.5%
on a test machine).

Long server hitches (over about a second) can lose a bit more, but the
rounding is by far the main cause.

## Measure it yourself

Open the console (<kbd>~</kbd>) and run `/playtime` repeatedly (or send
`commandToServer('playtime');` a few times a second with a script). Note the
real time each time the minute changes; the gap between two changes is the
length of a server minute. Several minutes in a row give a precise average.
