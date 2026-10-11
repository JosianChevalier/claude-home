# Factory Methods for Instantiation

In aggregate roots, use private constructors with distinct factory methods to clarify instantiation intent.

## Rules

- Constructors are `private` - only factory methods create instances
- **Domain creation**: Static factory methods with domain-meaningful names (e.g., `raiseFrom`, `createFor`)
- **Hydration**: Static `from()` or `reconstitute()` for loading from storage
- **State transitions**: Instance methods returning new state objects (e.g., `solve()`, `close()`)

## Example

```java
public final class PendingAlert implements Alert {
    private final AlertId id;
    private final Instant raisedDate;

    private PendingAlert(AlertId id, Instant raisedDate) {
        this.id = requireNonNull(id);
        this.raisedDate = requireNonNull(raisedDate);
    }

    // Domain creation - meaningful name
    public static PendingAlert raiseFrom(AlertTrigger trigger, Instant at) {
        return new PendingAlert(AlertId.random(), at);
    }

    // Hydration - generic name for reconstruction
    public static PendingAlert from(AlertId id, Instant raisedDate) {
        return new PendingAlert(id, raisedDate);
    }

    // State transition - returns new type
    public SolvedAlert solve(Instant solvedAt) {
        return SolvedAlert.from(this, solvedAt);
    }
}
```
