---
name: debug-systematically
category: coding
tags: [debugging, diagnosis, failures]
---

# Debug Systematically

## Purpose

Diagnose software failures using evidence and hypothesis elimination rather than guessing.

## When to use

Use for bugs, failing tests, unexpected output, crashes, regressions, or inconsistent behavior.

## Instructions

1. Reproduce the failure when possible.
2. Capture the exact error, input, environment, and expected behavior.
3. Minimize the failing case.
4. Trace backward from the observable failure to the earliest incorrect state.
5. Generate competing hypotheses.
6. Test the cheapest distinguishing hypothesis.
7. Apply the smallest correct fix.
8. Re-run the original reproduction and regression tests.
9. Explain the root cause.
10. If the cause cannot be established, label it unresolved.

## Inputs

- Error or unexpected behavior
- Reproduction steps or failing input
- Expected behavior
- Relevant code and environment

## Outputs

- Reproduction
- Root cause or remaining uncertainty
- Minimal fix
- Verification results

## Example

User: "This test fails only when the input is empty."

Expected behavior: isolate the empty-input case, trace the first invalid state, fix it, and rerun the relevant tests.

## Limitations

Intermittent or environment-dependent failures may require logs, instrumentation, or access to the runtime environment.