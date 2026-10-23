# Factory Methods for Instantiation

In aggregate roots, use private constructors with distinct factory methods to clarify instantiation intent.

## Rules

- Constructors are `private` - only factory methods create instances
- **Domain creation**: Static factory methods with domain-meaningful names (e.g., `placeFrom`, `createFor`)
- **Hydration**: Static `from()` or `reconstitute()` for loading from storage
- **State transitions**: Instance methods returning new state objects (e.g., `ship()`, `cancel()`)

## Example

```java
public final class PendingOrder implements Order {
    private final OrderId id;
    private final Instant placedDate;

    private PendingOrder(OrderId id, Instant placedDate) {
        this.id = requireNonNull(id);
        this.placedDate = requireNonNull(placedDate);
    }

    // Domain creation - meaningful name
    public static PendingOrder placeFrom(Cart cart, Instant at) {
        return new PendingOrder(OrderId.random(), at);
    }

    // Hydration - generic name for reconstruction
    public static PendingOrder from(OrderId id, Instant placedDate) {
        return new PendingOrder(id, placedDate);
    }

    // State transition - returns new type
    public ShippedOrder ship(Instant shippedAt) {
        return ShippedOrder.from(this, shippedAt);
    }
}
```
