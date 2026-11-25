# Magic

Spells in *Age of Time* are cast through the **Voice Menu**. Each spell draws
from your shared mana pool, which regenerates over time.

## Casting a spell

1. Press <kbd>V</kbd> to open the Voice Menu.
2. Press <kbd>S</kbd> to enter the **Spells** submenu.
3. Press the spell's hotkey:

    | Key | Spell |
    |:---:|---|
    | <kbd>B</kbd> | [Ball](#ball) |
    | <kbd>V</kbd> | [Burn](#burn) |
    | <kbd>F</kbd> | [Fireball](#fireball) |
    | <kbd>L</kbd> | [Light](#light) |
    | <kbd>C</kbd> | [Cloak](#cloak) |

!!! tip "Quick-switch"
    The menu accepts buffered input, so you can chord the keys quickly. For
    example, mashing <kbd>V</kbd>+<kbd>S</kbd>+<kbd>B</kbd> in rapid succession
    will swap to **Ball** without ever looking at the menu.

## Casting from chat

Every spell can also be cast directly from chat by typing `/cast <spell>`.
This skips the Voice Menu entirely and is often the fastest way to switch
spells in combat.

| Command | Spell |
|---|---|
| `/cast ball` | [Ball](#ball) |
| `/cast burn` | [Burn](#burn) |
| `/cast fireball` | [Fireball](#fireball) |
| `/cast light` | [Light](#light) |
| `/cast cloak` | [Cloak](#cloak) |

See [Slash Commands](commands.md#casting-spells) for the full list of chat
commands.

## Spell summary

| Spell | Mana cost | Best used for |
|---|---|---|
| [Ball](#ball) | Very low (~35 shots per full bar) | General-purpose damage and crowd control |
| [Burn](#burn) | Moderate | Very niche; generally worse than just using a sword |
| [Fireball](#fireball) | High (~3 shots per full bar) | Splash damage on grouped or moving targets; strong in PvP |
| [Light](#light) | Low | Illuminating dark areas, especially at night |
| [Cloak](#cloak) | Very high (~75% of full bar) | Disengaging or ambushing in PvP |

---

## Ball

A small projectile that can be fired in rapid succession. Ball is the most
commonly used spell because of its very low mana cost — you can fire roughly
**35 consecutive shots** before draining a full mana bar.

| Property | Value |
|---|---|
| Damage | **15** per hit (7 hits kill a full-health player or Orc) |
| Speed | **30 m/s**, plus your own running or jumping speed |
| Push | **10 m/s** per hit, whatever the Ball's speed |
| Lasts | about **5 s** |

**Behavior**

- Bounces off any surface it hits, and falls with normal gravity.
- Disappears **5 seconds** after being cast.
- On hit against an NPC, player, or horse, deals **15 damage** and **pushes
  the target** 10 m/s along the Ball's path, tilted upward — a flat shot
  also lifts the target by about 4 m/s.
- Off a player or creature the Ball comes **straight back** the way it came,
  at 90% of its speed, instead of glancing off.
- A raised [Shield](items/weapons.md#blocking) blocks the damage but **not**
  the push, and the shield's metal effect does not trigger.
- Does **not** damage the player who cast it, but does push them.

**Tactics**

- Because Balls don't damage their caster, a shot fired at a nearby target will
  often **ricochet between you and the target** until it expires — keeping the
  enemy at range while continuing to apply damage and knockback. This makes
  Ball excellent for kiting NPCs.
- **Rocket-jumping:** look straight down, jump, and fire a Ball at the ground.
  The projectile bounces between you and the floor, launching your character
  upward. This only works reliably while standing still on flat ground.

---

## Burn

A short, slow stream of fire emitted in front of the caster.

| Property | Value |
|---|---|
| Damage | **2** per hit, about 15 hits a second (one every 0.064 s) |
| Damage per second | about **30** while the stream stays on the target |
| Reach | about **11.5 m** |
| Stream speed | **12 m/s**, plus your own movement |
| Knockback | None |
| Mana | Drains steadily while you hold the button; stops when your mana runs out |

The stream flies straight (it doesn't drop) and didn't burn the caster in our
tests. Each bit of fire ends in a small burst, though, and aiming straight down at
your own feet may burn you (reported, not yet measured). The
fire actually travels along **where you are looking**, but the flame you see
comes out of your hand, so it sprays slightly off from where the fire really
lands, which makes it awkward to aim.

Most players skip Burn. It is sometimes mentioned as an anti-[Imp](enemies.md) spell, but that only really
works if the Imp is already trapped or pinned down; in most real situations,
using a sword is better.

---

## Fireball

A large fiery projectile. With a high mana cost, you can typically fire only
about **three** before your mana is depleted.

Fireball deals **area-of-effect damage** where it lands, which makes it
forgiving to aim — you don't need a direct hit. Aiming at the ground near a
target will still inflict significant splash damage, and the AoE makes it
effective against tightly-grouped enemies or players who are dodging.

| Property | Value |
|---|---|
| Blast damage | **22** within about 1.75 m, fading to nothing at about **3.5 m** |
| Direct hit | **44** (22 for the hit plus 22 from the blast) |
| Push | about **4.5 m/s** at full strength, fading like the damage |
| Speed | **20 m/s**, plus your own running or jumping speed |
| Arc | a gentle arc (80% of normal gravity) |

- The blast distances are measured to the edge of the target's body, not its
  centre.
- Walls block the blast.
- A Fireball blast does no damage to players inside a safe zone.
- Fireballs don't fell trees — only [Dynamite](items/weapons.md#dynamite)
  does — but they do break crates.

Fireball is also one of the better PvP spells because the splash damage makes
it hard to dodge cleanly.

As with every spell, Fireball can also be triggered from chat with
`/cast fireball` — see [Casting from chat](#casting-from-chat).

---

## Light

A small ball of light that illuminates the area it's placed in. Useful for
exploring caves, tunnels, and the overworld at night where ambient lighting
is poor.

---

## Cloak

Renders the caster invisible to other players for a short window.

| Property | Value |
|---|---|
| Duration | ~20 seconds |
| Mana cost | ~75% of a full mana bar |
| Affects NPCs? | **No** — only hides you from other players |

**Caveats**

- Your **footsteps usually remain visible**. For example, walking on dirt will
  still kick up dust that other players can see. Interior-style surfaces such
  as [Woods](world/locations/woods.md), [Level 1](world/locations/level-1.md),
  and [Starboard Town](world/locations/starboard-town.md) do not show that
  visible-footstep effect.
- Because NPCs ignore the cloak entirely, this spell is **purely a PvP tool**
  — useful for setting up ambushes, breaking line of sight, or evading police.
