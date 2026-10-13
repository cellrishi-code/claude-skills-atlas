---
name: implementation-review
category: coding
tags: [review, correctness, maintainability]
---

# Implementation Review

## Purpose

Review completed implementation work against requirements, repository conventions, correctness risks, tests, and maintainability.

## When to use

Use before opening a pull request or when reviewing completed coding work.

## Instructions

1. Read the task or acceptance criteria.
2. Inspect the diff and changed files.
3. Trace changed behavior through callers and dependencies.
4. Check correctness, edge cases, error handling, compatibility, security, and regression risk.
5. Compare the implementation with repository conventions.
6. Inspect focused tests and documentation.
7. Separate blocking issues from suggestions.
8. Do not request speculative abstractions without demonstrated need.

## Inputs

- Task or acceptance criteria
- Implementation or diff
- Relevant tests and repository context

## Outputs

- Verdict: ready or needs changes
- Blocking and non-blocking findings
- Missing tests or documentation
- Suggested verification commands

## Example

User: "Review this PR before I submit it."

Expected behavior: inspect the changes against requirements and identify concrete risks with actionable fixes.

## Limitations

Static review cannot prove complete correctness. Runtime behavior and environment-specific issues may require actual testing.