---
name: system-design-basics
category: computer-science
tags: [systems, architecture, scalability]
---

# System Design Basics

## Purpose

Structure an introductory system-design discussion around requirements, architecture, scale, bottlenecks, and failure modes.

## When to use

Use when learning or planning a system design and the problem needs a structured architecture discussion.

## Instructions

1. Clarify functional and non-functional requirements.
2. Estimate scale only from stated assumptions.
3. Separate APIs, data model, architecture, bottlenecks, failure modes, and trade-offs.
4. Explain why each major component exists.
5. Consider how components can fail and recover.
6. Do not present speculative capacity numbers as facts.

## Inputs

- System requirements
- Expected users or workload, when known
- Reliability, latency, and consistency constraints

## Outputs

- Requirements
- API and data model outline
- Architecture
- Bottlenecks and failure modes
- Trade-offs and assumptions

## Example

User: "Design a basic URL-shortening service."

Expected behavior: clarify requirements, define the API and storage model, propose an architecture, and discuss scale and failure modes.

## Limitations

Introductory design estimates are sensitive to assumptions and should be validated against real workload data.