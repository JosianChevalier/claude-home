# No Mockito Rule

**Applies to:** All test code in the project

## Rule

**Do NOT use Mockito (or any mocking framework) in tests.**

Use in-memory implementations, stubs, or real objects instead.

## Why

Mockito encourages testing mock behavior rather than real component behavior. This leads to:
- Tests that verify mock interactions instead of observable outcomes
- Brittle tests that break when implementation changes
- False confidence in test coverage
- Obscured test intent with complex mock setup

## Preferred Approach

### Use In-Memory Implementations

```java
// ✅ GOOD: InMemorySiteInventory behaves like real storage
private InMemorySiteInventory siteInventory = new InMemorySiteInventory();
```

### Use Test Stubs with Real State

```java
// ✅ GOOD: Stub with real behavior
@Stub
class StubAlertRepository implements AlertRepository {
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

## What to Do When You Need a Dependency

1. **Check for existing in-memory implementations** in `src/test/java/.../domain/spi/`
2. **Create an in-memory stub** if one doesn't exist
3. **Use the real implementation** if it's fast and has no external dependencies

## Enforcement

- No `org.mockito` imports in test files
- No `mock()`, `when()`, `verify()` calls
- Constructor injection of real or stub implementations only

## Exceptions

None. If you think you need Mockito, reconsider the design or ask for help finding an alternative approach.
