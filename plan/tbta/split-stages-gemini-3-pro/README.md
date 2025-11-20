# Planning: Splitting STAGES.md for Modular Agentic Workflow

**Model**: gemini-3-pro
**Date**: 2025-11-20

## Context & Goal
The user wants to refactor the monolithic `STAGES.md` into a modular system (`.instructions-to-build-feature-{model}/`) where each stage is a separate file suitable for a dedicated sub-agent. This is to manage context window limitations and enforce better isolation/focus.

## Analysis of Previous Approaches (Cursor vs ClaudeFlow)
From the `number-systems` analysis:
1.  **Cursor**:
    *   **Good**: Caught data leakage. Strong python scripting (`blind_test_v3.py`).
    *   **Bad**: Documentation drifted from code reality. English-centric validation.
    *   **Lesson**: The new instructions must mandate *automated* checks for data leakage (locked files) and explicitly require checks for language availability *before* generating massive scripts.
2.  **ClaudeFlow**:
    *   **Good**: Honest about data limitations. Product-focused "Tiered" deployment.
    *   **Bad**: "Hallucinated" report existence. Wasted effort on missing languages (Fijian/Slovenian not in eBible).
    *   **Lesson**: The "Analysis" stage must include a "Capabilities Audit" step (using Quote Bible skill) to verify which languages are actually available before hypothesizing about them.

## Structure Plan

### Entry Point
`TBTA-FEATURE-BUILDER-gemini-3-pro.md`: The "overachieving file". Acts as the manager/orchestrator guide.

### Directory: `.instructions-to-build-feature-gemini-3-pro/`

1.  **`README.md` (Core Context)**
    *   Links to `tbta-source`, `languages`, `features`.
    *   Defines the "Philosophy" (LLM-based, generalization, no expert systems).
    *   Lists the stages.

2.  **`01-research.md` (Agent: Researcher)**
    *   TBTA documentation review.
    *   Language family analysis (theoretical).
    *   Arbitrarity classification.

3.  **`02-analysis.md` (Agent: Data Scientist/Linguist)**
    *   **New Workflow**:
        *   Extract TBTA data.
        *   *New*: Align with Strong's (requires smart agent).
        *   *New*: Discovery Audit (Query OT/NT to find *actual* available languages).
        *   *New*: Hypothesis Generation (If feature=X, Language Y should use Word Z).
        *   *New*: Validation Script (Check presence of Word Z in actual verses).
        *   Output: JSONL raw data + Agreement Scorecard.

## Implementation Details for Analysis Stage
The user specifically asked for a workflow that:
1.  Extracts TBTA data (verse, label).
2.  Identifies the specific word/concept (Strongs).
3.  Discovers *available* languages via Quote Bible skill.
4.  Guesses target words for those languages based on TBTA feature.
5.  Validates guesses against actual text.

This shifts the paradigm from "Reading translations to find patterns" to "Predicting translations to validate TBTA".

## Progressive Disclosure
I will ensure files are ≤500 lines (easily done with splitting) and inline key code snippets.

## Actions
1.  Write `TBTA-FEATURE-BUILDER-gemini-3-pro.md`.
2.  Write `.instructions-to-build-feature-gemini-3-pro/README.md`.
3.  Write `.instructions-to-build-feature-gemini-3-pro/01-research.md`.
4.  Write `.instructions-to-build-feature-gemini-3-pro/02-analysis.md`.

