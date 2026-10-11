# Hexagon Annotations

Custom annotations to decouple from Spring while allowing dependency injection.

## Annotations

- **@DomainService** - Domain components that can be injected
  (Location: `domain/`)
- **@AntiCorruptionLayer** - Right adapters translating between domain and
  external models (Location: `acl/`)
- **@Stub** - Test implementations of SPI interfaces
  (Location: `domain/spi/`)
