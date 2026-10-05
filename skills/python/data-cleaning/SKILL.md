---
name: data-cleaning
category: python-data-science
tags: [python, pandas, cleaning]
---

# Python Data Cleaning

## Purpose

Clean tabular data reproducibly while preserving important records and making transformations explicit.

## When to use

Use when preparing structured datasets for analysis or machine-learning workflows.

## Instructions

1. Inspect schema, missingness, duplicates, types, ranges, and categorical values.
2. Identify suspicious records before changing data.
3. Define transformations explicitly.
4. Preserve the raw data.
5. Validate row counts and key constraints after major operations.
6. Do not silently drop records or fabricate missing values.
7. Record assumptions and cleaning decisions.

## Inputs

- Tabular dataset
- Cleaning requirements
- Data dictionary or schema, when available

## Outputs

- Cleaned dataset or transformation plan
- Cleaning decisions
- Validation results
- Remaining data-quality issues

## Example

User: "Clean this CSV before training a model."

Expected behavior: inspect the data first, document transformations, and validate the resulting dataset rather than silently deleting problematic rows.

## Limitations

Cleaning rules depend on domain meaning. Automated transformations may remove valid but unusual observations if the context is not understood.