---
tags: [planning, probe-sense-respond, cynefin, session-state]
---

# Planning is everything

**Thesis.** Planning is everything, the plan is nothing (Eisenhower): a plan is direction, not prescription, redrawn by what its probes return.

## Two objects, two reasons to probe

The code is deterministic, inspectable, finite: Cynefin's complicated domain. It is still probed rather than analyzed, because the probe is an **epistemic action** (Kirsh & Maglio): the compiler, the tests and the runtime compute the consequences of a change faster than the engineer can simulate them, and git undoes the change for free. Acting beats computing.

The activity of software development is complex, because it is modeling: the model emerges from the interaction of the user, the code and now the agent, and sits nowhere before the probe. The probe makes the model's tensions emerge; the belt transmits them as friction ([[philosophy/transmission-belt]]); the engineer's metis reads in them when it is time to change ([[philosophy/metis-kairos]]).

So the work runs as probe-sense-respond (Snowden) because the activity is complex, and the code's nature is what makes the probing cheap. Planning everything ahead is dearer than cutting small steps and going with what each returns: a step-by-step prescription encodes knowledge not yet had, no plan survives contact with the code (Moltke), and its stale letter is then followed instead of what was found.

## The plan orients the learning

Working code is the side effect of learning (Brandolini). A plan does not pre-write the code, which would pretend the learning already happened; it orients it: the goal, the stages as probes in order, room for what each reveals. A stage gives intent, never the way ([[philosophy/batch-slicing]]). Each stage is a synchronization point where the learning is written back before the next probe.

Reshaping stages come before implementing ones, because reshaping is the cheapest probe ([[philosophy/make-the-change-easy]]).

## Forecast and state

The plan carries two contents of opposite nature.

The **forecast**, the stages left: a best guess, rewritten freely, expected to be wrong in detail, and optional. Options stay open to the last responsible moment (Poppendieck): the stages left may never be built, and nothing half-done is thrown away. The map is not the territory (Korzybski): where the territory contradicts the map, the territory wins and the map is redrawn, never the reverse.

The **state**: decisions made, discovered context, blockers, the real next step, which the first unchecked box may not be. Facts, as they really are. A wish belongs in the forecast; smuggled into the state, it corrupts the only facts the next session has.

"The plan is nothing" disposes of the forecast, never the state. As execution proceeds, content migrates from one to the other: each stage consumed turns a guess into a fact. The map keeps the done stages marked, since position is state and position needs the walked route.

## A plan is not a backlog

A plan carries one task, long enough to need splitting: a tree of stages and a map of the route. The list of tasks is another document, the work file ([[philosophy/session-state-in-documents]]).

## Related

- Reshaping as the cheapest probe: [[philosophy/make-the-change-easy]].
- The prototype as the probe before any plan: [[philosophy/prototypes-are-probes]].
- Stages as missions, intent without the way: [[philosophy/batch-slicing]].
- The work file, the backlog a plan is not: [[philosophy/session-state-in-documents]].
- The friction a probe sends up: [[philosophy/transmission-belt]]; what reads it: [[philosophy/metis-kairos]].
- How a stage is walked, the terrain against the map: [[philosophy/map-isnt-territory]].
