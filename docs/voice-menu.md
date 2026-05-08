# Voice Menu

The **Voice Menu** is opened by pressing <kbd>V</kbd>. Despite the name, it is
the unified menu for **emotes, voice lines, animations, and spells** — most of
the non-combat interactions you'll perform in *Age of Time* run through it.

## Top-level menu

After pressing <kbd>V</kbd>, choose a category:

| Key | Category |
|:---:|---|
| <kbd>E</kbd> | [Emotes](#emotes) |
| <kbd>V</kbd> | [Voice](#voice) |
| <kbd>A</kbd> | [Animation](#animation) |
| <kbd>S</kbd> | [Spells](#spells) |
| <kbd>Esc</kbd> | Exit the menu |

!!! tip "Quick-chord input"
    The menu accepts buffered keypresses, so you can chord directly to a
    final action without waiting for each menu to render. For example,
    mashing <kbd>V</kbd>+<kbd>S</kbd>+<kbd>B</kbd> casts **Ball** instantly,
    and <kbd>V</kbd>+<kbd>E</kbd>+<kbd>L</kbd> plays the **Love** emote.

## Emotes

Visual reactions that appear above your character's head.

| Key | Emote | Effect |
|:---:|---|---|
| <kbd>L</kbd> | Love | Hearts swirl around your head. |
| <kbd>H</kbd> | Hate | Black smoke flies out of the top of your head. |
| <kbd>W</kbd> | WTF | Question marks appear around your head. |

Each emote can also be triggered as a [slash command](commands.md#emotes)
(`/love`, `/hate`, `/wtf`, `/alarm`).

There is also a hidden slash-command-only emote:

| Command | Emote | Effect |
|---|---|---|
| `/alarm` | Alarm | Shows an exclamation mark above your head and plays <audio controls preload="none" src="../assets/audio/voice/alarm.wav">alarm.wav</audio>. |

## Voice

Short voice lines used to coordinate or roleplay with other players. Click
play on any row to preview the in-game audio.

| Key | Voice line | Preview |
|:---:|---|---|
| <kbd>Y</kbd> | Yes  | <audio controls preload="none" src="../assets/audio/voice/yes.wav">yes.wav</audio> |
| <kbd>N</kbd> | No   | <audio controls preload="none" src="../assets/audio/voice/no.wav">no.wav</audio> |
| <kbd>E</kbd> | Help | <audio controls preload="none" src="../assets/audio/voice/help.wav">help.wav</audio> |
| <kbd>S</kbd> | Stop | <audio controls preload="none" src="../assets/audio/voice/stop.wav">stop.wav</audio> |
| <kbd>G</kbd> | Greet 1 | <audio controls preload="none" src="../assets/audio/voice/greet1.wav">greet1.wav</audio> |
| <kbd>H</kbd> | Greet 2 | <audio controls preload="none" src="../assets/audio/voice/greet2.wav">greet2.wav</audio> |
| <kbd>J</kbd> | Greet 3 | <audio controls preload="none" src="../assets/audio/voice/greet3.wav">greet3.wav</audio> |
| <kbd>Esc</kbd> | Exit the menu | — |

!!! note "Audio source"
    Clips are extracted from `base/data/sound/female/voiceA/` in the official
    game install (the only voice set shipped with v0030).

## Animation

Full-body character animations. Useful for taking a break, idling at a shop,
or just goofing off.

| Key | Animation |
|:---:|---|
| <kbd>S</kbd> | Sit |
| <kbd>L</kbd> | Lounge |
| <kbd>E</kbd> | Sleep |
| <kbd>Esc</kbd> | Exit the menu |

`Sit` and `Lounge` are also available as the [`/sit`](commands.md#emotes) and
[`/lounge`](commands.md#emotes) slash commands. Sleeping in a bed regenerates
your health — see [`/sleep`](commands.md#actions).

## Spells

Casts a spell from your shared mana pool. For full mechanics, mana costs, and
tactics, see the [Magic](magic.md) page.

| Key | Spell |
|:---:|---|
| <kbd>B</kbd> | [Ball](magic.md#ball) |
| <kbd>V</kbd> | [Burn](magic.md#burn) |
| <kbd>F</kbd> | [Fireball](magic.md#fireball) |
| <kbd>L</kbd> | [Light](magic.md#light) |
| <kbd>C</kbd> | [Cloak](magic.md#cloak) |

!!! tip
    Every spell above can also be cast directly from chat with
    `/cast <spell>` (e.g. `/cast ball`, `/cast cloak`). See
    [Slash Commands](commands.md#casting-spells) for the full list.
