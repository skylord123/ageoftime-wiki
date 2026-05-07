# Datablocks

Datablocks are Torque's mechanism for sharing static, read-only definitions
between the server and every connected client — projectile templates,
weapon stats, item descriptions, particle effects, and so on. Each
datablock gets a unique numeric ID at server start.

In *Age of Time*, datablock IDs are **stable across game restarts**, which
means an ID identified once can be referenced reliably by ID in scripts,
console snippets, or research notes from then on.

## Identified datablocks

The list below records IDs that have been positively identified by the
community while poking at the live game. Contributions welcome — see
[Contributing](../../contributing.md).

| ID | Datablock |
|---:|---|
| 376 | Meteor shower projectile |
