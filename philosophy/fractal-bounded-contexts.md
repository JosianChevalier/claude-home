---
tags: [ddd, bounded-contexts, domain-modeling, architecture]
---

# Fractal bounded contexts

**Thesis.** A bounded context is a shell: strategic design sees only the model it exposes, the inside is free, and the shape repeats at every scale, down to a widget.

The bounded context (Evans) is where a model and its language hold: one word, one meaning (Verraes). The reading added here is where that boundary is looked at from. From outside, a context is only what crosses its boundary: the language it speaks, the decisions it makes, what comes in and what goes out. The Bounded Context Canvas (Tune, Gunia, DDD Crew) describes a context entirely by those and says nothing of its inside, and that is the point, not a simplification.

## The shell

Strategically, a context *is* its exposed model. Two contexts are two because what they expose differs in meaning, not because two teams or two deployables stand behind them (Khononov's physical boundary is a consequence, not the test; the tests are in φmodel-expressions). What sits inside the shell has no strategic existence: several models, vertical slices each with their own representation, a hidden context or three. A shell can obfuscate a whole context map.

## Fractal

The shape repeats. Zoom out: a product is a shell exposing one language to its market. Zoom in: a context exposes one model to its neighbours; inside, a slice exposes one capability; inside again, a widget exposes one value. Brandolini's EventStorming already zooms this way, Big Picture then Design-level, the same notation at each depth. Each level is a shell to the level above and a map to the level below (φzoom-levels).

The smallest shell is a complicated widget. A triad picker has its own representation of the world, pointer, drag, snap, geometry, and emits one barycentric coordinate. From its page it is a value object; from inside it is a tiny application with its own model. Both are true, at two zoom levels.

## The gate

A sub-shell is drawn when the inside says something the exposed model does not: a concept with no outside name, a rule the outside cannot state. Until then the widget is a value object and some UI, and drawing a context around it is a compensation for complexity that is not there (φsystems-of-compensations). The default is the value object; the inside earns its map.

## Not a relationship

Rendering another context's widget in one's own page is not Conformist, nor any context-mapping pattern (Evans; Plöd for the team reading). The widget is one expression of the neighbour's model, shown elsewhere: layers are expression boundaries, not model boundaries (φmodel-expressions). The relationship patterns apply where a model meets another model, not where pixels meet a page.

## Related

- One model or two, settled by test: φmodel-expressions.
- Tiny contexts, integrity owed within and not between: φchange-inertia.
- A level is a shell above and a map below: φzoom-levels.
- The consistency boundary inside the shell: φaggregates.
