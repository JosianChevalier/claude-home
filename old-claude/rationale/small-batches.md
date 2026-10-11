---
tags: [small-batches, planning, continuous-delivery]
---

# Rationale: Stages Are Small Batches

Governing frame: Reinertsen's *Principles of Product Development Flow* — product development is an economics problem, and the dominant variable is **batch size**. A plan stage is a batch. Its size and shape determine feedback speed, inventory, and risk.

## Work in process is inventory

Code that is written but not shipped is **design-in-process inventory** (Reinertsen's DIP): it holds cost without returning value or information. Unlike factory inventory it is invisible — nothing on a shelf — which is why it silently accumulates. Every stage that completes without producing a working, deployed increment adds to this inventory. Inventory depreciates: a priority shift, a design pivot, or a discovery in a later stage can write it off entirely. The only way to zero the write-off risk is to ship each batch as it completes.

## Small batches buy feedback and options

- **Fast feedback**: a deployed stage returns real information (does it work? does it hold in production? was the design right?). Feedback deferred is defects and wrong assumptions compounding at zero interest to us and full interest against us.
- **Cost of delay**: value delivered at stage 2 of 6 starts earning immediately — economically, capturing value early beats capturing it all at the end, and delay has a quantifiable cost even when nothing "goes wrong".
- **Option value**: remaining stages are options, not obligations. If priorities change after stage 3, stages 4-6 are simply not exercised — nothing is dumped, because nothing half-done exists. This is why the forecast is disposable while the state is precious.
- **Bounded risk**: each batch is a small, independently revertible bet. Big batches concentrate integration risk at the end — the big-bang integration where everything is discovered to not fit, at the moment it is most expensive to fix.

## Two granularities, two loops

Batches nest in three cadences, each with its own invariant:

| Cadence | Unit | Invariant | Owner |
|---|---|---|---|
| **Functional** (~days) | User-visible increment | Returns *value and information* | Plan |
| **Technical** (~hours) | Sub-stage on the way to a functional batch | App *works, zero regression* | Plan |
| **Atomic commit** (~minutes) | One logical change | Tested, deployable | Implementer — below the plan |

The technical cadence nests recursively — a sub-stage that still spans layers splits again (`1.2.1`) under the same invariant. Only the functional cadence banks value; the atomic commit stays the floor, below the plan.

The **functional loop** is the one all the economics above apply to: it is the smallest unit that returns value and validates assumptions, so it must be cut as small as possible. The **technical loop** returns no user value — only the weaker (but non-negotiable) feedback that nothing broke. It exists because reality is layered: an improvement may touch 17 layers, and forcing all 17 into one batch just recreates the big batch at a lower level. Cutting it into technical sub-stages keeps each step green, revertible, and deployed — inventory measured in hours, not days.

The nesting is the batch-size discipline applied recursively: never let the pursuit of a functional slice inflate any single step beyond what stays continuously working.

## Layers are not *functional* increments

A plan sliced as "1. change database, 2. change domain, 3. wire x and y" is broken not because it touches layers one at a time, but because it presents layer-work as the **only** structure — there is no functional batch these steps serve, so feedback, value, and de-risking all arrive at the very end: maximal inventory, maximal cost of delay, big-bang integration. Layer-touching steps are legitimate only as *technical sub-stages inside* a functional slice, each keeping the app working. The functional axis owns the plan; the technical axis serves it.

## The valid two-beat cut

Within a functional slice, the principled split is the workflow rhythm: **make the change easy** (reshaping — pure refactoring, behavior preserved, hence shippable by construction), then **make the easy change** (the behavior increment on prepared ground). Both beats are technical batches, independently deployable. This is small batches applied to preparation itself: the reshaping ships and returns feedback before the feature bet is placed. Full treatment of the rhythm and its fractal scales: @rationale/workflow-rhythm.md

## Consequence for plans

Every stage — functional or technical — must end in a state that **works and is deployed**; continuous deployment makes this literal: every commit lands in production, so a stage that "can't ship yet" blocks the pipeline. Functional stage boundaries additionally bank value and information, closing the loop the plan exists to serve. Atomic commits stay out of the plan entirely: they are the implementer's cadence, governed by the atomic-commit skill.