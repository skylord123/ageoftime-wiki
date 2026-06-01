// -----------------------------------------------------------------------------
// Script: inventory.cs
// Author: skylord123 <skylord123@gmail.com>
// Description:
//   Provides inventory helpers for finding, equipping, and unequipping client
//   inventory items without manually interacting with the inventory UI.
// -----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
// Function: findInventoryItem
// Description:
//     Searches the player's inventory for an item whose name matches the given
//     name (case-insensitive exact match). Useful for identifying a specific
//     item within a potentially large inventory.
//
// Parameters:
//     %name - The exact item name to search for (case-insensitive).
//
// Returns:
//     The inventory item matching the name, or false if not found.
//
// Example Usage:
//     %item = findInventoryItem("Blue Potion");  // Finds the "Blue Potion" item
//-----------------------------------------------------------------------------
function findInventoryItem(%name)
{
    for(%i = 0; %i < $numClientInvSlots; %i++) {
        %t = $clientInv[%i];
        if( isObject(%t) && %t.getClassName() $= "ScriptObject" && stricmp(%t.name, %name) == 0) {
            return %t;
        }
    }

    return false;
}

//-----------------------------------------------------------------------------
// Function: findInventoryItemById
// Description:
//     Searches the player's inventory for an item matching a server-side ID.
//
// Parameters:
//     %id - The serverID of the inventory item to find.
//
// Returns:
//     The inventory item matching the ID, or false if not found.
//
// Example Usage:
//     %item = findInventoryItemById(1234);
//-----------------------------------------------------------------------------
function findInventoryItemById(%id)
{
    for(%i = 0; %i < $numClientInvSlots; %i++) {
        %t = $clientInv[%i];
        if( isObject(%t) && %t.getClassName() $= "ScriptObject" && %t.serverID == %id) {
            return %t;
        }
    }

    return false;
}

//-----------------------------------------------------------------------------
// Function: equipInventoryItemByName
// Description:
//     Equips an inventory item by name if it is not already in use. This function
//     streamlines the process of using items without directly interacting with the
//     inventory UI or slot management.
//
// Parameters:
//     %name - The name of the inventory item to equip.
//
// Example Usage:
//     equipInventoryItemByName("HealingPotion");  // Equips a Healing Potion, if found and not in use
//-----------------------------------------------------------------------------
function equipInventoryItemByName(%name)
{
    %item = findInventoryItem(%name);
    if(%item && !%item.inUse)
    {
        commandToServer('use', %item.serverID);
    }
}

//-----------------------------------------------------------------------------
// Function: equipInventoryItemById
// Description:
//     Equips an inventory item by its server-side ID if it is not already in
//     use. Mirrors equipInventoryItemByName() but performs the lookup against
//     %t.serverID instead of the item name.
//
// Parameters:
//     %id - The serverID of the inventory item to equip.
//
// Returns:
//     The matching inventory item, or false when no slot has the given ID.
//
// Example Usage:
//     equipInventoryItemById(1234);
//-----------------------------------------------------------------------------
function equipInventoryItemById(%id)
{
    %item = findInventoryItemById(%id);
    if(%item && !%item.inUse)
    {
        commandToServer('use', %item.serverID);
    }

    return %item;
}

//-----------------------------------------------------------------------------
// Function: unequipInventoryItemByName
// Description:
//     Unequips an inventory item by name if it is currently in use.
//
// Parameters:
//     %name - The name of the inventory item to unequip.
//
// Returns:
//     The matching inventory item, or false when no item matches the name.
//
// Example Usage:
//     unequipInventoryItemByName("HealingPotion");
//-----------------------------------------------------------------------------
function unequipInventoryItemByName(%name)
{
    %item = findInventoryItem(%name);
    if(%item && %item.inUse)
    {
        commandToServer('use', %item.serverID);
    }

    return %item;
}

//-----------------------------------------------------------------------------
// Function: unequipInventoryItemById
// Description:
//     Unequips an inventory item by its server-side ID if it is currently in use.
//
// Parameters:
//     %id - The serverID of the inventory item to unequip.
//
// Returns:
//     The matching inventory item, or false when no slot has the given ID.
//
// Example Usage:
//     unequipInventoryItemById(1234);
//-----------------------------------------------------------------------------
function unequipInventoryItemById(%id)
{
    %item = findInventoryItemById(%id);
    if(%item && %item.inUse)
    {
        commandToServer('use', %item.serverID);
    }

    return %item;
}

//-----------------------------------------------------------------------------
// Function: unequip
// Description:
//     Unequips the currently used item, if it is not classified as clothing or ammo,
//     to avoid situations where the player might be left without essential items.
//     This function is particularly useful for quickly changing equipment.
//
// Returns:
//     A boolean indicating if an item was successfully unequipped.
//
// Example Usage:
//     %success = unequip();  // Attempts to unequip the current item
//-----------------------------------------------------------------------------
function unequip()
{
    for(%i = 0; %i < $numClientInvSlots; %i++) {
        %t = $clientInv[%i];
        if(
            isObject(%t)
            && %t.baseId.classname !$= "Clothing" // don't want to be naked lol
            && %t.baseId.classname !$= "Ammo" // don't want to be naked lol
            && %t.getClassName() $= "ScriptObject"
            && %t.inUse
        ) {
            commandToServer('use', %t.serverID);
        }
    }

    return false;
}

//-----------------------------------------------------------------------------
// Function: dropInventoryItemById
// Description:
//     Drops (discards) an inventory item by its server-side ID, removing it from
//     the player's inventory onto the ground. Mirrors the 'Discard' command the
//     inventory UI sends.
//
// Parameters:
//     %id - The serverID of the inventory item to drop.
//
// Returns:
//     The matching inventory item, or false when no slot has the given ID.
//
// Example Usage:
//     dropInventoryItemById(1234);
//-----------------------------------------------------------------------------
function dropInventoryItemById(%id)
{
    %item = findInventoryItemById(%id);
    if(%item)
    {
        commandToServer('Discard', %item.serverID);
    }

    return %item;
}

//-----------------------------------------------------------------------------
// Function: dropInventoryItemByName
// Description:
//     Drops (discards) an inventory item by name (case-insensitive exact match).
//     Useful for dropping items without knowing their serverID up front.
//
// Parameters:
//     %name - The exact name of the inventory item to drop (case-insensitive).
//
// Returns:
//     The matching inventory item, or false when no item matches the name.
//
// Example Usage:
//     dropInventoryItemByName("Blue Potion");
//-----------------------------------------------------------------------------
function dropInventoryItemByName(%name)
{
    %item = findInventoryItem(%name);
    if(%item)
    {
        commandToServer('Discard', %item.serverID);
    }

    return %item;
}
</content>
