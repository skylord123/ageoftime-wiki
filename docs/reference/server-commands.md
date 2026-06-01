# Server Commands (`commandToServer`)

Many of the things your client asks the server to do — chatting, using items,
banking, mailing — go through the TorqueScript function **`commandToServer`**:

```cpp
commandToServer('CommandName', %arg1, %arg2, ...);
```

The first parameter is the command name (a [tagged string](torque-script/tagged-strings.md)),
followed by zero or more arguments. The server has a matching handler for each
command name.

!!! note "Movement is not a server command"
    Player **movement is not sent with `commandToServer`** — it is handled by
    the engine's own input/move system, not the command layer described here.

## Slash commands are `commandToServer` calls

Every [slash command](../commands.md) you type in chat is turned into a
`commandToServer` call by the client. When the chat input starts with `/`, the
client **splits the line on spaces**: the first word (minus the `/`) becomes
the command name, and **each remaining word is passed as a separate
argument**:

```cpp
// typing:  /CommandName the rest of the line
commandToServer('CommandName', "the", "rest", "of", "the", "line");
```

This has an important consequence:

!!! warning "Slash command arguments cannot contain spaces"
    Because the slash form splits on spaces, **a single argument can never
    contain a space**, and a command whose arguments need to hold spaces
    cannot be triggered from chat.

    For example, `MailItem` takes three arguments:

    ```cpp
    commandToServer('MailItem', "34020", "Some Player", "0");
    ```

    There is no slash equivalent for mailing to a player whose name has a
    space: typing `/MailItem 34020 Some Player 0` splits into **four**
    arguments — `"34020"`, `"Some"`, `"Player"`, `"0"` — so the recipient
    arrives as just `"Some"` and the `anonymous` flag is wrong.

    Commands that need space-containing arguments (or simply more arguments
    than you can cleanly space-separate) must be sent by calling
    `commandToServer` directly from the console or a script.

## Common commands

The commands below are the ones you'll see most often. Those whose arguments
never contain spaces (`cast`, `use`, `Discard`, `BankDeposit`, `suicide`,
`respawn`, …) can be typed directly as [slash commands](../commands.md).
`Talk` and `MessageSent` are what the chat box sends for ordinary messages, so
they carry your whole message — spaces and all — as a single argument (they
are not meant to be typed as `/talk`). See [Slash Commands](../commands.md)
for the player-facing list, including emotes like `/love`, `/sit`, and the
`/cast` easter eggs, which are all single-argument server commands too.

| Command & arguments | Effect |
|---|---|
| `commandToServer('Talk', %message)`<br>• `%message` — text (spaces allowed) | Local / proximity chat. This is what the chat box sends in local mode. |
| `commandToServer('MessageSent', %message)`<br>• `%message` — text (spaces allowed) | Global chat. This is what the chat box sends in global mode. |
| `commandToServer('cast', %spell)`<br>• `%spell` — `ball`, `burn`, `fireball`, `light`, `cloak` (also the `sandwich` / `boobs` easter eggs) | Equips the named spell. Backing command for [`/cast`](../commands.md#casting-spells). |
| `commandToServer('use', %serverID)`<br>• `%serverID` — an item's [`serverID`](inventory.md#clientinventoryso-fields) | Equips / uses the inventory item with that server ID (toggles equipped items). |
| `commandToServer('Discard', %serverID)`<br>• `%serverID` — an item's `serverID` | Drops (discards) the inventory item onto the ground. See [Inventory](inventory.md). |
| `commandToServer('Combine', %serverID1, %serverID2)`<br>• `%serverID1` — first item's `serverID`<br>• `%serverID2` — second item's `serverID` | Combines two inventory items into one — e.g. mixing two [Dyes](../items/dyes.md) together. |
| `commandToServer('BankDeposit', %amount)`<br>• `%amount` — gold (negative withdraws) | Deposits gold at the [bank](../npcs/banker.md); a negative amount withdraws. Backs [`/bankdeposit`](../npcs/banker.md#depositing-with-bankdeposit). |
| `commandToServer('action')`<br>• *(no arguments)* | Interact with what you're looking at — pick up items, open doors, talk to NPCs, etc. Same as pressing <kbd>E</kbd>. |
| `commandToServer('respawn')`<br>• *(no arguments)* | Respawn after death. See [Death & Respawning](../death.md). |
| `commandToServer('suicide')`<br>• *(no arguments)* | Kill your own character. Backs [`/suicide`](../commands.md#actions). |
| `commandToServer('logout')`<br>• *(no arguments)* | Return to the character select without disconnecting. Backs [`/logout`](../commands.md#system). |
| `commandToServer('ToggleCamera')`<br>• *(no arguments)* | Toggle between player control and a free-flying camera. |
| `commandToServer('dropCameraAtPlayer', %atPlayer)`<br>• `%atPlayer` — optional bool | Leave a camera at the player's position. |
| `commandToServer('DropPlayerAtCamera')`<br>• *(no arguments)* | Teleport the player to the free camera's position. |
| `commandToServer('stopAction')`<br>• *(no arguments)* | Same as pressing <kbd>Ctrl</kbd>+<kbd>E</kbd>. Despite the name it does not "stop an action" — it **drops a player you are carrying**, or, if you are driving a horse, **boots the passenger off**. |
| `commandToServer('SetQuickSlot', %serverID, %idx)`<br>• `%serverID` — an item's `serverID`<br>• `%idx` — quick-slot number (`0`–`9`) | Assign an inventory item to a quick slot (`$QuickSlot[%idx]`). |
| `commandToServer('voice', %line)`<br>• `%line` — `greet1`, `greet2`, `greet3`, `yes`, `no`, `Help`, `stop` | Plays a [Voice Menu](../voice-menu.md) line / emote. |
| `commandToServer('SelectBotChatOption', %index)`<br>• `%index` — option number | Choose a dialogue option when talking to an NPC. |

!!! note "`use` and `Discard` still need a `serverID`"
    Although these accept a single argument, that argument is an item's server
    ID — not something you'd normally type by hand. The
    [Inventory helpers](inventory.md#helper-functions) look the ID up by item
    name for you.

## Commands usually sent directly

These take several arguments, and at least one of them can hold a **space**
(player names, the space-separated ability list, etc.). Because the slash
parser splits on spaces, those are normally sent by calling `commandToServer`
directly rather than from chat.

### `MailItem`

```cpp
commandToServer('MailItem', %itemServerID, %recipient, %anonymous);
```

Mails an inventory item to another player. You must be **within 5 meters of
the [Post Master](../npcs/post-office.md)**.

A slash form (`/MailItem <id> <recipient> <anonymous>`) only works when the
recipient's name has **no space** — otherwise the name splits across
arguments. Send it directly to mail anyone reliably.

| Argument | Meaning |
|---|---|
| `%itemServerID` | The [`serverID`](inventory.md#clientinventoryso-fields) of the item in your inventory to send. |
| `%recipient` | The name of the player receiving the item. |
| `%anonymous` | `0` to send normally, `1` to send anonymously. |

### `login`

```cpp
commandToServer('login', %user, %passwordHash);
```

Authenticates at the login screen. `%passwordHash` is the password run through
`getStringCRC()`, not the plain-text password.

### `newCharacter`

```cpp
commandToServer('newCharacter', %name, %passwordHash, %gender, %posture,
    %chest, %xScale, %yScale, %zScale, %skinTone, %lipTone, %hairStyle,
    %hairColor, %eyeColor, %face, %ears, %glasses, %abilities, %overwrite);
```

Creates a new character — the command behind the character-creation GUI. It
takes the full appearance and ability spread as separate arguments, so it can
only be sent programmatically. Key arguments:

| Argument | Meaning |
|---|---|
| `%name` | Character / account name. |
| `%passwordHash` | `getStringCRC()` of the password (6+ chars in the GUI). |
| `%gender` | `0` = Male, `1` = Female. |
| `%posture`, `%chest` | Body sliders, `0.0`–`1.0`. |
| `%xScale`, `%yScale`, `%zScale` | Body scale, `0.9`–`1.1` (height ≈ `zScale × 66` inches). |
| `%skinTone`, `%lipTone` | `0`–`9` tone indices. |
| `%hairStyle` | `0` = Part, `1` = Up, `2` = Exotic. |
| `%hairColor` | `0` = Blonde, `1` = Brown, `2` = Black, `3` = Red, `4` = White. |
| `%eyeColor` | `0` = Blue, `1` = Green, `2` = Brown, `3` = Black. |
| `%face` | `0` = A, `1` = B. |
| `%ears` | `0` = Human, `1` = Elf. |
| `%glasses` | `0` = Off, `1` = On. |
| `%abilities` | Space-separated `Strength Stamina Dexterity Agility Intelligence Wisdom Charisma`, each `1`–`10` (GUI total is 29). |
| `%overwrite` | `0` = fail if the character exists, `1` = overwrite it. |

## Shop & crafting commands

These are sent by the blacksmith / shop GUIs. Their arguments are item
`serverID`s and numbers, so there is no need to type them by hand.

### `Craft`

```cpp
commandToServer('Craft', %recipeIndex, %ingredient1, %ingredient2, %ingredient3, %ingredient4);
```

Crafts a recipe at the [Blacksmith](../npcs/blacksmith.md). `%recipeIndex` is
the selected recipe, followed by the [`serverID`](inventory.md#clientinventoryso-fields)
of each ingredient placed in the four material slots.

### `SellItem`

```cpp
commandToServer('SellItem', %serverID, %amount, %price);
```

Sells an inventory item at a [shop](../npcs/shopkeepers.md). `%serverID` is the
item, `%amount` how many to sell, and `%price` the per-listing price.

## Parchment commands

Used by the [parchment](../items/index.md) writing GUI. The title and body are
free text containing spaces, so these are sent directly rather than from chat.

### `WriteParchment`

```cpp
commandToServer('WriteParchment', %serverID, %title, %body);
```

Writes a parchment's title and body. `%serverID` is the parchment item; pass
`""` for `%body` to set only the title.

### `WriteParchmentAppend`

```cpp
commandToServer('WriteParchmentAppend', %serverID, %text);
```

Appends a line of text to an existing parchment.

## Account & admin commands

### `changePassword`

```cpp
commandToServer('changePassword', %oldPassword, %newPassword);
```

Changes your account password.

### `SAD` / `SADSetPassword`

```cpp
commandToServer('SAD', %password);            // authenticate as server admin
commandToServer('SADSetPassword', %password); // set the server-admin password
```

Server-admin ("SAD") authentication. `SAD` submits the admin password to gain
elevated privileges. `SADSetPassword` sets that password and can **only be
called once you are already server admin**. The exact privileges these grant
are not fully documented here.

## Internal handshake commands

The client also sends a few `commandToServer` calls as part of normal engine
bookkeeping — you would not call these by hand:

- `commandToServer('MissionStartPhase1Ack', %seq)`
- `commandToServer('MissionStartPhase2Ack', %seq)`
- `commandToServer('MissionStartPhase3Ack', %seq)`

These acknowledge the phased mission/area load handshake (each with the load
sequence number) as you move between zones.

## See also

- [Slash Commands](../commands.md) — the player-facing command list.
- [Inventory](inventory.md) — `serverID`s and helpers for `use` / `Discard`.
- [Tagged Strings](torque-script/tagged-strings.md) — how command names and
  string arguments are encoded on the wire.
</content>
