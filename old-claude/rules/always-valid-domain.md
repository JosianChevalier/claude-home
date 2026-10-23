# Always Valid Domain Model

**TL;DR:** An invalid state should not be possible to represent. The very structure of
the model should make it impossible to represent a state that is not valid.

## Core Principle

Design types so that **invalid states cannot be represented**. The compiler and type system
should prevent invalid state, not runtime checks.

## Techniques

### 1. Sealed Classes for State Machines

Use sealed classes/interfaces to constrain valid states.

```java
// Order with two valid states only
public sealed interface Order permits PendingOrder, ShippedOrder { }

public final class PendingOrder implements Order {
    private final Instant placedDate;
    // No shippedDate field - doesn't exist in this state

    public ShippedOrder ship(Instant shippedAt) {
        return ShippedOrder.from(this, shippedAt);
    }
}

public final class ShippedOrder implements Order {
    private final Instant placedDate;
    private final Instant shippedDate;  // Always present, never null
    // No ship() method - already shipped
}
```

### 2. Value Objects with Validation

Wrap primitives to prevent invalid values.

```java
public record StockQuantity(int units) {
    public StockQuantity {
        if (units < 0) {
            throw new IllegalArgumentException("Stock quantity must not be negative");
        }
    }
    public boolean isLow() { return units <= 10; }
}
```

## Anti-Patterns

```java
// ❌ Status flags - invalid combinations possible
private boolean pending, shipped, delivered;

// ❌ Nullable fields for state - allows invalid mutations
private @Nullable Instant shippedDate;
public void ship(Instant when) { this.shippedDate = when; }

// ❌ Public setters - arbitrary state changes
public void setStatus(OrderStatus status) { this.status = status; }

// ✓ Type-based states prevent invalid operations
public void deliver(ShippedOrder order) { } // Must be shipped
```

### 3. If It Can Be Represented, Assume It Will Happen

If a data structure *can* represent an invalid state, code will eventually encounter it. Don't rely on implicit assumptions (matching sizes, consistent ordering, all fields populated together) — make the valid structure explicit.

```java
// ❌ Parallel lists — nothing enforces same size or alignment
record Order(List<Product> products, List<Integer> quantities) { }

// ✅ Single composite — alignment is structural
record OrderLine(Product product, int quantity) { }
record Order(List<OrderLine> lines) { }
```

### 4. No Unpacking Value Objects in Domain Code

Domain code must **never extract primitives** from value objects to pass to other domain
collaborators. If a collaborator takes a primitive where a value object exists, the
collaborator's API is wrong — fix the API first.

```java
// ❌ Unpacking to satisfy a primitive API
service.compute(amount.value(), distance.value());

// ✓ Collaborator accepts value objects directly
service.compute(amount, distance);
```

When you encounter a primitive-based domain API, **stop and challenge the design** before
adapting to it. The existing API may predate the value object.

### 5. One Handle for Multi-Object State

When an invariant spans several objects, expose a single root; interior state is reachable
only through it, so no external path can break the invariant.

```java
// ❌ Interior mutable from anywhere — total/lines agreement unenforceable
order.getLines().add(line);

// ✓ Root is the sole handle — invariant holds by construction
order.addLine(product, quantity);
```

Rationale: [[philosophy/always-valid-domain]]
