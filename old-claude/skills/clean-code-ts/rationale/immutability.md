---
tags: [typescript, immutability, cognitive-load]
---

# Rationale: Immutability

> **DRAFT — to be rebuilt from the training slides. Placeholder argument below.**

## Cognitive load

A mutable object is an open variable in the working set of *every* scope that holds a reference to it (aliasing): to know its value you must know every writer, so reasoning becomes global. An immutable value means one thing for its whole lifetime — reasoning stays local, and a name can be trusted wherever it appears (referential transparency). Hickey's critique of *place-oriented programming* names the root confusion: mutation conflates identity with state; immutable values + explicit transitions separate them.

## Functional approach

Immutability is the enabling assumption behind the rest of the skill: pipelines (`.map` steps can't corrupt their input), structural sharing (`{ ...this, deliveryAddress }`), typestate (the old reference keeps its old type honestly), event accumulation (history as appended facts), and safe concurrency (nothing to race on).
