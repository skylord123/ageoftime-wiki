# Police (Marshal)

The friendly NPC inside the [Police Station](../areas.md#police-station) is
the **Marshal**. They run the police force, hand out paychecks, accept fines,
publish the wanted list, and recruit new officers.

## Talking to the Marshal

Approach the Marshal and press <kbd>E</kbd> to bring up the dialogue. The
following options are available:

| Option | Outcome |
|---|---|
| What are the laws? | Hands you a free [Citizen's Law Guide](#the-citizens-law-guide). |
| I want to become a police officer. | [Enlists you](#becoming-a-police-officer) — if you qualify. |
| I want my paycheck. | Pays out your [share of recent fines](#paychecks). Officers only. |
| I want some information on criminals. | Shows the current demerits/wanted list. |
| I would like to pay a fine. | Lets you [pay off your demerits](#paying-fines). |

## The Citizen's Law Guide

Selecting **"What are the laws?"** prompts the Marshal:

> There are many laws. Please take a complementary Law Guide from the stand
> in the corner.

…with a single follow-up button **"How do I read the guide?"**:

> To read the guide:
>
> - Press <kbd>I</kbd> to go into your inventory
> - Click the "Items" tab
> - Select "Citizen's Law Guide"
> - Click the "Use/Equip" button

Picking up and reading the guide displays the following parchment:

```text
THE LAW:

1. No Public Nudity
2. No Throwing Knife Theft
3. No Cursing
4. No Spamming
5. No ALL CAPS
6. No Horse Theft

These laws are to be enforced by the people.

Demerits shall be issued for each violation of the law. When a citizen
accumulates 60 or more demerits, they may be apprehended by an officer of
the law and jailed for a period of 1 second for each demerit.

If you have less than 150 demerits, you can pay a fine to remove your
demerits. Civilians pay 5 gold per demerit, Police officers pay 15 gold
per demerit.

If you leave the game or log out while stunned by a police baton, you
will be automatically jailed for any crimes you have committed

This document is subject to magical change without notice.
```

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

- :material-baseball-bat: A **Police Baton** — used to stun perps for arrest.
- :material-file-document: A **Police Law Guide** parchment — see below for
  the full text.

### The Police Law Guide

```text
How To Arrest Someone:
--------------------------------------------
1. Make sure the perp has at least
   60 demerits.  Check with the Marshal.
2. When you are both inside a town area,
   hit the perp with your police baton.
   This will stun them.
     TIP: The harder you hit someone,
     the longer they will be stunned.
     After you knock them down, give them
     a good hard hit to make sure they
     don't get away.
3. While they are stunned, run up to them
   and press ACTION (default E) to pick
   them up.
4. Carry them to the police station and
   throw them into the bin next to the
   Marshal's cage by pressing STOP ACTION
   (default CTRL E)

+------------------------+---------+
| Crime Name             | Demerits|
+------------------------+---------+
| Throwing Knife Theft   |    5    |
| Public Nudity - 1st    |   60    |
| Public Nudity - Repeat |   90    |
| Cursing                |   10    |
| Spamming               |   20    |
| All Caps               |   20    |
| False Arrest           |   15    |
| Police Brutality       |   30    |
| Corruption             |   90    |
| Murder                 |  140    |
| Horse Theft            |   80    |
| Aiding Escape          |   60    |
+------------------------+---------+

Definitions:
--------------------------------------------
Throwing Knife Theft (500d max) -
     Picking up a knife that has been
     thrown by another person.

Public Nudity (1000d max) -
     Removing of the clothes outside of
     the inn rooms.

Cursing (200d max) -
     Using these words in global chat:
     shit, fuck, nigger, asshole, cunt

Spamming (200d max) -
     Saying the same thing more than once
     in a row within 2 seconds in
     global chat.

All Caps (200d max) -
     Talking in all capital letters in
     global chat.

False Arrest -
     Clubbing someone with your police
     baton who does not have more
     than 60 demerits.

Police Brutality -
     Clubbing someone REALLY HARD with
     your police baton who does not have
     more than 60 demerits.

Corruption -
     Being arrested as a police officer.

Murder -
     Killing an innocent person who has
been stunned by a police baton.

Horse Theft -
     Driving a horse that does not belong
     to you.  Community horses are simply
     labeled "Horse"

Aiding Escape -
     Non-police carrying a stunned
criminal.  (Must be stunned in the
act)

--------------------------------------------

Losing Police Status:
--------------------------------------------
You will permantly removed from the police force if:
 - You are arrested and jailed
 - You accumulate more than 150 demerits

You cannot become a police officer if:
 - You currently have more than 60
   demerits
 - You have served more than 150 seconds
   in jail
--------------------------------------------
Your Paycheck:
--------------------------------------------
You do not get paid for jailing criminals

When someone pays a fine, it is divided
up among all of the on-duty cops.  This
is your paycheck.
--------------------------------------------
```

## Demerits at a glance

For quick reference, the same crimes summarised:

| Crime | Demerits | Cap |
|---|---:|---:|
| Throwing Knife Theft | 5 | 500 |
| Cursing | 10 | 200 |
| False Arrest | 15 | — |
| Spamming | 20 | 200 |
| All Caps | 20 | 200 |
| Police Brutality | 30 | — |
| Aiding Escape | 60 | — |
| Public Nudity (1st offence) | 60 | 1000 |
| Horse Theft | 80 | — |
| Public Nudity (repeat) | 90 | 1000 |
| Corruption (officer arrested) | 90 | — |
| Murder | 140 | — |

A citizen with **60 or more demerits** can be arrested. The **cap** column
is the maximum total demerits a single crime category can contribute.

## Arrest mechanics

1. **Stun** the perp with the police baton. The harder the hit, the longer
   the stun.
2. **Pick up** the stunned body with <kbd>E</kbd>.
3. **Carry** them to the police station.
4. **Drop** them into the bin next to the Marshal's cage with
   <kbd>Ctrl</kbd>+<kbd>E</kbd>.

Jail time is **1 second per demerit** the perp is carrying when arrested.

Successful arrests also remove **15 demerits** from the arresting officer as
a kind of community-service credit.

!!! note "Stunning outside towns"
    The Police Law Guide says *"When you are both inside a town area, hit
    the perp with your police baton."* — but in practice the baton works
    anywhere. You can stun a wanted player out in the wilderness, the
    woods, or any other zone and still carry them all the way back to the
    Marshal's cage to complete the arrest.

!!! warning "Logout while stunned"
    If you log out — or just close the game — while stunned by a police
    baton, you are automatically jailed for any outstanding crimes the
    moment you next log in.

!!! note "Respawn shortcut to jail"
    If a wanted player is **dead**, is being **carried by a police officer**,
    and then chooses **Respawn**, they are jailed immediately. This gives
    officers a reliable shortcut for finishing arrests without repeatedly
    re-stunning the body on the trip back. Logging out instead of respawning
    does **not** trigger this shortcut.

## Paying fines

If you have **fewer than 150 demerits** you can choose **"I would like to
pay a fine."** to wipe them.

| Payer | Cost per demerit |
|---|---:|
| Civilian | 1 gold |
| Police officer | 3 gold |

At 150+ demerits, fines are no longer accepted — you must serve jail time.

!!! note "Law Guide numbers are outdated"
    The parchment reproduced above still says **5** and **15** gold per
    demerit. In practice, the actual fine appears to be **1** gold per
    demerit for civilians and **3** for police.

## Paychecks

Selecting **"I want my paycheck."** pays out your share of recent fines.

- Officers are **not** paid for making arrests.
- Whenever someone pays a fine, the gold is split evenly between every
  officer on-duty at that moment. Only the **base fine** is distributed this
  way; the police surcharge is not.
- Asking for a paycheck while not on the force gets:
  *"Hey! You're not even a police officer."*

## Losing police status

You are permanently removed from the force if:

- You are arrested and jailed, **or**
- You accumulate more than 150 demerits.

You cannot re-enlist if:

- You currently have more than 60 demerits, **or**
- You have served more than 150 cumulative seconds in jail.

## Jail & IP-based persistence

Jail time must be served — there is no skipping it.

!!! danger "Same-IP jailing"
    Jail enforcement keys off your **IP address**, not just your account.
    If you log out while jailed and log back in on a different account, the
    new account inherits the remaining sentence. **Anyone else playing from
    the same household / IP** also gets jailed when they next log in until
    the sentence is served. Community reports suggest this linkage expires
    after roughly **30 minutes**.
