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
| [Burn](#burn) | Moderate | Niche — close-range against Imps |
| [Fireball](#fireball) | High (~3 shots per full bar) | Splash damage on grouped or moving targets |
| [Light](#light) | Low | Illuminating dark areas, especially at night |
| [Cloak](#cloak) | Very high (~75% of full bar) | Disengaging or ambushing in PvP |

---

## Ball

A small projectile that can be fired in rapid succession. Ball is the most
commonly used spell because of its very low mana cost — you can fire roughly
**35 consecutive shots** before draining a full mana bar.

**Behavior**

- Bounces off any surface it hits.
- Disappears **5 seconds** after being cast.
- On hit against an NPC, player, or horse, **pushes the target backward** while
  also dealing damage.
- Does **not** damage the player who cast it.

**Tactics**

- Because Balls don't damage their caster, a shot fired at a nearby target will
  often **ricochet between you and the target** until it expires — keeping the
  enemy at range while continuing to apply damage and knockback. This makes
  Ball excellent for kiting NPCs.
- **Rocket-jumping:** look straight down, jump, and fire a Ball at the ground.
  The projectile bounces between you and the floor, launching your character
  upward. Repeating this can build significant air time and is a useful
  movement tech.

---

## Burn

A short, slow stream of fire emitted in front of the caster.

Burn has poor damage and very limited range, so most players skip it. Its main
historical use is at point-blank range against [Imps](enemies.md), which are
otherwise small and fast-moving.

---

## Fireball

A large fiery projectile. With a high mana cost, you can typically fire only
about **three** before your mana is depleted.

Fireball deals **area-of-effect damage** where it lands, which makes it
forgiving to aim — you don't need a direct hit. Aiming at the ground near a
target will still inflict significant splash damage, and the AoE makes it
effective against tightly-grouped enemies or players who are dodging.

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

- Your **footsteps remain visible**. For example, walking on dirt will still
  kick up dust that other players can see.
- Because NPCs ignore the cloak entirely, this spell is **purely a PvP tool**
  — useful for setting up ambushes or breaking line of sight to disengage.
