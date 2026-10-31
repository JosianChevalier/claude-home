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


## Mission command

The field that already holds this file is **mission command** (Auftragstaktik; US Army ADP 6-0): commander's intent, disciplined initiative, report by exception. The echelon above hands down the task, the intent behind it, and its **CCIR**, the critical information requirements, what it wants to hear at once. Below, each echelon absorbs what is its job and never asks about the door; what would surprise the echelon above is reported before acting. The test at each move: could this surprise the echelon above? Measured against the brief: what the brief already settled is never a surprise.

Mapped onto this file: the intent is the business as usual a flow declares; the CCIR name what lands in the error status; the **back-brief**, the task restated in the subordinate's own words before moving, is the calibration gate ([[philosophy/kairos-gates]]), where a doubt about the premise goes. The echelon above is a human in a session, an agent or a script lower down; the same words serve each rung ([[philosophy/abstraction-ladder]]).

When a task declares no CCIR, four stand by default, the places a small change hides a large reach:

- scope: the step grew past one small change ([[philosophy/map-isnt-territory]])
- structural: the step changes the rest of the plan or flow
- security: the class of consequence changes, as civilians change the rules of engagement
- domain: the shape at the level being validated, its conceptual integrity (Brooks); the lower levels are the subordinate's, unless they get awkward

## Related
