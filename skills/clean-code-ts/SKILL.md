---
name: clean-code-ts
description: Use when writing or reviewing TypeScript code to enforce clean code principles. Ensures code reads like English.
---

# Clean Code (TypeScript)

Principles for writing code that reads like prose. Inspired loosely by Object Calisthenics.

## The Prime Directive

**Code should read as close as possible to English.** A reader should understand *what* the code does without deciphering *how*. Each function tells a story at one level of detail.

## Single Layer of Abstraction (SLAP)

The most important rule. Every function must operate at **one consistent level of abstraction**.

```ts
// BAD — domain intent buried under technical noise
function generateReport(orders: Order[]): Report {
  const active = orders.filter(o => o.isActive());
  let total = 0;
  for (const order of active) {
    total += order.price * order.quantity;
  }
  const formatted = `Total: ${total.toFixed(2)}`;
  return new Report(formatted, active.length);
}

// GOOD — reads like English, each line is one domain concept
function generateReport(orders: Order[]): Report {
  const activeOrders = removeInactive(orders);
  const total = sumOrderTotals(activeOrders);
  return formatReport(total, activeOrders.length);
}
```

**The test:** read the function aloud. If you hear "filter, reduce, for-loop" you're reading implementation. If you hear "remove inactive, sum totals, format report" you're reading intent.

**Smell:** If you need a comment to separate sections within a function, each section should be its own function.

**Anti-pattern: variables as fake abstraction.** Giving a name to an expression does not raise the abstraction level. SLAP means each line operates at the same *domain* level — and the tool for that is **extracting a function**, not naming a variable. The function name describes the concept; the body hides the mechanism.

```ts
// BAD — variables label steps but the function still mixes levels
const validated = input.filter(isValid);
const sorted = [...validated].sort(byPriority);
return new Report(sorted);

// GOOD — each concept is a function; the function reads as a plan
const validated = removeInvalid(input);
const prioritized = sortByPriority(validated);
return new Report(prioritized);
```

**In functional pipelines too.** When composing via `.map()`/`.flatMap()` on a `Result` or array chain, each step should be a named domain concept — not raw lambdas or grouping mechanics.

```ts
// GOOD — pipeline reads as a plan, each step is a named concept
fullPrice(): TotalPriceResult {
  return Result.success(this.orderLines)
    .flatMap(validateNonEmpty)
    .map(mapArray(addVat))
    .flatMap(Result.combine)
    .map(associateWithTotalDiscount(this.discounts))
    .map(computeTotalPrice)
    .flatMap(ensureHigherThan(this.deliveryFees))
    .map(sumEuros(this.deliveryFees))
    .valueOrError();
}
```

Partial application functions (`associateWithTotalDiscount`, `ensureHigherThan`) capture context and return a function — the pipeline reads like a plan: validate, add VAT, apply discount, total, check floor, add fees.

```ts
// BAD — comments revealing hidden functions
function process(customerId: CustomerId): void {
  // Fetch current state
  const orders = orderRepository.findPending(customerId);
  const payments = paymentRepository.findByCustomer(customerId);

  // Detect failed payments
  const failedPayments: FailedPayment[] = [];
  for (const payment of payments) {
    if (payment.isDeclined()) {
      failedPayments.push(FailedPayment.declined(payment));
    }
  }

  // Reconcile orders with failed payments
  for (const order of orders) {
    if (failedPayments.some(f => f.matches(order))) {
      order.cancel();
    }
  }
}

// GOOD — each step is a function, the story is clear
function process(customerId: CustomerId): void {
  const pendingOrders = fetchPendingOrders(customerId);
  const failedPayments = detectFailedPayments(customerId);

  reconcile(pendingOrders, failedPayments);
}
```

## Small, Focused Functions

Functions should do **one thing**. If you can describe what a function does using "and", it does too much.

Extract until each function name fully describes its content. Bodies of 1-5 lines are normal and good.

## Naming Is Design

Names should reveal intent and belong to the domain language.

```ts
// BAD
function proc(s: string, t: number) { }
function getPayments(f: boolean): Payment[] { }
const tmp = computeResult();

// GOOD
function cancelUnpaidOrders(customerId: CustomerId) { }
function findDeclinedPayments(): Payment[] { }
const dailyRevenue = splitByDay(monthlyRevenue);
```

**No abbreviations.** `quantity` not `qty`. `repository` not `repo` (in code, fine in conversation).

## Minimize Indentation

Prefer early returns over nested conditions. Flat code reads easier.

```ts
// BAD
function process(product: Product | undefined): void {
  if (product !== undefined) {
    if (product.isListed()) {
      if (product.isLowOnStock()) {
        reorder(product);
      }
    }
  }
}

// GOOD
function process(product: Product | undefined): void {
  if (product === undefined || !product.isListed()) {
    return;
  }
  if (product.isLowOnStock()) {
    reorder(product);
  }
}
```

## Push Behavior to Objects

Ask objects to do things, don't extract their data to decide for them.

```ts
// BAD — asking for data, deciding externally
if (order.status === Status.Pending && order.createdAt < cutoff) {
  order.status = Status.Expired;
}

// GOOD — telling the object what to do (returns the new state)
const expired = order.expireIfOlderThan(cutoff);
```

## First-Class Collections

When a collection has domain meaning, wrap it. This gives behavior a home.

```ts
// Instead of Product[] with external filtering logic
class Products {
  constructor(private readonly values: readonly Product[]) {}

  lowOnStock(): Products {
    return new Products(this.values.filter(product => product.isLowOnStock()));
  }
}
```

## Services: Closures by Default, Classes for Cohesion

A domain service is a **closure**: context captured once, one behavior returned.

```ts
// one behavior + context → closure
const computeMissing = (period: Period) =>
  (stockLevels: StockLevels): StockLevelsWithGaps => { ... };

// pipeline: .map(computeMissing(period))
```

When several closures would capture the **same context** and belong together — sharing a resource, calling each other, evolving together — you have rebuilt a class by hand: promote it. The repository shape (a few cohesive operations over one shared store) is the archetype, applied here to pure domain:

```ts
class DeliveryCalendar {
  constructor(private readonly slots: readonly DeliverySlot[]) {}

  canDeliver(order: Order, at: Date): boolean { ... }

  nextSlotFor(customer: CustomerId): DeliverySlot | undefined { ... }

  schedule(slot: DeliverySlot): DeliveryCalendar {
    return new DeliveryCalendar([...this.slots, slot]);
  }
}
```

The gradient: one behavior → closure. A cluster of cohesive behaviors over shared context/resource → class. Never a utility module of unrelated exported functions.

Rationale: @rationale/services-closures-first.md

## Members vs Module Functions

Placement rule:

- Uses `this` (state, other members) or is **public API** → class member
- Pure private helper → **non-exported function below the class**

The module is the privacy boundary — non-exported functions are `private` without living inside the class.

```ts
export class Order {
  fullPrice(): TotalPriceResult {
    return Result.success(this.orderLines)
      .flatMap(validateNonEmpty)   // module functions compose point-free
      .map(mapArray(addVat))
      ...
  }
}

// pure helpers below — invisible outside the module
function validateNonEmpty(orderLines: OrderLine[]): Result<OrderLine[], InvalidPrice> { ... }
function addVat(orderLine: OrderLine): Result<OrderLine, InvalidPrice> { ... }
```

Pure module functions keep the functional advantages in idiomatic dot-free form while avoiding language quirks — `array.map(myFunction)` just works, whereas `array.map(this.myFunction)` silently loses its `this` binding.

Rationale: @rationale/members-vs-module-functions.md

## Make Illegal States Unrepresentable

TypeScript version of @rules/always-valid-domain.md — states are **types**, transitions are methods returning the **next state's type**. Illegal transitions don't compile.

```ts
export abstract class Order {
  readonly id: OrderId;
  readonly orderLines: OrderLines;
  readonly events: OrderEvent[];
  abstract readonly state: OrderState;
}

export class OrderReady extends Order {
  readonly state: OrderState.Ready = OrderState.Ready;  // literal type → discriminated union over classes

  cancel(): OrderCancelled { return OrderCancelled.from(this, new Date()); }
  process(): OrderExpedited { return OrderExpedited.from(this, new Date()); }

  updateDeliveryAddress(address: DeliveryAddress): OrderReady {
    return new OrderReady({
      ...this,
      deliveryAddress: address,
      events: [...this.events, orderEvent(new Date(), { type: 'UPDATE_ADDRESS', data: { address } })],
    });
  }
}

export class OrderExpedited extends Order {
  readonly state: OrderState.Expedited = OrderState.Expedited;
  readonly expeditedAt: Date;
  // no cancel() — an expedited order cannot be cancelled; the compiler enforces it
}

// consumers demand the only state they can handle
const processOrder = (order: OrderReady, ...): Promise<ProcessOrderOutput> => ...
```

Aggregates are immutable: every change returns a new instance (`new OrderReady({ ...this, ... })`), every transition returns a new type, and each change appends its domain event.

Rationale: @rationale/typestate.md, @rationale/immutability.md

## Nominal Types for Value Objects

TypeScript is structurally typed — every `string` is every other `string`. Value objects need deliberate nominal-ness:

- Rich behavior (arithmetic, comparison) → **class wrapper** (`Euros.add/times/deduct`)
- Id-like primitives → **branded type + factory**

```ts
declare function findByCustomer(customer: CustomerId): Order[];

findByCustomer('alice');              // ❌ does not compile — a plain string is not a CustomerId
findByCustomer(customerId('alice'));  // ✅ built through the factory
```

The branding mechanism itself heavily depends on each project's needs and standards — follow the project's existing branding utility rather than introducing a new one.

Rationale: @rationale/nominal-value-objects.md

## Functional Pipeline Composition

When a workflow is a sequence of transformations, compose it as a **functional pipeline** using `.map()`/`.flatMap()` on a monadic type (e.g. `Result`). Each step is a named function.

```ts
// BAD — manual variable wiring
const translated = stockMovementsToLevels(movements);
const withGaps = fillGaps(translated, period);
const extrapolated = extrapolateFrom(withGaps, period);
if (extrapolated.size === 0) return new Set();
return distribute(extrapolated, warehouseStorageCost);

// GOOD — pipeline reads as a story
translateToStockLevels(movements)
  .map(computeMissing(period))
  .map(extrapolateMissing(period))
  .map(distribute(warehouseStorageCost))
  .fold(groupByProduct, () => new Set());
```

Key principles:
- Each brick is a `(input: In) => Out`, context captured by closure
- Use `Result.map()` for error short-circuiting (no early returns)
- Use a mix between functional and OOP approaches:
  - functional in the spirit (pure functions, immutability, pipeline approach)
  - behavior attaches to objects to create DSL. Examples:
    - use monads such as `Result`/`Option` that compose functions through `.map` or `.flatMap`
    - methods returning a new instance computed from the previous state of the object

**Prefer chaining over unwrapping.** When a type offers `map`/`flatMap`/`orElse`, use the chain instead of unwrapping with `isEmpty` + `get`. Not all types are chainable — for those, imperative style is fine, but extract any non-trivial branch into a named function.

## Higher-Order Functions in Array Chains

In functional-style array pipelines, extract inline lambdas to named functions returning functions (partial application). This makes the chain read like English.

```ts
// BAD — inline lambdas obscure intent
return expectedTimestamps
  .filter(ts => !covered.has(ts))
  .map(ts => new MissingStockLevel(ts, unit));

// GOOD — named higher-order functions
return expectedTimestamps
  .filter(notCoveredBy(covered))
  .map(asMissing(unit));

const notCoveredBy = (covered: Set<Instant>) => (timestamp: Instant): boolean =>
  !covered.has(timestamp);

const asMissing = <Unit>(unit: Unit) => (timestamp: Instant): StockLevel<Unit> =>
  new MissingStockLevel(timestamp, unit);
```

Each extracted function captures context via its parameters and returns a function that reads as a verb phrase in the pipeline. A trivial delegation like `product => product.isLowOnStock()` may stay inline — extract when the lambda holds logic, not just a call.

## Errors

See [clean-code-ts:exceptions](exceptions/SKILL.md) — tagged unions for outcomes, `Result` railway for recoverable flows, local try-catch for local recovery, `throw` for the unrecoverable.

## Domain Expressiveness Over TypeScript Convention

When a general TypeScript convention conflicts with the domain model's ability to represent reality, **domain expressiveness wins**. The model must faithfully capture what exists — including absence, partiality, and uncertainty.

```ts
// Convention says: avoid optional-looking fields in domain types
// But the domain has partial data — some prices may be missing
// ✅ Domain expressiveness wins — absence is modeled explicitly
type PriceSnapshot = Readonly<{
  listPrice: Option<Price>;
  salePrice: Option<Price>;
}>;

// ❌ Convention wins, domain suffers — no way to represent "missing"
type PriceSnapshot = Readonly<{
  listPrice: Price;
  salePrice: Price;
}>;
```

**The test:** does following the convention force you to lose information, add edge cases, or filter upstream? If yes, the convention is wrong *here*.

## TypeScript Preferences

### Named Imports for Factory Functions

Import a factory function directly when its name alone is sufficient to understand what is being built.

```ts
// GOOD — name is self-explanatory, direct import
import { customerId } from './customerId';
import { success, failure } from './result';
import { nonBlank } from './nonBlankString';

const customer = customerId('alice');
return success(result);
return failure(error);

// BAD — generic name, no idea what it builds without the qualifier
import { of } from './customerId';

const customer = of('alice');  // of what?

// GOOD — keep a qualifier for generic names
const customer = CustomerId.of('alice');
const duration = Duration.of(5, 'minutes');
```

**Rule of thumb:** read the call site without the qualifier. If it still makes sense, direct import. If not, keep the qualifier.

## Checklist

When writing or reviewing code, verify:

1. **SLAP** — Does each function stay at one abstraction level?
2. **Reads like English** — Can you read the function aloud and it makes sense?
3. **No "how" comments** — See [clean-code-ts:comments](comments/SKILL.md)
4. **Small functions** — Is every function doing exactly one thing?
5. **Meaningful names** — Do names reveal intent without needing context?
6. **Flat structure** — Are early returns used instead of deep nesting?
7. **Behavior on objects** — Is logic pushed into the objects that own the data?
8. **Named lambdas** — Are non-trivial lambdas extracted to higher-order functions?
9. **Services** — Closures by default; classes only for cohesive behavior clusters sharing context?
10. **Placement** — `this`/public API as members; pure helpers as non-exported functions below?
11. **Illegal states** — Are domain states types, with transitions returning the next type?
12. **Nominal value objects** — Classes for rich behavior, brands for id-like primitives (project's own mechanism)?
13. **Pipelines** — Are multi-step transformations composed via `.map()` with named steps?
14. **Errors** — Does failure handling follow the ladder in [clean-code-ts:exceptions](exceptions/SKILL.md)?
