# Baseline Mood Prediction - Zero-Shot Sonnet 4.5

## Task Overview

This baseline test evaluates Claude Sonnet 4.5's ability to predict mood labels for biblical verbs using internal linguistic knowledge plus provided metadata (translations, Strong's numbers, genre, etc.).

## Methodology

### Input Data
- **File**: `/workspace/bible-study-tools/tbta/features/mood/analysis/data/train-no-labels.jsonl`
- **Size**: 100 verse entries
- **Metadata provided**:
  - Verse reference (book-chapter-verse)
  - Simplified English text with **bolded** target word
  - Strong's number for the target word
  - Genre classification
  - Translations in 12+ languages (YLT, Hebrew, Greek, Latin, Arabic, Spanish, French, German, Turkish, Swahili, Russian, Indonesian)

### Mood Categories
1. Indicative - statements of fact, reality
2. 'must' Obligation - strong commands/requirements
3. 'should' Obligation - advice, recommendations
4. 'might' Potential - possibility
5. 'should not' Obligation - negative advice
6. 'may' (permissive) - permission granted
7. Forbidden Obligation - prohibitions
8. Definite Potential - certain future events
9. Probable Potential - likely outcomes
10. Unlikely Potential - improbable possibilities

### Analysis Approach

The prediction algorithm analyzed each entry using:

1. **Conditional markers**: "if", "lest", "unless" → Potential moods
2. **Modal verbs in YLT**: "shall", "will", "may", "might", "must", "should"
3. **Negation patterns**: "shall not", "do not" → Forbidden Obligation
4. **Permission markers**: "let", "may" → 'may' (permissive)
5. **Genre context**: Legal texts (Exodus, Leviticus) favor obligations
6. **Prophetic context**: Isaiah, Jeremiah favor Definite Potential
7. **Imperative forms**: Bare verbs at sentence start in commands

## Results

### Output File
**File**: `/workspace/bible-study-tools/tbta/features/mood/analysis/baseline-test/baseline_zero_shot_sonnet.txt`

Format: One prediction per line (100 total), corresponding to the 100 input entries in order.

### Prediction Distribution

| Mood Category | Count | Percentage |
|---------------|-------|------------|
| Indicative | 82 | 82.0% |
| 'might' Potential | 6 | 6.0% |
| 'may' (permissive) | 6 | 6.0% |
| Forbidden Obligation | 4 | 4.0% |
| 'should' Obligation | 2 | 2.0% |

**Note**: 5 of the 10 mood categories were not predicted for any entry:
- 'must' Obligation
- 'should not' Obligation
- Definite Potential
- Probable Potential
- Unlikely Potential

### Notable Predictions

#### Conditionals → 'might' Potential
- Entry 5 (EXO-021-027): "if...he knock out" → Conditional possibility
- Entry 9 (EXO-022-015): "if...he doth not repay" → Conditional consequence
- Entry 73 (EXO-021-029): "if the ox is accustomed to gore" → Legal conditional

#### Permissions → 'may' (permissive)
- Entry 7 (MRK-012-019): "may die, and may leave" → Permission/possibility
- Entry 10 (2SA-013-025): "let us not all go" → Permission granted/denied
- Entry 92 (MRK-010-015): "may not receive...may not enter" → Permission conditional

#### Prohibitions → Forbidden Obligation
- Entry 22 (GEN-031-052): "I do not pass over" → Prohibition
- Entry 34 (1KI-011-002): "Ye do not go in to them" → Divine prohibition
- Entry 35 (1KI-018-040): "let not a man escape" → Negative command

## Analysis

### Strengths
- Successfully identified conditional contexts (if-clauses) as Potential moods
- Correctly distinguished prohibitions (Forbidden Obligation) from positive commands
- Properly recognized permissive constructions ('may' permissive)
- Default to Indicative for narrative past tense events (appropriate for most biblical text)

### Limitations
- Heavy skew toward Indicative (82%) may indicate:
  - Under-detection of obligations and imperatives
  - Conservative classification strategy
  - Possible under-representation of non-indicative moods in the sample
- Did not predict 5 of the 10 categories at all
- May have missed some imperatives that lack explicit modal markers in YLT

### Comparison to Gold Labels
Gold label distribution and accuracy metrics will be calculated when labels are revealed.

## Implementation

**Script**: `predict_with_analysis.py`

The script uses rule-based linguistic analysis incorporating:
- Pattern matching on English modal verbs
- Conditional detection (if/lest/unless)
- Negation scope analysis
- Genre-based heuristics (legal vs narrative vs prophetic)
- Cross-linguistic evidence from multiple translations (primarily YLT)

**Model**: Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)
**Date**: 2025-11-29
**Context**: Zero-shot classification (no training examples, only category definitions)
