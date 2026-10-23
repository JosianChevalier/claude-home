# Exception Strategy

## Heuristic

| Situation | Mechanism |
|---|---|
| Caller must react (retry, fallback, degrade) | **Checked exception** or **`Result<T, E>`** |
| Nothing to do — let the left adapter return 500 | **Unchecked exception** |

If you need to catch it, make it visible in the type system. If you don't, let it propagate.

## SPI Boundaries

SPIs that can fail (network, database, external services) **must declare their failure mode** — a checked exception or a `Result` return type. The domain should never `catch (Exception e)` blindly; it should catch the SPI-specific failure.

```java
// GOOD — SPI declares what can go wrong
public interface ProductCatalog {
    List<Product> fetchAll() throws ProductCatalogUnavailable;
}

// BAD — domain catches everything, doesn't know what failed
try { catalog.fetchAll(); }
catch (Exception e) { /* what is this? */ }
```

## Domain

The domain **does not catch unchecked exceptions**. If an unchecked exception reaches the domain, it's a bug — let it propagate to the left adapter.

## Left Adapters

Controllers and message listeners catch unchecked exceptions at the boundary and translate them to appropriate responses (HTTP 500, NACK, etc.).
