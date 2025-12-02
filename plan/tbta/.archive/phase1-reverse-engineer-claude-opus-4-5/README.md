# TBTA Linguistic Pattern Analysis

## Overview

This directory contains comprehensive analysis of linguistic patterns discovered in TBTA (Text for Better Translation Accuracy) verse encodings. Analysis of 500 verses from `chunk-aj.tsv` revealed **13 distinct patterns** used to enhance AI understanding and translation accuracy.

## Key Files

### 1. **PATTERN_ANALYSIS.md** (Primary Document)
Comprehensive 2000-line analysis with full descriptions, examples, and insights:
- Detailed pattern breakdown with linguistic explanations
- 3 example verses for each pattern
- Frequency statistics and implementation recommendations
- Architectural insights on the encoding system

### 2. **PATTERN_QUICK_REFERENCE.md** (Lookup Guide)
Fast reference for pattern identification and usage:
- All 13 patterns in table format
- Pattern categories by function
- Underscore marker reference table
- Parenthetical tag categories
- Quick lookup by marker symbol

### 3. **PATTERN_REGISTRY.yaml** (Structured Data)
Machine-readable pattern definitions:
- Pattern metadata and categorization
- Implementation priority levels
- Related pattern relationships
- Distribution statistics
- Implementation strategy phases

## Pattern Summary

### 13 Patterns Discovered

| High-Frequency (25%+) | Medium (10-25%) | Low (<10%) |
|---|---|---|
| 1. Nested square brackets (70%) | 7. Verb alternatives (19%) | 11. Dash explanations (1%) |
| 2. Person clarifications (54%) | 8. Underscore markers (18%) | 12. Quote closures (1%) |
| 3. Grammatical tags (40%) | 9. Capital suffixes (18%) | 13. Means definitions (1%) |
| 4. Logical clauses (35%) | 10. Subject chains (12%) | |
| 5. Hyphenated units (35%) | | |
| 6. Function tags (32%) | | |

## Pattern Functions

### Structural (70%)
- **Nested brackets** mark hierarchical clausal relationships
- **Logical clauses** extract why/when/purpose connections

### Disambiguation (54%)
- **Person clarifications** resolve pronoun ambiguity
- **Subject chains** repeat subjects to avoid confusion

### Translation Guidance (40%)
- **Grammatical tags** mark mood and translation approach
- **Function tags** indicate complex/simple/literal/dynamic
- **Verb alternatives** show multiple valid translations

### Semantic Precision (35%)
- **Hyphenated units** preserve multi-word concepts
- **Capital suffixes** distinguish semantic variants
- **Underscore markers** flag linguistic features

## Key Insights

1. **Multi-Layer Disambiguation**: Three independent mechanisms resolve ambiguity
2. **Target Language Focus**: 54% person clarification suggests complex pronoun systems
3. **Translation-Aware**: 40% include explicit translation guidance for different approaches
4. **Extensible System**: Underscore markers provide unlimited annotation capability
5. **Theological Precision**: Capital suffixes enable fine-grained semantic distinction

## Usage Recommendations

### Implementation Phases

**Phase 1 (Critical)**: Patterns 1-6
- 70% nested brackets
- 54% person clarifications
- 40% grammatical tags
- 35% logical clauses and hyphenated units
- 32% function tags

**Phase 2 (Recommended)**: Patterns 7-10
- 19% verb alternatives
- 18% underscore markers and capital suffixes
- 12% subject reference chains

**Phase 3 (Specialized)**: Patterns 11-13
- <1% etymology and definitions
- <1% quote closures

## Data Source

**Dataset**: `/workspace/plan/tbta/phase1-policy/data/chunk-aj.tsv`
- 500 verses analyzed
- Pattern threshold: 3+ occurrences
- Detection method: Regex-based pattern matching
- Date: December 2, 2025

## Pattern Categories

### By Function
- **Structural Markers**: 8 patterns (brackets, clauses, units)
- **Disambiguation**: 2 patterns (person/subject reference)
- **Translation Guidance**: 3 patterns (tags, alternatives, function)
- **Semantic Precision**: 3 patterns (hyphens, suffixes, markers)
- **Specialized Notation**: 3 patterns (explanations, quotes, definitions)

### By Frequency Band
- **High-Frequency (25%+)**: 6 patterns covering 70% of verses
- **Medium-Frequency (10-25%)**: 4 patterns covering 12-19% of verses
- **Low-Frequency (<10%)**: 3 patterns covering 0.6-0.8% of verses

## Underscore Marker System

15 distinct semantic markers identified:
- `_implicit` (22% frequency) - Content reader must infer
- `_paragraph` (6% frequency) - Structural boundaries
- `_implicitNecessary` (5% frequency) - Grammar-required but unstated
- `_implicitActiveAgent` (3% frequency) - Subject not named
- Plus 11 additional markers for number, modality, and perspective

## Parenthetical Tag System

10 distinct grammatical tags identified:
- **Mood**: `(imp)` - Imperative, `(title)` - Section header
- **Approach**: `(literal)` - Word-for-word, `(dynamic)` - Meaning equivalence
- **Structure**: `(complex)` - Multi-clause, `(simple)` - Simplified
- **Type**: `(footnote)`, `(implicit-situational)`, `(implicit-info)`, `(paragraph)`

## Files in This Directory

```
.
├── README.md (this file)
├── PATTERN_ANALYSIS.md (comprehensive analysis)
├── PATTERN_QUICK_REFERENCE.md (lookup guide)
└── PATTERN_REGISTRY.yaml (structured data)
```

## Next Steps

1. **Validate** patterns with additional verse samples
2. **Extend** underscore marker system with new features as needed
3. **Implement** Phase 1 patterns in all TBTA encodings
4. **Document** new patterns discovered in future analysis
5. **Establish** guidelines for consistent pattern application

## Related Documentation

- Source data: `/workspace/plan/tbta/phase1-policy/data/chunk-aj.tsv`
- Project overview: See parent directory documentation
- TBTA encoding standards: See project STANDARDIZATION.md

---

*Analysis completed: December 2, 2025*
*Dataset: 500 verses from chunk-aj.tsv*
*Patterns discovered: 13 (3+ occurrence threshold)*
