---
name: api-design
category: web-development
tags: [api, backend, http]
---

# API Design

## Purpose

Design a maintainable HTTP API with explicit resources, contracts, validation, and failure behavior.

## When to use

Use when designing a new API or changing an existing API contract.

## Instructions

1. Identify resources and operations.
2. Define request and response shapes.
3. Specify validation and error semantics.
4. Consider authentication and authorization boundaries.
5. Define pagination, filtering, idempotency, and versioning only when needed.
6. Add examples and verification cases.
7. Prefer consistency with the existing service.
8. Never invent undocumented external behavior.

## Inputs

- API requirements
- Existing service conventions
- Resource and operation definitions
- Security and compatibility constraints

## Outputs

- API contract
- Request and response shapes
- Validation and error semantics
- Examples and verification cases

## Example

User: "Design endpoints for creating and listing projects."

Expected behavior: define resource-oriented endpoints, schemas, validation, errors, and pagination only where needed.

## Limitations

API design cannot guarantee compatibility with clients or infrastructure that has not been inspected.