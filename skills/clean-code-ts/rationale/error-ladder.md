---
tags: [typescript, type-safety, error-handling]
---

# Rationale: The Error Handling Ladder

Governing distinction: a thrown exception is a **non-local goto**; a returned error is a **value**. Values appear in signatures, compose, and can be matched exhaustively; gotos are invisible to the type system but free to write. The ladder prices each failure by one question — inherited from @rules/exception-strategy.md: *must someone react to this?* If yes, make it visible in types; if no, let it propagate.

## Rung 1 — tagged union: failure as outcome

When the caller decides what happens next, failure is not exceptional — it is part of the function's real codomain. Returning it as data makes the function **total** over that codomain, and exhaustive `switch` + `assertNever` turns "did every caller handle every case?" into a compile-time question. New outcome variant → every call site fails to compile until handled.

## Rung 2 — railway: recoverable failure in a flow

Railway-oriented programming (Wlaschin): monadic short-circuiting factors the repeated "if failed, skip the rest" out of every step, and the error type rides in the signature. The economic test in the skill ("cheaper than try-catch at every step") is literal — past roughly two failure points in a flow that is already a pipeline, the Result chain is less code *and* keeps the flow declarative.

## Rung 3 — local try-catch: don't tax the trivial

Monads are a tax when recovery is one line sitting right next to the risky call in already-imperative code. Threading a `Result` through there is ceremony — the inverse error of rung 2. The boundary condition matters: a try-catch must not interrupt a functional pipeline with imperative logic; if the failure crosses steps, it belongs to rung 2.

## Rung 4 — throw: no one can react

Bugs, broken invariants, unreachable states: visibility buys nothing because no caller has a meaningful reaction. Throw, never catch in the domain, translate at the boundary (left adapter → 500, NACK…). Catching these in the domain doesn't handle the bug — it hides the evidence.
