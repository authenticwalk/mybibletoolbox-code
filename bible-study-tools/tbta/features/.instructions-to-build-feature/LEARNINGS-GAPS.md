# Missing Learnings from Past Work

**Purpose**: Checklist of validated patterns from past TBTA features that could improve this plan.

---

## Research Phase (01-research.md)

- [ ] **Cross-linguistic translation validation as PRIMARY approach**
  - **What**: Use 3-9 languages that grammatically encode the feature to discover answers via translator consensus
  - **Why**: 98% inter-translator agreement on Person system; avoids prediction when discovery is possible
  - **Example**: For clusivity, check Indonesian/Tagalog/Fijian translations - if 5/5 agree on inclusive, use that (99% confidence)
  - **Where to add**: After "Scholarly Research" section, before "Arbitrarity Classification"

- [ ] **Check explicit encoding FIRST (but don't extract as solution)**
  - **What**: Verify if feature exists in TBTA YAML structure (for validation), but always develop prediction prompts
  - **Why**: Mood was 100% extractable but goal is prediction for unlabeled 63% of Bible
  - **Example**: "Mood field exists in TBTA → use as answer sheet, but develop prompt from verse text"
  - **Where to add**: In "TBTA Documentation Review" - clarify this is for understanding structure only, not extraction

- [ ] **Gateway features identification**
  - **What**: Identify features that constrain others (e.g., Mood → Aspect, Genre → Structure)
  - **Why**: Proven 100% correlation (Potential mood → Inceptive aspect in 6/6 cases)
  - **Example**: "If feature depends on Mood, check Mood value first before predicting"
  - **Where to add**: New subsection in "TBTA Documentation Review"

---

## Analysis Phase (02-analysis.md)

- [ ] **Rarity principle (baseline distribution)**
  - **What**: Establish dominant value first (e.g., 90.7% Unmarked for Aspect), only override with strong triggers
  - **Why**: Prevents over-predicting rare values; establishes confidence baseline
  - **Example**: "If 90% are Unmarked, default to Unmarked unless 2-3 factors converge for marked value"
  - **Where to add**: In "Hypothesis Generation" section - add baseline distribution analysis

- [ ] **Multi-factor convergence scoring**
  - **What**: Require 2-3 independent factors agreeing before overriding baseline
  - **Why**: 3-factor convergence achieved 100% accuracy for Inceptive aspect
  - **Example**: "Action verb + Potential mood + Near-future time → 95% confidence for Inceptive"
  - **Where to add**: In "Advanced Quantitative Analysis" - add convergence analysis step

- [ ] **Theological edge cases in adversarial test design**
  - **What**: Actively hunt for Trinity, Incarnation, corporate solidarity cases
  - **Why**: These are highest-stakes errors (theological impact) and common failure points
  - **Example**: "Include Gen 1:26 (Trinity), Matt 28:19 (Trinity), John 1:14 (Incarnation) in adversarial set"
  - **Where to add**: In "Validation Script" section - add theological edge case checklist

---

## Algorithm/Experimentation Phase (03-algorithm.md, 03-experimentation.md)

- [ ] **Hierarchical prompting framework**
  - **What**: 5-level hierarchy: Theological → Capability → Discourse → Grammar → Baseline
  - **Why**: Resolved 70%+ of Person cases at Level 1; prioritizes meaning over form
  - **Example**: "Level 1: Does this involve divine prerogative? → Resolves 60-70% of cases"
  - **Where to add**: In "Prompt Engineering" - replace flat analysis with hierarchical structure

- [ ] **Capability analysis as primary filter**
  - **What**: "Can the addressee perform this action?" resolves most ambiguous cases
  - **Why**: Filtered 60%+ of ambiguous situations in Person experiment
  - **Example**: "If addressee cannot participate → EXCLUSIVE; if can participate → continue analysis"
  - **Where to add**: In "Track B: Concise Logic" - add capability check as first filter

- [ ] **Pattern recognition across contexts**
  - **What**: Document established patterns (Divine Speech → EXCLUSIVE, Prayer → EXCLUSIVE of God)
  - **Why**: Once validated, patterns reliably predict similar cases (100% for Divine Speech)
  - **Example**: "Divine Speech pattern: Creation/judgment → EXCLUSIVE (100% reliable)"
  - **Where to add**: In "Track B: Concise Logic" - add pattern library section

- [ ] **Discourse-level context strategy**
  - **What**: For features requiring discourse memory (Participant Tracking, Definiteness), use LLM memory or ±3 verse context
  - **Why**: Participant Tracking achieved 85-90% accuracy with LLM memory approach
  - **Example**: "For Participant Tracking: Use LLM's Bible knowledge + ±3 verses context → 85-90% accuracy"
  - **Where to add**: In "Data Supplementation" - add discourse context enrichment step

- [ ] **Adversarial testing phases**
  - **What**: Three-phase testing: Pattern Discovery (15-20 verses) → Adversarial (10-15 edge cases) → Random (10-15 verses)
  - **Why**: Random should exceed adversarial by 15-25 points; if reversed, signals overfitting
  - **Example**: "Adversarial: 60-70% expected; Random: 80-90% expected; if reversed → algorithm problems"
  - **Where to add**: New section after "Self-Correction Loop" - "Adversarial Testing Protocol"

---

## Common Error Patterns

- [ ] **Theological misunderstanding detection**
  - **What**: Add theological context questions to catch missing divine prerogatives
  - **Why**: Common error pattern - missing that creation is exclusively God's work
  - **Example**: "Error: Missing Trinity context → Fix: Add theological framework questions"
  - **Where to add**: In "Self-Correction Loop" - add error pattern checklist

- [ ] **Morphological ≠ Semantic warning**
  - **What**: Always check semantic analysis before morphological (e.g., Hebrew plural form but singular meaning)
  - **Why**: Common error - following morphology instead of meaning (e.g., "heaven" plural form, singular meaning)
  - **Example**: "Hebrew שָׁמַיִם (dual morphology) → Singular semantics → Use semantic value"
  - **Where to add**: In "Prompt Engineering" - add semantic-first principle

- [ ] **Gateway feature ignored detection**
  - **What**: Check gateway features before predicting constrained features
  - **Why**: Common error - predicting Aspect without checking Mood first
  - **Example**: "Error: Predicted Aspect without checking Mood → Fix: Always check gateway features"
  - **Where to add**: In error analysis section

---

## Testing & Validation

- [ ] **Translation validation as PRIMARY validation method**
  - **What**: Use 5-9 languages encoding the feature to validate predictions
  - **Why**: Translation consensus more reliable than single-source prediction; 98% agreement on Person
  - **Example**: "9/9 translations agree → 99.9% confidence; 5/9 agree → 95% confidence"
  - **Where to add**: In "Validation Script" section - prioritize translation validation over TBTA-only validation

- [ ] **Confidence calibration by agreement level**
  - **What**: Map translation agreement levels to confidence scores
  - **Why**: Provides quantitative confidence metrics (9/9 = 99.9%, 5/9 = 95%)
  - **Example**: "Agreement levels: 9/9 → 99.9%, 8/9 → 99%, 7/9 → 97%, 6/9 → 95%, <5/9 → flag for review"
  - **Where to add**: In "Validation Script" output section

- [ ] **Random vs Adversarial accuracy comparison**
  - **What**: Track both metrics; random should exceed adversarial by 15-25 points
  - **Why**: Reversed pattern signals overfitting (Person: 73% adversarial, 50-60% random = problem)
  - **Example**: "If random < adversarial → overfitting detected → expand training set, reduce specificity"
  - **Where to add**: In "Self-Correction Loop" - add comparison metric

---

## Critical Anti-Patterns (from invalid attempts)

- [ ] **Explicit warning: Never extract from TBTA as solution**
  - **What**: Add red flag checklist: "Extract from TBTA position X" = cheating
  - **Why**: Third time this mistake made; invalidated 3 features
  - **Example**: "❌ 'Extract from TBTA position 7' → This is cheating, not prediction"
  - **Where to add**: In Core Rules section - add "Anti-Pattern Detection" subsection

- [ ] **Goal clarification: PROMPTS not extraction**
  - **What**: Emphasize final deliverable is prompt that works on any verse, not extraction script
  - **Why**: Prevents confusion about what success looks like
  - **Example**: "✅ Success: Prompt predicts from verse text; ❌ Failure: Script extracts from TBTA YAML"
  - **Where to add**: In "Core Rules" - clarify "Predict, Don't Memorize" with examples

---

## Quick Reference Integration

- [ ] **Add "Formula for High Accuracy" quick reference**
  - **What**: Consolidated checklist of all patterns in priority order
  - **Why**: Provides single reference point for implementation
  - **Example**: "1. Translation Validation (if 3+ languages) → 2. Hierarchical Prompts → 3. Multi-Factor Convergence"
  - **Where to add**: New file "QUICK-REFERENCE.md" or appendix in README.md

