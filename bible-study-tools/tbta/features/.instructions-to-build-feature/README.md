# TBTA Feature Builder Instructions

## Short Intro to TBTA

TBTA (Translation By Theological Analysis) is a comprehensive translation tool that provides linguistic, cultural, and theological analysis for Bible translation work. It handles cases where linguistical features are required for translation but are not present in the original text.

**Key TBTA Files**:
- [../README.md](../README.md) - Main TBTA overview and thesis
- [../tbta-source/README.md](../tbta-source/README.md) - TBTA source documentation

## Features: What It Is, Why It Matters

TBTA features represent grammatical, discourse, or linguistic characteristics that are important for Bible translation. For instance, "let us" in English just means "more than one" but languages may be more specific like two, three, five, etc. 

The key to solving this is to look at what languages require this feature and look at their current translations. If they all agree it is easy to follow that; if they disagree then the analysis of why and providing hints and the consequences of each potential choice is really valuable.

**Why This Matters**: Many languages require grammatical distinctions that English doesn't make. Without TBTA, translators must guess these distinctions, potentially losing theological precision or introducing errors.

See [../features/README.md](../features/README.md) for the complete list of features and their status.

## Goals for Building This

We want to rebuild TBTA using an LLM-only approach. The original TBTA features were built manually with extensive hardcoding. This rebuild aims to:

1. **Leverage AI capabilities**: Use LLMs to analyze and extract patterns from existing data
2. **Improve maintainability**: Generate features from patterns rather than hardcoding
3. **Reduce code size**: Smaller, more focused implementations that generalize better
4. **Truth grounding**: Must cite sources and avoid hallucination

**Context**: You are building a component of the "The Meaning of the Text" layer for AI Bible translation.

## Core Rules (CRITICAL)

These rules are non-negotiable. Violation invalidates the work.

### 1. Predict, Don't Memorize
- Do not create an expert system with thousands of hardcoded rules.
- Create prompt-based logic that learns general patterns (e.g., "If divine speaker + plural -> Trial").
- Test for overfitting: If I remove this specific verse, does the logic still work?
- **Must generalize** - don't make an expert system with just hardcoded values

### 2. Zero-Knowledge Testing
- **Never** look at the answer key;
- **Never** look up the tbta answer from their files; that is cheating; 
- **Must**  call the scripts in /src/tools/predict to create, fetch and get your data.

### 3. Must Peer Review
- All features require peer review by Theologian, Linguist, and Translator personas
- Critical theological contexts must be validated
- See [STAGE-4-VALIDATION.md](./STAGE-4-VALIDATION.md) for peer review requirements

### 4. Smaller is Better
- Keep implementations focused and concise
- Prefer simple, generalizable patterns over complex rule systems
- Progressive disclosure: Keep READMEs ≤200 lines, topic files ≤400 lines

### 5. Data-Driven Reality
- **Verify** language availability before planning experiments.
- **Verify** data coverage: Check that all documented feature values exist in TBTA (≥80% coverage required).
- **Honesty**: If the data is ambiguous, report low accuracy. Do not hallucinate success.

### 6. Secure Data Handling (The "Secret File" Rule")
- **Split Data**: Train (60%), Test (20%), Validate (20%).
- **Secret Answers**: Answer keys for Test and Validate sets must be stored as `*-answers.secret.jsonl`.
- **Ignore Policy**: You are **FORBIDDEN** from reading any file ending in `.secret.jsonl`.
- **Scoring**: Only specialized scoring scripts in /src/tools/predict are allowed to access these files to calculate metrics.

### 7. Progressive Disclosure
- Keep your output files (READMEs, Reports) under 500 lines.
- Inline essential code/data. Link to `experiments/` for raw dumps.
- Keep to the rules of `.claude/skills/progressive-disclosure/SKILL.md`

## Why Rebuild with LLMs?

The original TBTA features were built manually with extensive hardcoding. This rebuild aims to:
1. **Leverage AI capabilities**: Use LLMs to analyze and extract patterns from existing data.
2. **Improve maintainability**: Generate features from patterns rather than hardcoding.
3. **Reduce code size**: Smaller, more focused implementations that generalize better.
4. **Truth grounding**: Must cite sources and avoid hallucination.

## Development Stages

This directory contains instructions for each stage of feature development. Each stage is designed to be assigned to its own agent to keep context low, and each agent will need all the core information it needs to achieve its goals.

1. **Research**: [STAGE-1-RESEARCH.md](./STAGE-1-RESEARCH.md)
2. **Analysis**: [STAGE-2-ANALYSIS.md](./STAGE-2-ANALYSIS.md)
3. **Experimentation**: [STAGE-3-EXPERIMENTATION.md](./STAGE-3-EXPERIMENTATION.md)
4. **Validation**: [STAGE-4-VALIDATION.md](./STAGE-4-VALIDATION.md)

# Development Stages

This document outlines the 4-stage development process for rebuilding TBTA features using LLMs.

## Stage 1: Research & Definition
**File**: [STAGE-1-RESEARCH.md](./STAGE-1-RESEARCH.md)
- Define the feature and its theological significance.
- Identify linguistic constraints and target languages.
- Determine "Arbitrarity" (Which contexts are non-negotiable?).

## Stage 2: Analysis & Hypothesis Validation
**File**: [STAGE-2-ANALYSIS.md](./STAGE-2-ANALYSIS.md)
- Extract data from existing TBTA system.
- Analyze patterns and verify data coverage.
- Generate "Smart" datasets aligned with Strong's numbers.
- Split data into Train/Test/Validate sets (Secure Handling).

## Stage 3: Experimentation & Iterative Development
**File**: [STAGE-3-EXPERIMENTATION.md](./STAGE-3-EXPERIMENTATION.md)
- Develop the prompt/algorithm logic.
- Run parallel experimental tracks (Baseline, Logic, Strong's Annotation, Translation Consensus).
- Iterate on the "One-Pass" evaluation loop.
- Achieve high accuracy and calibration on Training/Test sets.

## Stage 4: Validation & Peer Review
**File**: [STAGE-4-VALIDATION.md](./STAGE-4-VALIDATION.md)
- Final "Exam" on the held-out Validation set.
- Critical peer review by Theologian, Linguist, and Translator personas.
- Decision on Production Readiness (Tier 1 vs Full Deployment).

## Feature Directory Structure

Each feature follows this standard directory structure:

```
features/{feature-name}/
├── README.md                     (≤500 lines - feature overview + stage checklist)
│   ├── Purpose (50-100 lines)
│   ├── Methodology (200-300 lines, INLINE - no external refs)
│   ├── Output Schema (100-150 lines)
│   └── Related Features (50 lines)
├── scripts/                      (Feature-specific scripts and tools)
│   ├── verify_coverage.py       (Stage 2 coverage check)
│   ├── validate_hypotheses.py   (Stage 2 hypothesis validation)
│   ├── split_data.py            (Stage 2 data splitting)
│   └── [other feature-specific tools] (NOT extract_data.py or validate.py)
├── data/                         (Clean, split datasets from Stage 2)
│   ├── train.jsonl               (Full training data)
│   ├── test_inputs.jsonl         (Test inputs only)
│   ├── test_answers.secret.jsonl (Test answers - SECRET/FORBIDDEN)
│   ├── validate_inputs.jsonl     (Validation inputs only)
│   ├── validate_answers.secret.jsonl (Validation answers - SECRET/FORBIDDEN)
│   ├── adversarial_candidates.jsonl (Hand-picked edge cases)
│   └── README.md                 (Data lineage and split details)
├── research/                     (Research outputs from Stage 1)
│   ├── ARBITRARITY-CLASSIFICATION.md (Theological analysis of arbitrarity)
│   └── [Scholarship notes]
├── analysis/                     (Analysis outputs from Stage 2)
│   ├── raw_data.jsonl            (Initial extraction)
│   ├── scorecard.md              (Hypothesis validation summary)
│   ├── validation_raw.jsonl      (Detailed hypothesis logs)
│   ├── strongs_correlation.csv   ("Magic words" analysis)
│   ├── coverage_report.md        (Data coverage verification)
│   └── convergence_report.md     (Multi-factor analysis)
├── learnings/                    (Learnings and error analysis)
│   ├── LEARNINGS.md              (6-step error analysis, algorithm evolution)
│   └── GAPS.md                   (Identified gaps or issues)
├── experiments/                  (Iterative Prompt Engineering - Stage 3)
│   ├── v1/                       (First algorithm iteration)
│   │   ├── PROMPT.md             (THE ACTUAL PROMPT - this is what gets executed)
│   │   ├── predictions.yaml      (Predictions on test/validate sets - commit to git to "lock")
│   │   ├── validation.md         (Validation results for this iteration)
│   │   └── results.md             (Iteration-specific results and notes)
│   ├── v2/                       (Second algorithm iteration - alternative approach)
│   │   ├── PROMPT.md             (THE ACTUAL PROMPT)
│   │   ├── predictions.yaml
│   │   ├── validation.md
│   │   └── results.md
│   └── VALIDATION-RESULTS.md     (Aggregated validation results - markdown table with summary)
```

### Key Points:

1. **The Actual Prompt**: Lives in `experiments/v{N}/PROMPT.md` - this is the executable prompt/algorithm.

2. **Experiments Organization**: 
   - `experiments/v{N}/` folders for each algorithm iteration
   - `experiments/VALIDATION-RESULTS.md` for aggregated summary (Markdown table)
   - No `archive/` folder; keep history in git.

3. **Data Files**: 
   - Located in `data/` (feature root)
   - Uses `.jsonl` format as per Stage 2
   - `*.secret.jsonl` files contain answers for Test/Validate sets (FORBIDDEN to read)

4. **Workflow Output Folders**:
   - `research/`: Stage 1 outputs (Arbitrarity classification)
   - `analysis/`: Stage 2 outputs (Raw data, scorecards, coverage reports)
   - `learnings/`: Error analysis and gaps (Stage 5/6)

5. **Scripts**: Feature-specific scripts in `scripts/` (e.g. `verify_coverage.py`, `validate_hypotheses.py`).

6. **General Tools**: `extract_data.py` and `validate.py` are in `src/tools/predict`.

## Planning Files

Do NOT put feature-specific planning files in this directory. This directory is for instructions and guidelines.

Do not add progress updates here or planning here. Put planning files into `/plan/tbta/features/{feature-name}/`.

Do not log progress here. Update the plan at `/plan/tbta/features/{feature-name}/plan.md`.

## Questions?

- Check [../README.md](../README.md) for TBTA feature documentation.
- Check [../features/README.md](../features/README.md) for the complete feature catalog (don't list all features here).
