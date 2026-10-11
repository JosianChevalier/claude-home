# Domain Services

## Internal vs Injected Collaborators

**Inject only SPIs** (ports to the outside world).

Domain services that orchestrate a pipeline **own their
collaborators**. Internal bricks are implementation details —
create them as fields, don't inject them.

```java
// GOOD — internal orchestration, hidden implementation
public class DisaggregatedConsumption {
    private final ComputeMissing computeMissing = new ComputeMissing();
    private final Distribute distribute = new Distribute();
}

// BAD — leaking internal structure through constructor
public class DisaggregatedConsumption {
    public DisaggregatedConsumption(ComputeMissing cm, Distribute d) { }
}
```
