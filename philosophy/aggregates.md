---
tags: [ddd, domain-modeling, aggregates, consistency, invariants, tactical-ddd]
---

# Aggregates

**Thesis.** The aggregate is the cluster that must hold together at every moment domain code can see it. Its boundary is derived from the safety properties, never drawn; it holds those properties itself, by structure first, and is saved whole.

The aggregate (Evans) is a **consistency boundary**: the cluster of objects whose invariants must hold together at every save. It is not an object-graph convenience, a table grouping, or a transaction scope. Those are other media's boundaries, and borrowing one is contamination ([[philosophy/model-expressions]]) transposed to the tactical axis: a grammar's own constraint masquerading as a domain decision.

## Invariants first

The boundary is derived, never drawn. List the properties that must never be violated, in domain vocabulary: no table, transaction, or framework words. The engineer who models states them, from their understanding of the business, built with the domain experts.

The aggregate is whatever those properties force together. Anything not forced stays out, which is why well-derived aggregates come out small.

## Safety versus liveness (Lamport)

- **Safety**: "nothing bad ever happens." Violated by a state you can point at ("this order's total disagrees with its lines").
- **Liveness**: "something good eventually happens." No finite state violates it; only never arriving does ("every placed order is eventually invoiced").

Only safety is a coherency constraint. A safety property must hold at every observable point, so everything it mentions must be saved together: that is what forces the boundary. Liveness forces no co-saving; it may span aggregates and go eventual.

Vernon's rule, full consistency inside the aggregate and eventual consistency between aggregates, is the operational face of this classification. The guard runs backwards too: demanding immediate consistency across two aggregates means the boundary is wrong, or a liveness property is being treated as safety.

## Always valid

The aggregate is domain model, so it is always valid: its invariants hold at every moment domain code can see it, by structure first ([[philosophy/always-valid-domain]]). Nothing below the aggregate enforces anything.

It is saved whole, in one call to a repository. The repository is one more consumer: what it saves is valid because what it was handed was. How the save is made atomic is a modality of saving, the repository's business, and the model has no need to know it. Writes split across several saves leak the transaction into the domain code: the boundary was drawn wrong, back to the invariants.

## Example: one invariant each way

- *"An order's total equals the sum of its lines."* Safety; forces order and lines into one aggregate; held by structure, the total computed, never stored.
- *"A shipped order has a shipping date; an unshipped one has none."* Safety; held by structure, one type per state, the nullable `shippedAt` beside a status being the symptom ([[philosophy/always-valid-domain]]).
- *"Every placed order is eventually invoiced."* Liveness; order and invoice are separate aggregates, linked eventually. Pulling invoice into the order aggregate to make it immediate is the backwards guard firing: liveness mistaken for safety.

## Related

- Where the model exists, and the contamination a borrowed boundary is: [[philosophy/model-expressions]].
- What a model is: [[philosophy/model-phenomenology]].
- The property the aggregate holds, and how: [[philosophy/always-valid-domain]].
