# Torque Script

*Age of Time* is built on the [Torque Game Engine](../../about.md), which
ships with its own embedded scripting language — **TorqueScript**. The game
client and server are largely written in it, and most of the engine's
runtime behaviour can be inspected and (with admin access) altered from the
in-game console.

This section collects reference material for poking at the game from the
script side: dumps captured directly from the live client, notes on
specific subsystems, and any documentation we accumulate while
reverse-engineering the build.

<div class="grid cards" markdown>

- :material-code-braces: **[Console Function Dump](console-function-dump.md)**

    A verbatim listing of every TorqueScript console function exposed by
    the *Age of Time* client, captured with `dumpConsoleFunctions();`. A
    handful of entries are hand-annotated with `//` comments.

- :material-code-tags: **[Console Class Dump](console-class-dump.md)**

    A verbatim listing of every TorqueScript console class — including
    inherited methods and exposed fields — captured with
    `dumpConsoleClasses();`. Hand-annotated where useful.

- :material-tag-text: **[Tagged Strings](tagged-strings.md)**

    How Torque's `netStringTable`, `addMessageCallback`/`$MSGCB`, and the
    `getTag` / `detag` / `buildTaggedString` family actually work on the
    wire and in script.

- :material-database: **[Datablocks](datablocks.md)**

    What datablocks are, why their IDs are stable across restarts, and a
    running list of identified IDs.

</div>

More pages will be added here as we document additional TorqueScript
internals (object types, datablocks, network traffic, useful console
snippets, etc.).
