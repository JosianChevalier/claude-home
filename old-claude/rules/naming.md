# Naming Conventions

## Case

Respect Java conventions.

## Classes

### Domain layers

- Entities and Value Object: names representative of the domain concept being represented
- Services and SPIs: 
  - ideally the domain concept represented by the action
    - ex: PhoneNumberRepository -> PhoneBook, ProductRepository -> Catalog
  - else a name reflecting the pattern employed or the action
    - ex: CustomerRepository, StorageCostAllocator

## Methods

Use descriptive verbs that clearly indicate what the method does.

```java
// Good
public void checkStockLevels() { }
public boolean isValid() { }
public Optional<Order> findPendingOrder() { }

```

Use `fetch` rather than get to imply remote access to a data

## Generic Type Parameters

Use explicit, domain-meaningful names **at the declaration site**
(where the type parameter is first introduced). Downstream classes
that just propagate the parameter can use a short form.

```java
// BAD — declaration site uses opaque letter
public sealed interface StockLevel<T> { }

// GOOD — declaration site names the concept
public sealed interface StockLevel<Unit> { }
public record WeightedEntry<Product>(Product key, double weight) { }

// GOOD — downstream class propagates, short form is fine
public class ExtrapolateMissing {
    public <U> ExtrapolatedStockLevels<U> extrapolate(StockLevelsWithGaps<U> input) { }
}
```

## Constants

**UPPER_SNAKE_CASE** - All caps with underscores

```java
public static final int MAX_ITEMS_PER_CART = 30;
public static final String DEFAULT_SHIPPING_METHOD = "STANDARD";
```
