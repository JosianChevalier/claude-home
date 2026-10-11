# Immutability

Domain objects are **immutable**: `final` fields, no setters, private constructors with factory methods.

## Rules

- All fields must be `final`
- No setters or methods that mutate state
- When state changes, return a new object instead of mutating the current one

## Example

```java
public record Temperature(double celsius) {
    public Temperature offset(double delta) {
        return new Temperature(celsius + delta);  // New instance, never mutate
    }
}
```

For sealed class state transitions (returning a different type), see `always-valid-domain.md`.
