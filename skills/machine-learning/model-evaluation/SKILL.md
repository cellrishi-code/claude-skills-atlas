---
name: model-evaluation
category: machine-learning
tags: [evaluation, metrics, experiments]
---

# Model Evaluation

## Purpose

Evaluate machine-learning models using appropriate metrics, validation strategies, and error analysis rather than relying on a single performance measure.

## When to use

Use this skill when comparing model performance, selecting evaluation metrics, assessing generalization, or preparing an evaluation report.

## Instructions

1. Identify the task type, target variable, and relevant evaluation objective.
2. Establish an appropriate baseline for comparison.
3. Select metrics that match the task and decision costs.
4. Keep training, validation, and test evidence clearly separated.
5. Inspect errors and subgroup performance when relevant.
6. Check calibration when probabilistic predictions are used.
7. Report uncertainty and important evaluation assumptions.
8. Check for data leakage and avoid repeated use of the test set.
9. Never fabricate performance numbers or claim results that were not observed.

## Inputs

- Model or models to evaluate
- Evaluation dataset or test split
- Task type and target variable
- Relevant metrics or decision criteria, when specified
- Baseline results, when available

## Outputs

- Selected evaluation metrics
- Baseline comparison
- Error and subgroup analysis, when applicable
- Validation and test-set assessment
- Limitations and uncertainty

## Example

User: "Compare two binary classifiers and determine which is better for a dataset with imbalanced classes."

Expected behavior: evaluate both models with appropriate metrics such as precision, recall, F1, and ROC-AUC or PR-AUC as appropriate, compare them against the same evaluation protocol, and explain important error trade-offs.

## Limitations

Evaluation results depend on dataset quality, sampling, metric choice, and the evaluation protocol. A test result does not guarantee performance in every deployment setting, and domain-specific validation may still be required.
