# Tagged Strings

Tagged strings are a Torque Engine optimisation for sending strings between
client and server. Instead of sending the same literal text over the wire
every time, Torque keeps a shared **`netStringTable`** of strings and sends
a small numeric index plus a single control byte. Both endpoints look the
index up in their copy of the table to recover the original text.

This page documents how tagged strings are encoded, how the related
TorqueScript functions behave, and why they interact with `$MSGCB` /
`addMessageCallback` the way they do.

!!! quote "Source"
    The bulk of this writeup is adapted from notes by **Jetz**, shared in
    the *Age of Time* Discord on **2024-03-31**. Phrasing has been
    reorganised into sections; the technical claims are his.

## Wire format

A tagged string is **not** a normal string. It carries an out-of-band
identifier so the engine can tell tagged strings apart from regular ones:

| Stage | Byte layout |
|---|---|
| **Before sending** | `SOH` + *index* |
| **After receiving** | `SOH` + *index* + ` ` *(space)* + *resolved string* |

`SOH` is ASCII control character `0x01` — "Start of Heading". It is the
reason a tagged string isn't a valid identifier in TorqueScript and why the
console handles it specially (more on that below).

## Argument substitution: `%1`, `%2`, …

When a tagged string is sent via `commandToClient` or `commandToServer`,
any `%1`, `%2`, … placeholders in the table entry are automatically
substituted with the **arguments that appear that many places after the
tagged string itself** in the call. Substitution is resolved
**last-to-first**, so placeholders can be nested — a `%2` argument can
itself be a tagged string referring to `%1`, `%2`, … of the surrounding
call, and they will all resolve correctly.

A typical handler signature looks like:

```torquescript
function clientCmdServerMessage(%msgString, %a1, %a2, %a3, %a4, ...)
{
    // %a1, %a2, ... are the substitution arguments. The script body
    // usually doesn't need to touch them — by the time this function
    // runs, %msgString already has them resolved into its tail.
}
```

You will not normally **use** `%a1`/`%a2`/… inside the function — they're
already baked into the resolved portion of `%msgString` — but their values
are still relevant internally, because the engine needed them to perform
the substitution.

## Looking up handlers via `$MSGCB`

`addMessageCallback('SomeName', callback)` registers a handler in the
global array `$MSGCB`. The lookup key is the **first word of the received
tagged string**, which (because of the wire format above) is
*`SOH` + index*, **not** the human-readable name.

That has a few practical consequences:

- `getWord(%msgString, 0)` and `getTag(%msgString)`-style operations both
  pull out that prefix, which is what `$MSGCB` is keyed on. So the
  callback name passed to `addMessageCallback` matches automatically.
- You **cannot** reference `$MSGCB[10, 0]` directly with a numeric index —
  the actual key has a leading `SOH` byte attached, so the engine sees a
  different key entirely.
- You **can** reference it by name:

    ```torquescript
    $MSGCB['SetTeamCaptain', 0]
    ```

    This works because the array key is built from the same `SOH` + index
    prefix that received tagged strings carry.

- An equivalent (ugly) form using a borrowed `SOH` byte from any other
  tagged string demonstrates how the key is composed:

    ```torquescript
    $MSGCB[ getSubStr('any other tagged string', 0, 1) @ 10, 0 ]
    ```

!!! tip "The phantom space in the console"
    If you tab through `$MSGCB` entries in the in-game console, you have
    to press <kbd>←</kbd> or <kbd>→</kbd> twice to step the cursor past
    the space that follows the `B` in `$MSGCB`. That extra invisible
    character is the leading `SOH` byte of the key.

## Function reference

### `getTag(taggedString)`

Returns the **numeric netStringTable index** of a tagged string, with the
leading `SOH` stripped — effectively `getWord(taggedString, 0)` minus the
control byte, parsed as a number.

If you pass something that isn't a tagged string, `getTag` returns its
input unchanged.

### `detag(taggedString)`

Returns everything **after** the `SOH` + *index* + space prefix — i.e. the
resolved (substituted) string body that came down the wire.

`detag` only works on tagged strings that were **received** from a
`commandToClient` / `commandToServer` (because that is when the resolved
body is appended). Calling it on a tagged string you have only built
locally does nothing useful. As with `getTag`, passing a non-tagged string
returns it unchanged.

### `getTaggedString(index)`

Takes either a netStringTable index or a tagged string (in which case it
extracts the index itself) and returns the **raw entry** from the
netStringTable — unformatted, with the `%1`, `%2`, … placeholders still
present.

### `buildTaggedString(formatString, args...)`

Same idea as `getTaggedString`, but performs the `%1`, `%2`, … substitution
locally using the supplied arguments. Unlike network delivery, this
**does not** automatically resolve tagged strings passed in as arguments —
nesting only works through the network path.

### `addTaggedString(str)`

Adds a normal string to the netStringTable (if it isn't already present)
and returns its index. You can use this to mint tagged strings
programmatically, although doing so routinely defeats the optimisation —
the whole point of tagged strings is reusing entries that are already in
the table.

### `removeTaggedString(...)`

Decrements the **script-side** reference count incremented by
`addTaggedString`. From observation it never actually evicts the entry,
because the engine also keeps an **internal** reference count that is
incremented on add but not decremented on remove.
