---
name: create-script-flyway
description: |
  Use when creating a new Flyway database migration script.
  
  Invoke when:
  - You need to create a new table for a domain
  - You need to add/modify columns
  - You need to create indexes or constraints
  
  Don't invoke when:
  - Modifying existing data (use repository/DSL instead)
---

# Create Flyway Migration Script

## Determine Migration Number

**CRITICAL:** Version numbers must be unique across ALL migration directories, not just within one folder.

Check existing migrations across **all** directories to find the next available number:

```bash
find src/main/resources/db/migration -name "V*.sql" | grep -oE 'V[0-9]+' | sort -V | tail -1
```

Pattern: **VXXXX** (4 digits, zero-padded)

⚠️ **Common mistake:** Only checking one subdirectory (e.g., supervision/) and incrementing from there, ignoring higher versions in other directories (e.g., monitoring/).

## Migration Location

| Domain | Path |
|--------|------|
| supervision | `src/main/resources/db/migration/supervision/` |
| monitoring | `src/main/resources/db/migration/monitoring/` |

## Naming Convention

Format: `VXXXX__descriptive_name.sql`

- Double underscore after number
- Lowercase with underscores
- Descriptive of the change

Examples:
- `V0012__create_controller_incidents_table.sql`
- `V0005__init_table_incident_battery.sql`

## SQL Template

For new domain tables, follow this pattern (based on battery supervision):

```sql
CREATE SCHEMA IF NOT EXISTS {schemaname};

CREATE TABLE IF NOT EXISTS {schemaname}.incidents (
    id BIGSERIAL PRIMARY KEY,
    mac_address TEXT NOT NULL,
    site_id TEXT NOT NULL,
    status TEXT NOT NULL, -- 'PENDING' or 'SOLVED'
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_incidents_site_status 
    ON {schemaname}.incidents(site_id, status);
```

## Schema Naming

**Rules:**
- No special characters (`_`, `-`) in schema names
- Use camelCase converted to lowercase (e.g., `BatterySupervision` → `batterysupervision`)

**Supervision domain:**
- `alertlifecycleflow`
- `batterysupervision`
- `controllersupervision`

**Monitoring domain:**
- `monitoringconsumption`
