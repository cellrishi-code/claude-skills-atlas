---
name: skill-author
category: claude
tags: [skills, prompting, agent-design]
---

# Skill Author

## Purpose

Design or improve reusable agent skills with precise activation criteria, focused instructions, examples, verification, and safe boundaries.

## When to use

Use when creating or refactoring a reusable SKILL.md for an agent workflow.

## Instructions

1. Define one clear job for the skill.
2. Write activation criteria that state when it should be used.
3. Keep instructions focused on behavior.
4. Separate required steps from optional guidance.
5. Include failure conditions and safety boundaries.
6. Add examples that clarify expected behavior.
7. Define verification that can expose common failures.
8. Keep large reference material outside the main skill.
9. Test representative tasks.
10. Check for duplication with existing Atlas resources.

## Inputs

- Skill goal
- Activation context
- Expected inputs and outputs
- Safety and verification requirements

## Outputs

- Skill purpose and activation criteria
- Instructions
- Examples
- Verification plan
- Known limitations

## Example

User: "Create a skill that reviews pull requests for security issues."

Expected behavior: define when it activates, what it checks, what it returns, and what it must not claim.

## Limitations

A skill is only as reliable as its instructions, context, and verification. It cannot guarantee correct behavior on every task.