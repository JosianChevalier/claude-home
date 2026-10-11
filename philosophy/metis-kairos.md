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

Observation comes back up the belt. Not all of it should. Variety is absorbed at the lowest level that can hold it (a subsidiarity reading of Beer's recursion, after Ashby's law): the variety a level can take as business as usual stays there. What escalates is the variety that breaks expectation, so that feedback shows up in the layer that can act on it.

Two reasons hold the rule up, and the ladder splits them.

Capacity (Beer): the level above has fewer states and a narrower channel, so what it receives must be what it alone can decide. It dominates on the rungs where the engineer sits.

Near-decomposability (Simon): parts coupled weakly, each strong inside; in software, layers of abstraction and loose coupling. Varieties multiply (Ashby), so a whole made of parts that each absorb their own variety faces only the product of what leaks out. It dominates on the rungs below, where it is context economics ([[philosophy/context-economics]]).

Escalation has the semantics of an exception. Each level detects, then decides: absorb, or bubble up. Bubbling adds the level's own context and leaves the cause as it came; a level translates the cause only for the failure types it is declared to handle. Any level can install a handler. A fault no level catches reaches the engineer uncaught, with the chain of levels it crossed.

That arrival is the *kairos*: the opportune moment, as against *chronos*, mere duration. *Metis* seizes it: the engineer's situated, practical sense, felt in the situation and not transmitted (Scott, after Detienne and Vernant), reads the error as the opportunity to destroy their own world and make the improvement.

The belt feeling its own strain belongs here too: "I am doing many things at once" is a signal to send up, so the engineer can decide whether the strain is the task's or the model's.

## The gradient

Between absorbing everything and escalating everything lies a gradient, and the harness sets where each level sits on it. Power steering is the image: the assistance removes the effort of turning and the whole design problem is to keep the road felt.

Its two ends are the belt's two failures ([[philosophy/transmission-belt]]): too tight, everything escalates, noise drowns signal and cognition overloads; too loose, nothing escalates, the engineer's Observe starves and the philosophy goes stale.

Kaizen's drift guard ([[philosophy/kaizen]]) is the last guard against too loose: a fix that contradicts the philosophy is a disappointment that reached the top, and one of the two changes, explicitly.

The abstraction ladder ([[philosophy/abstraction-ladder]]) is the discrete form of the gradient: a stack of levels, each absorbing what it can and passing the rest one rung up.

## Related

- Where the loop runs and why it must return: [[philosophy/transmission-belt]].
- Steps added on top of the loop to make the moment systematic: [[philosophy/kairos-gates]].
- The discrete form of the gradient: [[philosophy/abstraction-ladder]].
- The last guard against too loose: [[philosophy/kaizen]].
- The rungs below, where decomposability rules: [[philosophy/context-economics]].
