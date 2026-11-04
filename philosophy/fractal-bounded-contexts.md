---
tags: [ddd, bounded-contexts, domain-modeling, architecture]
---

# Fractal bounded contexts

**Thesis.** A bounded context is the limit of applicability of one model and exposes that model to the world; implementing it may hide other contexts inside, down to a single algorithm or widget.

A bounded context (Evans) is the limit of applicability of one model, and it exposes that model: from outside, a context is the language it speaks and what crosses its boundary, nothing else (the Bounded Context Canvas, Tune and the DDD Crew, describes one by that alone); a microservice is a context, a context is not a microservice. Implementing it sometimes takes things the rest of the world never sees, a representation the exposed model has no word for; that inside is hidden from strategic design, a context within the context, and the shape repeats at every scale, as EventStorming keeps one notation from Big Picture to Design-level (Brandolini).

Evans's shipping example has one: the routing service takes an itinerary's legs and hands them to a network traversal model that knows only nodes, arcs and paths, so a graph algorithm can run; the service translates back. A tiny module around one algorithm, with a different representation, is technically a bounded context. The same shape sits in a front: a sub-component carrying more complexity than the value it emits has its own representation inside, pointer, drag, geometry, and is a value object to its page. The inner context is drawn when the inside says something the exposed model cannot, a concept with no outside name; until then it stays a value object and some UI.

A subdomain is a part of the problem, a bounded context a part of the solution (Vernon): the business is cut into subdomains by what it does, the solution into contexts by which models hold together, and the two cuts need not coincide. A context is built for one purpose, one subdomain's problem, and kept small: a small model keeps its conceptual integrity (Brooks), asks less of whoever holds it, and moves at its own inertia (φchange-inertia). Where one model serves two purposes it strains, and the strain is where the seam goes (φmodel-phenomenology).

## Related

- Where the seam goes: one model or two settled by test, and the tensions that show it before the test: φmodel-expressions, φmodel-phenomenology.
- Tiny contexts, integrity owed within and not between: φchange-inertia.
- A level is a shell above and a map below: φzoom-levels.
