---
tags: [harness-design, session-design, cynefin, architecture]
---

# Rationale: The Abstraction Ladder

An approach: ways of working compliant with [[philosophy/metis-kairos]] take the shape of a ladder. Levels ordered by abstraction, each rung delegating cognitive load and context to the rung below, and taking back only what that rung could not absorb. Down is closer to where variation arrives first.

- **Absorb down.** Variation is absorbed at the lowest rung that can take it as business as usual.
- **Escalate up, one rung.** What breaks a rung's expectation goes to the rung above, which has the orientation to decide on it. In a harness ladder the engineer sits on the top rung, and the arrival there is the kairos.
- **Trickle down.** A change made on a rung is a consequence for every rung below.
- **Reliable bricks move down.** Once a rung absorbs a variation as business as usual, that absorption can be codified into the rung below ([[philosophy/harness-direction]]).

In the harness ladders the top rung is also the slowest, and pace layering (Brand) applies: fast layers propose, slow layers dispose; the slow constrain the fast, the fast keep the slow alive; change shears between layers. Hexagonal architecture shows that inertia is not the ordering axis: the domain on top is the fast-evolving part, and the inertia of databases and external tools is the environment the bottom rung absorbs.

## Sightings

| Ladder | Top | Bottom | Where |
|---|---|---|---|
| Knowledge | philosophy | know-how | [[philosophy/three-layer-harness]] |
| Process | session, the human | leaf | [[philosophy/session-design]] |
| Persistence | repo | conversation | [[philosophy/session-design]] |
| Feedback | philosophy on trial, last | know-how, first | [[philosophy/kaizen]] |
| Harness direction | steered in session | headless | [[philosophy/harness-direction]] |
| The belt, two rungs | the engineer's type | the code's concept | [[philosophy/transmission-belt]] |
| Architecture | domain logic | adapters, meeting databases and tools | hexagonal |

The Cynefin labels in the process table (session complex, leaf clear) name the domain the orchestrator works in, not where variation arrives: complexity arrives at the leaf and is decided on at the session.
