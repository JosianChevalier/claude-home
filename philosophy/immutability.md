---
tags: [craft, clean-code, functional-programming, domain-modeling, reliability, context-economics, refactoring]
---

# Immutability

**Thesis.** A value that never changes after creation keeps a change local. It removes the margin of error, which cuts both the decisions that compound and the spatial context to read.

## Aliasing

A value that is mutable and shared is **aliased**: every name holding it sees every write made through any other. To know what it holds, every place that holds it has to be read, with its context. Reasoning goes global, and a change's blast radius becomes the whole reference graph (φcontext-splitting, the spatial axis).

An immutable value can be held anywhere and still be read in one place: **local reasoning** (O'Hearn, Reynolds), as with a parsed type (φparse-dont-validate). Code is the level an agent walks through (φlevel-design): what it has read stays true behind it.

## Side effects

Accidental complexity grows with the combinatorics side effects bring in. An immutable domain layer goes with keeping them out: the domain meets infrastructure only at entry and exit, the **functional core, imperative shell** (Bernhardt).

- **Invariants stay explicit**: implemented once, on the value that holds them.
- **Composition**: functions compose because their inputs can't change under them.
- **States as values**: each state of φtypestate is its own value, carrying the data of the states before it.
- **Concurrency at the edges**: synchronisation happens at the start and end of a business process, in the infrastructure, never inside the domain.

## For an agent

- **A removed decision.** "Has it changed since I read it?" is never asked; an error that can't be made doesn't compound (φcompounding-decisions).
- **Moves without checks.** Immutable code is referentially transparent: reorder and loop-to-map need no precondition check, so the agent refactors without understanding the code (φmechanical-refactoring).

## Where it is hard

Enforcing immutability shows where it is hard to hold. That difficulty is usually a model tension (φmodel-phenomenology): a signal of a design issue.

## Sharing, a minor reason

Sharing is the point of a **value object** (Evans): being immutable, it can be held by any number of owners, a **flyweight** (GoF). A changed value copies only what changed and points at the rest: **structural sharing**. This is a performance gain, not a reason on its own.

## Related

- The spatial axis a change's blast radius lives on: φcontext-splitting.
- Local reasoning through types: φparse-dont-validate.
- Moves that need side-effect-free code: φmechanical-refactoring.
- A decision removed rather than made: φcompounding-decisions.
- States as values: φtypestate.
- The tension felt where immutability resists: φmodel-phenomenology.
