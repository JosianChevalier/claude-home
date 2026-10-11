---
name: logging
description: Use when adding, reviewing, or choosing log levels. Defines the project's logging policy and cost implications.
---

# Logging Policy

## Log Levels

### DEBUG

Temporary or detailed info useful during development. Typically used when deploying a new flow to validate behavior before wiring to a front-end or other consumer. Not shipped to Datadog.

### INFO

First level that reaches **Datadog**, which costs money. Only log what provides legitimate operational visibility: key lifecycle events, supervision results, meaningful state transitions.

### WARN

Important impacting errors. Triggers **Slack alerting**. Use for degraded behavior that the team should be aware of during business hours: failed external calls, partial data, retries exhausted.

### ERROR

Unrecoverable failures: the server is dead, no other instance can come back. Triggers **on-call developer paging** (even at night). Reserve for catastrophic situations only. When in doubt, use WARN.

## Decision Guide

| Question | Level |
|---|---|
| Is it only useful while developing a feature? | DEBUG |
| Does the team need ongoing visibility? | INFO |
| Is something broken but the system keeps running? | WARN |
| Is the service completely down with no recovery? | ERROR |
