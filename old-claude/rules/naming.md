# Naming Conventions

## Case

Respect Java conventions.

## Classes

### Domain layers

- Entities and Value Object: names representative of the domain concept being represented
- Services and SPIs: 
  - ideally the domain concept represented by the action
    - ex: PhoneNumberRepository -> PhoneBook, TemperatureSetter -> Thermostat
  - else a name reflecting the pattern employed or the action
    - ex: SiteRepository, GasConsumptionDisaggregator

## Methods

Use descriptive verbs that clearly indicate what the method does.

```java
// Good
public void checkThermostats() { }
public boolean isValid() { }
public Optional<Alert> findActiveAlert() { }

```

Use `fetch` rather than get to imply remote access to a data

## Generic Type Parameters

Use explicit, domain-meaningful names **at the declaration site**
(where the type parameter is first introduced). Downstream classes
that just propagate the parameter can use a short form.

```java
// BAD — declaration site uses opaque letter
public sealed interface Measure<T> { }

// GOOD — declaration site names the concept
public sealed interface Measure<Dimension> { }
public record WeightedEntry<Room>(Room key, double weight) { }

// GOOD — downstream class propagates, short form is fine
public class ExtrapolateMissing {
    public <D> ExtrapolatedMeasures<D> extrapolate(MeasuresWithGaps<D> input) { }
}
```

## Constants

**UPPER_SNAKE_CASE** - All caps with underscores

```java
public static final int MAX_TEMPERATURE = 30;
public static final String DEFAULT_ALERT_TYPE = "TEMPERATURE";
```
