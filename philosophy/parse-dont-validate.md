---
tags: [types, invariants, context-economics, domain-modeling, reliability]
---

# Parse, don't validate

**Thesis.** A spatial cut made inside the code. Parse once, where the data enters, into a type with no invalid inhabitant; the value then carries its proof, and a call site's whole context is its signature.

## Less to read

A parsed type reduces what must be read to act. The signature says what the value is; the callers that built it, and theirs, stay closed. That is the spatial axis of a context, the blast radius, and a parsed type shrinks it (φcontext-splitting).

Separation logic calls it **local reasoning** (O'Hearn, Reynolds), the frame rule: a specification mentions only its footprint, and everything outside the footprint need not be read to understand it. A signature of parsed types is a footprint.

The feedback is the fastest there is: the checker, in the editor, before any test runs.

## Validate versus parse

King's distinction: a validation learns and forgets, a parse learns and keeps it in the type. Validation left to spread is **shotgun parsing** (LangSec): every reader checks again, so every reader must be read.

## Shape is spec

A parsed type puts the specification in the shape of the value. `[T, ...T[]]` is a non-empty array: the reader does not have to know it, they see it, and `head` is callable. The property is an **affordance** (Gibson, Norman): what the thing lets you do is visible in the thing.

A property to be aware of is cognitive load spent holding it (φzoom-levels); a property in the shape costs nothing to hold. For an agent the difference is a decision: a check is a decision at each call site, and decisions compound (φcompounding-decisions). A type is no decision at all.

## Unrepresentable, therefore unchecked

The parse holds because its target type has no invalid inhabitant: make illegal states unrepresentable (Minsky, Wlaschin), and holding the value is holding the proof. Three checks it deletes: the excluded branch (totality), the callee's precondition (Meyer's non-redundancy), the re-check on the way (immutability).

## Two levels

Low, the check is a type the language has, or narrows by decoration: `[T, ...T[]]` over an array, a brand over a string, a `Positive` over a number. The runtime value is untouched; only what the checker admits changes, and nothing is reimplemented. The field's name is refinement types (Freeman, Pfenning). Where the language cannot express one it is manufactured: a wrapper, a brand, a factory as the only door.

High, the parse is not a decoration. It is the model: which states exist, which fields each state has, which transitions each state allows. Finding that is domain modeling, and its home is φalways-valid-domain.

## Instances

In the domain: φalways-valid-domain for the model, φaggregates for the consistency boundary.

## Where the parse lives

Once, at the entry, and never again inside. The boundary is where the raw thing exists: the adapter, the deserializer, the factory. Inside, the domain holds parsed types only and re-checks nothing; a check inside is the boundary leaking.

A grammar that cannot express the type (SQL without sum types, JSON without brands) is not a reason to validate instead: parse at the crossing, back into the type, and compensate locally (φmodel-expressions).

## Vocabulary

What pulls away from it has the field's own names: primitive obsession, shotgun parsing. Both are basins already in the weights, so naming them pushes away rather than carving them (φattractors).

## Related

- The property this enforces in domain code: φalways-valid-domain.
- The cut this is the in-code form of: φcontext-splitting.
- A check as a decision: φcompounding-decisions.
- Grammar limits and local compensation: φmodel-expressions.
