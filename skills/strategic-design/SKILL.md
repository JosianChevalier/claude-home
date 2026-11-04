---
name: strategic-design
description: Trigger words: "strategic design", "context map", "bounded contexts", "challenge the design from a DDD perspective", "which subdomains". A session where the user splits a domain into contexts and the agent names them.
---

# Strategic design

## Doctrine

- The user cuts, the agent names. The user sees the problems and how to split them; the agent brings the field's words and the reference practice's, as proposals. A name is decided by the user, never by the agent.
- The map is the turn's deliverable: the whole context map, redrawn with the corrections folded in, names marked as proposals, asked back as "is this your model?". The user corrects the drawing.
- A context is its exposed model; what is inside has no strategic existence until it says something the outside cannot (φfractal-bounded-contexts).
- One seam per turn. A rival reading goes on the table as a second reading and the user decides.
- The map lives in the work file from the first turn; consequential choices become decision records once the model settles; the work file dies when the code carries the map.

## The session

```
 open     the repo's state in one line, then the user's model drawn with proposed names
 turn     one seam: redraw ──▶ hazard ──▶ names ──▶ "is this your model?" ──▶ stop
 land     work file each turn · decision records at the end · handover for the code
```

## Know-how

- Open with what domain code exists, one line. A greenfield map is drawn from the user's words alone.
- Classify by the Core Domain Chart (Tune): the core is where business differentiation is high, and it is usually what the commodity equivalent treats as an afterthought. Supporting and generic stay thin (Khononov's subdomain types).
- Find the lifecycle: the pivotal events (Brandolini) of the main aggregate name the orchestrating context. An orchestrator may own no aggregate: the state lives on the aggregate, the orchestrator issues the transitions and answers "may I?" to the others.
- Steal the reference practice's vocabulary and structure: when a field or a product already does this, search how it names and shapes things before inventing. Search, do not recall. The model is still designed, not found (Verraes, Wirfs-Brock, Design and Reality): name the bet, where this product departs from the reference.
- Modelling on a product: check its marks and patents before cloning, and keep its mark out of the product's name and copy.
- A complicated widget is a value object and some UI until its inner model shows past the value it emits. Rendering a neighbour's widget is not a context relationship.
- Each turn's hazard goes before what it concerns, marked ⚠️: the seam that breaks if a published thing changes, the name that pulls the wrong field, the concept that already exists under another name.

## A turn

> Taken: Assessment is the core, the scorecard widget stays a value object. Redrawn:
>
> ```
> ┌─ Opening ──── Draft ─▶ Posted ─▶ Interviewing ─▶ Filled ────────────────┐
> │ may edit?          may apply?                   may read?               │
> ┌───────────┐     ┌───────────┐     ┌──────────────────────┐
> │ Job       │     │ Applying  │     │ Assessment    CORE   │
> │ Design    │     │ Applicant │     │ Interview → Score[]  │
> └───────────┘     └───────────┘     └──────────────────────┘
> ```
>
> **Names on the table.** `Requisition` is the ATS word for an opening; `Opening` kept since hiring managers say it. `Candidate` in the model, "applicant" in the public copy.
>
> **Hazard ⚠️.** The seam holds only if a posted opening never changes once an application exists.
>
> Is this your model? Step 1 of 3: at posting, lock or snapshot?

Rationale: φfractal-bounded-contexts, φcollaborative-production, φubiquitous-language, φmodel-expressions, φmodel-phenomenology
