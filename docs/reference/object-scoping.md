# Object Scoping

The server doesn't send your client every object in the world. It only sends
("ghosts") the objects your character could plausibly see, and leaves the rest
out. This matters if you write scripts, bots or tools that look at objects on
the client: something missing from `ServerConnection` may just be out of
scope, not gone.

Age of Time does exactly what the stock Torque Game Engine does here (checked
against the game executable).

## What your character sees

The server scopes from your character's eye position, out to the sky's visible
distance. The outdoors is one zone, and each building has its own zones,
joined by portals (doorways and windows). The server follows the zones you
could see into through those portals, and only objects in them are sent to
you.

So other players can drop out of view when one of you is inside a building:

- you're inside and they're outside, out of sight of the doorways;
- you're outside and they're inside a building you can't see into.

## Seeing everything with the free camera

The free-flying camera isn't part of the scene the server scopes from, so
while you control it the server sends you **every object in the world**:
every crate field, every dungeon door, every player and NPC.

```torquescript
commandToServer('dropCameraAtPlayer');
```

A single left click (fire) returns control to your character. From a script:

```torquescript
$mvTriggerCount0++;   // press
// ...about 150 ms later:
$mvTriggerCount0++;   // release
```

Tested from inside the Marshal's office on a fresh connection: the client went
from 987 objects (30 crates, no dungeon doors) to 1,505 (all 84 crates, all 64
dungeon doors) about 8 seconds after switching to the camera.

## What stays after you switch back

Once an object has been sent, the server only checks again whether it's still
in scope when that object has something new to send. So after you switch back
to your character:

- objects that sit still (crates, doors, props, idle NPCs) **stay** on your
  client until you disconnect, even far away;
- anything that moves (players walking, monsters fighting) is checked again and
  drops out as soon as it's out of view.

Switching character without disconnecting keeps everything that was already
sent; a full disconnect starts over.

See also [Server Commands](server-commands.md) for the camera commands.
