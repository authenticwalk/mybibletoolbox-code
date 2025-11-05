# TBTA Features - Detailed Analysis

This directory contains in-depth analysis of each TBTA feature category, with focus on practical translation value and implementation insights.

## Structure

Each feature category has its own subdirectory:
- `01-nouns/` - Category 1: Nouns (Number, Person, Participant Tracking, etc.)
- `02-verbs/` - Category 2: Verbs (Time, Aspect, Mood, etc.)
- `03-adjectives/` - Category 3: Adjectives (Degree, etc.)
- ... (more to come)

## Analysis Format

Each analysis document covers:

1. **Most Valuable Sub-Features** - Translation value ranking
2. **Example Coverage** - What examples exist in our data
3. **Use Case Patterns** - When/why features matter for translation
4. **Implementation Learnings** - What works, what needs improvement
5. **Query Opportunities** - Useful searches for translators/researchers
6. **Transferable Patterns** - Insights applicable to other categories

## Current Status

- ✅ **01-nouns/** - Complete comprehensive analysis
  - Analyzed 12 sub-features
  - Documented Genesis 1:26 (Trial, First Inclusive)
  - Identified 10 high-value query patterns
  - Extracted 6 transferable implementation patterns

- ⏳ **02-verbs/** - Pending
- ⏳ **03-adjectives/** - Pending
- ... (13 more categories)

## Key Insights So Far

### Most Valuable Features (Across All Categories)
1. **Number Systems** (Nouns) - Trial, Dual, Paucal ⭐⭐⭐⭐⭐
2. **Person Systems** (Nouns) - Inclusive/Exclusive "we" ⭐⭐⭐⭐⭐
3. **Participant Tracking** (Nouns) - Discourse flow ⭐⭐⭐⭐⭐
4. **Time Granularity** (Verbs) - 20+ temporal distinctions ⭐⭐⭐⭐⭐
5. **Speaker Demographics** (Clauses) - Age, attitude, register ⭐⭐⭐⭐⭐

### Transferable Implementation Patterns
1. **Feature-based indexing** - Index features during processing for fast queries
2. **Semantic filtering** - Filter by meaning ("Not Applicable"), not pattern
3. **Validation through expected values** - Enumerate and validate all feature values
4. **Cross-dataset linking** - Link TBTA to Macula at verse level
5. **Feature-example documentation** - Every value needs examples and stats
6. **Hierarchical structure preservation** - Don't flatten prematurely

## Usage

### For Tool Developers
- Read analysis to understand feature value and implementation challenges
- Use "Query Opportunities" section to prioritize tool features
- Apply "Transferable Patterns" to new implementations

### For Translators
- "Most Valuable Sub-Features" shows which features matter for your language
- "Use Case Patterns" explains when features are needed
- "Example Coverage" shows where to find concrete examples

### For Researchers
- Comprehensive feature documentation
- Coverage statistics (what's annotated, what's not)
- Cross-reference opportunities with other datasets

## Next Steps

1. Complete analysis for Categories 2-8 (word-level)
2. Complete analysis for Categories 101-104 (phrase-level)
3. Complete analysis for Categories 105-120 (clause/discourse-level)
4. Build query tools based on identified opportunities
5. Create feature index for fast lookups

## Related Documents

- `../ALL-FEATURES.md` - Complete feature list from official TBTA docs
- `../FEATURE-SUMMARY.md` - High-level summary across all categories
- `../../tbta-analysis.md` - Initial TBTA analysis and examples
- `../../tbta-processing-summary.md` - Processing results (11,649 verses)
