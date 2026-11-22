---
tags: [ux, ddd, domain-modeling]
---

# UX

**Thesis.** The screen is the view of the model exposed to the user, an expression whose grammar is human cognition; designing it has the two axes of DDD, which models it exposes, then how the grammar expresses them.

## The grammar is cognition

The UI is one expression of the model (φmodel-expressions), the view exposed to the user. Its grammar is human cognition, 4E: the screen leans on what cognition carries unprompted, grouping, expectation, sequence, salience, and draws only the rest, Tufte's data-ink. What perception and habit carry is free, what memory would have to carry goes on the screen: knowledge in the head and in the world (Norman). The Laws of UX (Yablonski) catalogue that grammar, each a limit read as a lever.

## Two axes

Designing a screen has the two axes of DDD (Evans). Strategic: which models the screen exposes, and in whose words. Tactical: how that view is expressed in the grammar, where the laws apply.

Conceptual models (Johnson & Henderson) are the equivalent, in UX, of Evans's strategic design: the conceptual model is designed before the screen, and the screen is its presentation. That is the pivot between model and UI. Their lexicon, one set of terms for the interface, the code and the documentation, is Evans's ubiquitous language. Object-oriented UX (Prater) makes the same move as a method: the objects come before the actions and the layout.

## Tied to the backend's model

The screen ties to the model the backend holds through HATEOAS (Fielding): the response carries the transitions the model allows now, and the screen renders each as an affordance. A transition the model withdraws is a link absent, then an affordance absent. In the other direction the screen sends an intent, a command named as the model names the operation: the task-based UI (Young), Microsoft's inductive user interface before him.

## Related

- The model as expressed, each expression bounded by its grammar: φmodel-expressions.
