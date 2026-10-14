---
tags: [cognition, code-review, harness-design, collaboration]
---

# Embodied navigation

**Thesis.** The engineer thinks with the code by moving through it. Seeing it is not enough. For the best result, the code needs a stable spatial representation, and the engineer needs to navigate it actively.

This is the embodied face of the enacted loop ([[philosophy/collaborative-production]]). In its original sense (Varela, Thompson & Rosch), enaction is sensorimotor: a world is known by acting in it.

## The body thinks in space

Abstract thought reuses the body's spatial machinery:

- *Image schemas* (Lakoff & Johnson): container, path, near and far, learned bodily, carry abstract concepts.
- *Mental rotation* draws on motor circuits (Wexler, Kosslyn & Berthoz).
- *Grid cells*, the brain's code for physical space, also map abstract concept spaces (Constantinescu, O'Reilly & Behrens).

So a codebase laid out in space is navigated with the same machinery as a place. Position becomes something felt, not read.

## Viewing is not enough

Perception is built from the movements it affords: the *sensorimotor contingencies* (O'Regan & Noë). A representation one only looks at leaves the engineer a spectator, and the spectator builds no model ([[philosophy/collaborative-production]]).

A representation earns its place when the engineer acts on it: Kirsh & Maglio's *epistemic actions*, moves made to think, not to reach a goal. Coupling, not a picture.

## Two conditions

**For optimal result, we need stable spatial recognition and active navigation.**

- **Stable spatial recognition.** A thing stays where it was. Moving everything erases spatial memory: graph drawing calls the requirement *mental map preservation* (Misue, Eades et al.). Position derives from meaning, such as architectural role, not from layout accident, so a move is itself a signal. Stable across the team, the map becomes a shared artifact, a common reference: *distributed cognition* (Hutchins).
- **Active navigation.** The engineer chooses where to go. Wayfinding builds *route knowledge*, the sequence walked, and *survey knowledge*, the map from above (Siegel & White); a cognitive map grows from moving between the two.

One without the other fails: a stable map one is walked through is a guided tour; free movement in a shifting space never settles into a map.

## Related

- [[philosophy/collaborative-production]]: enaction, and why the spectator pays.
- [[philosophy/conversation-as-interface]]: gemba and the elevator, the embedded face.
- [[philosophy/zoom-levels]]: scale, the other dimension of the map.
