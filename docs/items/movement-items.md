# Movement Items

Movement items are inventory tools that primarily change how you travel around
the map.

<div class="grid cards" markdown>

- ![Hook](../assets/items/Hook.png){ width=64 } **Hook** — reward for completing [Level 1](../world/locations/level-1.md). Allows acrobatic grappling around the map, but lasts only about **15 seconds** after being fired (15.6 s on a stopwatch). It is thrown at **20 m/s**, so its shot drops off faster and does not reach as far as the Golden Hook.
- ![Golden Hook](../assets/items/Golden_Hook.png){ width=64 } **Golden Hook** — reward for completing the [Log Challenge](../world/locations/log-challenge.md). A stronger version of the Hook, thrown at **40 m/s** (twice as fast, so it flies much further and flatter) and lasting about **1 minute 2 seconds** after being fired. The thrown golden hook glows yellow.
- ![Insta-Horse](../assets/items/Insta-Horse.png){ width=64 } **Insta-Horse** — sold in the [Port Town Shop](../world/locations/port-town.md#shop). Spawns a Horse, but can only be used outside of safe zones.

</div>

## How the hook works

Measured on the official server (2026-11-23).

- **Throwing:** the hook flies from your hand at its throw speed plus your own movement. Running or jumping
  while you throw adds your full speed to it in that direction.
- **Sticking:** it sticks to whatever it hits first — ground, buildings, trees, rocks, even other players.
  It sticks to almost anything it hits, but a hook that only grazes a surface at a very shallow angle
  bounces off instead.
- **The rare bounce:** now and then a hook bounces even when it wasn't thrown at a shallow angle. The
  likely cause is a rounding quirk in the stick-or-bounce test. The game always means to stick, but a hit
  almost exactly **head-on** (straight into a wall or floor) or almost exactly **grazing** can push the
  test's maths just out of range, and then it counts as a bounce. Hits on edges and seams between
  surfaces, where the surface direction comes out odd, can do the same. *(From reading the game's code;
  not yet confirmed in game.)*
- **Rope length:** fixed when the hook sticks: the distance from your feet to the hook, rounded **down**
  to a whole metre. Standing still, the rope stays slack until you are further than that from the hook.
- **Swinging:** while the rope is tight, you swing around the hook and your body tilts to hang from the
  rope. Holding a movement key pushes you along the swing.
- **The rope seems to stretch:** while you swing you drift a little further from the hook (a few centimetres
  per swing). The rope's length never actually changes: the game stops you moving away from the hook but
  never pulls you back in, so small rounding errors add up. Move closer to the hook and you are back within
  the original length. At the end of a swing you can also creep slowly up and outward for several seconds
  instead of swinging straight back, for example when sliding along a wall.
- **Letting go:** crouch to release the rope. Throwing again replaces your old hook, and the rope lets go
  by itself when the hook times out (about 15 s for the Hook, about 1 minute for the Golden Hook).
- You only ever have one hook out at a time.
