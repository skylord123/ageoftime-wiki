# Police (Marshal)

<div markdown="1" style="display: flex; align-items: flex-start; gap: 1rem; flex-wrap: wrap; margin-bottom: 1rem;">

![Marshal](../assets/npcs/aot_marshal.png){ width=100 loading=lazy }

<div markdown="1" style="flex: 1; min-width: 240px;">

The friendly NPC inside the [Police Station](../world/locations/port-town.md#police-station)
is the **Marshal**. They run the police force, hand out paychecks, accept
fines, publish the wanted list, and recruit new officers.

For the actual law system, crime definitions, arrests, jail, and demerits,
see [Police Mechanics](../police-mechanics.md).

</div>
</div>

## Talking to the Marshal

Approach the Marshal and press <kbd>E</kbd> to bring up the dialogue. The
following options are available:

| Option | Outcome |
|---|---|
| What are the laws? | Hands you a free [Citizen's Law Guide](../police-mechanics.md#citizens-law-guide). |
| I want to become a police officer. | [Enlists you](#becoming-a-police-officer) if you qualify. |
| I want my paycheck. | Pays out your [share of recent fines](../police-mechanics.md#paychecks). Officers only. |
| I want some information on criminals. | Shows the current wanted list / demerits list. |
| I would like to pay a fine. | Lets you [pay off your demerits](../police-mechanics.md#paying-fines). |

## Becoming a police officer

Selecting **"I want to become a police officer."** has four possible
outcomes:

| Situation | Marshal's response |
|---|---|
| You qualify (1+ hour online, no crimes, not already an officer) | *"Congratulations, you're now on the police force. Please review the 'Police Law Guide' for specifics. Try not to screw up."* |
| You haven't been online long enough | *"Sorry, we don't take newbies."* |
| You're already on the force | *"You are already a police officer!"* |
| You already failed a previous chance | A refusal along the lines of *"You already had a chance. You blew it."* |

On enlistment you receive:

- :material-baseball-bat: A **[Police Baton](../weapons.md#other-weapon-items)** for stuns and arrests.
- :material-file-document: A **Police Law Guide** parchment. The full text and
  current practical notes are documented on [Police Mechanics](../police-mechanics.md#police-law-guide).

## Service limits

You are permanently removed from the force if:

- You are arrested and jailed, or
- You accumulate more than 150 demerits.

You cannot re-enlist if:

- You currently have more than 60 demerits, or
- You have served more than 150 cumulative seconds in jail.
