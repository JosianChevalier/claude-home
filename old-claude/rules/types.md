# Type Usage Rules

## Null Safety

**Avoid null values.** Model invalid states as impossible to represent (see [always-valid-domain.md](always-valid-domain.md)).

When nullability cannot be avoided:
- **Return values:** Use `Optional<T>`
- **Fields/parameters:** Use `@Nullable` from `org.jspecify.annotations`

## Records

Use records for immutable data (DTOs, value objects).

## Type Inference (var)

Use `var` for local variables when the type is obvious.

```java
var records = repository.findAll();  // Good - clear type
ProcessingResult result = process(); // Better when type unclear
```

Don't use `var` for fields, parameters, or with unclear types.

## Static Methods

Static methods are reserved for **factory methods** and **very simple helpers**.

Domain services with logic should be **instantiated classes** (see clean-code skill).
