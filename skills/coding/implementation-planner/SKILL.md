---
name: implementation-planner
category: coding
tags: [planning, implementation, architecture]
---

# Implementation Planner

## Purpose

Turn a coding request into a concrete implementation plan before changes are made.

## When to use

Use when a coding task is large enough to require repository inspection, affected files, risks, and verification.

## Instructions

1. Inspect repository structure and relevant configuration.
2. Identify the smallest set of files likely to change.
3. Trace existing patterns before proposing abstractions.
4. State assumptions explicitly.
5. Produce the objective, relevant architecture, files, implementation steps, risks, and verification plan.
6. Ask focused questions when critical information is missing.
7. Do not modify files unless implementation is explicitly requested.

## Inputs

- Coding task
- Repository context
- Constraints or acceptance criteria

## Outputs

- Concrete implementation plan
- Affected files
- Risks and edge cases
- Verification plan

## Example

User: "Plan the implementation of authentication for this API."

Expected behavior: inspect the existing architecture and produce a focused file-by-file plan without changing code.

## Limitations

A plan may need revision when hidden requirements, runtime behavior, or external dependencies are discovered.