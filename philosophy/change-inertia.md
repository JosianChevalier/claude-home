---
tags: [architecture, domain-modeling, conceptual-integrity, harness-design]
---

# Rationale: Change Inertia

Inertia is the effort it takes to put movement into a system. A system that stops moving is dead: the market, the organisation, the technology, and above all the team's understanding keep moving, and the code has to follow. Inertia is what resists.

## Inertia compounds

Coupled to a heavy part, the light part drags it into every experiment: instead of moving a 5 kg object, one hauls the 50 kg ball chained to it. And coupling adds inertia non-linearly: moving one 40 kg bag takes more energy than moving two of 20. Two consequences: cut between what has high inertia and what has little, so the light part moves at its own speed; and cut small, down to the smallest models a business problem allows.

The same mechanism acts on practices. A team that wants to change a convention, the naming, the approach to mocks, its model, everywhere at once, faces the whole codebase's weight. So it experiments less, queues the change as cleanup tickets for when there is time to breathe, and the inertia of its practices and its model grows. Continuous improvement is the first casualty; continuous is not once in a while.

## Integrity is local

Conceptual integrity is the property of a system that stays coherent and clear: uniform practices, one model, one vocabulary. Motion threatens it: evolving constantly in different directions dissolves it, and freezing to protect it is the trap above. The resolution is tiny bounded contexts, each with light inertia, each free to keep the architecture, test strategy, model, and style that work in its context. Integrity is required within each context, not between them.

Two reasons not to demand it between contexts, nor even within one while experimenting. The broken-window theory, often cited for entropy in software, is refuted in sociology and at best a sophism here. And the cost of transferring ownership of a codebase, the other usual reason for uniformity, is high in any case: code is hard to separate from the people who build it, and forcing the separation pays in documentation and inertia, justified only in cases like open source.

## Seams

Each row keeps a heavy side and a light side on their own sides of a seam.

| Heavy | Light | Seam |
|---|---|---|
| Public API, backward compatibility, versions | domain model | the API is a separate model, behind an anti-corruption layer |
| Public API | our own frontend | a dedicated private API; two APIs pay off quickly |
| Database, historical data, migrations | domain model | in-memory persistence while prototyping; an anti-corruption layer once the database is real; align the schema when the model has settled |
| Platform, stable for its consumers | stream-aligned team | a golden path that teams may bypass |
| Supporting and generic subdomains | core domain | concerns offloaded out of the core, so it iterates on production feedback |
| Codebase-wide conventions | one context's practice | the bounded context: integrity within, none owed between |
| Philosophy, the understanding of the activity | know-how in rules and skills | the doctrine and the rationale ref ([[philosophy/three-layer-harness]]) |
| The philosophy corpus | one idea | one idea per file, wikilinks between |

## Related

- The layers stay apart because their lifecycles differ: [[philosophy/three-layer-harness]].
- How variation flows across the rungs, where this file says where to cut them: [[philosophy/abstraction-ladder]].
- Foundation: pace layering (Brand), change shears between layers.
