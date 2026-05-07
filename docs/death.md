# Death & Respawning

Death in *Age of Time* is non-permanent, but it has a real cost: any gold you
were carrying drops at the spot where you died. Understanding the death and
respawn flow — and where players are likely to ambush you — is one of the
core skills of long-running characters.

## What happens when you die

When your health reaches zero, your character collapses and enters a **dead
state**. While dead:

- You **lay on the ground** at the spot where you were killed.
- You can still **look around** with the camera.
- A dialog appears the next time you click the mouse, titled **"You have
  died"**:

    > If you choose to respawn, you will drop all your gold.
    >
    > [ **Respawn** ]    [ **Wait** ]

| Button | Effect |
|---|---|
| **Wait** | Hides the dialog. It will reappear the next time you click. Your body remains where it fell. |
| **Respawn** | Sends you back to a spawn point. Any gold you were carrying is dropped at your body's last position. |

## Body recovery & rescue

A dead body persists in the world until the player respawns. While you're
down, another player can **pick you up** and drop you on a bed
(<kbd>Ctrl</kbd>+<kbd>E</kbd>) to bring you back to life — see
[Interacting with the world](getting-started.md#interacting-with-the-world).
You can resist being picked up by pressing jump (default <kbd>Space</kbd>).

## Where you respawn

Choosing **Respawn** sends you to your last visited "safe" location. If your
most recent safe location was one of these areas, you will respawn there:

- [Port Town](areas.md#port-town)
- [The Woods](areas.md#major-areas)
- [Starboard Town](areas.md#starboard-town)
- [The Tavern](areas.md#tavern)

Otherwise (e.g. you died deep in **The Wilderness** without recently passing
through one of the above), you respawn at **Port Town**.

!!! tip "Force a Port Town respawn"
    If you die out in The Wilderness and would rather restart at Port Town
    than at the closest safe zone, you can force it:

    1. `/suicide` (or <kbd>Ctrl</kbd>+<kbd>K</kbd>).
    2. Log out (`/logout`).
    3. Log back in.
    4. Respawn from the death dialog.

    You'll always end up at Port Town this way.

!!! note "Arena exception"
    Dying inside the [Arena](areas.md#arena) does **not** cause you to drop
    gold — it's a designated PvP zone designed for safe duels.

## Player-vs-player and gold farming

Because gold drops at the death location, intercepting a player on their way
back to the bank is one of the most reliable ways to make money in PvP.

- The <kbd>F2</kbd> player menu shows **everyone's location** on the server,
  which makes farmers easy to spot.
- A common pattern: a new player heads to the [Swamp](areas.md#major-areas)
  and grinds Orcs for gold. As soon as they leave Swamp on the way back to
  the bank in Port Town, a watching player intercepts and kills them.
- Once killed, the loser's only realistic options are to **respawn** (and
  surrender their gold), **wait** indefinitely for the killer to leave, or
  hope an ally arrives to rescue them.

## Historical exploits

!!! warning "For historical reference"
    The following describes a known exploit used by veteran players. It is
    documented here for community history; it is not endorsed.

Some players were notoriously stubborn and would refuse to respawn after
being killed. They would sometimes log out entirely and log back in later —
once the killer had left — to recover their body and gold. To defeat that
counter-play, killers developed a "body stash" trick that combined two
quirks of the engine:

1. **The shop interior is a separate space high in the sky.** The shop you
   see in [Port Town](areas.md#port-town) is just an exterior building. The
   actual shop interior sits far above the world; entering the door
   teleports you up to it, and leaving teleports you back down. The
   ground-level building itself is therefore an empty shell.
2. **Drop-through-walls.** A long-standing exploit lets a player drop down
   through a building's floor/wall, ending up inside it.

The trick combines the two:

1. The killer plants an **alt account** inside the empty exterior shell
   using the drop-through-walls exploit.
2. After killing a player carrying gold, the killer carries the body to
   the outside wall of the shop and drops it close to the wall.
3. The alt — already inside the building — looks at the body through the
   wall and presses <kbd>E</kbd> to pick it up, since interaction passes
   through the wall.
4. The alt throws the body into the middle of the (otherwise empty)
   exterior shell and logs out.
5. Believing they're safe, the victim eventually respawns. Their gold drops
   inside the shell, where they have no way to reach it.
6. The killer logs back in as the alt later and pockets the funds.

## See also

- [`/suicide`](commands.md#actions) — kill your character on demand.
- [`/dropgold`](commands.md#actions) — drop gold deliberately, e.g. to hand
  it off before risking a fight.
- [Banker](npcs/banker.md) — deposit gold so you can't lose it on death.
