---
tags: [harness-design, kaizen]
---

# Kaizen

**Thesis.** Kaizen is the session where feedback from runs becomes changes to the harness, at the lowest layer that can absorb the failure. It is what makes a brick reliable ([[philosophy/harness-direction]]).

Most changes land in the know-how; some in the doctrine, when a failure goes beyond it; a few in the rationales, when the understanding of the activity itself has changed ([[philosophy/three-layer-harness]]).

## Doctrine

- **Rules and skills are tied to their rationales.** A harness element has a rationale, usually a philosophy file. Every rule and skill points to its rationale, so that changing a rule starts from what it was trying to accomplish: context economics and auditability. How the pointer is written is the harness-improvement skill's business, not this file's.
- **Drift guard.** If a proposed fix contradicts the rationale behind the rule, either the fix is wrong or the rationale is outdated. One of the two changes, explicitly. This is the only mechanism keeping the rationales honest; never bypass it. It is the guard against the harness absorbing what should have reached the engineer ([[philosophy/metis-kairos]]).

## Triage

Triage climbs the ladder ([[philosophy/abstraction-ladder]]): the lowest layer that can absorb the failure takes it.

```
 failed run
    │
    ▼
 doctrine violated? ──yes──▶ compliance: the saying's pull as an attractor, or its placement
    │ no
    ▼
 know-how wrong? ─────yes──▶ the know-how
    │ no
    ▼
 the doctrine goes on trial in its rationale
```

| Finding | Meaning | Fix |
|---|---|---|
| Doctrine violated | compliance | the saying's pull as an attractor, or its placement; its content and its rationale stay |
| Doctrine obeyed, outcome bad | know-how wrong | the know-how; failing that, the doctrine goes on trial in its rationale |

Most failures are the first kind.

## Why kaizen is user-invoked

Feedback is noted in-flow but processed on explicit invocation ("kaizen"): agent-side triggers for "session end" are undecidable, and mid-session processing interrupts work and pollutes task context with harness context. The transcript itself carries the notes across compaction.

One way to install the reflex: a gate that puts kaizen as a step at the end of a session ([[philosophy/kairos-gates]]).

## Related

- The three layers and why they stay apart: [[philosophy/three-layer-harness]].
- Where a failure lands on the ladder: [[philosophy/abstraction-ladder]].
- The drift guard as the last guard against too loose: [[philosophy/metis-kairos]].
- Kaizen as a gate, for whoever lacks the reflex: [[philosophy/kairos-gates]].
- Kaizen as the step that makes a brick composable: [[philosophy/harness-direction]].
