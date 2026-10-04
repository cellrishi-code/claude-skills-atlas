---
name: test-and-verify
category: coding
tags: [testing, verification, regression]
---

# Test and Verify

## Purpose

Systematically verify a coding change through tests, regression checks, and relevant quality checks.

## When to use

Use after implementing code or when determining whether a completed change is safe to submit.

## Instructions

1. Inspect the diff and identify changed behavior.
2. Find existing tests and add focused tests when appropriate.
3. Run the narrowest useful test first.
4. Run broader checks when relevant.
5. Inspect failures instead of weakening tests.
6. Check formatting, linting, types, and builds when applicable.
7. Report exactly what ran and what did not.
8. Never claim a test passed unless it actually ran successfully.

## Inputs

- Code changes
- Existing tests
- Expected behavior and verification requirements

## Outputs

- Verification results
- Tests and checks executed
- Failures and remaining risks

## Example

User: "Verify this parser change before I open a PR."

Expected behavior: inspect the diff, run focused parser tests, then report results and any remaining risks.

## Limitations

Passing tests cannot guarantee correctness for all inputs or production environments.