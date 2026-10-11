---
name: review-walkthrough
description: Trigger: review, walkthrough, what moved, what should I compare. NOT exhaustive review or study.
---

# Review Walkthrough

Author explains, reviewer judges. The walk gives the concepts first, so the code pass afterwards is recognition: every hunk already known — what, why, how. A reviewer who has to open the code during the walk means the walk failed.

## Build the map (silent)

1. **Concept.** From the target (plan stage; the diff when there is none), lay the change out as a graph of beats in domain order: the flow the change lives in, the core that realizes the north star, the ripples it forced, the frictions. Edges carry their kind — forced by, flows to, friction with — named as the change needs. A beat may be purely conceptual when understanding requires it.
2. **Anchor.** Bind beats to code where code exists. Every hunk belongs to exactly one beat; moves safe by construction group into one closing beat.
3. **Route.** A default telling order: verdict first, then domain order, everything known said when it becomes relevant.
4. **Persist.** Map, route, hunk ledger, visited beats → `/tmp/walkthrough-<branch>.md`. Re-read it each turn; it is the walk's state. Shown on request.

Hunks that fit no beat: the change was not one batch, or the story is incomplete. Interpret, recommend (split, roll back), surface in the opening turn. The reviewer decides.

No domain flow (cross-cutting change): the graph is the core and what it forced.

## Opening turn

- Verdict and north star.
- ⚠ whole-change doubts: unplaced hunks, several concerns in one change.
- The map at a scale that fits a few lines; cluster when wide; a clustered list when the topology is large.
- Beat count, first stop. Stop.

## Each turn: one beat

    Beat 3 of 6 · Discount

    READ: behaviour changes as asked

    Finance needs the discount to shrink the taxable base.

    ⚠ Rounding now happens twice; totals may differ by a cent.

    <snippet>

      ← forced by   Pricing (core)
      → forces      1. Invoice total   2. Tax report
      ~ friction    3. Rounding policy

    next: Invoice total

- **Tag** — what the reviewer does. `GLANCE`: safe by construction (rename, extract, inline, move to file); confirm the shape — every occurrence changed, nothing else moved; anchors Old → New, a set moved together is one anchor. `READ`: behaviour changes as the target asked. These are archetypes: a beat that fits neither says so plainly and is read. A move that needs meaning to validate is `READ`.
- **Context** — one piece of information the snippet cannot carry: cause, domain reason, what was there before.
- **⚠ + plain reason**, on any beat, wherever there is doubt: behaviour may differ beyond what the target asked, or you are unsure.
- **Snippet** — verbatim, elided with `…`, the smallest recognizer. Context comes before it; reverse only when the question is whether the code speaks for itself, and say so.
- **Links** — the beat's direct neighbours by edge kind, numbered.
- Beats are addressed by concept; locators live in the map file, given on request.
- Blank line between parts.

Stop after each beat. The reviewer says `next` (route), a number (follow a link), `back`, `map`, or asks. After a detour, `next` resumes at the first unvisited beat on the route.

Reviewer corrects a domain assumption → update the map file at once, drop stale doubts.

All beats visited → say so; offer the ledger for the code pass.

Rationale: @rationale/walkthrough-narrative.md, @rationale/mechanical-refactoring.md, @rationale/transmission-belt.md, @rationale/kairos-gates.md, @rationale/zoom-levels.md
