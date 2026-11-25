# Slash Commands

Commands are entered into the chat box. Press <kbd>T</kbd> to open chat, type
the command, and press <kbd>Enter</kbd>.

## System

| Command | Effect |
|---|---|
| `/playtime` | Shows your character's total play time, for example *"Total Play Time: 42:05:00"* (hours:minutes; under an hour it shows just minutes, like *"54:00"*). You need **1 hour** to [join the police](npcs/police.md#becoming-a-police-officer). It counts on the [server's clock](reference/server-clock.md#playtime-is-close-but-not-exact), which runs about 4% slow, so it's a little behind your real play time. |
| `/logout` | Switch characters without disconnecting from the server, after a 5-second countdown. Logging out while stunned by a police baton [gets you arrested](police-mechanics.md#logging-out-while-stunned) if you are wanted. |

## Actions

| Command | Effect |
|---|---|
| `/suicide` | Kills your character. Useful if you get stuck or trapped, and a step in the [force-respawn-at-Port-Town trick](death.md#where-you-respawn). (Same as <kbd>Ctrl</kbd>+<kbd>K</kbd>.) |
| `/action` | Interact with what you're looking at — pick up items, open doors, talk to NPCs, etc. (Same as <kbd>E</kbd>.) |
| `/stopaction` | Drop a player you're carrying, or boot the passenger off if you're driving a horse. (Same as <kbd>Ctrl</kbd>+<kbd>E</kbd>.) |
| `/respawn` | Respawn after death. See [Death & Respawning](death.md). |
| `/sleep` | Sleep anywhere. Sleeping in a bed regenerates your health. |
| `/dropgold <number>` | Drops `<number>` gold coins. Example: `/dropgold 12`. **Never ask for more than you hold at balances over 1,000,000** — it [destroys nearly all of it](gold.md#large-balances-1000000-and-above). |
| `/bankdeposit <number>` | Deposits `<number>` gold at the [bank](npcs/banker.md) without opening the menu. A 5 gold fee comes out of the amount (so `/bankdeposit 100` banks 95). Works through walls within 5 m of the Banker. |

## Casting spells

Every spell in the [Voice Menu](voice-menu.md#spells) can also be cast
directly from chat using `/cast <spell>`. This skips opening the menu
entirely and is the fastest way to swap spells mid-combat.

| Command | Effect |
|---|---|
| `/cast ball` | Activates the [Ball](magic.md#ball) spell. |
| `/cast burn` | Activates the [Burn](magic.md#burn) spell. |
| `/cast fireball` | Activates the [Fireball](magic.md#fireball) spell. |
| `/cast light` | Activates the [Light](magic.md#light) spell. |
| `/cast cloak` | Activates the [Cloak](magic.md#cloak) spell. |

See the [Magic](magic.md) page for mana costs and tactics for each spell.

## Emotes

| Command | Effect |
|---|---|
| `/love` | Hearts swirl around your character's head. |
| `/hate` | A dark cloud forms above your head. |
| `/wtf` | Question marks swirl around your head. |
| `/alarm` | Shows an exclamation mark above your head and plays the alarm sound. |
| `/sit` | Sit down. |
| `/lounge` | Lie down. |

## Easter-egg commands

`/cast` also accepts a couple of hidden arguments that don't appear in the
[Voice Menu](voice-menu.md#spells):

| Command | Effect |
|---|---|
| `/cast sandwich` | Prints: *"You cast yourself a sandwich. Tastes Good."* |
| `/cast boobs` | Gradually grows the caster's bust from minimum to maximum size. |

See [Tips & Secrets](tips.md#easter-eggs) for the full list of easter eggs.

## See also

- [Server Commands](reference/server-commands.md) — the `commandToServer`
  layer behind every slash command, including commands that can't be typed in
  chat (and why).
