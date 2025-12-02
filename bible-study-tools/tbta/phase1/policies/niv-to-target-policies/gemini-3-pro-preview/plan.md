# Plan: Reverse Engineer TBTA Target Language Rules

Goal: Derive rules to convert Bible text (NIV/Original) into TBTA Target English format, using Ruth Chapter 1 as a training ground.

## Approach
1.  **Setup**: Create working directory and plan (Done).
2.  **Iterative Analysis (Ruth 1:1 - 1:5)**:
    *   Fetch Target English for the verse from `https://targets.tabitha.bible`.
    *   Compare with NIV and underlying Hebrew.
    *   Identify transformations (simplifications, explicitation, restructuring).
    *   Hypothesize rules.
    *   Refine rules based on accumulated evidence.
3.  **Rule Synthesis**: Maintain a `rules.md` file that consolidates findings into concise, actionable policies for an LLM.
4.  **Verification**: "Test" the rules by predicting the next verse before seeing it (mental check or explicitly stated).

## Directory Structure
- `bible-study-tools/tbta/phase1/policies/gemini-3-pro-preview/`
    - `plan.md`: This file.
    - `rules.md`: The evolving rule set.
    - `analysis/`: Analysis of individual verses.
        - `Ruth-01-01.md`
        - ...

## Current Focus
- Ruth 1:1 Analysis.

