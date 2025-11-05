# TBTA Reproduction Project

## Goal
Reproduce and extend the TBTA (Translation Brief for Translators and Assessors) annotation results using AI-powered analysis.

## Current Status
**Phase**: Initial setup and parallel research launch
**Started**: 2025-11-05
**Expected Duration**: ~12 hours

## Key Resources
- **TBTA Source**: https://github.com/AllTheWord/tbta_db_export
- **Languages Dataset**: `src/constants/languages.tsv` (1009 languages across multiple families)
- **Output Directory**: `plan/tbta-project/`

## Project Overview

### The Problem
TBTA manually annotated Bible verses with linguistic features crucial for translation. They identified features like:
- Noun participant tracking (first mention, routine, restaging, etc.)
- Verb temporal/aspectual/modal features (16+ time values, various aspects/moods)
- Person/number marking (including dual, trial, quadrial, paucal)
- Proximity distinctions
- Polarity and reflexivity

### Our Approach
1. **Deep Language Research**: Understand the unique features of all 1009 languages in our dataset
2. **Feature Documentation**: Comprehensively document each TBTA feature with research and examples
3. **Systematic Reproduction**: For each feature, develop methods to reproduce TBTA decisions
4. **Extension**: Add language-family-specific alternatives and improvements

## TBTA Feature Categories

### Core Annotations Identified:
1. **Nouns** (SyntacticCategory 1)
   - Number: Singular, Dual, Trial, Quadrial, Paucal, Plural
   - Participant Tracking: 9 states (First Mention → Offstage)
   - Polarity, Proximity, Person, Surface Realization

2. **Verbs** (SyntacticCategory 2)
   - Time: 16+ values
   - Aspect: 9 types (Inceptive, Completive, Cessative, etc.)
   - Mood: Indicative, Potential levels, Obligation, Permissive
   - Reflexivity, Polarity, Degree

3. **Adjectives** (SyntacticCategory 3)
   - Degree variations (11 types)

4. **Adverbs** (SyntacticCategory 4)
   - Degree variations

5. **Adpositions** (SyntacticCategory 5)
6. **Conjunctions** (SyntacticCategory 6)
7. **Phrasals** (SyntacticCategory 7)
8. **Particles** (SyntacticCategory 8)
9. **Phrases** (101-105)
10. **Discourse Levels** (110, 120)

## Directory Structure

```
plan/tbta-project/
├── README.md (this file)
├── PROGRESS.md (ongoing updates)
├── features/
│   ├── {feature-name}/
│   │   ├── README.md (detailed research)
│   │   ├── LEARNINGS.md (findings and thesis)
│   │   └── {experiment-name}.md (individual tests)
├── language-research/
│   ├── families/
│   │   └── {family-name}.md
│   └── unique-features/
│       └── {feature-name}.md
└── combined/
    ├── README.md (unified approach)
    └── reproduction-prompt.md (final prompt)
```

## Execution Strategy

### Phase 1: Parallel Research (Hours 0-4)
- 8 parallel agents researching language families
- 8 parallel agents documenting TBTA features in depth
- Focus: Comprehensive understanding before reproduction

### Phase 2: Feature Reproduction (Hours 4-10)
- For each feature, launch experimentation agents
- Test various methods to predict TBTA decisions
- Document failures and iterate on new thesis
- Use subagents with fresh context for unbiased testing

### Phase 3: Synthesis (Hours 10-12)
- Merge successful approaches into unified prompt
- Refine and test combined approach
- Document improvements over original TBTA

## Success Criteria
1. ✅ Reproduce TBTA annotations with high accuracy
2. ✅ Identify and correct TBTA annotation errors
3. ✅ Extend schema with language-family-specific alternatives
4. ✅ Create reusable prompt/skill for future annotations

## Next Steps
See PROGRESS.md for real-time updates as research proceeds.
