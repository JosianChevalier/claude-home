---
tags: [ddd, domain-modeling, aggregates, consistency, invariants, tactical-ddd]
---

# Rationale: Aggregates

The aggregate (Evans) is a **consistency boundary**: the cluster of objects whose invariants must hold together at every save. It is not an object-graph convenience, a table grouping, or a transaction scope — those are other media's boundaries, and borrowing one is contamination ([[philosophy/model-expressions]]) transposed to the tactical axis: a grammar's own constraint masquerading as a domain decision.

## Invariants first

Identification is invariants-first: the boundary is derived, never drawn. List the properties that must never be violated — in domain vocabulary, no table, transaction, or framework words. The engineer who models states them, from their understanding of the business, built with the domain experts. The aggregate is whatever those properties force together; anything not forced stays out, which is why well-derived aggregates come out small.

## Safety vs liveness (Lamport)

- **Safety** — "nothing bad ever happens." Violated by a state you can point at ("this order's total disagrees with its lines").
- **Liveness** — "something good eventually happens." No finite state violates it; only never arriving does ("every placed order is eventually invoiced").

Only safety is a coherency constraint. A safety property must hold at every externally observable point, so everything it mentions must be saved together — that is what forces the boundary. Liveness forces no co-saving: it may span aggregates and go eventual. Vernon's rule — full consistency inside the aggregate, eventual consistency between aggregates — is the operational face of this classification. The guard runs backwards too: demanding immediate consistency across two aggregates means the boundary is wrong, or a liveness property is being treated as safety.

## Always valid

The observer of an aggregate is any code in the domain that holds it. Its invariants hold at every moment such code can see it: after each of its operations, in memory, before any save. Only the inside of one operation is unobserved. The repository is one more consumer; what it saves is valid because what it was handed was.

## Enforcement

The aggregate holds its invariants itself: by structure, the bad state unrepresentable, the root the sole handle to the interior (Wlaschin: make illegal states unrepresentable); at minimum by its code, the methods refusing it. Nothing below the aggregate enforces anything.

It is saved whole, in one call to a repository. How that save is made atomic is a modality of saving, the repository's business, and the model has no need to know it. Writes split across several saves leak the transaction into the domain code: the boundary was drawn wrong, back to the invariants.

## Example: one invariant each way

*"An order's total equals the sum of its lines"* — safety; forces order + lines into one aggregate; enforced by structure (total computed, never stored). *"A shipped order has a shipping date; an unshipped one has none"* — safety, and the usual way to break it is a nullable `shippedAt` beside a `status`, with a constructor check that the two agree. The check is the symptom: the state is one of several, each with its own fields, and the type says so — `Placed`, `Shipped(shippedAt)`, `Cancelled(cancelledAt, reason)`. Every "if I am in this state I must also have this field" is a case waiting to be a variant. The same holds for any field that is coherent only given another: a deletion date, a validator's id while validation may not have happened. *"Every placed order is eventually invoiced"* — liveness; order and invoice are separate aggregates, linked eventually. Pulling invoice into the order aggregate to make it immediate is the backwards guard firing: liveness mistaken for safety.
