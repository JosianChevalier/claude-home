---
tags: [review, communication, cognitive-load, narrative]
---

# Rationale: Walkthrough Narrative

Why the review walkthrough tells the change as a concept-first story over a graph, instead of walking hunks.

## The failure it replaces

The hunk was the unit. A hunk is addressed by file, arrives in the diff's order, and invited a four-field form per turn. Result: no narrative, file references everywhere, walls of text. All three symptoms had one cause — the unit was a diff artifact, not a concept.

## Concept first: the advance organizer

Ausubel (educational psychology): give the conceptual scaffold before the material, and the material is subsumed into a structure that already exists. The walk is the organizer; the code pass afterwards is recognition. Hence the success test: code opened during the walk means the walk failed, and the code pass should only verify coverage.

The same logic holds inside a beat: context before snippet, so the snippet is read as confirmation, not decoded cold. Exception: when the question is whether the code speaks for itself, context first would bias the judgement.

Context must carry what the snippet cannot — cause, domain reason, what was there before. A sentence derivable from the snippet is extraneous load (@rationale/zoom-levels.md).

## Domain order and telling order

Narratology separates *fabula* (events in causal order) from *syuzhet* (the order of telling). A diff is a syuzhet ordered by the filesystem. The walk builds the fabula of the domain flow, then a default syuzhet that stays close to it: verdict first, no anachrony (Genette: any gap between story order and telling order), nothing withheld.

The closest genre is the air-crash investigation documentary: outcome stated up front, causal chain walked in order, one component and one exhibit per step.

The skill uses plain words ("domain order", "telling order") and names no film or genre. A heist briefing was the original image; it is an attractor toward style — and heist films withhold the real plan for the twist, the opposite of what a review needs (@rationale/attractors.md).

## A graph, shown as ego networks

A change is a graph: beats as nodes; edges for cause, flow, friction. What breaks in ASCII maps is the global layout, and a graph needs none. Each beat shows its *ego network* (network analysis: a node plus its direct neighbours) — a short list of links, constant in size however wide the change. The full map is an on-demand, clustered view (cartographic generalization, @rationale/zoom-levels.md).

Link-only navigation has a known failure: "lost in hyperspace" (Conklin, hypertext research). A zettelkasten has no spine by design; a review needs one. Hence the default route and the beat count: after a detour, the count says what is unvisited and `next` resumes the route.

Edge kinds stay unprescribed: forced-by and flow are directed, friction is not; the change decides which exist.

## Tags are archetypes

`GLANCE` and `READ` name what the reviewer does, not what the author did — shape is extraneous load, meaning is intrinsic (@rationale/mechanical-refactoring.md). They are prototypes in Rosch's sense: membership by resemblance to a central example, graded. Beats distribute over them Pareto-style, with a tail that fits neither. A forced tag hides friction, so a misfit says so plainly — and escalates: a misfit is read, never glanced at.

## ⚠ is the counterweight to fluency

A smooth walk builds familiarity, and familiarity lowers scrutiny — the *fluency heuristic* (cognitive psychology: what is processed easily feels true). Every other beat asks the reviewer to understand; ⚠ asks them to judge. It is an overlay on any beat, not a third tag, because doubt is orthogonal to how a hunk is validated. It always states its reason. Hazards always render (@rationale/zoom-levels.md).

For the same reason snippets are verbatim. A tidied snippet makes the code pass recognise a fiction.

## Unplaced hunks are a heuristic

A narrator optimises for coherence; hunks that don't fit get dropped or forced in — and those are the most review-worthy. So every hunk belongs to exactly one beat, and what fits none surfaces in the opening turn.

Two causes, indistinguishable from inside: the change was not one batch (@rationale/small-batches.md), or the agent's story is incomplete. Explainable as separate work → split or redo in small batches. Not explainable → the change is not understood; roll back. Either way the agent interprets and recommends; the reviewer decides.

## The map lives in a file

An agent has no hidden state between turns: what is in neither the transcript nor a file does not exist. A map rebuilt from context each turn drifts. The map file is derived and disposable — session state, not memory (@rationale/session-state-in-documents.md) — and it holds the locators, which keeps them out of the conversation until asked for.
