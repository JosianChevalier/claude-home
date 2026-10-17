---
tags: [types, invariants, context-economics, domain-modeling, reliability]
---

# Parse, don't validate

**Thesis.** A spatial cut made inside the code. Parse once, where the data enters, into a type with no invalid inhabitant; the value then carries its proof, and a call site's whole context is its signature.

## Less to read

A parsed type reduces what must be read to act. The signature says what the value is; the callers that built it, and theirs, stay closed. That is the spatial axis of a context, the blast radius, and a parsed type shrinks it ([[philosophy/context-splitting]]).

Separation logic calls it **local reasoning** (O'Hearn, Reynolds), the frame rule: a specification mentions only its footprint, and everything outside the footprint need not be read to understand it. A signature of parsed types is a footprint.

The feedback is the fastest there is: the checker, in the editor, before any test runs.

## Validate versus parse

King's distinction: a validation learns and forgets, a parse learns and keeps it in the type. Validation left to spread is **shotgun parsing** (LangSec): every reader checks again, so every reader must be read.

## Shape is spec

A parsed type puts the specification in the shape of the value. `[T, ...T[]]` is a non-empty array: the reader does not have to know it, they see it, and `head` is callable. The property is an **affordance** (Gibson, Norman): what the thing lets you do is visible in the thing.

A property to be aware of is cognitive load spent holding it ([[philosophy/zoom-levels]]); a property in the shape costs nothing to hold. For an agent the difference is a decision: a check is a decision at each call site, and decisions compound ([[philosophy/compounding-decisions]]). A type is no decision at all.

## Unrepresentable, therefore unchecked

The parse holds because its target type has no invalid inhabitant. Make illegal states unrepresentable (Minsky, Wlaschin): then holding a value of the type is holding the proof. Propositions as types reads the same way: a value of `NonEmpty<T>` is a proof that the list has a head.

Three consequences, each a check deleted:

- **Totality.** A function over a parsed type is total over it: no branch for the case the type excludes, no caller-dependent behaviour.
- **Non-redundancy** (Meyer, design by contract). A precondition is checked on one side only. Once the type is the precondition the callee checks nothing; checking anyway is defensive programming, client and supplier both paying.
- **No re-validation on the way.** The value cannot have lost the property: immutable, it is what it was parsed as.

## Two levels

Low, the check is a type the language has, or narrows by decoration: `[T, ...T[]]` over an array, a brand over a string, a `Positive` over a number. The runtime value is untouched; only what the checker admits changes, and nothing is reimplemented. The field's name is refinement types (Freeman, Pfenning). Where the language cannot express one it is manufactured: a wrapper, a brand, a factory as the only door.

High, the parse is not a decoration. It is the model: which states exist, which fields each state has, which transitions each state allows. Finding that is domain modeling, and its home is [[philosophy/always-valid-domain]].

## Sightings

| Where data enters | Enters as | Parsed into | Check deleted downstream |
|---|---|---|---|
| Domain model | primitives, flags | value object, one type per state | the null check, the status switch |
| Aggregate | several objects | one root as sole handle | the cross-object consistency check |
| Left adapter | request, arguments, message | command | re-reading the request shape in the domain |
| Configuration | strings from the environment | typed settings, once at startup | the missing-key check at use |
| SPI failure | an exception | `Result`, the error in the signature | the blind `catch` |
| Sub-agent | an exploration | a conclusion | reading the exploration |

The domain and aggregate rows: [[philosophy/always-valid-domain]], [[philosophy/aggregates]]. The last row is the same cut one level up: [[philosophy/context-splitting]].

## Where the parse lives

Once, at the entry, and never again inside. The boundary is where the raw thing exists: the adapter, the deserializer, the factory. Inside, the domain holds parsed types only and re-checks nothing; a check inside is the boundary leaking.

A grammar that cannot express the type (SQL without sum types, JSON without brands) is not a reason to validate instead: parse at the crossing, back into the type, and compensate locally ([[philosophy/model-expressions]]).

## Vocabulary

What pulls away from it has the field's own names: primitive obsession, shotgun parsing, defensive programming. All three are basins already in the weights, so naming them pushes away rather than carving them ([[philosophy/attractors]]).

## Related

- The property this enforces in domain code: [[philosophy/always-valid-domain]].
- The cut this is the in-code form of: [[philosophy/context-splitting]].
- A check as a decision: [[philosophy/compounding-decisions]].
- Grammar limits and local compensation: [[philosophy/model-expressions]].
