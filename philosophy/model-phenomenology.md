---
tags: [ddd, collaboration, domain-modeling, conceptual-integrity, cognitive-load, phenomenology]
---

# Model phenomenology

**Thesis.** The engineer holds a type, the code holds concepts, and every write forces the one through the other; the agent holds neither, and transmits.

Two gestalts are in play, on two sides of a seam. The code's gestalt is the conceptual integrity of the **concept**. The engineer's gestalt is something else in kind. This document names the two sides and what the agent is between them; what kind of transmission runs across the seam is the belt ([[philosophy/transmission-belt]]).

```
engineer's type        every write forces a concept       concept in the code
open, revisable,   ─────────────────────────────────▶   finite, predicative,
with a horizon     ◀─────────────────────────────────   definable
                    the concept's resistance: tension, felt

agent: sedimented culture, the library not the librarian; transmits, never originates
```

## Prägnanz, conceptual integrity, model tension

Gestalt psychology's founding claim: a whole is *other than* the sum of its parts — a melody survives transposition though every note changes. Its governing law is **Prägnanz**: perception settles on the simplest, most stable organisation the stimulus permits, the way a soap film settles on a minimal surface.

Two properties matter. Simplicity is relative to a vocabulary — a figure is pregnant in one and shapeless in another. And goodness includes stability — a good gestalt resists reorganisation; a poor one is fragile or flips.

In software the good gestalt has a name: **conceptual integrity** (Brooks). A model with conceptual integrity is one whose bounded context fixes the vocabulary against which it is simple, and which stays simple under use.

**Model tension** is its felt negation: not a defect you can point at, but the effort of maintaining a coherence the model does not provide on its own. The image is muscle tension: a body braces to hold together what does not hold itself, often against a load that originates elsewhere. Merleau-Ponty's *maximal grip*, in Dreyfus's reading, names it from the inside: the body constantly adjusts toward optimal hold on a situation, and deviation is felt before it is thought.

Model tension is seen before it is diagnosed: an expert recognises a shape at a glance, and the [model tension heuristics](https://gitlab.com/beyondxscratch/model-tension-heuristics/-/blob/main/english_version.md) name those shapes ("Implicit Lifecycle": adjectives clinging to a noun; "Recurring Tasks": a repeated preamble). The tests that diagnose it come after the feeling ([[philosophy/model-expressions]]).

## What the engineer holds: type, horizon, metis

Husserl distinguishes the **concept** — predicatively fixed, finite, definable — from the **type**: the pre-predicative familiarity you have with a thing after many encounters, open, endlessly revisable, never exhausted. Every type projects a **horizon**: the co-intended but not-given — the back of the cube, the cases not yet met.

A veteran of ten years in a domain has a *type* of "product", not a definition of it. A local reading is a well — deep, narrow, from the bottom you see only its walls. For the veteran the wells have become shallow basins: they drop into any local reading and climb out without effort, and the transition is so seamless that they stop being aware of it. This is why experts struggle at modeling. Wittgenstein from the other side: "product" has no necessary and sufficient conditions, only family resemblances. Polanyi: they know more than they can tell. The operative form is **metis** — cunning, situated practical intelligence that cannot be codified and that legible schemes destroy when they replace it (Scott, after Detienne and Vernant); what it seizes is in [[philosophy/metis-kairos]].

## What the code holds: concepts only

Code is finite, explicit, predicative. It can hold concepts and only concepts. This is not a tooling limit but an ontological one, and it is why software *needs* models at all: a model is the idealisation — Husserl's "garb of ideas" — that a type must be forced through to become executable. Naur (1985): a program is a theory held by its programmers and dies when they leave. The extension: that theory is a type with a horizon, the text cannot hold it, and the signal of the parting is tension.

The **type-to-concept transition** is therefore the central act of development. Every write forces a concept; the type has no favoured one.

Two failure modes, mirror images:

- **The veteran**: fluent reader, spork writer. A type emitted through whichever local concept each spot suggests, none chosen (below). That is a big ball of mud.
- **The recruit**: a concept with no type to revise it against — stuck at the bottom of one well.

## Rivalry and the spork

A type projects more than one concept that fits. Two predications of "product", both complete, both consistent; the code cannot tell them apart, because telling them apart needs the horizon, and only the type has one. This is **rivalry**, and it is the normal case of the transition, not an accident: a type with a horizon has no favoured concept.

What to do with a rivalry is already said elsewhere: it goes up to the holder of the horizon. A rival reading is offered at a gate ([[philosophy/kairos-gates]]); an unchosen concept returns up the belt ([[philosophy/transmission-belt]]). Model tension is the same arrival felt from the code side, and the gate that catches it after a model change is in the same file.

Two ways of settling it below instead, and both report success:

- **Silent choice** — one reading picked, the engineer discovers late that the direction was decided below ([[philosophy/collaborative-production]]). A concept came out, at least.
- **The spork** — none picked. Two complete readings of one concept fit, and instead of two contexts with a translation at the seam, one artifact is made to hold both: the union of their state, the intersection of their behaviour, which is nearly empty. What remains is get, set, save. The lens-switching a type does without effort is pushed into the artifact, which cannot do it, so each use site does it instead: the translation inlined everywhere, each use paying the dispatch, never located in one anti-corruption layer.

The spork is not the god object: that one fails on cohesion and splits into differently named things; the spork fails on context and splits into two things with the same name. The veteran writes it fluently: the basins hopped without noticing, emitted as code.

## What the agent holds: sedimented culture

The agent is not a third holder of a type. Gopnik's reading: a large language model is a **cultural technology**, in the family of writing and print — a transmission of accumulated human typifications, not a learner and not an agent in her sense, because it did not build its familiarity through intervention and exploration in *this* world. It carries sedimented generic domain knowledge: millions of people's typifications of "order", "product", "transfer", second-hand. That is why it emits concepts fluently — it is made of the language in which types get predicated. It is also why it cannot originate: its familiarity is generic, unsituated, without the horizon that only coping in this organisation, with this data, produces. The library, not the librarian.

This settles the agent's role: **transmission**. It moves the engineer's situated type toward concepts in code, and moves the concept's resistance back toward the type, at conversational speed. The medium that used to sit between the two — keyboard, language, IDE, the extraneous load in Sweller's sense — is what the agent removes. The library was the first belt across time; the agent is the first belt that runs at the speed of a conversation.

The same fact settles what the agent may do with its familiarity: it supplies and never adjudicates. Handing over a reading the engineer has not met is the library's job; choosing between readings needs a horizon, and only the type has one. A better idea from the library is a rival reading put on the table ([[philosophy/kairos-gates]]), never a substitution made in the code.

The agent's own failure mode follows: the veteran's, at scale — it resolves rivalries by emitting a spork and reports success. What the transmission must do about that is the belt ([[philosophy/transmission-belt]]).

## Related

- What kind of transmission runs across the seam: [[philosophy/transmission-belt]].
- What the type seizes when the concept resists: [[philosophy/metis-kairos]].
- Where supply without adjudication is put to work: [[philosophy/kairos-gates]].
- The tests that come after the feeling: [[philosophy/model-expressions]].
- The seam seen from the workflow side: [[philosophy/collaborative-production]].
