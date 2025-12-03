# TBTA Pattern Analysis - Complete Documentation Index

## Analysis Overview

**Dataset**: chunk-aj.tsv (500 TBTA-encoded verses)
**Analysis Date**: December 2, 2025
**Patterns Discovered**: 13 distinct linguistic patterns
**Pattern Threshold**: 3+ occurrences minimum
**Analysis Method**: Regex-based pattern matching + manual validation

## Documentation Files

### Entry Points (Start Here)

1. **README.md**
   - High-level overview of the analysis
   - Pattern summary tables
   - Key findings and insights
   - Implementation recommendations
   - Quick navigation guide
   - Start here for context and overview

### Comprehensive References

2. **PATTERN_ANALYSIS.md** (MAIN DOCUMENT - 12KB)
   - Complete pattern descriptions
   - Detailed linguistic explanations
   - 3 verse examples per pattern
   - Frequency statistics
   - Architectural insights
   - Category breakdown
   - Implementation guidance
   - **Use this for**: Deep understanding of each pattern

3. **PATTERN_QUICK_REFERENCE.md** (5.9KB)
   - All 13 patterns in table format
   - Category-based organization
   - Underscore marker reference table (15 markers)
   - Parenthetical tag system
   - Pattern nesting examples
   - Quick lookup by symbol
   - **Use this for**: Fast lookups and pattern identification

4. **PATTERN_REGISTRY.yaml** (13KB, Machine-Readable)
   - Structured pattern metadata
   - Implementation priorities
   - Related pattern relationships
   - Distribution statistics
   - Strategy phases
   - Tag catalogs
   - **Use this for**: System integration and automation

## Pattern Summary by Category

### STRUCTURAL MARKERS (6 patterns)

| # | Pattern | Frequency | Purpose |
|---|---|---|---|
| 1 | Nested Square Brackets | 70.0% | Hierarchical clausal grouping |
| 4 | Bracketed Logical Clauses | 35.0% | Causal/conditional/temporal relationships |
| 5 | Hyphenated Semantic Units | 34.6% | Multi-word concept preservation |
| 6 | Grammatical Function Tags | 31.8% | Translation choices and grammar |
| 9 | Capital Letter Suffixed Compounds | 18.0% | Semantic variant distinction |
| 8 | Underscore Semantic Markers | 18.4% | Linguistic feature flagging |

### DISAMBIGUATION (2 patterns)

| # | Pattern | Frequency | Purpose |
|---|---|---|---|
| 2 | Parentheses Person Clarifications | 54.4% | Pronoun resolution |
| 10 | Subject Reference Chains | 12.0% | Multi-sentence subject clarity |

### TRANSLATION GUIDANCE (3 patterns)

| # | Pattern | Frequency | Purpose |
|---|---|---|---|
| 3 | Parenthetical Grammatical Tags | 39.6% | Mood and translation approach |
| 6 | Grammatical Function Tags | 31.8% | Translation structure choices |
| 7 | Verb Alternative Forms | 19.2% | Multiple valid interpretations |

### SPECIALIZED NOTATION (3 patterns)

| # | Pattern | Frequency | Purpose |
|---|---|---|---|
| 11 | Dash Prefixed Explanations | 0.8% | Etymology and footnotes |
| 12 | Double Quote Closures | 0.6% | Speech boundary marking |
| 13 | Means Definition Statements | 0.6% | Name and concept definitions |

## Quick Navigation

### By Pattern Number
- **Pattern 1-6**: High-frequency patterns (25%+) - Core mechanisms
- **Pattern 7-10**: Medium-frequency patterns (10-25%) - Common extensions
- **Pattern 11-13**: Low-frequency patterns (<10%) - Specialized use

### By Use Case

**For Translation Aids**:
- Pattern 2 (Person clarifications)
- Pattern 3 (Grammatical tags)
- Pattern 6 (Function tags)
- Pattern 7 (Verb alternatives)
- Pattern 10 (Subject chains)

**For Structure Understanding**:
- Pattern 1 (Nested brackets)
- Pattern 4 (Logical clauses)
- Pattern 5 (Hyphenated units)

**For Semantic Precision**:
- Pattern 5 (Hyphenated units)
- Pattern 8 (Underscore markers)
- Pattern 9 (Capital suffixes)

**For Specialized Information**:
- Pattern 11 (Etymology explanations)
- Pattern 12 (Quote marks)
- Pattern 13 (Definitions)

### By Frequency Band

**High Impact (implement first)**:
- Patterns 1, 2, 3, 4, 5, 6 (70-32% frequency)

**Medium Impact (add next)**:
- Patterns 7, 8, 9, 10 (19-12% frequency)

**Specialized (add as needed)**:
- Patterns 11, 12, 13 (<1% frequency)

## Key Underscore Markers (15 types)

From highest to lowest frequency:

1. `_implicit` (22%) - Inferred from context
2. `_paragraph` (6%) - Structural division
3. `_implicitNecessary` (5%) - Grammar-required unstated
4. `_implicitActiveAgent` (3%) - Subject unnamed
5. `_plural` (2%) - Plural grammatical number
6. `_dual` (2%) - Exactly two (dual number)
7. `_generic` (1%) - Generic reference
8. `_singular` (1%) - Singular reference
9. `_hyperbolic` (1%) - Rhetorical exaggeration
10. `_frameInferable` (1%) - Context-inferable
11. `_incl` (1%) - Inclusive pronouns
12. `_excl` (1%) - Exclusive pronouns
13. `_instrument` (1%) - Means of action
14. `_descriptive` (1%) - Descriptive clause
15. `_1stAs3rd` (1%) - First person as third

## Key Parenthetical Tags (10 types)

### Grammatical Mood
- `(imp)` - Imperative mood
- `(title)` - Section title/heading

### Translation Approach
- `(literal)` - Word-for-word translation
- `(dynamic)` - Meaning-for-meaning translation

### Sentence Structure
- `(complex)` - Multi-clause structure
- `(simple)` - Simplified or single clause
- `(paragraph)` - Paragraph boundary marker

### Special Context
- `(footnote)` - Explanatory annotation
- `(implicit-situational)` - Situation provides meaning
- `(implicit-info)` - Information context provides meaning

## Implementation Strategy

### Phase 1: Core Infrastructure (Critical)
Implement patterns 1-6 covering 70% of verses:
- Nested brackets for structure
- Person clarifications for pronouns
- Grammatical tags for translation choices
- Logical clause marking
- Hyphenated semantic units
- Function tags

### Phase 2: Extended Features (Recommended)
Add patterns 7-10 covering additional 12-19% of verses:
- Verb alternatives for ambiguity
- Underscore markers for linguistic features
- Capital suffixes for semantic variants
- Subject reference chains for clarity

### Phase 3: Specialized Tools (As Needed)
Include patterns 11-13 for rare specialized cases:
- Etymology explanations
- Definition statements
- Quote closures

## Data Source Details

**File**: `/workspace/plan/tbta/phase1-policy/data/chunk-aj.tsv`
**Format**: Tab-separated values with columns:
- `reference`: Verse reference (e.g., "Matthew 15:6")
- `verse`: Full TBTA-encoded verse text
- `book`: Bible book name

**Statistics**:
- Total verses: 500
- Pattern coverage: 13 distinct types
- Minimum occurrence threshold: 3
- Analysis method: Regex + manual validation

## Related Resources

- Project documentation: See parent directory
- TBTA encoding standards: See STANDARDIZATION.md
- Source data: chunk-aj.tsv
- Previous analyses: Check parent directory

## Quick Stats

- **70%** of verses use nested brackets
- **54%** use person clarifications
- **40%** include grammatical tags
- **35%** mark logical relationships
- **35%** use hyphenated semantic units
- **19%** show verb alternatives
- **18%** use underscore markers
- **18%** use capital-letter suffixes
- **<1%** use specialized notation

## Contact & Questions

For questions about:
- Pattern interpretation: See PATTERN_ANALYSIS.md
- Quick lookup: See PATTERN_QUICK_REFERENCE.md
- System integration: See PATTERN_REGISTRY.yaml
- Implementation: See README.md

---

**Analysis Summary**:
13 linguistic patterns discovered in 500 TBTA-encoded verses representing three functional categories (structural, disambiguation, translation guidance) plus specialized notation. All patterns documented with examples, frequencies, and implementation guidance.

**Created**: December 2, 2025
**Files**: 4 comprehensive documents + index
**Total Analysis**: 30KB+ of detailed documentation
