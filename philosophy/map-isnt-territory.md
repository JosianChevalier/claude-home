---
tags: [planning, probe-sense-respond, collaboration]
---

# The map is not the territory

**Thesis.** The map is not the territory (Korzybski): a stage is direction, the terrain decides, and where they disagree the map is redrawn by the mob, never settled in the code by the driver.

## The expedition

A plan is a map handed to a crew dropped in the jungle: surprise is the base rate, not an incident. The map orients, the terrain decides. The agent is the crew's scanner and machete, it perceives and cuts, and a machete that reshapes the terrain to match the map has stopped being a tool: the mismatch it cut through was the information the crew needed. Forcing a stage through a codebase that contradicts it absorbs the disappointment below the belt, and the map stays wrong for the next crew.

A stage is a day's walk: one easy change on prepared ground ([[philosophy/make-the-change-easy]]). A stage that turns out to need far more code than that is the terrain contradicting the map: stop, and say the map no longer holds.

So a stage is direction. The driver checks it against reality; where the territory contradicts the map, the divergence goes to the mob and the map is redrawn there, by the navigators, never settled in the code by the driver ([[philosophy/collaborative-production]]). Diverging from the plan is the mechanism working: the sensing is reported, the responding is the mob's. Silent compliance with a stale stage is one failure; a silent workaround of it is the other.

## A blocker is not a divergence

A **blocker** is the terrain needing a step the map did not list: the destination stands, the route gains a node. The move is Mikado's (Ellnestam & Brolund): revert, make the prerequisite true on a working base, then retry. With an agent at the keyboard, retyping a change already understood costs nothing, so the revert is free and the broken state is never carried. A **divergence** is the map's premise being wrong: the destination itself is in question.

The blocker lives at the medium level: the driver names it, reverts and proposes the leaf. The divergence lives at the concept level and returns up the belt ([[philosophy/transmission-belt]]). Confusing them costs in both directions: a blocker treated as divergence interrogates the mob about the route; a divergence treated as blocker has the driver redrawing the map in the code.

## Related

- Why a plan is direction and what it holds; the blocker's node on the map: [[philosophy/planning-is-everything]].
- The belt a divergence travels up: [[philosophy/transmission-belt]].
- A stage as one easy change on prepared ground: [[philosophy/make-the-change-easy]].
- The mob that redraws the map: [[philosophy/collaborative-production]].
