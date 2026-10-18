---
tags: [harness-design, collaboration, variety-absorption, kaizen]
---

# Metis and kairos

**Thesis.** Each level absorbs the variety it can hold; what none can hold reaches the engineer, and that arrival is the moment to improve.

The engineer's loop, observe, orient, decide, act, runs on the transmission belt ([[philosophy/transmission-belt]]). The harness does not run this loop. It enables it, at every level of the work: writing the model, running a session, improving the harness itself. This document says what reaches the engineer, and what seizes it.

```
engineer   ◀── uncaught: kairos, metis seizes it
   ▲
session    detects, then absorbs or bubbles up; adds context, keeps the cause
   ▲
workflow   same
   ▲
leaf       variety arrives here first
```

## What comes up

Read the abstraction ladder first ([[philosophy/abstraction-ladder]]): variety absorbed at the lowest rung that can hold it, the rest escalated one rung with the semantics of an exception. This file is the top rung.

Observation comes back up the belt. Not all of it should: what escalates is the variety that breaks expectation, so that feedback shows up in the level that can act on it. A fault no level catches reaches the engineer uncaught, with the chain of levels it crossed.

That arrival is the engineer's Observe, and what it opens is the *kairos*: the opportune moment. *Metis* seizes it: the engineer's situated, practical sense, felt in the situation and not transmitted (Scott, after Detienne and Vernant), reads the error as the opportunity to destroy their own world and make the improvement.

The belt feeling its own strain belongs here too: "I am doing many things at once" is a signal to send up, so the engineer can decide whether the strain is the task's or the model's.

## Designing for uncertainty

Designing for uncertainty (after Snowden): no level predicts what will go wrong; it guarantees that whatever goes beyond what was expected of it surfaces. Each flow declares its business as usual ([[philosophy/abstraction-ladder]]). Anything else, whatever it is, lands in an error status: detected fast, flagged, set aside for the engineer. The agent's part is to recognise that something went beyond what was expected of it, instead of improvising past it. In code, that recognition is felt as model tension ([[philosophy/model-phenomenology]]).

An agent runs a plan step: "extract the discount rule into its own function". It finds the rule computed two ways, one for display and one for billing. Business as usual covers the extraction, not a choice between two readings of "discount". The agent stops, flags what it found, and the step lands in the error status; the engineer, later, reads a model tension and decides.

The error status pulls up every disappointment, unranked. Which one to redesign first is the engineer's choice, made later, and not the belt's concern. A disappointment is redesigned once it is understood; one too small to understand yet waits for a better idea.

Power steering is the image of the belt: the assistance removes the effort of turning and the whole design problem is to keep the road felt. Its two failures ([[philosophy/transmission-belt]]) are misclassifications, not settings:

- **Too tight.** What the level could handle as business as usual climbs anyway: noise drowns signal and cognition overloads.
- **Too loose.** What went beyond expected is absorbed silently, improvised past: the engineer's Observe starves and the philosophy goes stale.

Kaizen's drift guard ([[philosophy/kaizen]]) is the last guard against too loose: a fix that contradicts the philosophy is a disappointment that reached the top, and one of the two changes, explicitly.


## Related

- Where the loop runs and why it must return: [[philosophy/transmission-belt]].
- Steps added on top of the loop to make the moment systematic: [[philosophy/kairos-gates]].
- The pattern this file is the top rung of: [[philosophy/abstraction-ladder]].
- The last guard against too loose: [[philosophy/kaizen]].
- The abstraction ladder's lower rungs, where decomposability rules: [[philosophy/context-economics]].
