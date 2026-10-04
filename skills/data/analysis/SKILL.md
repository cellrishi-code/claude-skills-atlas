---
name: data-analysis
category: data
tags: [analysis, statistics, visualization]
---

# Data Analysis

## Purpose

Analyze datasets and produce reproducible findings, tables, visualizations, or statistical conclusions.

## When to use

Use when a dataset needs structured exploratory, statistical, or confirmatory analysis.

## Instructions

1. Inspect schema, types, missingness, duplicates, and suspicious values.
2. Clarify the analytical question.
3. Define transformations explicitly.
4. Choose methods appropriate to the data and question.
5. Separate exploratory findings from confirmatory claims.
6. Quantify uncertainty where appropriate.
7. Produce clear tables or visualizations with labels.
8. Check leakage, selection bias, confounding, and assumptions when relevant.
9. Make the analysis reproducible.
10. State limitations.
11. Never invent observations or claim a computation was performed when it was not.

## Inputs

- Dataset
- Analytical question
- Relevant assumptions and constraints

## Outputs

- Reproducible analysis
- Findings and uncertainty
- Tables or visualizations
- Assumption and limitation assessment

## Example

User: "Analyze this dataset for differences between two groups."

Expected behavior: inspect the data, select an appropriate method, report uncertainty, and distinguish observed results from interpretation.

## Limitations

Statistical conclusions depend on data quality, sampling, assumptions, and method choice. Analysis alone cannot eliminate confounding or sampling bias.