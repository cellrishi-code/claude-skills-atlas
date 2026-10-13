---
name: codebase-explorer
category: coding
tags: [codebase, architecture, exploration]
---

# Codebase Explorer

## Purpose

Build a concise evidence-based model of an unfamiliar codebase before editing it.

## When to use

Use when entering an unfamiliar repository or when architecture, entry points, dependencies, conventions, or data flow are unclear.

## Instructions

Inspect relevant documentation, package or build configuration, entry points, directory structure, important modules, tests, and configuration. Then identify the project purpose, main entry points, major components, data/control flow, conventions, relevant files, and unknowns. Do not invent architecture unsupported by repository evidence.

## Inputs

- Repository or relevant source tree
- Requested feature, bug, or investigation

## Outputs

- Repository map
- Entry points and major components
- Relevant data/control flow
- Relevant files and conventions
- Unknowns requiring further inspection

## Example

User: "I just joined this project. Where should I implement authentication?"

Expected behavior: inspect the repository and identify the existing authentication boundary and relevant files before suggesting changes.

## Limitations

Exploration can miss behavior hidden behind generated code, external services, runtime configuration, or undocumented operational systems.