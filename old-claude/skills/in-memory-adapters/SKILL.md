---
name: in-memory-adapters
description: Use when implementing a new SPI interface or needing a first working adapter for domain development.
---

# In-Memory Adapters

In-memory implementations of SPI interfaces that **behave like real systems** — not empty stubs.

## Why

Develop domain logic first without coupling to databases, HTTP clients, or messaging. An in-memory adapter lets you design, test, and iterate on the domain contract before writing any technical code.

Typically temporary — replaced with persistent or remote adapters when the domain is stable.

## Behavior, Not Stubs

An in-memory adapter must behave correctly:
- A repository stores and retrieves data using a `List` or `Map` — like a real database
- A finder returns consistent results across calls
- Constraints are enforced (uniqueness, not-found cases)

```java
public class InMemoryAlertRepository implements AlertRepository {
    private final List<Alert> alerts = new ArrayList<>();

    @Override
    public void save(Alert alert) {
        alerts.add(alert);
    }

    @Override
    public List<Alert> findBySite(SiteId siteId) {
        return alerts.stream()
            .filter(a -> a.siteId().equals(siteId))
            .toList();
    }
}
```

## Examples

| Real adapter | In-memory alternative |
|---|---|
| PostgreSQL repository (jOOQ) | `ArrayList` / `HashMap` storage |
| HTTP client to external API | Static or configurable responses |
| Message publisher (RabbitMQ) | Collected messages in a `List` |

## Location

`infra/rightadapter/inmemory/` — these are **production adapters** (temporary or permanent). Test-only stubs live in `domain/spi/` with `@Stub`.
