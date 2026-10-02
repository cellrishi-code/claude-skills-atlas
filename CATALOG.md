# Resource Catalog

This catalog is the human-readable index of reusable resources in Claude Skills Atlas.

Use it to find a resource by type and domain. Paths are relative to the repository root.

## Skills

| Domain | Resource | Purpose | Path |
|---|---|---|---|
| Coding | Code Review | Review code for correctness, maintainability, security, and clarity | [SKILL.md](skills/coding/code-review/SKILL.md) |
| Coding | Implementation Planner | Inspect a codebase and produce an implementation plan before editing | [SKILL.md](skills/coding/implementation-planner/SKILL.md) |
| Coding | Test and Verify | Inspect changes, run appropriate checks, and report verification honestly | [SKILL.md](skills/coding/test-and-verify/SKILL.md) |
| Coding | Codebase Explorer | Build a concise mental model of an unfamiliar repository | [SKILL.md](skills/coding/codebase-explorer/SKILL.md) |
| Research | Evidence Checker | Check claims against available evidence without fabricating support | [SKILL.md](skills/research/evidence-checker/SKILL.md) |
| Research | Literature Synthesizer | Extract and synthesize themes, methods, findings, and limitations across papers | [SKILL.md](skills/research/literature-synthesizer/SKILL.md) |
| Research | Source Verification | Verify source quality and distinguish evidence from unsupported claims | [SKILL.md](skills/research/source-verification/SKILL.md) |
| Mathematics | Problem Solver | Solve mathematical problems with explicit assumptions, steps, and verification | [SKILL.md](skills/mathematics/problem-solver/SKILL.md) |
| Data | Analysis | Structure reproducible data analysis from schema inspection through uncertainty checks | [SKILL.md](skills/data/analysis/SKILL.md) |
| Writing | Technical Editor | Improve technical writing while preserving meaning and avoiding invented claims | [SKILL.md](skills/writing/technical-editor/SKILL.md) |
| Education | Tutor | Teach progressively with examples, checks for understanding, and practice | [SKILL.md](skills/education/tutor/SKILL.md) |
| Biology | Paper Analysis | Analyze biology papers and extract research-relevant information | [SKILL.md](skills/biology/paper-analysis/SKILL.md) |

## Prompts

| Domain | Resource | Purpose | Path |
|---|---|---|---|
| Coding | Debugging | Diagnose and fix coding failures systematically | [debugging.md](prompts/coding/debugging.md) |
| Coding | Refactor | Guide safe, focused refactoring while preserving behavior | [refactor.md](prompts/coding/refactor.md) |
| Mathematics | Proof Explainer | Explain mathematical proofs clearly and step by step | [proof-explainer.md](prompts/mathematics/proof-explainer.md) |
| Research | Claim Audit | Audit claims against cited or supplied evidence | [claim-audit.md](prompts/research/claim-audit.md) |
| Research | Paper Reading | Read papers systematically from question through limitations | [paper-reading.md](prompts/research/paper-reading.md) |
| Learning | Active Learning | Teach through explanation, questions, feedback, and practice | [active-learning.md](prompts/learning/active-learning.md) |
| Claude Code | Task Breakdown | Break repository tasks into inspect, plan, implement, and verify stages | [task-breakdown.md](prompts/claude-code/task-breakdown.md) |
| Biology | Literature Analysis | Analyze and organize biology literature | [literature-analysis.md](prompts/biology/literature-analysis.md) |
| Research | Literature Review | Structure a research literature review | [literature-review.md](prompts/research/literature-review.md) |

## Workflows

| Domain | Resource | Purpose | Path |
|---|---|---|---|
| Coding | Plan Implement Verify | Move from repository inspection to implementation and verification | [plan-implement-verify.md](workflows/coding/plan-implement-verify.md) |
| Research | Source First Research | Start research from sources and distinguish evidence from inference | [source-first-research.md](workflows/research/source-first-research.md) |
| Research | Literature Review | Repeatable workflow for literature review tasks | [literature-review.md](workflows/research/literature-review.md) |

## Agents

| Domain | Resource | Purpose | Path |
|---|---|---|---|
| Research | Research Assistant | Structured assistance for research tasks | [research-assistant.md](agents/research/research-assistant.md) |

## Templates

| Type | Resource | Purpose | Path |
|---|---|---|---|
| Skills | Skill Template | Starting structure for a new skill | [skill-template.md](templates/skill-template.md) |
| Prompts | Prompt Template | Starting structure for a reusable prompt | [prompt-template.md](templates/prompt-template.md) |

## Adding a resource

When adding a new resource, update this catalog in the same pull request. Keep the description short and describe what the resource actually does.

The catalog is intentionally human-readable. Automated generation can be added later without changing the public format.
