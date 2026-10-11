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
// Alert with two valid states only
public sealed interface Alert permits PendingAlert, SolvedAlert { }

public final class PendingAlert implements Alert {
    private final Instant raisedDate;
    // No solvedDate field - doesn't exist in this state

    public SolvedAlert solve(Instant solvedAt) {
        return SolvedAlert.from(this, solvedAt);
    }
}

public final class SolvedAlert implements Alert {
    private final Instant raisedDate;
    private final Instant solvedDate;  // Always present, never null
    // No solve() method - already solved
}
```

### 2. Value Objects with Validation

Wrap primitives to prevent invalid values.

```java
public record BatteryLevel(double value) {
    public BatteryLevel {
        if (value < 0 || value > 100) {
            throw new IllegalArgumentException("Battery level must be 0-100");
        }
    }
    public boolean isLow() { return value <= 10; }
}
```

## Anti-Patterns

```java
// ❌ Status flags - invalid combinations possible
private boolean pending, solved, closed;

// ❌ Nullable fields for state - allows invalid mutations
private @Nullable Instant solvedDate;
public void solve(Instant when) { this.solvedDate = when; }

// ❌ Public setters - arbitrary state changes
public void setStatus(IncidentStatus status) { this.status = status; }

// ✓ Type-based states prevent invalid operations
public void closeAlert(SolvedAlert alert) { } // Must be solved
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

Rationale: @rationale/aggregates.md
