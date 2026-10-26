---
name: clean-code-kotlin
description: Writing or reviewing Kotlin code. Clean code: methods at one level of abstraction, reading like English.
---

# Clean code (Kotlin)

## Doctrine

- **Code reads as close as possible to English.** A reader understands *what* the code does without deciphering *how*.
- **One level of abstraction per method** (Beck, Composed Method): each method tells a story at one level of detail.
- Object Calisthenics, loosely.

## Single Layer of Abstraction (SLAP)

Every method operates at **one consistent level of abstraction**.

```kotlin
// BAD — domain intent buried under technical noise
fun generateReport(orders: List<Order>): Report {
    val active = orders.filter { it.isActive }
    var total = 0.0
    for (order in active) {
        total += order.price * order.quantity
    }
    val formatted = "Total: %.2f".format(total)
    return Report(formatted, active.size)
}

// GOOD — reads like English, each line is one domain concept
fun generateReport(orders: List<Order>): Report {
    val activeOrders = removeInactive(orders)
    val total = sumOrderTotals(activeOrders)
    return formatReport(total, activeOrders.size)
}
```

**The test:** read the method aloud. If you hear "filter, for-loop, format" you're reading implementation. If you hear "remove inactive, sum totals, format report" you're reading intent.

**Smell:** If you need a comment to separate sections within a method, each section should be its own method.

**Anti-pattern: variables as fake abstraction.** Giving a name to an expression does not raise the abstraction level. SLAP means each line in the method operates at the same *domain* level — and the tool for that is **extracting a method**, not naming a variable. The method name describes the concept; the method body hides the mechanism.

```kotlin
// BAD — variables label steps but the method still mixes levels
val validated = input.filter { it.isValid }
val sorted = validated.sortedByDescending { it.priority }
return Report(sorted)

// GOOD — each concept is a method; the method reads as a plan
val validated = removeInvalid(input)
val prioritized = sortByPriority(validated)
return Report(prioritized)
```

**In functional pipelines too.** When composing via `.map()` on a `Result` or a collection, each step should be a named domain concept — not raw lambdas or grouping mechanics.

```kotlin
// BAD — pipeline mixes domain steps with plumbing
return toResult(stockLevels)
    .map { computeMissing.fillGaps(it, units, period) }
    .map { extrapolate.extrapolate(it) }
    .map { distribute.distribute(it, warehouseStorageCost) }
    .fold(
        onSuccess = { costs ->
            costs.groupBy({ it.key }, { it.value })
                .map { (product, productCosts) -> ProductResult(product, productCosts.toSet()) }
                .toSet()
        },
        onFailure = { emptySet() },
    )

// GOOD — each .map reads as a verb phrase, fold delegates to a named concept
return toResult(stockLevels)
    .map(fillGapsUsing(units, period))
    .map(extrapolate::extrapolate)
    .map(distributeUsing(warehouseStorageCost))
    .fold(groupByProduct::group, noData())
```

`noData()` returns a function that ignores the error and returns an empty set — even error handling reads like a domain concept. Partial application methods (`fillGapsUsing`, `distributeUsing`) capture context and return a function — the pipeline reads like a plan: fill gaps, extrapolate, distribute, group by product.

```kotlin
// BAD - comments revealing hidden methods
fun process(customerId: CustomerId) {
    // Fetch current state
    val orders = orderRepository.findPending(customerId)
    val payments = paymentRepository.findByCustomer(customerId)

    // Detect failed payments
    val failedPayments = mutableListOf<FailedPayment>()
    for (payment in payments) {
        if (payment.isDeclined) {
            failedPayments.add(FailedPayment.declined(payment))
        }
    }

    // Reconcile orders with failed payments
    for (order in orders) {
        if (failedPayments.any { it.matches(order) }) {
            order.cancel()
        }
    }
}

// GOOD - each step is a method, the story is clear
fun process(customerId: CustomerId) {
    val pendingOrders = fetchPendingOrders(customerId)
    val failedPayments = detectFailedPayments(customerId)

    reconcile(pendingOrders, failedPayments)
}
```

## Small, Focused Methods

Methods should do **one thing**. If you can describe what a method does using "and", it does too much.

Extract until each method name fully describes its content. Method bodies of 1-5 lines are normal and good.

## Naming Is Design

Names should reveal intent and belong to the domain language.

```kotlin
// BAD
fun proc(s: String, t: Int) { }
fun getPayments(f: Boolean): List<Payment> { }
val tmp = computeResult()

// GOOD
fun cancelUnpaidOrders(customerId: CustomerId) { }
fun findDeclinedPayments(): List<Payment> { }
val dailyRevenue = splitByDay(monthlyRevenue)
```

**No abbreviations.** `quantity` not `qty`. `repository` not `repo` (in code, fine in conversation).

## Minimize Indentation

Prefer early returns over nested conditions. Flat code reads easier.

```kotlin
// BAD
fun process(product: Product?) {
    if (product != null) {
        if (product.isListed) {
            if (product.isLowOnStock) {
                reorder(product)
            }
        }
    }
}

// GOOD
fun process(product: Product?) {
    if (product == null || !product.isListed) return
    if (product.isLowOnStock) reorder(product)
}
```

## Push Behavior to Objects

Ask objects to do things, don't extract their data to decide for them.

```kotlin
// BAD - asking for data, deciding externally
if (order.status == Status.PENDING && order.createdAt.isBefore(cutoff)) {
    order.status = Status.EXPIRED
}

// GOOD - telling the object what to do
order.expireIfOlderThan(cutoff)
```

## First-Class Collections

When a collection has domain meaning, wrap it. This gives behavior a home.

```kotlin
// Instead of List<Product> with external filtering logic
@JvmInline
value class Products(val values: List<Product>) {
    fun lowOnStock() = Products(values.filter { it.isLowOnStock })
}
```

## Domain Services Are Classes

Domain services are **instantiated classes**, not singleton `object`s or top-level functions. Top-level functions and companion objects are reserved for factory functions and very simple helpers.

A service captures its context (dependencies, configuration) in the constructor and exposes behavior through instance methods. This makes services composable, testable, and injectable.

```kotlin
// BAD - singleton utility object
object ComputeMissing {
    fun <U> fillGaps(stockLevels: Set<RecordedStockLevel<U>>, period: Period): StockLevelsWithGaps<U> { ... }
}
// caller: val withGaps = ComputeMissing.fillGaps(stockLevels, period)

// GOOD - instantiated service
@DomainService
class ComputeMissing<U>(private val period: Period) : (Set<RecordedStockLevel<U>>) -> StockLevelsWithGaps<U> {
    override fun invoke(stockLevels: Set<RecordedStockLevel<U>>): StockLevelsWithGaps<U> { ... }
}
```

**Prioritize this style unless it really adds noise** — a one-line helper like `maxOf()` is fine as a top-level function.

## Functional Pipeline Composition

When a workflow is a sequence of transformations, compose it as a **functional pipeline** using `.map()` on a monadic type (e.g. `Result`). Each step is a function instance.

```kotlin
// BAD - manual variable wiring with singleton calls
val translated = StockMovementsToLevels.from(movements)
val withGaps = ComputeMissing.fillGaps(translated, period)
val extrapolated = ExtrapolateMissing.from(withGaps, period)
if (extrapolated.isEmpty()) return emptySet()
return distribute(extrapolated, warehouseStorageCost)

// GOOD - pipeline reads as a story
translateToStockLevels(movements)
    .map(computeMissing)
    .map(extrapolateMissing)
    .map(computeWeights)
    .map(distribute)
    .fold(groupByProduct) { noData -> emptySet() }
```

Key principles:
- Each brick is a class implementing `(In) -> Out`, with context in its constructor
- Use `Result.map()` for error short-circuiting (no early returns)
- Use a mix between functional and OOP approaches :
  - functional in the spirit (pure functions, immutability, pipeline approach)
  - behavior attaches to objects to create DSL. Examples:
    - use monads such as collections/result that compose the functions through .map or .flatMap
    - methods returning a new instance computed from the previous state of the object

**Prefer chaining over unwrapping.** When a type offers `map`/`flatMap`, or a value is nullable (`?.`, `?.let`, `?:`), use the chain instead of unwrapping with a null check or `!!`.

## Higher-Order Functions in Collection Chains

In functional-style collection pipelines, extract inline lambdas to named functions returning a function type (partial application). This makes the chain read like English.

```kotlin
// BAD - inline lambdas obscure intent
return expectedTimestamps
    .filter { it !in covered }
    .map { MissingStockLevel(it, unit) }

// GOOD - named higher-order functions
return expectedTimestamps
    .filter(notCoveredBy(covered))
    .map(asMissing(unit))

private fun notCoveredBy(covered: Set<Instant>): (Instant) -> Boolean =
    { timestamp -> timestamp !in covered }

private fun <U> asMissing(unit: U): (Instant) -> StockLevel<U> =
    { timestamp -> MissingStockLevel(timestamp, unit) }
```

Each extracted function captures context via its parameters and returns a function that reads as a verb phrase in the pipeline.

## Kotlin Preferences

### Imports for Factory Functions

Import a factory function on its own when its name alone is sufficient to understand what is being built.

```kotlin
// GOOD - name is self-explanatory, imported on its own
import CustomerId.Companion.customerId
import Result.Companion.success
import Result.Companion.failure
import NonBlankString.Companion.nonBlank

val customer = customerId("alice")
return success(result)
return failure(error)

// BAD - generic name, no idea what it builds without the class
import CustomerId.Companion.of

val customer = of("alice")  // of what?

// GOOD - keep the class qualifier for generic names
val customer = CustomerId.of("alice")
```

**Rule of thumb:** read the call site without the class name. If it still makes sense, import the function alone. If not, keep the qualifier.

## Checklist

When writing or reviewing code, verify:

1. **SLAP** - Does each method stay at one abstraction level?
2. **Reads like English** - Can you read the method aloud and it makes sense?
3. **No "how" comments** - See [clean-code-kotlin:comments](comments/SKILL.md)
4. **Small methods** - Is every method doing exactly one thing?
5. **Meaningful names** - Do names reveal intent without needing context?
6. **Flat structure** - Are early returns used instead of deep nesting?
7. **Behavior on objects** - Is logic pushed into the objects that own the data?
8. **Named lambdas** - Are collection lambdas extracted to higher-order functions?
9. **Services are classes** - Are domain services instantiated, not singleton objects or top-level functions?
10. **Pipelines** - Are multi-step transformations composed via `.map()` with function classes?

Rationale: [[philosophy/ubiquitous-language]]
