The following summarizes the correct stages to build a new feature.  If you are improving a feature you should validate that it has done all of these stages

# 1. Research TBTA Documentation

 - [ ] Review the source documentation of TBTA for this feature
   - Official TBTA documentation: See `/plan/tbta-rebuild-with-llm/README.md` for links to source materials
   - Reference: [FEATURE-SUMMARY.md](FEATURE-SUMMARY.md) for high-level feature overview
 - [ ] Review our TBTA analysis for that feature
   - Check existing feature directory: `/plan/tbta-rebuild-with-llm/features/{feature}/`
   - Review [CROSS-FEATURE-LEARNINGS.md](CROSS-FEATURE-LEARNINGS.md) for transferable patterns
 - [ ] Generate the README.md for the feature with the information learnt about this feature
   - Include: Feature definition, theological/linguistic context, TBTA encoding details
   - Add stage checklist (copy from this file)

# 2. Language Study

 - [ ] Review language families to determine which languages need this feature
   - Check: `/languages/families/` directory (when available)
   - Reference: `src/constants/languages.tsv` for available language codes
   - Consider: Which language families grammatically encode this feature?
 - [ ] Update README.md with language analysis
   - List: Language families that require this feature
   - Note: Languages where feature is grammatically obligatory vs optional
   - Example: Target translation scenarios

# 3. Scholarly and Internet Research

  - [ ] Look for scholarily articles about this subject to get the latest research into it
  - [ ] Look into general web information
  - [ ] Update the README

# 4. Generate a Proper Test Set

**CRITICAL**: This stage MUST be done in a subagent to prevent seeing the answers!

## Dataset Requirements

**Data Source**: Use only verses that have TBTA data (complete annotation)

**Sample Size**: 100 verses per value minimum
- Small datasets (<50 verses) cannot support claims of 100% accuracy
- Need statistical power to distinguish algorithm quality from chance

**Balanced Sampling** across multiple dimensions:
1. **Testament**: Proportional OT/NT distribution
2. **Genre**: Narrative, Poetry, Prophecy, Epistle, etc.
3. **Book Distribution**: Avoid concentration in single book
4. **Difficulty**: Include both typical cases AND adversarial cases

## Adversarial Selection Strategy

For the **test set** (30%), deliberately include challenging cases:
- Edge cases where multiple values might apply
- Verses with theological ambiguity
- Contexts where annotation rules might conflict
- Genre boundaries (e.g., quoted speech, vision contexts)
- Translation-divergent passages
- Rare or complex discourse structures

**Purpose**: Find algorithm blind spots, not just confirm what works

## External Validation Preparation

**During data construction**, identify external validation opportunities:
 - [ ] For features with observable translation differences (clusivity, tense, etc.):
   - List which languages/language families grammatically mark this feature
   - Note which Bible translations exist in these languages
   - Document expected translation patterns per value
   - This enables validation against real translator decisions, not just TBTA
 - [ ] Store this information in train.yaml metadata for reference

## Subagent Script Requirements

Create a python script (or use existing tools) to:
 - [ ] Clone/access TBTA data repository
 - [ ] Loop through all TBTA files looking for this feature
 - [ ] Filter to verses with complete TBTA data only
 - [ ] Generate frequency counts for each VALUE this feature can have
 - [ ] Sample with stratification:
   - Testament (OT/NT)
   - Genre (narrative/poetry/prophecy/epistle/etc.)
   - Difficulty (typical + adversarial)
 - [ ] Split into train (40%), test (30%), validate (30%)
 - [ ] Generate YAML files with structure:
   ```yaml
   feature: {feature-name}
   value: {specific-value}
   total_verses: {count}
   distribution:
     OT: {count}
     NT: {count}
   genres:
     narrative: {count}
     poetry: {count}
     prophecy: {count}
     epistle: {count}
   external_validation:
     languages: [list of languages that mark this feature]
     families: [language families with this feature]
   verses:
     - reference: "{BOOK} {chapter}:{verse}"
       tbta_value: "{value}"
       genre: "{genre}"
       difficulty: "typical|adversarial"
       notes: "Why adversarial (if applicable)"
   ```
 - [ ] **Main agent**: Receive only file paths, never see test/validate data
 - [ ] Store files in: `features/{feature}/experiments/train.yaml`, `test.yaml`, `validate.yaml`
 - [ ] Generate TBTA-REVIEW.md template (see Stage 6 below)

# 5. Propose your Hypothesis and First Prompt

## Analysis Phase
 - [ ] Review the train.yaml file and the source TBTA files for the training verses
 - [ ] Review `CROSS-FEATURE-LEARNINGS.md` for transferable patterns from other features
 - [ ] Create `experiments/ANALYSIS.md` with up to 12 different approaches
   - Weight pros and cons of each approach
   - Consider: theological factors, grammatical cues, discourse patterns, genre signals
   - Identify which approaches might work best for this feature

## First Prompt Development
 - [ ] Given the top methods, create `experiments/PROMPT1.md` with most likely approach
 - [ ] **LOCKED PREDICTIONS**: Before testing against TBTA, commit predictions to git
   ```bash
   # Create predictions file first
   # Commit: "feat({feature}): lock PROMPT1 predictions before TBTA check"
   # Push to remote
   # Record commit SHA in LEARNINGS.md
   ```
 - [ ] Apply prompt to each verse in test set, predicting main value
   - If one clear option: predict only the value
   - If multiple good options: predict dominant with rationale (which may include language family preferences)

## Success Criteria & Iteration

**Accuracy Targets** (with sufficient sample size ≥100 verses):
 - [ ] **Stated values** (single answer): 100% accuracy goal
   - The text is God's inerrant word - less than 100% means we're missing something
   - **Caveat**: Small datasets (<50 verses) cannot reliably demonstrate 100% - need larger samples
 - [ ] **Dominant values** (primary + rationale): 95% accuracy goal

## Systematic Error Analysis (6-Step Process)

For EVERY error, follow this rigorous debugging process:

 - [ ] **Step 1: Verify Data Accuracy**
   - Check TBTA annotation is correct for this verse
   - Verify verse reference matches (no transcription errors)
   - Confirm value encoding is what you think it is

 - [ ] **Step 2: Re-analyze Source Text**
   - Read Greek/Hebrew if applicable
   - Check multiple English translations
   - Look for linguistic details missed initially

 - [ ] **Step 3: Re-analyze Context**
   - Read surrounding verses (±3 verses minimum)
   - Check chapter context
   - Consider book-level patterns

 - [ ] **Step 4: Cross-Reference Sources**
   - Check 3+ Bible translations
   - Review LXX/Vulgate if OT
   - Consult commentaries if available

 - [ ] **Step 5: Test Hypotheses**
   - Why did algorithm predict X when answer is Y?
   - What rule/pattern led to wrong prediction?
   - What should algorithm have noticed?
   - Would a different approach have succeeded?

 - [ ] **Step 6: Final Determination**
   - Is TBTA annotation correct? (95%+ of time: yes)
   - Is this a valid perspective difference? (rare, document carefully)
   - Is this a potential TBTA annotation error? (very rare, flag for review)
   - What algorithmic change would fix this?

 - [ ] Document analysis in `experiments/LEARNINGS.md` with:
   - Verse reference
   - Predicted vs. actual
   - Error category
   - Root cause
   - Proposed fix

## Iterative Refinement

 - [ ] **PROMPT2.md**: Focus on different approaches first (try alternatives before refining)
 - [ ] **PROMPT3+.md**: Refine winning approach using:
   - Prompt engineering (clearer language)
   - Examples (few-shot learning)
   - Logic flowcharts (decision trees)
   - Minimal prompt optimization (remove unnecessary complexity)
 - [ ] Repeat until you cannot achieve better results
 - [ ] Each iteration: Lock predictions → Test → Analyze errors → Refine
 - [ ] Typical iterations: 3-5 prompts (v1.0 → v2.0 → v2.1 etc.)
 - [ ] Stop when: Accuracy plateaus or reaches target

## External Validation (If Applicable)

 - [ ] If feature has observable translation differences:
   - Check predictions against real Bible translations in marking languages
   - Compare with expected patterns from train.yaml metadata
   - Document agreement rate (target: 95%+ across languages)
   - Note any systematic divergences (may indicate valid perspective differences)
 - [ ] Store results in `experiments/EXTERNAL-VALIDATION.md`

## Documentation

 - [ ] Summarize top learnings in `experiments/LEARNINGS.md`:
   - What worked best and why
   - Common error patterns
   - 6-step analysis results for failures
   - Algorithm evolution (v1 → v2 → v3...)
 - [ ] Update `CROSS-FEATURE-LEARNINGS.md` with transferable patterns:
   - Successful approaches reusable for other features
   - Error analysis techniques
   - Validation strategies
 - [ ] If CROSS-FEATURE-LEARNINGS.md exceeds 400 lines, apply progressive disclosure (split into topic files)

# 6. Test Against Validate Set & Peer Review

## Subagent Validation (Blind Testing)

 - [ ] **Subagent 1**: Apply best prompt to validate.yaml (blind - never sees answers)
   - Generate predictions file
   - Lock predictions with git commit
   - Return only predictions file path to main agent

 - [ ] **Subagent 2**: Score predictions against TBTA
   - Load validate.yaml (has TBTA answers)
   - Load predictions file
   - Calculate accuracy (stated values, dominant values)
   - Identify errors for analysis
   - Return only: accuracy percentages + list of error verse references (NOT the answers)

 - [ ] **Main agent**: Analyze errors using 6-step process
   - If accuracy < 95%: return to Stage 5, refine prompt
   - If accuracy ≥ 95%: proceed to peer review

## Critical Peer Review (3 Subagents)

Launch 3 subagents for independent critical review:

 - [ ] **Subagent 3 (Theological Reviewer)**: Assume junior wrote this with theological blind spots
   - Review prompt for theological soundness
   - Check if prompt handles key doctrinal distinctions
   - Look for oversimplifications or category errors
   - Test edge cases: Does prompt handle divine speech correctly? Prayer contexts? Prophetic literature?

 - [ ] **Subagent 4 (Linguistic Reviewer)**: Assume junior missed linguistic nuances
   - Review prompt for linguistic accuracy
   - Check if prompt handles genre differences
   - Look for grammar vs. semantics confusion
   - Test discourse complexity: Quoted speech? Multiple speakers? Narrative vs. direct address?

 - [ ] **Subagent 5 (Methodological Reviewer)**: Assume junior cut corners
   - Check sample size adequacy (is n=100+ per value?)
   - Verify balanced sampling (OT/NT, genres)
   - Review error analysis rigor (6-step process followed?)
   - Check locked predictions discipline (git commits present?)
   - Verify external validation attempted (if applicable)

## TBTA Reviewer Communication

 - [ ] Create `experiments/TBTA-REVIEW.md` with:

```markdown
# TBTA Team Review Request: {Feature Name}

## Executive Summary
- Feature: {feature-name}
- Values analyzed: {list values}
- Sample size: {n} verses
- Algorithm accuracy: {stated}% / {dominant}%
- Review purpose: Validate our understanding of TBTA annotation principles

## Strategic Questions (Priority Order)

### High Priority
1. **Annotation Philosophy**: When {specific scenario}, should we annotate based on:
   - Text-internal discourse structure (speaker→listener relationship), OR
   - Translation guidance (speaker→reader relationship)?
   - Example: Genesis 1:26 "Let us make man"

2. **Edge Case Handling**: For {specific feature}, how should we annotate:
   - {Edge case 1 with example}
   - {Edge case 2 with example}
   - {Edge case 3 with example}

3. **Value Ambiguity**: When multiple values seem equally valid, what is the decision rule?
   - {Specific ambiguous example from our data}

### Medium Priority
4. **Cross-Feature Interactions**: How does {this feature} interact with {related feature}?
   - Example: {specific verse showing interaction}

5. **Genre Handling**: Do annotation rules differ by genre (narrative vs. poetry vs. epistle)?
   - We observed {pattern} - is this intentional?

## Our Observations & Concerns

### Observation 1: {Pattern we noticed}
- **Data**: We found {specific pattern} in {n} verses
- **Question**: Is this TBTA's intended annotation approach?
- **Impact**: If yes, affects {aspect of algorithm}

### Observation 2: {Divergence we found}
- **Data**: Our algorithm predicts {X} but TBTA shows {Y} in these cases:
  - {Verse 1}: {brief description}
  - {Verse 2}: {brief description}
- **Question**: Is this a valid perspective difference, or are we misunderstanding TBTA's annotation principle?

### Concern: {Potential issue}
- **Issue**: We suspect {possible annotation inconsistency}
- **Evidence**: Compare {verse 1} with {verse 2} - seem contradictory
- **Request**: Please clarify annotation rule

## Labeling Examples for Review

**Instructions**: Please re-label these verses if our understanding is incorrect.

| Verse | Text Snippet | Our Prediction | TBTA Value | Our Confidence | Notes |
|-------|-------------|----------------|------------|----------------|-------|
| {REF} | "{snippet}" | {our value} | {TBTA value} | Low | We suspect TBTA may be {alternative} because {reason} |
| {REF} | "{snippet}" | {our value} | {TBTA value} | Medium | Theological ambiguity - could be {alternative}? |
| {REF} | "{snippet}" | {our value} | {TBTA value} | High | Strong divergence - please explain annotation rationale |

**Priority for Review**: {Top 5 verses where we're most uncertain}

## Our Methodology (For Context)

- Sample size: {n} verses per value
- Balanced: {OT/NT split}, {genre distribution}
- Algorithm: {brief description of approach}
- Accuracy: {stated}% stated, {dominant}% dominant
- External validation: {if applicable - languages checked, agreement rate}

## Requested Feedback

1. Are our strategic questions addressing real TBTA annotation principles?
2. Do our observations match your understanding of TBTA methodology?
3. Are any of our "suspected errors" actually correct TBTA annotations we misunderstood?
4. Should we adjust our algorithm to match TBTA perspective, or document as valid divergence?
5. Any systematic patterns we're missing in our approach?

---

**Contact**: {Your information}
**Date**: {YYYY-MM-DD}
**Feature Status**: Stage 6 validation in progress
```

 - [ ] Send TBTA-REVIEW.md to TBTA team (if applicable)
 - [ ] Incorporate TBTA feedback into algorithm refinement

## Integration & Iteration

 - [ ] Review all peer review feedback
 - [ ] Categorize feedback:
   - **Critical**: Must fix before production
   - **Important**: Should fix if possible
   - **Nice-to-have**: Consider for future iterations

 - [ ] If material feedback exists: Return to Stage 5
   - Refine prompt based on feedback
   - Re-test on validate set
   - Repeat peer review

 - [ ] When peer reviewers are satisfied (non-material feedback only):
   - Mark Stage 6 complete
   - Document final accuracy
   - Update README.md with production status

## Production Readiness Checklist

 - [ ] Accuracy ≥ 95% on validate set (≥100 verses)
 - [ ] Peer review complete (3 critical reviews passed)
 - [ ] Error analysis documented (6-step process for all failures)
 - [ ] Locked predictions throughout (git commits present)
 - [ ] External validation conducted (if applicable)
 - [ ] TBTA review feedback integrated (if applicable)
 - [ ] README.md updated with final status
 - [ ] CROSS-FEATURE-LEARNINGS.md updated with transferable insights

**Only when all above complete**: Mark feature as production ready

