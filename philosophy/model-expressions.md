---
tags: [ddd, domain-modeling, bounded-contexts, vocabulary, conceptual-integrity, architecture]
---

# Model expressions

**Thesis.** The model exists only as expressed, and each expression keeps what its grammar can say. Layers are expression boundaries; one model or two is settled by test, not by layer.

The domain model is intangible. It never exists anywhere directly; it exists only as it is *expressed* through the media of the socio-technical system — plain oral discussion, domain code, SQL schema, REST contract, UI, user stories, dashboards, even the org chart (Topçu).

Every expression has two defining constraints:

- **Grammar-bounded** — each medium has its own grammar (a type system, relational algebra, REST's uniform interface, natural language), and an expression can only say what its grammar allows. SQL has no sum types; REST has no lifecycle preconditions.
- **Concern-focused** — each grammar was built for one concern, so each expression is a projection: it preserves the dimensions matching its concern and loses the rest. SQL preserves structure, loses behavior; REST preserves resource state, loses workflow; a user story preserves intent, loses structure; oral discussion preserves everything informally, enforces nothing.

## Bounded context = system of cohesive expressions

Cohesion here means **homomorphism** — over concepts and their relationships, not over constraints. Each expression must map every domain concept, and every domain change, to the same concept rendered in its own grammar; it may still be unable to *enforce* a constraint its grammar cannot state (SQL loses the sum-type rule yet still speaks of the same fulfillment). If an expression maps a domain change to a different concept, you are looking at two models, hence two bounded contexts.

The decisive consequence: **layer boundaries are expression boundaries, not model boundaries.** Frontend, API, and backend being distinct media never by itself justifies distinct models. A second representation of the same concept is warranted only by a genuinely different model (another context) or by a local compensation for a grammar limit — never by the mere existence of a layer.

## One model or two? Three tests, weakest to strongest

**1. Static check** (Model Mitosis shared-kernel rules). Same model requires all four: same meaning of concepts, same representation (types and format), same business rules, same invariants. Any mismatch → two models. All match → candidate for one model; confirm dynamically.

**2. Perturbation test.** Change a structuring constraint (round-trip → multi-destination). If every artifact absorbs it as the same concept, just re-rendered in its own grammar → expressions. If one maps it to a different concept (or a false cognate) → separate model.

**3. Invariant enforceability test.** Could expression B enforce the invariant — setting aside security, performance, and every other non-modeling concern? If yes, B holds the invariant's referent and can state it: placement is a design choice, one model, expressions. If no, the best B can state is about a copy — a different statement: different models, two bounded contexts, designated owner plus a contract.

A front-end price check ("selected price must match the real fare"): the front-end only ever holds a snapshot, so what it enforces is "matches my copy" — a false cognate. Contrast "delivery ⇒ address" in a form holding both fields: it *could* be sole enforcement; that it shouldn't be is security, not modeling.

Note the fit: the static rules and the dynamic tests check the same thing at different times. Rules 1–2 (meaning, representation) are what test 2 perturbs; rules 3–4 (business rules, invariants) are what test 3 probes.

**Caveat: a grammar limit isn't divergence.** SQL forcing an id on a value object doesn't make the DB a different model — normal: the root cause is the grammar, not ours to treat, so compensate locally (ACL), a trade-off accepted, and don't let it spread.

Divergence is saying something the model doesn't, *beyond* what the grammar forces — a **model tension** (φmodel-phenomenology): either the expression is wrong or there is a second model asking for its own context.

## Pathologies

- **Contamination** — a grammar's own constraint (SQL's mandatory primary key) leaks into neighboring expressions until it masquerades as a domain constraint.
- **Permeability** — an invariant enforced solely in an expression that cannot state it (price check in the front-end) breaks the always-valid property of the whole context.
- **Impedance mismatch** — expressions that no longer preserve the homomorphism get patched with heavy translation layers while the business capability itself diverges.
- **Confusion** — treating one expression as a bounded context (or a context as one expression) generates model tensions that erode conceptual integrity.

## Example: one invariant, five expressions

Invariant: *an order is picked up in store (no address) or delivered (exactly one address); the choice freezes once payment starts.*

**Oral** — "Delivery needs an address, pickup doesn't, and once they start paying they can't switch." Says everything, enforces nothing.

**UI** — Radio Pickup / Delivery; the address form renders only for Delivery; the "Change delivery" button is absent from the payment page. Enforced in the nominal path by absent affordance — the form holds both the type and the address.

**Domain code**

```kotlin
sealed class Fulfillment {
    object Pickup : Fulfillment()
    data class Delivery(val address: Address) : Fulfillment()
}
class OrderInPayment { fun confirm(): Order }  // no changeFulfillment() — frozen by construction
```

Both invariants uncompilable.

**SQL**

```sql
INSERT INTO fulfillment (order_id, type) VALUES ('42', 'DELIVERY');
-- no address row, yet accepted: the sum-type rule is cross-row, CHECK is row-local
```

**REST**

```http
PATCH /orders/42/fulfillment  →  422  (payment started)
```

`oneOf` preserves the shape; the freeze is absent from the documented contract, so the 422 is a runtime surprise. Hypermedia could express it the way the UI does — withdraw the fulfillment link once payment starts — the grammar allows it; this contract doesn't use it.

Other media — user story, diagram, dashboard, org chart — project the same way: each keeps what its grammar can say, drops the rest.

**Perturbation, transposed.** Add delivery to a pickup locker (address = locker ID): all expressions must absorb it as the same concept — a third radio, a `Locker(lockerId)` case, a discriminated address shape. If a neighboring system maps it onto `DELIVERY` with a fake street address — different concept, same word — that's not a lagging expression, that's a second bounded context wearing a false cognate.

## Related

- What a model is, the tension felt before the tests, the spork: φmodel-phenomenology.
- The model's consistency boundary: φaggregates.
- Translation located, not diffused: φtransmission-belt.
