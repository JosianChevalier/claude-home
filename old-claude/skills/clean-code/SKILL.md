---
name: clean-code
description: Use when writing or reviewing code to enforce clean code principles. Ensures code reads like English.
---

# Clean Code

Principles for writing code that reads like prose. Inspired loosely by Object Calisthenics.

## The Prime Directive

**Code should read as close as possible to English.** A reader should understand *what* the code does without deciphering *how*. Each method tells a story at one level of detail.

## Single Layer of Abstraction (SLAP)

The most important rule. Every method must operate at **one consistent level of abstraction**.

```java
// BAD — domain intent buried under technical noise
Report generateReport(List<Order> orders) {
    var active = orders.stream().filter(o -> o.isActive()).collect(toList());
    double total = 0;
    for (var order : active) {
        total += order.price() * order.quantity();
    }
    var formatted = String.format("Total: %.2f", total);
    return new Report(formatted, active.size());
}

// GOOD — reads like English, each line is one domain concept
Report generateReport(List<Order> orders) {
    var activeOrders = removeInactive(orders);
    var total = sumOrderTotals(activeOrders);
    return formatReport(total, activeOrders.size());
}
```

**The test:** read the method aloud. If you hear "stream, filter, collect, for-loop" you're reading implementation. If you hear "remove inactive, sum totals, format report" you're reading intent.

**Smell:** If you need a comment to separate sections within a method, each section should be its own method.

**Anti-pattern: variables as fake abstraction.** Giving a name to an expression does not raise the abstraction level. SLAP means each line in the method operates at the same *domain* level — and the tool for that is **extracting a method**, not naming a variable. The method name describes the concept; the method body hides the mechanism.

```java
// BAD — variables label steps but the method still mixes levels
var validated = input.stream().filter(isValid()).collect(toList());
var sorted = validated.stream().sorted(byPriority()).collect(toList());
return new Report(sorted);

// GOOD — each concept is a method; the method reads as a plan
var validated = removeInvalid(input);
var prioritized = sortByPriority(validated);
return new Report(prioritized);
```

**In functional pipelines too.** When composing via `.map()` on a `Result` or `Stream`, each step should be a named domain concept — not raw lambdas or collector mechanics.

```java
// BAD — pipeline mixes domain steps with plumbing
return toResult(measures)
    .map(m -> computeMissing.fillGaps(m, dimensions, period))
    .map(e -> extrapolate.extrapolate(e))
    .map(w -> distribute.distribute(w, siteConsumption))
    .fold(
        result -> result.stream()
            .collect(groupingBy(Entry::getKey, mapping(Entry::getValue, toSet())))
            .entrySet().stream()
            .map(e -> new RoomResult(e.getKey(), e.getValue()))
            .collect(toSet()),
        _ -> emptySet()
    );

// GOOD — each .map reads as a verb phrase, fold delegates to a named concept
return toResult(measures)
    .map(fillGapsUsing(dimensions, period))
    .map(extrapolate::extrapolate)
    .map(distributeUsing(siteConsumption))
    .fold(groupByRoom::group, noData());
```

`noData()` returns a `Function` that ignores the error and returns an empty set — even error handling reads like a domain concept. Partial application methods (`fillGapsUsing`, `distributeUsing`) capture context and return a `Function` — the pipeline reads like a plan: fill gaps, extrapolate, distribute, group by room.

```java
// BAD - comments revealing hidden methods
void process(SiteId siteId) {
    // Fetch current state
    var alerts = alertRepository.findActive(siteId);
    var devices = deviceRepository.findBySite(siteId);

    // Detect anomalies
    var anomalies = new ArrayList<Anomaly>();
    for (var device : devices) {
        if (device.isUnreachable()) {
            anomalies.add(Anomaly.unreachable(device));
        }
    }

    // Reconcile alerts with anomalies
    for (var alert : alerts) {
        if (anomalies.stream().noneMatch(a -> a.matches(alert))) {
            alert.close();
        }
    }
}

// GOOD - each step is a method, the story is clear
void process(SiteId siteId) {
    var currentAlerts = fetchActiveAlerts(siteId);
    var anomalies = detectAnomalies(siteId);

    reconcile(currentAlerts, anomalies);
}
```

## Small, Focused Methods

Methods should do **one thing**. If you can describe what a method does using "and", it does too much.

Extract until each method name fully describes its content. Method bodies of 1-5 lines are normal and good.

## Naming Is Design

Names should reveal intent and belong to the domain language.

```java
// BAD
void proc(String s, int t) { }
List<Device> getDevices(boolean f) { }
var tmp = computeResult();

// GOOD
void closeResolvedAlerts(SiteId siteId) { }
List<Device> findUnreachableDevices() { }
var dailyConsumption = disaggregateByDay(monthlyTotal);
```

**No abbreviations.** `temperature` not `temp`. `repository` not `repo` (in code, fine in conversation).

## Minimize Indentation

Prefer early returns over nested conditions. Flat code reads easier.

```java
// BAD
void process(Device device) {
    if (device != null) {
        if (device.isActive()) {
            if (device.hasLowBattery()) {
                raiseAlert(device);
            }
        }
    }
}

// GOOD
void process(Device device) {
    if (device == null || !device.isActive()) {
        return;
    }
    if (device.hasLowBattery()) {
        raiseAlert(device);
    }
}
```

## Push Behavior to Objects

Ask objects to do things, don't extract their data to decide for them.

```java
// BAD - asking for data, deciding externally
if (alert.getStatus() == Status.PENDING && alert.getCreatedAt().isBefore(cutoff)) {
    alert.setStatus(Status.EXPIRED);
}

// GOOD - telling the object what to do
alert.expireIfOlderThan(cutoff);
```

## First-Class Collections

When a collection has domain meaning, wrap it. This gives behavior a home.

```java
// Instead of List<Device> with external filtering logic
public record Devices(List<Device> values) {
    public Devices withLowBattery() {
        return new Devices(values.stream()
            .filter(Device::hasLowBattery)
            .toList());
    }
}
```

## Domain Services Are Classes

Domain services are **instantiated classes**, not static utility methods. Static methods are reserved for factory methods and very simple helpers.

A service captures its context (dependencies, configuration) in the constructor and exposes behavior through instance methods. This makes services composable, testable, and injectable.

```java
// BAD - static utility class
public class ComputeMissing {
    public static MeasuresWithGaps<D> fillGaps(Set<MeasuredMeasure<D>> measures, Period period) { ... }
}
// caller: var withGaps = ComputeMissing.fillGaps(measures, period);

// GOOD - instantiated service
@DomainService
public class ComputeMissing<D> implements Function<Set<MeasuredMeasure<D>>, MeasuresWithGaps<D>> {
    private final Period period;

    public ComputeMissing(Period period) { this.period = period; }

    @Override
    public MeasuresWithGaps<D> apply(Set<MeasuredMeasure<D>> measures) { ... }
}
```

**Prioritize this style unless it really adds noise** — a one-line `Math.max()` helper is fine as static.

## Functional Pipeline Composition

When a workflow is a sequence of transformations, compose it as a **functional pipeline** using `.map()` on a monadic type (e.g. `Result`). Each step is a `Function` instance.

```java
// BAD - manual variable wiring with static calls
var translated = ValvePositionsToMeasures.from(measures);
var withGaps = ComputeMissing.fillGaps(translated, period);
var extrapolated = ExtrapolateMissing.from(withGaps, period);
if (extrapolated.isEmpty()) return Set.of();
return distribute(extrapolated, heating);

// GOOD - pipeline reads as a story
translateToMeasures(measures)
    .map(computeMissing)
    .map(extrapolateMissing)
    .map(computeWeights)
    .map(distribute)
    .fold(groupByRoom, noData -> Set.of());
```

Key principles:
- Each brick is a `Function<In, Out>` with context in its constructor
- Use `Result.map()` for error short-circuiting (no early returns)
- Use a mix between functional and OOP approaches :
  - functional in the spirit (pure functions, immutability, pipeline approach)
  - behavior attaches to objects to create DSL. Examples:
    - use monads such as stream/result that compose the functions through .map of .flatMap
    - methods returning a new instance computed from the previous state of the object

**Prefer chaining over unwrapping.** When a type offers `map`/`flatMap`/`orElse`, use the chain instead of unwrapping with `isEmpty` + `get`. Not all wrapper types are chainable (e.g. `OptionalDouble` has no `map`) — for those, imperative style is fine, but extract any non-trivial branch into a named method.

## Higher-Order Functions in Stream Chains

In functional-style stream pipelines, extract inline lambdas to named methods returning `Function` or `Predicate` (partial application). This makes the stream chain read like English.

```java
// BAD - inline lambdas obscure intent
return expectedTimestamps.stream()
    .filter(ts -> !covered.contains(ts))
    .map(ts -> new MissingMeasure<>(ts, dimension));

// GOOD - named higher-order functions
return expectedTimestamps.stream()
    .filter(notCoveredBy(covered))
    .map(asMissing(dimension));

private static Predicate<Instant> notCoveredBy(Set<Instant> covered) {
    return timestamp -> !covered.contains(timestamp);
}

private static <Dimension> Function<Instant, Measure<Dimension>> asMissing(Dimension dimension) {
    return timestamp -> new MissingMeasure<>(timestamp, dimension);
}
```

Each extracted method captures context via its parameters and returns a function that reads as a verb phrase in the pipeline.

## Domain Expressiveness Over Java Convention

When a general Java convention conflicts with the domain model's ability to represent reality, **domain expressiveness wins**. The model must faithfully capture what exists — including absence, partiality, and uncertainty.

```java
// Convention says: don't use Optional in records
// But the domain has partial data — some readings may be missing
// ✅ Domain expressiveness wins
record TimestampReading(Optional<CelsiusDegree> temperature, Optional<CelsiusDegree> setpoint) { }

// ❌ Convention wins, domain suffers — no way to represent "missing"
record TimestampReading(CelsiusDegree temperature, CelsiusDegree setpoint) { }
```

**The test:** does following the convention force you to lose information, add edge cases, or filter upstream? If yes, the convention is wrong *here*.

## Java Preferences

### Static Imports for Factory Methods

Use static imports when the method name alone is sufficient to understand what is being built.

```java
// GOOD - name is self-explanatory, static import
import static SiteId.siteId;
import static Result.success;
import static Result.failure;
import static NonBlankString.nonBlank;
import static java.util.stream.Stream.concat;

var site = siteId("paris");
return success(result);
return failure(error);
return concat(streamA, streamB);

// BAD - generic name, no idea what it builds without the class
import static SiteId.of;
import static Duration.of;
import static Stream.of;
import static Optional.of;

var site = of("paris");  // of what?
var duration = of(5);    // of what?

// GOOD - keep the class qualifier for generic names
var site = SiteId.of("paris");
var duration = Duration.of(5, ChronoUnit.MINUTES);
var stream = Stream.of(a, b);
var opt = Optional.of(value);
```

**Rule of thumb:** read the call site without the class name. If it still makes sense, static import. If not, keep the qualifier.

## Checklist

When writing or reviewing code, verify:

1. **SLAP** - Does each method stay at one abstraction level?
2. **Reads like English** - Can you read the method aloud and it makes sense?
3. **No "how" comments** - See [clean-code:comments](comments/SKILL.md)
4. **Small methods** - Is every method doing exactly one thing?
5. **Meaningful names** - Do names reveal intent without needing context?
6. **Flat structure** - Are early returns used instead of deep nesting?
7. **Behavior on objects** - Is logic pushed into the objects that own the data?
8. **Named lambdas** - Are stream lambdas extracted to higher-order methods?
9. **Services are classes** - Are domain services instantiated, not static utility classes?
10. **Pipelines** - Are multi-step transformations composed via `.map()` with `Function` instances?
