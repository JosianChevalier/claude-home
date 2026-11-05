---
name: clean-code-ts
description: Writing or reviewing TypeScript code. Clean code: functions at one level of abstraction reading like English, states as types.
---

# Clean code (TypeScript)

## Doctrine

- SLAP, always: one level of abstraction per function (Composed Method, Beck). The tool is extracting a function, never naming a variable.
- Model-driven design (Evans), stratified (Abelson & Sussman): each abstraction layer is a zoom level with its own model, built from the words of the layer beneath.
- Intention-revealing interfaces (Evans): a reader digs into a function to see how, never to understand what.
- Stepdown rule: each layer reads as a coherent English sentence, like well-written prose (Booch).
- Idiomatic TypeScript: the method pipeline, extended to the `Option` and `Result` monads, carries the flow; partial application hides the syntax.
- Behaviour lives on the object that owns the data; a collection with domain meaning is a class.
- Illegal states are unrepresentable: a state is a type, a transition returns the next state's type.
- Everything is immutable: a change returns a new instance.
- Domain expressiveness wins over TypeScript convention: a convention that loses information, absence or partiality included, is wrong here.
- Object Calisthenics, loosely.

## Know-how

### Composition

- Read aloud: "filter, reduce, for" is implementation, "remove inactive, sum totals" is intent.
- A comment separating sections, or an "and" in the description, names the functions to extract. Bodies of one to five lines.
- Early return over nesting.

```ts
// before
function process(customerId: CustomerId): void {
  // Fetch current state
  const orders = orderRepository.findPending(customerId);
  const payments = paymentRepository.findByCustomer(customerId);

  // Detect failed payments
  const failedPayments: FailedPayment[] = [];
  for (const payment of payments) {
    if (payment.isDeclined()) failedPayments.push(FailedPayment.declined(payment));
  }

  // Reconcile
  for (const order of orders) {
    if (failedPayments.some(f => f.matches(order))) order.cancel();
  }
}

// after
function process(customerId: CustomerId): void {
  const pendingOrders = fetchPendingOrders(customerId);
  const failedPayments = detectFailedPayments(customerId);

  reconcile(pendingOrders, failedPayments);
}
```

- A pipeline, `.map`/`.flatMap` on a `Result` or an array, has a named concept at each step. A lambda holding logic becomes a function returning a function, partial application; a bare delegation such as `p => p.isListed()` stays inline.
- Chaining over unwrapping: `map`, `flatMap`, `orElse`, never `isEmpty` then `get`. A type without a chain is handled imperatively, each non-trivial branch extracted.

```ts
return expectedTimestamps
  .filter(notCoveredBy(covered))
  .map(asMissing(unit));

const notCoveredBy = (covered: Set<Instant>) => (timestamp: Instant): boolean =>
  !covered.has(timestamp);
```

### Names

- Intent, in the domain's language; no abbreviation in code: `quantity`, `repository`.
- A factory is imported by name when the call reads without its qualifier, `customerId('alice')`, `success(result)`; the qualifier stays when it does not, `CustomerId.of('alice')`.

### Placement

- A service is a closure: context captured once, one behaviour returned. Several closures over the same context, calling each other or evolving together, are a class, the repository shape being the archetype. Never a module of unrelated exported functions.
- A function using `this` or part of the public API is a member; a pure helper is a non-exported function below the class, the module being the privacy boundary. It composes point-free: `array.map(helper)` works where `array.map(this.helper)` loses its binding.

### Types

- A state is a class with a literal `state` field, a discriminated union over classes. The transition a state lacks does not compile; a consumer demands the one state it handles.

```ts
export class OrderReady extends Order {
  readonly state: OrderState.Ready = OrderState.Ready;

  cancel(): OrderCancelled { return OrderCancelled.from(this, new Date()); }
  process(): OrderExpedited { return OrderExpedited.from(this, new Date()); }
}

export class OrderExpedited extends Order {
  readonly state: OrderState.Expedited = OrderState.Expedited;
  // no cancel(): an expedited order cannot be cancelled, the compiler says so
}

const processOrder = (order: OrderReady): Promise<ProcessOrderOutput> => ...
```

- A value object is nominal: a class when it has behaviour (`Euros.add`), a branded type with a factory when it is id-like, through one branding utility for the whole project.
- Absence is modelled, `Option<Price>`, never a required field filtered upstream.

### Errors and comments

- Errors: [clean-code-ts:exceptions](exceptions/SKILL.md), tagged unions for outcomes, `Result` for recoverable flows, local try-catch for local recovery, `throw` for the unrecoverable.
- Comments: [clean-code-ts:comments](comments/SKILL.md).

Rationale: φservices-closures-first, @philosophy/members-vs-module-functions.md, φtypestate, φimmutability, φnominal-value-objects, φubiquitous-language
