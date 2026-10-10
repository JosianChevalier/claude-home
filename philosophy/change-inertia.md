---
tags: [architecture, domain-modeling, conceptual-integrity, harness-design]
---

# Rationale: Change Inertia

A product and its codebase must stay in motion or they are dead: the market moves, the organisation moves, the technology moves, and above all the team learns. When context or understanding changes, the code must change too. Inertia is the effort it takes to put movement into a system.

## The cutting heuristic

Separate what has high inertia from what has little, so the light part can move at its own speed. A database schema is harder to change than a model made of plain objects, so coupling the domain to the database makes every modelling experiment drag the database's weight: instead of moving a 5 kg object, one hauls the 50 kg ball chained to it.

Coupling adds inertia non-linearly: moving one 40 kg bag takes more energy than moving two of 20. That is why business problems are divided into the smallest models possible.

| Heavy side | Light side | Seam |
|---|---|---|
| Public API, backward compatibility, versions | domain model | the API is a separate model, with an anti-corruption layer |
| Public API | our own frontend | a dedicated private API; two APIs pay off quickly |
| Database, historical data, migrations | domain model | in-memory persistence while prototyping; an anti-corruption layer once the database is real; align the schema when the model has settled |
| Platform, stable for its consumers | stream-aligned team | a golden path that teams may bypass |
| Supporting and generic subdomains | core domain | offload concerns out of the core, so it can iterate on production feedback |

## The consequence: conceptual integrity dissipates

Conceptual integrity is the property of a system that stays coherent and clear: uniform practices, one model, one vocabulary. Practices and models evolve. Keeping integrity across a whole codebase at once costs so much that the team stops experimenting and queues tickets for naming, line length, the approach to mocks, to be handled when there is time to breathe. The inertia of its practices and its model has grown, and continuous improvement is cut off; continuous is not once in a while.

Evolving constantly in different directions loses integrity too. The answer is tiny bounded contexts, each with light inertia, each free to keep the architecture, test strategy, model, and style that work in its context. Integrity is required within each, not between them.

Two objections not to accept: the broken-window theory, refuted in sociology and at best a sophism in software; and the cost of transferring ownership of a codebase, which is high in any case, since code is hard to separate from the people who build it, and forcing the separation pays in documentation and inertia, justified only in cases like open source.

## In the harness

The three layers stay apart because their lifecycles differ ([[philosophy/three-layer-harness]]); a philosophy file holds one idea so that each can move on its own. Where the abstraction ladder ([[philosophy/abstraction-ladder]]) says how variation flows across the rungs, this file says why the rungs are cut where they are. Pace layering (Brand) is the shared foundation: change shears between layers.
