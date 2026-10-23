---
name: clean-code:comments
description: Use when code contains comments. Iterate on naming and structure until every comment is redundant and can be removed. Only "why" comments survive.
---

# Comments Are Code Smells

A comment is an admission that the code failed to express itself. The goal is **zero comments**, reached by iterating on the code until each comment becomes redundant.

## The Rule

1. See a comment explaining *what* or *how* → **iterate on the code** until the comment is redundant
2. Delete the redundant comment
3. Only keep comments that explain *why* something non-obvious exists

## Process: Eliminate a Comment

For every comment, ask: **"Can I change the code so this comment is unnecessary?"**

### Rename to replace the comment

```java
// BAD
// Check if the cart has not been updated for more than 24 hours
if (Duration.between(cart.lastUpdated(), now).toHours() > 24) {

// ITERATION 1 - extract to method, delete comment
if (cart.isInactiveSince(now, Duration.ofHours(24))) {

// ITERATION 2 - push behavior into the object
if (cart.isAbandoned()) {
```

### Extract method to replace the comment

```java
// BAD - comment separating a section
void replenish(WarehouseId warehouseId) {
    var products = productRepository.findByWarehouse(warehouseId);

    // Filter products running short
    var shortages = products.stream()
        .filter(p -> p.quantityInStock() < 10 || p.hasBackorders())
        .toList();

    shortages.forEach(this::reorder);
}

// GOOD - the method name IS the comment
void replenish(WarehouseId warehouseId) {
    var products = productRepository.findByWarehouse(warehouseId);
    var shortages = detectShortages(products);

    shortages.forEach(this::reorder);
}
```

### Introduce a domain concept to replace the comment

```java
// BAD
// Fewer than 10 units is considered low stock
if (product.quantityInStock() < 10) {

// GOOD - the domain concept speaks for itself
if (product.isLowOnStock()) {
// Inside Product, the threshold is a named constant or part of StockQuantity value object
```

### Replace conditional comment with expressive boolean

```java
// BAD
// Only sell the product if it is listed and not out of stock
if (product.status() == LISTED && !outOfStockProducts.contains(product.id())) {

// GOOD
var isPurchasable = product.isListed() && !product.isOutOfStock();
if (isPurchasable) {
```

## The Only Surviving Comments

Comments that explain **why** — a business rule, a workaround, a non-obvious constraint. These cannot be expressed in code.

```java
// DST transitions produce 23h or 25h days, so we use calendar days, not duration
var dayBoundaries = computeCalendarDayBoundaries(zone);

// Legal requirement: invoices must be retained for 10 years even after payment
var retentionCutoff = now.minus(Period.ofYears(10));
```

If you can turn the "why" into a well-named method or constant, do it. The comment only survives when it truly can't be expressed otherwise.

## Checklist

For every comment in the code:

1. **Is it explaining how/what?** → Rename, extract, or restructure until it's redundant, then delete it
2. **Is it separating sections?** → Each section becomes its own method
3. **Is it explaining why?** → Keep it, but try once more to express it in code
4. **Is it a TODO?** → Acceptable as short-lived markers. Handle each TODO before moving to another task, in its own commit
