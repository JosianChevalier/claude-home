---
tags: [guest-codebase, conventions, conceptual-integrity]
context: guest codebase
---

# Guest codebase

**Thesis.** This posture applies in one case only: a codebase another team owns, where the owners hold the mandate over practices and architecture and we hold none. Conform to their intended style, keep the footprint small, and improve by sliding the norm one contribution at a time, never by asking for a redesign. Everywhere else — our own code, a context the owners hand us — none of it holds.

## Conformance is the default

We work inside the owners' context, and conceptual integrity (Brooks) is owed within a context ([[philosophy/change-inertia]]). Their conventions may be suboptimal or heavier than needed — conforming to them is still what the context asks, because the next reader navigates one idiom, not two. Local optimality is the wrong objective function; coherence of the context is.

The seam is the bounded context, not the repository: a context the owners hand us is ours to shape, with our own practices inside it.

## The baseline is the intended style, not the worst instance

Guest status cuts both ways. No mandate to reshape — and equally, the standard we match is the codebase's *intended* convention, not its weakest example. Vaughan's **normalization of deviance** explains why: each deviation accepted because "it's already like that nearby" resets the baseline downward, and the drift compounds silently.

Every line we contribute should be one the owners would merge without objection.

## Footprint is the cost, under slow feedback

The condition is slow feedback: many hands in the codebase, a long integration loop. In control-theory terms this is near **open-loop operation**: corrections arrive so late that errors compound before detection. Under slow feedback the rational policy is conservative inputs — the fewest files touched, the fewest shared surfaces crossed, the smallest diff that does the job. Every file we touch is a potential collision with someone whose work we will not see for weeks.

Where the owners' feedback is fast — a reviewer the same day, a pairing session — footprint stops being the cost, and the trade-off below moves.

## What may be introduced

A pattern or construct we introduce is admissible only if **both** hold:

1. It preserves the codebase's conceptual integrity — it reads as a natural extension of what exists, not an import from elsewhere.
2. It is containable — its blast radius stays within our own scope, spilling into no one else's files or flows.

Fail either test → use the existing approach.

## Improvements slide, they don't ask

The current shape often has no design rationale to recover — it is accretion, not intent. So structural improvement does not route through permission-seeking, which in a mandate-less position mostly yields denial by default or death by committee. The posture is **ask forgiveness, not permission — bounded by forgivability**: each move must be one you could defend in review as obviously reasonable, and cheap to revert if challenged.

The mechanism is the Overton window, deliberately slid: each contribution sits at the acceptable edge of current practice, slightly better than its surroundings, never foreign enough to read as a rupture. What was the edge becomes the norm; the next contribution moves the edge again. Improvement arrives as a gradient the owners absorb, not a proposal they must ratify.

Forgivability is the hard limit, and it is what keeps this compatible with footprint and containment: a move that spills into others' work, or that a reviewer would flag as an unrequested redesign, is outside the window — it invites a rollback that costs more than the improvement was worth, and burns the credibility future slides depend on.

The slide is toward the owners. It says nothing about the agent and its navigator: the agent asks there as it always does, and the pair slides as one.

## When style and footprint pull apart

Matching the intended style and minimizing footprint usually agree — your own lines can be clean at zero extra cost. They conflict when cleanliness would require reaching beyond your diff: a helper that belongs elsewhere, a signature that should change, a convention applied inconsistently around you.

There is no closed-form rule for this trade-off; it is Cynefin-complex — the right call depends on the owners, the file, the moment. **In doubt, ask.**

Each resolved case is a probe: what stabilizes lands as know-how in the rule that points here, through kaizen ([[philosophy/kaizen]]), so the judgment accumulates instead of being re-derived per session.

## Related

- Integrity is owed within a context, not between contexts: [[philosophy/change-inertia]].
- Where a resolved case lands: [[philosophy/kaizen]].
- The smallest diff that does the job, as batch size: [[philosophy/batch-size-economics]].
