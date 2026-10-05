---
name: bioinformatics-planning
category: biology
tags: [bioinformatics, genomics, pipelines]
---

# Bioinformatics Workflow Planning

## Purpose

Plan reproducible bioinformatics workflows with explicit inputs, reference versions, quality controls, tools, and outputs.

## When to use

Use when designing or documenting a genomics, transcriptomics, sequence-analysis, or related bioinformatics pipeline.

## Instructions

1. Define input data and reference versions.
2. Specify preprocessing and quality control.
3. Identify analysis tools and parameters.
4. Define intermediate artifacts and outputs.
5. Record software and database versions.
6. Make assumptions explicit.
7. Separate pipeline design from biological interpretation.
8. Include validation checks appropriate to the workflow.

## Inputs

- Biological data and file formats
- Reference genomes or databases
- Analysis objective
- Tool and reproducibility constraints

## Outputs

- Workflow plan
- Tool and parameter choices
- QC and validation steps
- Intermediate artifacts and final outputs
- Reproducibility record

## Example

User: "Plan a reproducible RNA-seq analysis workflow."

Expected behavior: define reference versions, QC, preprocessing, quantification, statistical analysis, software versions, and validation checkpoints.

## Limitations

Pipeline validity depends on the biological system, data quality, tool versions, and domain-specific assumptions. Biological conclusions require appropriate expert interpretation.