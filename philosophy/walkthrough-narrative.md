---
tags: [communication, cognitive-load, code-review, session-design]
---

# Narrative walkthrough

**Thesis.** Anything with several parts handed to a human, a change, a plan, a session, a corpus, is walked, not dumped: a map first, then one beat at a time along a route from the centre of impact outward, each beat carrying all the context it needs and its neighbours, the count as the you-are-here.

The screen is a strategy game's: the map in the corner, the camera on one point showing the status there, and the player moving it.

## The unit is the concept

The artifact comes in its own order: a diff by filesystem, a plan by stage, a transcript by time. Told in that order the walk has no narrative, every stop is addressed by location, and each turn fills a form. Three symptoms, one cause: the unit was the artifact's piece, not a concept. A beat is a concept; the pieces it anchors to are locators, kept out of the telling.

## From the centre of impact outward

Narratology separates the fabula, the events in causal order, from the syuzhet, the order of telling (Genette). The artifact's order is a syuzhet chosen by nobody. The walk builds the fabula of the domain, the centre of impact and what it forced, ripple by ripple, and tells it close to that order: verdict first, no anachrony, nothing withheld. The telling is a pyramid (Minto): the governing thought at the top, the centre of impact, and under it the ripples that support it, each a group of its own; the reader stops at the level that answers them. The nearest genre is the air-crash investigation: outcome stated up front, causal chain walked in order, one component and one exhibit per step.

The map is built whole before the first word is told, silently, in a file. A telling that starts from the artifact takes the artifact's structure: patchwriting (Howard), the bias the map offsets.

## Concept first, then the thing

Concept first, then the thing (φconversation-as-interface): the walk is the advance organizer; the pass over the artifact afterwards is recognition. Hence the success test: the artifact opened during the walk means the walk failed, and the pass afterwards only verifies coverage.

The same order holds inside a beat: context before the thing. Exception: when the question is whether the thing speaks for itself, context first would bias the judgement.

## A map and a camera

The whole is a graph: beats as nodes, edges for cause, flow, friction; which kinds exist, the material decides. What breaks in an ASCII map is the global layout, and a graph needs none: each beat shows its ego network, the node and its direct neighbours, a short list constant in size however wide the whole. The full map is the survey view, on demand, clustered as a map is generalized at small scale (φzoom-levels).

The walk is active navigation of a stable map (φembodied-navigation): the player moves the camera to the next beat on the route, to a neighbour, back, up to the map; route knowledge from the beats walked, survey knowledge from the map, and the picture grows from moving between the two. A map one is walked through is a guided tour.

Link-only navigation has its own failure, lost in hyperspace (Conklin): a zettelkasten has no spine by design, and a walk needs one. The default route and the count are the spine: after a detour, the count says what is unvisited and the route resumes.

## A beat is complete, and fast

A beat holds everything needed to understand it on the spot: what the thing cannot say, the cause, the domain reason, what was there before; the thing itself, verbatim, elided to the smallest recognizer; its neighbours. Nothing has to be opened, nothing is derived twice, and it is read in one look, so the camera moves on.

## ⚠ against fluency

A smooth walk builds familiarity, and familiarity lowers scrutiny: the fluency heuristic. Every other beat asks the reader to understand; ⚠ asks them to judge. It is an overlay on any beat, not a kind of beat, because doubt is orthogonal to what the beat asks; it always states its reason, and it always renders (φzoom-levels). For the same reason the thing is shown verbatim: a tidied exhibit makes the pass afterwards recognise a fiction.

## What fits no beat

A narrator optimises for coherence: what does not fit the story gets dropped or forced in, and that is the part most worth looking at. So every piece of the artifact belongs to exactly one beat, and what fits none opens the walk. Two causes, indistinguishable from inside: the artifact is not one thing (a change that was not one batch, φbatch-slicing), or the narrator's story is incomplete. Separable: split it. Not explainable: it is not understood; roll it back. The narrator interprets and recommends; the reader decides.

## The map lives in a file

The map, the route, the pieces placed and the beats visited are session state, derived and disposable (φsession-state-in-documents); rebuilt from context each turn, they drift. The file also holds the locators, which keeps them out of the telling until asked for.

## Instances

- A change reviewed: hunks placed on beats, the centre and its ripples, the act asked of the reviewer on each.
- A session: decisions as beats, the map drawn at the open, step X of Y at each.
- A retrospective: misses grouped by shared cause, numbered, one round per turn.
- The work's next item: a breadcrumb from the project down to the item.
- A corpus: walks that carry one question through the files.

## Related

- φembodied-navigation: stable map, active navigation; route and survey knowledge.
- φconversation-as-interface: concept before thing; one beat per turn.
- φzoom-levels: hazards always render; the clustered map at small scale.
- φsession-state-in-documents: the map file as derived, disposable state.
- φbatch-slicing: a change that fits no story was not one batch.
