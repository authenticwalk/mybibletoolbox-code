# Feature Builder Instructions: Core Context

**Scope**: Global rules for all sub-agents working on TBTA features.
**Context**: You are building a component of the "The Meaning of the Text" layer for AI Bible translation.

## Project Overview (TBTA)
MyBibleToolbox Translation Assistant (TBTA) aims to provide extensive semantic data (essentially "a book's worth of information") for every single verse in the Bible to ground AI translations in truth.
*   **Original System**: A C++ expert system with hardcoded rules.
*   **Our Mission**: Rebuild these features using LLMs to be more flexible, accurate, and generalizable.

## Core Rules

1.  **Predict, Don't Memorize**
    *   Do not create an expert system with thousands of hardcoded rules.
    *   Create prompt-based logic that learns general patterns (e.g., "If divine speaker + plural -> Trial").
    *   Test for overfitting: If I remove this specific verse, does the logic still work?

2.  **Zero-Knowledge Testing (The "Cursor" Rule)**
    *   **Never** look at the answer key (`test.yaml` or `validate.yaml`) while testing.
    *   **Must** lock predictions to a file (`predictions_LOCKED.yaml`) via git commit *before* scoring.
    *   Violation of this rule invalidates all work.

3.  **Data-Driven Reality (The "ClaudeFlow" Rule)**
    *   **Verify** language availability before planning experiments. Don't write scripts for "Fijian" if Fijian isn't in our API.
    *   **Honesty**: If the data is ambiguous (e.g., English doesn't distinguish Dual/Paucal), report the low accuracy. Do not hallucinate success.
    *   **Tiered Deployment**: If a feature works 100% for Trinity but 0% for generic plurals, deploy it as "Tier 1 (Trinity Only)".

4.  **Progressive Disclosure**
    *   Keep your output files (READMEs, Reports) under 500 lines.
    *   Inline essential code/data. Link to `experiments/` for raw dumps.

5.  **Secure Data Handling (The "Secret File" Rule)**
    *   **Split Data**: Data must be split into Train/Test/Validate sets.
    *   **Secret Answers**: Answer keys for Test and Validate sets must be stored as `*-answers.secret.jsonl`.
    *   **Ignore Policy**: You are **FORBIDDEN** from reading any file ending in `.secret.jsonl`.
    *   **Scoring**: Only specialized scoring scripts are allowed to access these files to calculate metrics.

## Directory Structure
All work for a feature happens in: `bible-study-tools/tbta/features/{feature-name}/`

*   `README.md` (The progressive disclosure summary)
*   `experiments/` (All data, scripts, logs)
*   `.../01-research/` (Research outputs)
*   `.../02-analysis/` (Data analysis outputs)

## References
*   **TBTA Source**: `bible-study-tools/tbta/tbta-source/`
*   **Languages**: `bible-study-tools/tbta/languages/`
*   **Features List**: `bible-study-tools/tbta/features/README.md`

## Execution
Do not log progress here. Update the plan at: `/plan/tbta/features/{feature-name}/plan.md`
