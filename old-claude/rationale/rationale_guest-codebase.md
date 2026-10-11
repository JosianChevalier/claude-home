---
tags: [guest-codebase, conventions, conceptual-integrity]
---

# Rationale: Guest Posture in a Foreign Codebase

We work in codebases owned by other teams. The owners hold the mandate
over practices and architecture; we hold none. This asymmetry defines
everything below.

## Conformance is the default

Brooks (conceptual integrity, *The Mythical Man-Month*): a system that
reflects one coherent set of design ideas is worth more than one made
of locally superior but inconsistent parts. The owners' conventions may
be suboptimal or heavier than needed — conforming to them still
produces a better *system* than injecting a foreign style, because the
next reader navigates one idiom, not two. Local optimality is the wrong
objective function; coherence of the whole is.

## The baseline is the intended style, not the worst instance

Guest status cuts both ways. No mandate to reshape — and equally, the
standard we match is the codebase's *intended* convention, not its
weakest example. Vaughan's **normalization of deviance** explains why:
each deviation accepted because "it's already like that nearby" resets
the baseline downward, and the drift compounds silently. Every line we
contribute should be one the owners would merge without objection.

## Footprint is the cost function

Many developers share this codebase, and the integration feedback loop
is very long. In control-theory terms this is near **open-loop
operation**: corrections arrive so late that errors compound before
detection. Under slow feedback, the rational policy is conservative
inputs — the fewest files touched, the fewest shared surfaces crossed,
the smallest diff that does the job. Every file we touch is a potential
collision with someone whose work we will not see for weeks.

## Admissibility heuristic for anything new

A pattern or construct we introduce is admissible only if **both**
hold:

1. It preserves the codebase's conceptual integrity — it reads as a
   natural extension of what exists, not an import from elsewhere.
2. It is containable — its blast radius stays within our own scope,
   spilling into no one else's files or flows.

Fail either test → use the existing approach.

## Improvements slide, they don't ask

The current shape often has no design rationale to recover — it is
accretion, not intent. So structural improvement does not route through
permission-seeking, which in a mandate-less position mostly yields
denial by default or death by committee. The posture is **ask
forgiveness, not permission — bounded by forgivability**: each move
must be one you could defend in review as obviously reasonable, and
cheap to revert if challenged.

The mechanism is the Overton window, deliberately slid: each
contribution sits at the acceptable edge of current practice, slightly
better than its surroundings, never foreign enough to read as a
rupture. What was the edge becomes the norm; the next contribution
moves the edge again. Improvement arrives as a gradient the owners
absorb, not a proposal they must ratify.

Forgivability is the hard limit, and it is what keeps this compatible
with footprint and containment: a move that spills into others' work,
or that a reviewer would flag as an unrequested redesign, is outside
the window — it invites a rollback that costs more than the
improvement was worth, and burns the credibility future slides depend
on.

## When the two forces pull apart

Matching the intended style and minimizing footprint usually agree —
your own lines can be clean at zero extra cost. They conflict when
cleanliness would require reaching beyond your diff (a helper that
belongs elsewhere, a signature that should change, a convention applied
inconsistently around you).

There is no closed-form rule for this trade-off; it is Cynefin-complex
— the right call depends on the owners, the file, the moment.
**In doubt, ask.** Each resolved case is a probe: document the emerging
heuristic here as it stabilizes, so the judgment accumulates instead of
being re-derived per session.

### Emerged heuristics

(none yet — append as cases are resolved)
