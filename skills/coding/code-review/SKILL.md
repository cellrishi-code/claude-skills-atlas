---
name: code-review
category: coding
tags: [code-review, software-engineering, debugging]
recommendation_use_cases: [review source code, identify bugs, assess maintainability, assess security and clarity]
recommendation_audience: [software developers, software engineers]
recommendation_domain: software-engineering
recommendation_prerequisites: [source code to review]
recommendation_related_skills: [coding/debug-systematically, coding/implementation-review]
---

# Code Review Skill

## Purpose

Review source code for correctness, bugs, maintainability, security concerns, and clarity without rewriting the entire project unless asked.

## When to use

Use this skill when a user provides code and asks for a review, bug hunt, logic check, or improvement suggestions.

## Instructions

1. Identify the language and relevant context from the supplied code.
2. Look for correctness issues first.
3. Separate definite bugs from style suggestions and uncertain concerns.
4. Explain each important finding with a concise reason and, when useful, a minimal corrected example.
5. Preserve the user's intended behavior unless they ask for a redesign.
6. Never claim code was executed unless it was actually executed.
7. For security-sensitive code, call out security implications explicitly.

## Inputs

- Source code
- Language and runtime, when known
- Intended behavior
- Error messages or tests, when available

## Outputs

- Findings ordered by impact
- Explanation of each finding
- Minimal fixes or next steps
- Remaining uncertainty, when relevant

## Example

User: "Check whether this C++ binary-search implementation is correct."

Expected behavior: identify concrete boundary/loop bugs, explain why they occur, and show the smallest useful correction.

## Limitations

Static review cannot prove that a program is correct for every input. Runtime tests and domain-specific validation may still be required.
