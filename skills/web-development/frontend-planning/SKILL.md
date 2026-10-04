---
name: frontend-planning
category: web-development
tags: [frontend, architecture, accessibility]
---

# Frontend Planning

## Purpose

Plan a frontend feature with clear user flows, component boundaries, states, accessibility requirements, and verification criteria.

## When to use

Use before implementing a frontend feature or when an existing UI needs structured planning.

## Instructions

1. Identify user flows and required states.
2. Inspect existing components and styling conventions.
3. Define data flow and API dependencies.
4. Account for loading, empty, error, keyboard, and responsive states.
5. Include accessibility requirements.
6. Define verification criteria before implementation.
7. Do not invent APIs or framework conventions not present in the project.

## Inputs

- Feature requirements
- Existing frontend code and conventions
- API or data dependencies
- Accessibility and responsive constraints

## Outputs

- Affected files
- Component structure
- State model
- Accessibility checks
- Verification steps

## Example

User: "Plan a dashboard page for this existing React app."

Expected behavior: inspect current components and plan the dashboard using established project patterns.

## Limitations

Planning cannot fully predict browser-specific behavior or APIs that are not yet implemented.