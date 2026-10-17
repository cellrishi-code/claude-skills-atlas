---
name: open-source-contribution
category: coding
tags: [open-source, github, pull-request, contribution, maintainers]
---

# Open Source Contribution

## Purpose

Turn a real open-source task into a focused, reviewable contribution. Use this skill to inspect a repository, identify a concrete change, implement the smallest useful fix, and prepare a clear pull request without inventing requirements.

## When to use

Use this skill when a user wants to contribute to an existing open-source repository, fix an issue, improve documentation, add a small feature, or prepare a pull request.

## Instructions

1. Identify the target repository, issue, or requested improvement.
2. Read the repository's contribution guide, relevant documentation, and nearby code before changing anything.
3. Search existing issues, pull requests, and code for duplicates or related work.
4. Confirm the intended behavior from the issue or repository conventions before implementation.
5. Prefer a small, focused change over a broad refactor.
6. Preserve existing APIs and project conventions unless the task explicitly requires a change.
7. Add or update tests when the change has testable behavior.
8. Run the most relevant available checks and report exactly what was run and what passed or failed.
9. Review the final diff for unrelated changes, generated files, secrets, and accidental formatting churn.
10. Write a pull request description that explains:
   - the problem
   - the change
   - verification performed
   - any limitations or follow-up work
11. Never claim an issue is fixed, tests pass, or behavior is verified unless that was actually established.
12. If requirements are ambiguous or the change could break compatibility, stop and ask a focused question rather than guessing.

## Inputs

- Repository URL or owner/name
- Issue, bug report, feature request, or contribution goal
- Relevant language/runtime
- Existing tests or reproduction steps, when available
- Project contribution rules

## Outputs

- A focused implementation or documentation change
- Relevant tests or verification results
- A concise diff summary
- A pull request title and description
- Remaining risks or limitations

## Example

User: "Find a beginner-friendly issue in a Rust repository and prepare a PR."

Expected behavior: inspect the repository and contribution rules, locate a concrete non-duplicate issue, make the smallest appropriate Rust change, run the project's relevant checks, and prepare a PR description that accurately reports the verification.

## Limitations

Repository access, permissions, CI availability, and maintainer decisions can prevent a contribution from being completed. Static inspection alone cannot establish runtime correctness.
