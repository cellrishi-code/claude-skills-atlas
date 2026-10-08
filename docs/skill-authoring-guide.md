\# Skill Authoring Guide



A practical guide to turning a focused task into a reusable skill for Claude Skills Atlas.



A good skill is not simply a long prompt. It is a focused, reusable set of instructions that helps a model perform a specific task consistently across different users and situations.



\## 1. Start with a Focused Task



Begin with a task that has a clear purpose and a useful, repeatable outcome.



A good task should answer:



\- What should the skill help accomplish?

\- Who is likely to use it?

\- What information does it need?

\- What should it produce?

\- Where should the skill stop?



Prefer one coherent task over a collection of loosely related tasks.



\### Good scope



> Review a Python function for correctness, maintainability, and common security issues.



This has a clear input, purpose, and expected outcome.



\### Too broad



> Help with software development.



This covers too many unrelated tasks and does not define a consistent workflow or output.



If a proposed skill covers several substantially different tasks, consider splitting it into smaller skills.



\## 2. Define the Scope and Boundaries



Before writing the instructions, write down the skill's scope.



Identify:



\- \*\*Purpose\*\* â€” the problem the skill solves.

\- \*\*When to use\*\* â€” situations where the skill is appropriate.

\- \*\*When not to use\*\* â€” situations outside its intended scope.

\- \*\*Inputs\*\* â€” information or materials the skill needs.

\- \*\*Outputs\*\* â€” what the user should receive.

\- \*\*Limitations\*\* â€” important constraints, uncertainty, or unsupported cases.



Clear boundaries make a skill easier to reuse and reduce unexpected behavior.



\## 3. Define Inputs and Outputs



Make the expected input explicit.



For example:



```text

Input:

\- Source code

\- Programming language

\- Relevant requirements or constraints

```



Then define the expected output:



```text

Output:

\- Findings grouped by severity

\- Explanation of each finding

\- Suggested improvements

\- Areas requiring human review

```



Avoid assuming information that the user may not provide.



If an input is optional, state that explicitly.



\## 4. Write the Instructions as a Procedure



A reusable skill should explain what to do, not just describe the desired result.



Prefer concrete steps such as:



1\. Inspect the provided input.

2\. Identify the relevant requirements.

3\. Analyze the input against those requirements.

4\. Separate confirmed findings from uncertain observations.

5\. Produce the requested output format.

6\. Identify anything that requires human verification.



Make important constraints explicit.



Avoid instructions such as:



> Do the task really well.



Instead, define what "well" means for the specific task.



\## 5. State Assumptions Explicitly



Skills often fail when they silently assume information that was never provided.



Document assumptions such as:



\- required input formats

\- expected programming language or domain

\- available context

\- required permissions

\- expected output format

\- whether external sources are allowed



If an assumption may not hold, explain how the skill should handle that case.



\## 6. Define Failure Modes



Consider what can go wrong before publishing the skill.



Common failure modes include:



\- required input is missing

\- input is ambiguous

\- input is malformed

\- information is insufficient to reach a conclusion

\- the requested operation is outside the skill's scope

\- the result requires human judgment

\- an external dependency is unavailable



A strong skill tells the model what to do in these situations.



For example:



> If the input does not contain enough information to determine the result, state what is missing instead of inventing a value.



This is generally safer and more reusable than guessing.



\## 7. Include a Realistic Example



Examples should demonstrate how the skill is intended to be used.



A useful example should show:



\- representative input

\- the expected reasoning or procedure

\- representative output



Keep examples realistic and safe.



Do not include:



\- passwords

\- API keys

\- access tokens

\- session cookies

\- private documents

\- personal data



Use placeholders when information is user-specific.



For example:



```text

Repository: {{repository}}

Language: {{language}}

Code to review: {{source\_code}}

```



\## 8. Weak vs Strong Skill



\### Weak



```text

\# Code Review



Review the code carefully and find any problems.

Give useful suggestions.

```



This is too vague. It does not define scope, inputs, outputs, review criteria, or failure handling.



\### Stronger



```text

\# Code Review



\## Purpose



Review source code for correctness, maintainability, clarity, and common security issues.



\## When to use



Use this skill when a developer provides source code and wants a structured review.



\## Inputs



\- Source code

\- Programming language

\- Relevant requirements, when available



\## Instructions



1\. Identify the language and relevant context.

2\. Review the code for correctness and likely defects.

3\. Check maintainability and clarity.

4\. Check for common security concerns relevant to the code.

5\. Separate confirmed problems from potential concerns.

6\. Explain each finding and suggest an appropriate improvement.

7\. State when additional context or human verification is required.



\## Outputs



Return findings with:

\- severity

\- location

\- explanation

\- suggested improvement



\## Limitations



Do not claim that code is secure or correct without sufficient context or testing.

```



The stronger version gives the model a defined task, inputs, procedure, output, and boundaries.



\## 9. Avoid Overly Broad Skills



A skill should solve a recognizable problem.



Before creating one, ask:



> Could this skill be split into two or more independently useful skills?



If yes, consider narrowing the scope.



For example, instead of:



> Software Engineering Assistant



consider separate skills such as:



\- Code Review

\- Debug Systematically

\- Implementation Planning

\- Test and Verify



Focused skills are easier to test, discover, reuse, and maintain.



\## 10. Keep Skills Model-Agnostic



Write instructions around the task rather than around a particular model's branding or interface.



Prefer:



> Analyze the supplied source code and identify likely defects.



Avoid unnecessary assumptions such as:



> Ask Claude Opus to use its advanced reasoning mode to...



The skill should describe the behavior required to complete the task, not depend on a particular model name, interface, or proprietary feature unless that dependency is essential to the skill itself.



\## 11. Follow the Atlas Skill Structure



Skills belong under:



```text

skills/<category>/<name>/SKILL.md

```



A skill should normally contain front matter with:



```yaml

\---

name: example

category: coding

tags: \[example, relevant-tag]

\---

```



The main document should include:



```text

\# Example



\## Purpose



\## When to use



\## Instructions



\## Inputs



\## Outputs



\## Example



\## Limitations

```



Follow the repository's contribution and validation requirements rather than inventing a different structure.



See \[Contributing](../CONTRIBUTING.md) for repository contribution rules.



\## 12. Test Before Submitting



Test the skill's instructions and examples before opening a pull request.



Check that:



\- the instructions are understandable

\- the example is realistic

\- the expected output is achievable

\- edge cases and limitations are clear

\- the skill does not rely on missing information

\- no unsafe or private information is included



See \[Testing Prompts and Skills](testing-prompts-and-skills.md) for the repository's testing guidance.



Also run the repository validator:



```bash

python scripts/validate\_atlas.py

```



If you change repository resources, regenerate the catalog when required:



```bash

python scripts/generate\_catalog.py

```



\## 13. Final Author Checklist



Before submitting a skill, ask:



\- \[ ] Is the task focused and reusable?

\- \[ ] Is the purpose clear?

\- \[ ] Is the intended use clear?

\- \[ ] Are inputs defined?

\- \[ ] Are outputs defined?

\- \[ ] Are assumptions explicit?

\- \[ ] Are failure modes addressed?

\- \[ ] Is there a realistic example?

\- \[ ] Are limitations documented?

\- \[ ] Is the skill narrow enough to avoid overlapping unrelated tasks?

\- \[ ] Is the wording model-agnostic?

\- \[ ] Is sensitive information excluded?

\- \[ ] Has the skill been tested?

\- \[ ] Does the repository validator pass?



A small, focused, tested skill is preferable to a broad skill with unclear behavior.
