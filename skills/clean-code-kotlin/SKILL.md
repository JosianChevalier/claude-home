---
name: clean-code-kotlin
description: Writing or reviewing Kotlin code. Clean code: functions at one level of abstraction reading like English, states as types.
---

# Clean code (Kotlin)

## Doctrine

- SLAP, always: one level of abstraction per function (Composed Method, Beck). The tool is extracting a function, never naming a variable.
- Model-driven design (Evans), stratified (Abelson & Sussman): each abstraction layer is a zoom level with its own model, built from the words of the layer beneath.
- Intention-revealing interfaces (Evans): a reader digs into a function to see how, never to understand what.
- Stepdown rule: each layer reads as a coherent English sentence, like well-written prose (Booch).
- Idiomatic Kotlin: the collection pipeline, extended to `Result` and the safe-call chain, carries the flow; partial application hides the syntax.
- Tell, don't ask: behaviour lives on the object that owns the data; a collection with domain meaning is a class.
- Illegal states are unrepresentable: a state is a type, a transition returns the next state's type.
- Everything is immutable: `val`, read-only collections, a change returns a new instance.
- Object Calisthenics, loosely.

## Know-how

### Composition

- Read aloud: "filter, reduce, for" is implementation, "remove inactive, sum totals" is intent.
- A comment separating sections, or an "and" in the description, names the functions to extract. Bodies of one to five lines.
- Early return over nesting; inside a `Result` pipeline the chain short-circuits instead.

```kotlin
// before
fun process(customerId: CustomerId) {
    // Fetch current state
    val orders = orderRepository.findPending(customerId)
    val payments = paymentRepository.findByCustomer(customerId)

    // Detect failed payments
    val failedPayments = mutableListOf<FailedPayment>()
    for (payment in payments) {
        if (payment.isDeclined) failedPayments.add(FailedPayment.declined(payment))
    }

    // Reconcile
    for (order in orders) {
        if (failedPayments.any { it.matches(order) }) order.cancel()
    }
}

// after
fun process(customerId: CustomerId) {
    val pendingOrders = fetchPendingOrders(customerId)
    val failedPayments = detectFailedPayments(customerId)

    reconcile(pendingOrders, failedPayments)
}
```

- A pipeline, `.map`/`.flatMap` on a `Result` or a collection, has a named concept at each step. A lambda holding logic becomes a function returning a function, partial application; a bare delegation such as `Product::isListed` stays inline.
- Chaining over unwrapping: `map`, `flatMap`, `?.`, `?.let`, `?:`, never a null check then `!!`. A type without a chain is handled imperatively, each non-trivial branch extracted.

```kotlin
return expectedTimestamps
    .filter(notCoveredBy(covered))
    .map(asMissing(unit))

private fun notCoveredBy(covered: Set<Instant>): (Instant) -> Boolean =
    { timestamp -> timestamp !in covered }
```

### Names

- Intent, in the domain's language; no abbreviation in code: `quantity`, `repository`.
- A factory is imported on its own when the call reads without its qualifier, `customerId("alice")`, `success(result)`; the qualifier stays when it does not, `CustomerId.of("alice")`.

### Placement

- A service is a closure: context captured once, one behaviour returned. Several closures over the same context, calling each other or evolving together, are a class, the repository shape being the archetype.
- A function using the object's state or part of its public API is a member; a pure helper is a `private` top-level function below the class, the file being the privacy boundary.

```kotlin
fun distributeUsing(storageCost: StorageCost): (StockLevels) -> Costs =
    { stockLevels -> stockLevels.distribute(storageCost) }

toResult(stockLevels).map(distributeUsing(warehouseStorageCost))
```

### Types

- A state is a class in a sealed hierarchy. The transition a state lacks does not compile; a consumer demands the one state it handles; a `when` over the hierarchy is exhaustive, without `else`.

```kotlin
sealed interface Order

data class OrderReady(val lines: OrderLines) : Order {
    fun cancel(): OrderCancelled = OrderCancelled(lines, Instant.now())
    fun process(): OrderExpedited = OrderExpedited(lines, Instant.now())
}

data class OrderExpedited(val lines: OrderLines, val expeditedAt: Instant) : Order {
    // no cancel(): an expedited order cannot be cancelled, the compiler says so
}

fun processOrder(order: OrderReady): ProcessOrderOutput = ...
```

- A value object is its own type, never a bare primitive: a class when it has behaviour (`Euros.add`), a `@JvmInline value class` when it is id-like.
- Absence is modelled, `Price?`, never a required field filtered upstream.

### Errors and comments

- Errors: a sealed hierarchy for outcomes the caller decides on, `Result` for recoverable flows, local try-catch for local recovery, `throw` for the unrecoverable.
- Comments: [clean-code-kotlin:comments](comments/SKILL.md).

Rationale: @../clean-code-ts/rationale/services-closures-first.md, φubiquitous-language
