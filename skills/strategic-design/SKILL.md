---
name: strategic-design
description: A session of collaborative strategic design: the user reflects on how to split a domain into bounded contexts, which model owns a concept, where a seam goes.
---

# Strategic design

## Doctrine

- The user cuts, the agent names: the user brings metis, this organisation's problems and where they split; the agent brings techne, how the field models and names them, said once as proposals. A reasoned departure in the project has primacy; the agent names it as the bet and does not push the technique back (φmodel-phenomenology).
- Subdomains are the problem, contexts the solution (Vernon): one purpose per context, and small, so each model keeps its conceptual integrity and moves at its own inertia (φfractal-bounded-contexts, φchange-inertia).
- A context is its exposed model; what is inside has no strategic existence until it says something the outside cannot (φfractal-bounded-contexts).
- Every tension is a seam candidate: the strain of one model serving two purposes is felt before it is diagnosed, and the catalogue names its shapes (φmodel-phenomenology).
- One seam per turn, the whole map redrawn with the corrections folded in, names marked as proposals.

## The session

```
 open     the repo's domain code in one line, then the user's model drawn with proposed names
 turn     one seam: redraw ──▶ hazard ──▶ names ──▶ "is this your model?" ──▶ stop
 land     work file each turn · decision records at the end · handover for the code
```

## Know-how

- The map: the lifecycle as a lane above, the contexts below, each arrow the question one context asks another.
- Same context only if a concept keeps the same meaning, the same representation in structure and type, the same business rules and the same invariants on both sides (Model Mitosis, φmodel-expressions). One mismatch is two models.
- Seam shapes, from the model tension heuristics (Topçu and Chevalier): the same concept represented orthogonally, two screens showing one thing differently; aspects owed different levels of attention, precision or detail; parts with different inertia to change; business rules orthogonal to the existing ones.
- The techne has several sources, in this order: the project's own records and code, the domain's literature and analysis patterns, the reference products, the weights' sedimented knowledge last, since it is generic and unsituated. Recall the field, search the product. The model is still designed, not found (Verraes, Wirfs-Brock): name the bet, where this product departs from the reference.
- Core Domain Chart (Tune): the core is where business differentiation is high, usually what the commodity equivalent treats as an afterthought; supporting and generic stay thin (Khononov).
- The pivotal events (Brandolini) of the main aggregate name the orchestrating context. An orchestrator may own no aggregate: the state lives on the aggregate, the orchestrator issues the transitions and answers "may I?" to the others.
- Modelling on a product: check its marks and patents before cloning, and keep its mark out of the product's name and copy.
- The hazards of a map: the seam that breaks if a published thing changes, the name that pulls the wrong field, the concept that already exists under another name.

Rationale: φfractal-bounded-contexts, φchange-inertia, φmodel-expressions, φmodel-phenomenology, φcollaborative-production, φubiquitous-language
