# Strong's Number Analysis for Number Systems

## Overview

This analysis examines whether specific Hebrew/Greek words (Strong's numbers) show consistent patterns in grammatical number usage. The analysis is based on the training dataset (`train.jsonl`) which contains 331 entries.

## Methodology

1. Grouped all training entries by Strong's number
2. Analyzed only Strong's numbers with >= 10 occurrences
3. Calculated label distribution for each Strong's number
4. Identified patterns with >= 95% consistency

## Summary Statistics

- **Total entries analyzed**: 331
- **Unique Strong's numbers**: 174
- **Strong's numbers with >= 10 occurrences**: 3

## Top Strong's Numbers by Frequency

### 1. H376 (אִישׁ - "man") - 17 occurrences

**English**: "man"
**Part of Speech**: Noun
**Label Distribution**:
- Dual: 5/17 (29.4%)
- Paucal: 4/17 (23.5%)
- Quadrial: 3/17 (17.6%)
- Trial: 2/17 (11.8%)
- Singular: 2/17 (11.8%)
- Plural: 1/17 (5.9%)

**Pattern**: HIGHLY VARIABLE - No consistent pattern
**Sample verses**: GEN.018.005, JOS.002.022

**Analysis**: The Hebrew word for "man" shows significant variability across all number categories. This is expected as it appears in diverse grammatical contexts (e.g., "two men", "three men", "several men", etc.). The variability makes it unsuitable as a predictive hint.

### 2. G4771 (σύ - "you") - 12 occurrences

**English**: "you"
**Part of Speech**: Pronoun
**Label Distribution**:
- Plural: 12/12 (100.0%)

**Pattern**: HIGHLY CONSISTENT - 100% Plural
**Sample verses**: MAT.004.019, MAT.010.016, MAT.025.035

**Analysis**: This Greek second-person pronoun ALWAYS appears in Plural contexts in the training data. This is a perfect predictor, but likely reflects sampling bias - all instances happened to be plural "you" rather than singular "you". The word itself can be either singular or plural depending on context.

**Recommendation**: NOT suitable as a Strong's hint - the 100% pattern is likely due to sampling bias, not inherent word meaning.

### 3. G5207 (υἱός - "son") - 10 occurrences

**English**: "son"
**Part of Speech**: Noun
**Label Distribution**:
- Singular: 6/10 (60.0%)
- Dual: 2/10 (20.0%)
- Plural: 2/10 (20.0%)

**Pattern**: Moderate preference for Singular (60%), but not consistent
**Sample verses**: LUK.003.029, MAT.020.021, MAT.021.028

**Analysis**: The Greek word for "son" shows some preference for Singular usage but also appears in Dual ("two sons") and Plural ("sons") contexts. The 60% rate is not strong enough to be predictive.

## Patterns with >= 95% Consistency

**G4771 (σύ - "you")**: 100% Plural (12/12 occurrences)

However, this pattern is NOT recommended as a hint because:
1. The 100% consistency likely reflects sampling bias
2. The pronoun σύ can be either singular or plural depending on grammatical context
3. All 12 occurrences happened to be in plural contexts, but this doesn't mean the word itself predicts plurality

## Recommendations

### For Strong's Enrichment

**None of the patterns identified should be added as hints to Strong's files** because:

1. **G4771 (σύ)**: While showing 100% consistency, this is sampling bias. The pronoun can be singular or plural.
2. **G5207 (υἱός)**: Only 60% consistency - too low to be predictive.
3. **H376 (אִישׁ)**: Highly variable (29% max) - no predictive value.

### For TBTA Feature Development

The lack of strong patterns suggests that:

1. **Number systems are primarily determined by grammatical context, not lexical choice**
2. Strong's-based hints would not significantly improve prediction accuracy
3. Focus should be on syntactic and contextual features rather than individual word patterns

### Potential Issues for TBTA-POTENTIAL-ISSUES.md

None identified. The variability in these high-frequency words is expected and indicates that the number system feature is working correctly - number is determined by grammatical context, not lexical semantics.

## Detailed Pattern Analysis

The grouping script identified the following discriminative patterns (from log output):

**Top 10 patterns for G4771**:
- eng contains 'and' → Plural (100%, support=321)
- eng contains 'you' → Plural (100%, support=286)
- eng contains 'the' → Plural (100%, support=281)
- grc contains 'kai' → Plural (100%, support=207)
- eng contains 'to' → Plural (100%, support=201)

**Note**: These patterns show high support (many co-occurrences) but are NOT causative. They indicate that G4771 appears in verses containing these common words, not that these words predict the number system.

## Conclusion

The analysis reveals that Strong's numbers alone are poor predictors of grammatical number. The only pattern with >= 95% consistency (G4771 at 100%) is due to sampling bias rather than inherent word meaning. This confirms that number systems are context-dependent features that require syntactic and semantic analysis beyond lexical lookup.

**No Strong's hints should be added based on this analysis.**
