---
name: codebase-understanding
category: coding
tags: [codebase, architecture, dependencies]
---

# Codebase Understanding

## Purpose

Build a reliable mental model of an unfamiliar repository before proposing or implementing changes.

## When to use

Use when entering a new codebase, investigating architecture, or deciding where a feature belongs.

## Instructions

1. Identify entry points, package/build files, configuration, tests, and documentation.
2. Map the relevant directory structure.
3. Trace the execution path for the requested feature or bug.
4. Identify data models, interfaces, dependencies, and integration boundaries.
5. Search for existing implementations before proposing new ones.
6. Record constraints, conventions, and regression points.
7. Distinguish observed facts from hypotheses.

## Inputs

- Repository or relevant files
- Requested feature or bug
- Existing documentation and tests

## Outputs

- Repository map
- Relevant execution/data flow
- Existing patterns to reuse
- Constraints and risks
- Proposed change locations
- Verification plan

## Example

User: "Where does this repository handle database connections?"

Expected behavior: trace configuration and call sites to identify the existing database boundary instead of guessing from directory names.

## Limitations

Repository inspection may not reveal runtime behavior controlled by external services, deployment configuration, or undocumented conventions.