---
name: experiment-analysis
category: machine-learning
tags: [experiments, reproducibility, tracking]
---

# ML Experiment Analysis

## Purpose

Analyze and compare machine-learning experiments in a reproducible way while distinguishing observed results from hypotheses about why they occurred.

## When to use

Use this skill when comparing model runs, investigating experiment results, documenting reproducibility, or identifying factors that may explain performance differences.

## Instructions

1. Record the dataset and version, preprocessing, random seed, model configuration, training procedure, metrics, and evaluation split.
2. Compare experiments using the same evaluation protocol whenever possible.
3. Distinguish observed results from hypotheses about their causes.
4. Preserve failed experiments when they contain useful evidence.
5. Check for data leakage, inconsistent metric definitions, and changes in evaluation methodology.
6. Consider whether observed improvements exceed expected experimental variance.

## Inputs

- Experiment runs and their recorded results
- Dataset and preprocessing details
- Model and training configuration
- Evaluation protocol and metrics
- Random seeds or other reproducibility information

## Outputs

- Structured comparison of experiments
- Reproducibility assessment
- Evidence-based interpretation of results
- Potential explanations clearly separated from observations
- Identified risks, inconsistencies, and follow-up experiments

## Example

User: "Why did experiment B outperform experiment A?"

Expected behavior: compare their datasets, preprocessing, configurations, training procedures, metrics, and evaluation splits; identify measurable differences first; then present plausible explanations separately from established facts.

## Limitations

Experiment comparisons can be misleading when datasets, evaluation protocols, random seeds, or training conditions differ. Correlation between a configuration change and an observed improvement does not by itself establish causation.
