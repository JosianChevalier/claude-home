---
tags: [harness-design, kaizen]
---

# Rationale: Kaizen

Kaizen is the session where feedback from runs becomes changes to the harness: to the know-how most often, to the doctrine when a failure goes beyond it, to the philosophy when the understanding of the activity itself has changed ([[philosophy/three-layer-harness]]).

## Doctrine

- **Layers 1 and 2 are tied to layer 3.** Every rule and skill points to the philosophy it came from. The reasons are context economics and auditability: changing a rule means understanding precisely what it was trying to accomplish, so everything that went into it must be easy to reach. How the pointer is written is the kaizen skill's business, not this file's.
- **Drift guard.** If a proposed fix contradicts the philosophy behind the rule, either the fix is wrong or the philosophy is outdated. One of the two changes, explicitly. This is the only mechanism keeping layer 3 honest; never bypass it. It is the guard against the harness absorbing what should have reached the engineer ([[philosophy/metis-kairos]]).

## Triage

Triage climbs the ladder ([[philosophy/abstraction-ladder]]): the lowest layer that can absorb the failure takes it. The first question after a failed run:

| Finding | Meaning | Fix |
|---|---|---|
| Doctrine violated | compliance | the saying's pull or its placement; its content and its philosophy stay |
| Doctrine obeyed, outcome bad | know-how wrong | the know-how; failing that, the doctrine goes on trial in its philosophy file |

Most failures are the first kind.

## Why kaizen is user-invoked

Feedback is noted in-flow but processed on explicit invocation ("kaizen"): agent-side triggers for "session end" are undecidable, and mid-session processing interrupts work and pollutes task context with harness context. The transcript itself carries the notes across compaction.
