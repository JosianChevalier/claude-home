---
tags: [harness-design, session-design, variety-absorption]
---

# The abstraction ladder

**Thesis.** Ways of working that let kairos reach the engineer ([[philosophy/metis-kairos]]) take the shape of a ladder: levels ordered by abstraction, each absorbing the variety it can and passing the rest one rung up. This file is the general pattern; each sighting reads it first and keeps only what is specific to its own rungs.

Each rung delegates cognitive load and context to the rung below, and takes back only what that rung could not absorb. Down is closer to where variety arrives first.

```
   top      slowest; decides on what climbed; sees nothing else
    ▲  │
    │  │   up:    each rung absorbs what fits, escalates the rest one rung, wrapped, cause kept
    │  │   down:  a change trickles to every rung below; what became routine is codified one rung down
    │  ▼
  bottom    where variety arrives first
```

- **Absorb down.** Variety is absorbed at the lowest rung that can take it as business as usual: only variety absorbs variety (Beer, after Ashby), read as subsidiarity. A rung is a filter, not a wall: it absorbs the noise of its level and passes the signal up; the complexity underneath is untouched.
- **Escalate up, one rung.** What breaks a rung's expectation goes to the rung above, which has the orientation to decide on it. Like an exception: the rung catches what it declared business as usual; the rest it wraps and passes on, its context added, the cause preserved. A rung translates the cause only for the failure types it is declared to handle, and any rung can install a handler. Swallowing is the failure, not passing.
- **Trickle down.** A change made on a rung is a consequence for every rung below.
- **Reliable bricks move down.** Once a rung absorbs variety as business as usual, that absorption can be codified into the rung below: commodification, one rung at a time ([[philosophy/harness-direction]]). Each step down is a change of absorber, not of the variety: the work is as variable as before; the lower rung now absorbs what used to climb.

In a harness ladder the engineer sits on the top rung, and an uncaught arrival there, with the chain of rungs it crossed, is what the engineer observes and orients on; the moment it opens is the kairos ([[philosophy/metis-kairos]]). What a rung absorbs is invisible above it: the top sees only what climbed, and a filter misses some signal. That is why verification goes down the ladder instead of reading the report ([[philosophy/conversation-as-interface]]).

## Why absorb low

Two reasons hold the rule up, and the ladder splits them.

- **Near-decomposability (Simon), on the lower rungs.** Parts coupled weakly, each strong inside. Varieties multiply (Ashby), so a whole made of parts that each absorb their own variety faces only the product of what leaks out. In software: layers of abstraction, loose coupling; in a harness, context economics ([[philosophy/context-economics]]).
- **Capacity (Beer), on the upper rungs.** The rung above has fewer states and a narrower channel; what climbs must be what that rung alone can decide.

In every sighting the top rung is also the slowest, and pace layering (Brand) applies: fast layers propose, slow layers dispose; the slow constrain the fast, the fast keep the slow alive; change shears between layers. Why the rungs are cut where they are is change inertia ([[philosophy/change-inertia]]).

## Sightings

| Ladder | Top | Bottom | Where |
|---|---|---|---|
| Knowledge | philosophy | know-how | [[philosophy/three-layer-harness]] |
| Process | session, the human | leaf | [[philosophy/session-design]] |
| Feedback | philosophy on trial, last | know-how, first | [[philosophy/kaizen]] |
| Harness direction | steered in session | headless | [[philosophy/harness-direction]] |
| The belt, two rungs | the engineer's type | the code's concept | [[philosophy/transmission-belt]] |

## Related

- The gradient this is the discrete form of: [[philosophy/metis-kairos]].
- Where the rungs are cut: [[philosophy/change-inertia]].
- The brick's way down the rungs: [[philosophy/harness-direction]].
- Why the engineer still goes down: [[philosophy/conversation-as-interface]].
