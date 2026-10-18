---
tags: [batch-slicing, elephant-carpaccio, small-batches, planning]
---

# Batch slicing

**Thesis.** Everything is a hypothesis, and only feedback settles it. Batch slicing is finding the next hypothesis to test, and cutting the smallest slice that can test it. First an increment of value, then the steps that build it.

## Everything is a hypothesis

A user story bets that users want it. A step bets that the app still works. A commit bets that it merges without trouble. Any change is a bet, and only feedback settles it. A slice is the unit that puts one bet in front of its feedback. Each bet has its feedback loop, and the loops nest, the faster inside the slower ([[philosophy/feedback-loops]]).

## Increments of value

The top level: a functional increment that brings value to someone. Users, stakeholders, or engineers: monitoring is value too. Its bet is that they want it, and only production settles it. So the cut looks for the next hypothesis, and for the thinnest increment that reaches production to test it. Each piece is pulled: built because its user asks for it, and used as soon as it lands, just in time (Ohno). Elephant carpaccio (Cockburn) names this level.

The usual bad cuts:

- **All of CRUD when only read is used.** Create, update and delete get built before read has shown anyone wants the data.
- **A whole layer before moving up.** Nothing is tested until the top layer lands.

## Steps

Under each increment, the plan cuts steps. A step is a mission, in the sense of mission command (Auftragstaktik): it gives the intent, never the way. The intent holds a purpose, why the step serves the increment, and an end state: what matters, as it should stand once the step is done. In code, that is the code that matters, as it should read; elsewhere, a sketch or a sentence. What else has to change for it is left to those who carry it out.

The end state is the next shape of the same work, not a piece to build. Step after step, the work changes shape.

A step ends working and shipped, and banks no value.

The increment owns the plan; steps serve it. Layer steps with no increment above them are the bad cut "a whole layer before moving up".

## How big a step is

Understanding sets the size, not time: with agents, almost anything fits in one sitting. A mission is sized like an objective on a map: "take the bridge", not "take the region", nor "advance ten metres". The commander thinks in objectives; the units, in movements.

- **Between two steps, we know where we are.** Each boundary is a state a human can name and understand, a point on the map.
- **One step, one effect.** It has the unity and atomicity of an effect: done or not done. Two effects, two steps. Half an effect leaves a state nobody can name.
- **Never halfway across the ford.** The target is reached through lesser hills, each coherent on its own. A valley is crossed within a step, never stopped in (Kauffman). Making the change easy finds the path ([[philosophy/make-the-change-easy#Finding the path]]).
- **Too big**, nobody can say where we are until it ends. A step that resists a smaller cut often hides a redesign.
- **Too small**, the plan gives the way: the units' job, done from above.

## Inside a step

Execution is decentralized. Those who carry out the step choose the way: the smaller steps, the approaches, the adjustments when the ground is not what the plan assumed. The intent keeps them together: lost, they go back to the end state, not to a route. If the end state itself proves wrong, it goes back up; the intent is changed by whoever gave it.

The step is the human's unit of thought; below it, the plan says nothing.

## Related

- Why small: [[philosophy/batch-size-economics]].
- Crossing the valley: [[philosophy/make-the-change-easy]].
- Changing a live path, step by step: [[philosophy/change-in-place]].
- The floor below the step: [[philosophy/atomic-commit]].
