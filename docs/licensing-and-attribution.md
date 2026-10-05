# Licensing and Attribution

Claude Skills Atlas accepts original resources and appropriately licensed adaptations.

## Original resources

Original work does not need per-resource attribution metadata when it is distributed under the repository's project license. Contributors should still avoid copying material they do not have permission to redistribute.

## Adapted or externally sourced resources

If a resource is based on, adapted from, or substantially derived from an external work, add these front-matter fields:

```yaml
---
source: Example Guide
source_url: https://example.com/guide
license: CC-BY-4.0
attribution: Example Author or Organization
---
```

- **source** identifies the work used as a source.
- **source_url** points to the source when an online location is available.
- **license** records the relevant license stated by the source.
- **attribution** identifies the creator or organization that should receive credit.

When any of `source`, `source_url`, or `derived_from` is present, Atlas validation requires both `license` and `attribution`.

The validator checks that `source_url`, when supplied, is an HTTP(S) URL. It does not determine whether a license legally permits redistribution; maintainers and contributors remain responsible for reviewing the source terms.

## Examples

### Adapted material

```yaml
---
name: research-summary
source: Public Research Writing Guide
source_url: https://example.com/research-writing
license: CC-BY-4.0
attribution: Example Research Organization
---
```

### Original material

An original skill can omit these fields:

```yaml
---
name: code-review
category: coding
tags: [review]
---
```

## Contributor checklist

Before opening a PR:

1. Confirm you are allowed to redistribute any external material.
2. Identify the original source when adapting existing work.
3. Record the source license accurately.
4. Include appropriate attribution.
5. Run `python scripts/validate_atlas.py`.
6. Do not treat the automated check as legal advice.
