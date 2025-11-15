# Lexicon Core - Documentation

## Status
Research complete, Experimentation ongoing (Cycle 4)

## Overview
Extract authoritative lexical data from published lexicons to create the foundation for all Strong's enrichment work.

**Authority Level:** HIGH (published lexicons only)

**Timeline:** 14 weeks total
- Research: 2 weeks ✅
- Experiments: 4 weeks 🔄
- Validation: 2 weeks
- Production: 6 weeks

## Methodology (5 Steps)
1. **Read Base File** - Extract existing data from `.data/strongs/{num}/{num}.strongs.yaml`
2. **BibleHub Extraction** - Thayer's, HELPS Word-studies, usage statistics (parallel)
3. **StudyLight Extraction** - LSJ, Abbott-Smith, Vocabulary of Greek NT (parallel)
4. **Blue Letter Bible** - TDNT references, Trench's Synonyms, cross-refs (parallel)
5. **Synthesis** - Identify convergence, document divergence, apply fair use

## Data Sources
- Published lexicons: BDB, Thayer's, BDAG, LSJ, Abbott-Smith, HELPS Word-studies
- Web aggregators: BibleHub, StudyLight, Blue Letter Bible
- Cross-reference codes: TDNT, Louw-Nida, Trench's Synonyms

## Key Innovation
Fair use convergence grouping - "Most lexicons agree X {thayer} {bdb} {lsj}"

## Output Format
`.data/strongs/{num}/{num}-lexicon-core.yaml`

## Complete Documentation
**See:** `/plan/strongs-enrichment-tools/01-lexicon-core/` for detailed planning, experiments, and validation criteria.

This documentation will be migrated here as the tool reaches production readiness.
