# Inventory

How the client tracks the items you are carrying, and a set of
[TorqueScript](torque-script/index.md) helpers for working with them from the
console.

The client keeps your carried items in the global array **`$clientInv`**, with
`$numClientInvSlots` holding the slot count. Each populated slot is a
**`ClientInventorySO`** ScriptObject describing one stack of items.

| Global | Meaning |
|---|---|
| `$clientInv[%slot]` | The item array. Each entry is the `ClientInventorySO` for one occupied inventory slot. |
| `$numClientInvSlots` | How many slots are currently occupied. Walk the inventory with `for(%i = 0; %i < $numClientInvSlots; %i++)`. |
| `$BSD_CurrClickIndex` | Slot index of the item the player last clicked in the inventory UI (see [below](#getting-the-selected-item)). |

A typical loop over the whole inventory looks like this — guard each slot with
`isObject()` and a class check, since the engine briefly parks placeholder
objects in slots while an inventory is still streaming in:

```cpp
for(%i = 0; %i < $numClientInvSlots; %i++)
{
    %item = $clientInv[%i];
    if(isObject(%item) && %item.getClassName() $= "ScriptObject")
    {
        echo(%item.name @ " x" @ %item.quantity @ " (serverID " @ %item.serverID @ ")");
    }
}
```

!!! note "Slot index is not a stable identity"
    A slot number is just a UI position. When a stack is removed the engine
    deletes that slot's object and **compacts** the list — every higher slot
    shifts down and `$numClientInvSlots` drops by one. The only stable handle
    for an item is its `serverID` **field** (see below). Note that `serverID`
    is a field on the ScriptObject, not a Torque object id, so something like
    `15700.dump()` will not work.

## Getting the selected item

The slot the player last clicked in the inventory UI is stored in
`$BSD_CurrClickIndex`. To read the currently selected item's server ID from
the console:

```text
echo($clientInv[$BSD_CurrClickIndex].serverID);
```

`$clientInv[$BSD_CurrClickIndex]` is the full `ClientInventorySO` for that
slot, so you can read any of its fields the same way (for example
`.name`, `.quantity`, or `.dyeColor`).

## `ClientInventorySO` fields

A `ClientInventorySO` is a plain ScriptObject — its useful data lives in
dynamic fields set at runtime by the inventory sync commands. Dumping one (on
a build that supports `dump()`) looks like this for a pair of **W. Pants**:

```text
serverID = "34020"
inUse = "0"
name = "W. Pants"
baseID = "277"
ActiveBitmap = "12206"
mat1 = "24"
quantityLabel = "12210"
mat2 = "24"
InUseBitmap = "12207"
mat3 = "24"
quantity = "1"
dyeColor = "0 127 0 255"
mat4 = "24"
```

…and like this for a stack of **Yellow Dye**:

```text
serverID = "34042"
inUse = "0"
name = "Yellow Dye"
baseID = "136"
ActiveBitmap = "12316"
mat1 = "1"
quantityLabel = "12320"
mat2 = "1"
InUseBitmap = "12317"
mat3 = "1"
quantity = "524"
dyeColor = "127 127 0 255"
mat4 = "1"
```

| Field | Meaning |
|---|---|
| `serverID` | The item stack's **stable server-side ID**. This is the value you pass to server commands like `use` and `Discard`, and the only reliable way to identify a stack across inventory changes. |
| `inUse` | `1` if the item is currently equipped / active, `0` otherwise. |
| `name` | Display name of the item, e.g. `"W. Pants"` or `"Yellow Dye"`. |
| `baseID` | The item's **base item / datablock ID** — its type. Many stacks can share one `baseID`; `serverID` is unique per stack. |
| `quantity` | How many of the item are in this stack. |
| `dyeColor` | The stack's dye color as `"R G B A"` (0–255 each). |
| `ActiveBitmap` | [Tagged string](torque-script/tagged-strings.md) ID for the item's "active" inventory icon. |
| `InUseBitmap` | Tagged string ID for the icon shown while the item is in use. |
| `quantityLabel` | Tagged string ID used to render the stack's quantity label. |
| `mat1` – `mat4` | The item's material / ingredient slots. For crafted or dyed items these reference the materials used; for simple items they tend to repeat a single value. |

## Helper functions

The script below adds convenience functions for finding, equipping,
unequipping, and dropping inventory items by **name** (case-insensitive exact
match) or by `serverID`, without manually clicking through the inventory UI.
Each action ultimately sends the same `use` / `Discard` commands the UI sends,
keyed by `serverID`.

You can [download `inventory.cs`](../assets/downloads/inventory.cs) and `exec`
it, or copy the functions you need.

| Function | What it does |
|---|---|
| `findInventoryItem(%name)` | Returns the `ClientInventorySO` whose `name` matches `%name` (case-insensitive), or `false`. |
| `findInventoryItemById(%id)` | Returns the item whose `serverID` is `%id`, or `false`. |
| `equipInventoryItemByName(%name)` | Equips the named item if it isn't already in use. |
| `equipInventoryItemById(%id)` | Equips the item with the given `serverID` if not in use. |
| `unequipInventoryItemByName(%name)` | Unequips the named item if it is in use. |
| `unequipInventoryItemById(%id)` | Unequips the item with the given `serverID` if in use. |
| `unequip()` | Unequips the active item unless it is Clothing or Ammo (so you don't strip essentials). |
| `dropInventoryItemById(%id)` | Discards (drops) the item with the given `serverID`. |
| `dropInventoryItemByName(%name)` | Discards the named item. |

```cpp title="inventory.cs"
--8<-- "docs/assets/downloads/inventory.cs"
```
</content>
