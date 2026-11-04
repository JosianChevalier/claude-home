---
tags: [typescript, type-safety, domain-modeling, immutability, always-valid-domain]
---

# Rationale: States as Types (Typestate)

The technique is **typestate** (Strom & Yemini, 1986; popularized by Rust API design): encode an object's lifecycle state in its *type*, so an operation exists only on the states where it is legal. `cancel()` is not guarded on `OrderExpedited` — it is *absent*; the illegal transition is a compile error, not a runtime branch.

## Why types beat runtime guards

Shift-left of failure detection: a runtime check catches the bug in production, or in a test if someone wrote it; a type makes the bug **unwritable**. This is the transition-level counterpart of @rules/always-valid-domain.md — value objects make invalid *values* unrepresentable, typestate makes invalid *transitions* unrepresentable. Consumers then demand the only state they can handle (`processOrder(order: OrderReady)`), which deletes a whole class of defensive checks downstream.

## TypeScript specifics

Union types plus literal discriminants give the exhaustiveness Java needs `sealed` for. The explicit literal annotation (`readonly state: OrderState.Ready = OrderState.Ready`) is what lets *classes* participate in discriminated-union narrowing.

## Immutability is load-bearing

Transitions return a fresh instance of the next state's type. Mutating in place would let a reference's runtime state diverge from its static type — the type would lie. Typestate formally wants linear/affine handling of the old reference; in practice, immutability plus "use the returned value" is the JavaScript-world equivalent. Each transition appending its domain event is the same discipline applied to history: state is derived, changes are facts.
