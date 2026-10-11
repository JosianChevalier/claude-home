---
tags: [harness-design, session-design, variety-absorption]
---

# The abstraction ladder

**Thesis.** Ways of working that let kairos reach the engineer ([[philosophy/metis-kairos]]) take the shape of a ladder: levels ordered by abstraction, each absorbing the variety it can and passing the rest one rung up.

Each rung delegates cognitive load and context to the rung below, and takes back only what that rung could not absorb. Down is closer to where variety arrives first.

```
   top      slowest; decides on what climbed; sees nothing else
    ▲  │
    │  │   up:    each rung absorbs what fits, escalates the rest one rung, wrapped, cause kept
    │  │   down:  a change trickles to every rung below; what became routine is codified one rung down
    │  ▼
  bottom    where variety arrives first
```

- **Absorb down.** Variety is absorbed at the lowest rung that can take it as business as usual: only variety absorbs variety (Beer, after Ashby).
- **Escalate up, one rung.** What breaks a rung's expectation goes to the rung above, which has the orientation to decide on it. Like an exception: the rung catches what it declared business as usual; the rest it wraps and passes on, its context added, the cause preserved. Swallowing is the failure, not passing.
- **Trickle down.** A change made on a rung is a consequence for every rung below.
- **Reliable bricks move down.** Once a rung absorbs variety as business as usual, that absorption can be codified into the rung below: commodification, one rung at a time ([[philosophy/harness-direction]]).

In a harness ladder the engineer sits on the top rung, and an uncaught arrival there is the kairos. What a rung absorbs is invisible above it: the top sees only what climbed. That is why verification goes down the ladder instead of reading the report ([[philosophy/conversation-as-interface]]).

## Why absorb low

Two reasons hold the rule up, and the ladder splits them ([[philosophy/metis-kairos]]).

- **Near-decomposability (Simon), on the lower rungs.** Variety absorbed close to where it arises; the whole faces only what leaks out of each part.
- **Capacity (Beer), on the upper rungs.** The channel narrows toward the engineer; what climbs must be what that rung alone can decide.

In every sighting the top rung is also the slowest, and pace layering (Brand) applies: fast layers propose, slow layers dispose; the slow constrain the fast, the fast keep the slow alive. Why the rungs are cut where they are is change inertia ([[philosophy/change-inertia]]).

## Sightings

| Ladder | Top | Bottom | Where |
|---|---|---|---|
| Knowledge | philosophy | know-how | [[philosophy/three-layer-harness]] |
| Process | session, the human | leaf | [[philosophy/session-design]] |
| Persistence | repo | conversation | [[philosophy/session-design]] |
| Feedback | philosophy on trial, last | know-how, first | [[philosophy/kaizen]] |
| Harness direction | steered in session | headless | [[philosophy/harness-direction]] |
| The belt, two rungs | the engineer's type | the code's concept | [[philosophy/transmission-belt]] |

The Cynefin labels in the process table of [[philosophy/session-design]] (session complex, leaf ordered) name the domain the orchestrator works in, not where variety arrives: complexity arrives at the leaf and is decided on at the session.

## Related

- The gradient this is the discrete form of: [[philosophy/metis-kairos]].
- Where the rungs are cut: [[philosophy/change-inertia]].
- The brick's way down the rungs: [[philosophy/harness-direction]].
- Why the engineer still goes down: [[philosophy/conversation-as-interface]].
