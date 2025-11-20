# TBTA Feature Builder System

**Version**: 1.0 (Gemini)
**Date**: 2025-11-20
**System Directory**: `.instructions-to-build-feature-gemini-3-pro/`

## Purpose

This document outlines the modular, agent-based workflow for building MyBibleToolbox Translation Assistant (TBTA) features using Large Language Models. It replaces the monolithic `STAGES.md` with a decentralized set of instructions designed to keep context low and precision high.

## The Philosophy

We are rebuilding TBTA (originally an expert system) using LLMs.

- **Goal**: Create a generalized predictive model, not a hardcoded rules engine.
- **Method**: Data-driven discovery. We do not assume we know the rules; we discover them from the data (TBTA corpus + Real World Translations).
- **Constraint**: Strict Train/Test separation. "Looking at the answers" during testing is immediate failure.

## The Workflow (Orchestration)

Each stage below corresponds to a specific instruction file in `.instructions-to-build-feature-gemini-3-pro/`. Assign a dedicated sub-agent to each stage.

### 1. Research & Definition

**Agent**: Researcher / Linguist
**Instructions**: `01-research.md`
**Output**: `features/{feature}/README.md`, `experiments/ARBITRARITY.md`
**Goal**: Define what we are building, who needs it, and why it matters theology.

### 2. Analysis & Hypothesis Validation

**Agent**: Data Scientist / Polyglot
**Instructions**: `02-analysis.md`
**Output**: `experiments/analysis/raw_data.jsonl`, `experiments/analysis/scorecard.md`
**Goal**: quantitatively validate the feature against real-world translations _before_ writing a single prompt.

- _Key Innovation_: Uses "Hypothesis Testing" (If TBTA says X, Fijian should say Y) rather than passive observation.

### 3. Experimentation & Refinement

**Agent**: ML Engineer / Prompt Optimizer
**Instructions**: `03-experimentation.md`
**Output**: `PROMPT.md`, `data/strongs/*-tbta.yaml`
**Goal**: Run parallel experiments (Baseline vs Logic vs Strong's Annotation) to find the optimal prediction method.

### 4. Validation & Review

**Agent**: QA / Critic
**Instructions**: `04-validation.md`
**Goal**: Blind testing and critical peer review.

## How to Start a New Feature

1.  Create directory: `bible-study-tools/tbta/features/{feature-name}/`
2.  Create planning dir: `plan/tbta/features/{feature-name}/`
3.  Initialize `plan/tbta/features/{feature-name}/plan.md`
4.  **Call Agent 1** with context `.instructions-to-build-feature-gemini-3-pro/01-research.md`.

---

_See `.instructions-to-build-feature-gemini-3-pro/README.md` for detailed system rules._
