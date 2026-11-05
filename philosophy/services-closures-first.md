---
tags: [craft, clean-code, functional-programming, code-structure]
---

# Closures first

**Thesis.** A closure by default; a class only when cohesion (Constantine) asks for one.

Closure and object are duals. What differs is arity: one behaviour over a context, or several over shared state.

- **Promote**: several closures that capture the same context, call each other and change together are a hand-rolled class. The repository is the archetype.
- **Demote**, one litmus test among others: a class whose methods don't share `this` may be closures in a trench coat.
