---
tags: [typescript, code-structure, cohesion]
---

# Rationale: Closures First, Classes for Cohesion

Closures and objects are duals — the old koan: "a closure is a poor man's object; an object is a poor man's closure." Both bind behavior to captured context. The difference is arity: a closure carries **one** behavior over its context; an object carries **many** over shared state. Picking between them is therefore not a style question but a **cohesion** question (Constantine): units that share context and change together belong together.

- One behavior + context → closure. The cheapest construct that does the job; TypeScript functions are first-class values, so class ceremony buys nothing here. (The class-with-`apply` form was a Java transplant: Java needs a class because functions aren't values there.)
- Several closures capturing the **same** context, calling each other, evolving together → you have hand-rolled a class through parallel captures; promote it. The class makes the shared context explicit and gives the cluster one name.

The repository shape (a few cohesive operations over one shared store) is the archetype of the second case — communicational cohesion in its purest form — which is why it's the reference even though real repositories are infrastructure. `MaintenanceCalendar` is the same shape in pure domain.

The gradient also gives the demotion test: a class whose methods don't share `this` is closures wearing a trench coat — split it back down.
