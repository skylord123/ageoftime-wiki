# Orc Spawn Triggers

A **`RoomTrigger`** is an invisible box in the world that runs code when a
player walks into or out of it. This page covers three that spawn an
[Orc](../enemies.md) on entry: two out in the open world (one over the
[Swamp](locations/swamp.md), one in the hills north-east of the
[Woods](locations/woods.md)) and one at the bottom of the
[Cave](locations/cave.md) pit.

`RoomTrigger`s are not limited to these three locations: every room in
[Level 1](locations/level-1.md) and [Level 2](locations/level-2.md) uses one
for its room-specific encounters. They are distinct from the game's normal
around-the-player monster spawning because they fire when the player crosses a
box boundary, not merely from the player's position in the world.

## At a glance — official v30

| Trigger | Where | Size (X x Y x Z) | Behaviour |
|---|---|---|---|
| SwampBotZone A | Over the [Swamp](locations/swamp.md) | 344 x 223 x 71 | Starts with a persistent Orc; its Orcs spawn below the terrain and do not clean up normally |
| SwampBotZone B | Hills north-east of the [Woods](locations/woods.md) | 225 x 178 x 71 | Spawns on entry and removes its Orcs after the last player leaves |
| Cave pit | Floor of the [Cave](locations/cave.md) pit | not surveyed | Spawns a **red** Orc; basis of the [Monster Spawn Break](../reference/exploits/spawn-break.md) |

Both open-world triggers are named `SwampBotZone` in the world file, even
though only one of them is anywhere near the Swamp. The A/B labels below are
ours, to tell them apart.

!!! warning "The two versions are reversed"
    The **v0003 mission file** has the stale saved player count on
    SwampBotZone B (behind the Woods), while observed **official v30** behavior
    has the broken despawning on SwampBotZone A (over the Swamp). The behavior
    was evidently changed or reversed sometime between those versions.

## SwampBotZone A — the Swamp

[:material-video-3d: View this trigger in 3D](../map/3d/index.html?spawns=1#646,407,601,876.4,797,200.6){ .md-button }

A large box covering the middle of the Swamp:

| | X | Y | Z |
|---|---|---|---|
| Corner (min X, max Y) | 704.459 | 908.341 | 165.177 |
| Opposite corner | 1048.421 | 685.671 | 235.930 |

In **official v30**, every Orc spawned by this trigger appears below the
terrain at approximately **X 704.379, Y 908.284**, rather than at a usable
point in the Swamp.

In **official v30**, this is the broken trigger. An Orc is already spawned for
the zone when the server starts, and the trigger's player count never reaches
zero after real players leave. Its Orcs therefore never get removed
automatically — logging out or walking away does not fix them. They must be
killed to be removed.

This trigger has one spawned Orc for each player currently inside it: after a
restart, one player entering A results in two Orcs overall (the persistent A
Orc plus the new one). If a second player enters, there are three Orcs overall:
the original persistent Orc and one for each player in A.

The **v0003 mission file does not have this problem on A**. Its saved stale
counter is instead on B, as documented below.

## SwampBotZone B — north-east of the Woods

[:material-video-3d: View this trigger in 3D](../map/3d/index.html?spawns=1#305,599,522,474.5,889.4,221.8){ .md-button }

A smaller box in the hills past the Woods:

| | X | Y | Z |
|---|---|---|---|
| Corner (min X, max Y) | 361.987 | 978.285 | 186.410 |
| Opposite corner | 587.055 | 800.419 | 257.163 |

In **official v30**, this trigger works as intended: entering spawns Orcs, and
leaving removes them once the last player has left the box. It does not begin
with a stale player count or a persistent Orc.

The **v0003 mission file** is the reverse: B is saved with a player and an Orc
still inside it. The file stores its live counters mid-session:

```
botcount = "1";
botDeathCount = "0";
bot0 = "17158";
playerCount = "1";
```

`bot0 = 17158` is the object ID of an Orc that existed at the moment the v0003
mission was saved, and `playerCount = 1` means B begins with a player already
counted even though no player is actually there. This is a property of the
v0003 mission file, not the behavior observed in official v30.

## The Cave pit

[:material-video-3d: View the Cave in 3D](../map/3d/index.html#431,-159,448,575.9,72.4,246){ .md-button }

The floor of the [Cave](locations/cave.md) pit holds a third spawn trigger.
Step into it and an Orc spawns down in the pit, notices you and attacks; step
back out and it despawns. Unlike the two open-world triggers, this one spawns a
**red** Orc.

The trigger does not cover the whole pit floor — there is standing room along
the north-west side — and cycling in and out of it from there is the basis of
the [Monster Spawn Break](../reference/exploits/spawn-break.md) exploit.

!!! note "Not in the world file"
    This trigger isn't in the v0003 world file, or in the later v30 one, and
    nothing in the v0003 scripts creates it. Everything above is from playing
    the game rather than from the world data, which is why there is no surveyed
    box for it and why the 3D map doesn't draw it — the 3D map is built from
    the v0003 world. It's presumably content added in a later version, server
    side.

## How the trigger works

All of these use the `RoomTrigger` type, whose script is short:

```c
function RoomTrigger::onEnterTrigger(%this, %trigger, %obj)
{
    if (%obj.getClassName() $= "Player" && isObject(%obj.client))
    {
        %trigger.playerCount = %trigger.playerCount + 1;
        %spawnPoint = %trigger.getSpawnPoint();
        %newBot = AIPlayer::spawn("Monster", orcBody, %spawnPoint);
        ...
    }
}
```

- **A player enters** — the player counter goes up and one orc spawns. Every
  player who walks in spawns another one.
- **A player leaves** — the counter goes down. The trigger fades out and
  deletes its Orcs only when that count reaches zero. A saved count above zero,
  as in SwampBotZone A in official v30, prevents this cleanup.
- **An orc wanders out** while still alive — it fades out and deletes itself,
  and counts as a death.
- **An orc dies** — the trigger clears its orcs, opens any doors attached to it
  two seconds later, and about five and a half seconds after that spawns one
  fresh orc per counted player. (That door behaviour is there for the hedge
  maze, which builds a trigger like this into every one of its cells at
  runtime, with the cell's doors attached — kill the orc and the doors open.)

### Where orcs appear

Normally, the spawn point is picked at random inside the box, then dropped
onto whatever is underneath: the game shoots a ray straight down from the lid
of the box to just below its floor and puts the orc at the first terrain,
building or scenery it hits. SwampBotZone A in official v30 is an observed
exception: its Orcs always end up below the terrain at the location given
above.

Two quirks come out of that:

- The random point is only drawn from the **80% of the box nearest its corner**
  (the min-X, max-Y corner). The far fifth of every one of these boxes never
  gets a spawn.
- If the ray hits nothing — because the terrain there is higher than the lid of
  the box, so the ray starts inside the ground — the orc is placed at the
  trigger's corner instead, which can be tens of metres underground.

### Known bugs

!!! warning "Read from decompiled scripts"
    The game's scripts only exist as compiled `.dso` files; the code below was
    recovered with the [DSO decompiler](../reference/torque-script/dso-decompiler.md).
    The decompiler is not perfect at reconstructing loops, so the details of
    the counting loops in particular should be treated as probable rather than
    certain.

- **Official v30: SwampBotZone A has a stale player count.** It begins with an
  Orc and never reaches zero after real players leave. Its Orcs therefore
  persist until killed.
- **v0003 mission file: SwampBotZone B has the stale player count.** Its
  baked-in `playerCount = 1` and `bot0` value are in the mission data, the
  opposite arrangement from official v30.
- **Official v30: SwampBotZone A's Orcs spawn underground.** Its Orc spawn
  point is below the terrain at approximately X 704.379, Y 908.284.

!!! note "The position is a corner, not the centre"
    Worth knowing if you go looking at these in the world file: a trigger's
    stored position is the **min-X / max-Y / min-Z corner** of its box, and the
    box extends +X, -Y and +Z from there by the object scale. Reading the
    position as a centre point puts the box in the wrong place by half its
    size.
