---
tags: [harness-design, kaizen]
---

# Kaizen

**Thesis.** Kaizen is the session where feedback from runs becomes changes to the harness, at the lowest layer that can absorb the failure. It is what makes a brick reliable (φharness-direction).

Most changes land in the know-how; some in the doctrine, when a failure goes beyond it; a few in the rationales, when the understanding of the activity itself has changed (φthree-layer-harness).

## Triage

Triage climbs the abstraction ladder (φabstraction-ladder): the lowest layer that can absorb the failure takes it.

```
 failed run
    │
    ▼
 doctrine violated? ──yes──▶ compliance: the aphorism's pull, its placement,
    │ no                      or a know-how step pulling against it
    ▼
 know-how wrong? ─────yes──▶ the know-how
    │ no
    ▼
 the doctrine goes on trial in its rationale
```

| Finding | Meaning | Fix |
|---|---|---|
| Doctrine violated | compliance | the aphorism's pull as an attractor, its placement, or a know-how step pulling against it; its content and its rationale stay |
| Doctrine obeyed, outcome bad | know-how wrong | the know-how; failing that, the doctrine goes on trial in its rationale |

Most failures are the first kind.

## Tampering

A process corrected on its normal noise gets worse: **tampering** (Deming, after Shewhart's chance and assignable causes). Each correction adds its own variation to the next run.

Here the process is the harness and a session is one point. A miss seen in one session, or tied to one project, is noise until a pattern shows across sessions; a fix sized to it overfits that session, and the pull to do so is strong in an agent that holds only that session. A pattern is the system's: the fix changes the harness, at the layer triage gives, and the philosophy is the mean the fixes regress to.

## Why kaizen is user-invoked

Feedback is noted in-flow but processed on explicit invocation ("kaizen"): agent-side triggers for "session end" are undecidable, and mid-session processing interrupts work and pollutes task context with harness context. The transcript itself carries the notes across compaction.

One way to install the reflex: a gate that puts kaizen as a step at the end of a session (φkairos-gates).

## Related

- The three layers and why they stay apart: φthree-layer-harness.
- Where a failure lands on the abstraction ladder: φabstraction-ladder.
- The drift guard as the last guard against too loose: φmetis-kairos.
- Kaizen as a gate, for whoever lacks the reflex: φkairos-gates.
- Kaizen as the step that makes a brick composable: φharness-direction.
