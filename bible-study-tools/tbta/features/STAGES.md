The following summarizes the correct stages to build a new feature. If you are improving a feature you should validate that it has done all of these stages.

# 1. Research TBTA Documentation

 - [ ] Review the source documentation of TBTA for this feature
   - Official TBTA documentation: See `../tbta-source/README.md` for links to source materials
   - Reference: `/plan/tbta-rebuild-with-llm/FEATURE-SUMMARY.md` for high-level feature overview
 - [ ] Review our TBTA analysis for that feature
   - Check existing feature directory: `/plan/tbta-rebuild-with-llm/features/{feature}/`
   - Review `../learnings/README.md` for transferable patterns
 - [ ] Generate the README.md for the feature with the information learnt about this feature
   - Include: Feature definition, theological/linguistic context, TBTA encoding details
   - Add stage checklist (copy from this file)

# 2. Language Study

 - [ ] Review language families to determine which languages need this feature
   - Check: `../languages/` directory
   - Reference: Language codes and families
   - Consider: Which language families grammatically encode this feature?
 - [ ] Update README.md with language analysis
   - List: Language families that require this feature
   - Note: Languages where feature is grammatically obligatory vs optional
   - Example: Target translation scenarios

# 3. Scholarly and Internet Research

  - [ ] Look for scholarly articles about this subject to get the latest research into it
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
 - [ ] Review `../learnings/README.md` for transferable patterns from other features
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
 - [ ] Update `../learnings/README.md` with transferable patterns:
   - Successful approaches reusable for other features
   - Error analysis techniques
   - Validation strategies
 - [ ] If learnings README exceeds 400 lines, apply progressive disclosure (split into topic files)

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

## Critical Peer Review (4 Subagents)

Launch 4 subagents for independent critical review:

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

 - [ ] **Subagent 6 (Translation Practitioner)**: Assume role of Bible translator in target language
   - **Context**: "I'm translating the Bible into [language with this feature]. I have the TBTA data for this feature."
   - **Practical Questions**:
     - Is this data actually useful for translation decisions?
     - What's helpful vs. confusing in the annotations?
     - What mistakes might I make when using this data?
     - Does the algorithm guidance match real translation challenges?
   - **Test Scenarios**: Pick 5-10 verses and translate them using the TBTA data
     - What went right? (What mistakes did I avoid?)
     - What went wrong? (What errors did I make? Why?)
     - What was missing? (What information did I need but couldn't find?)
     - What was confusing? (What annotations led me astray?)
   - **Language Diversity**: Test with 2-3 different language families
     - Example: Austronesian (has clusivity) vs. Romance (doesn't have clusivity)
     - Do annotations make sense for both marking and non-marking languages?
   - **Report Format**: Create `experiments/TRANSLATOR-IMPACT.md` with findings

## TBTA Reviewer Communication

 - [ ] Create `experiments/TBTA-REVIEW.md` with structured review request (see template below)
 - [ ] Send to TBTA team (if applicable)
 - [ ] Incorporate TBTA feedback into algorithm refinement

**TBTA-REVIEW.md Template**:
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
1. **Annotation Philosophy**: When {specific scenario}, should we annotate based on text-internal discourse structure OR translation guidance?
2. **Edge Case Handling**: For {specific feature}, how should we annotate: {examples}
3. **Value Ambiguity**: When multiple values seem equally valid, what is the decision rule?

### Medium Priority
4. **Cross-Feature Interactions**: How does {this feature} interact with {related feature}?
5. **Genre Handling**: Do annotation rules differ by genre?

## Our Observations & Concerns

### Observation 1: {Pattern we noticed}
- **Data**: We found {pattern} in {n} verses
- **Question**: Is this TBTA's intended approach?
- **Impact**: Affects {aspect of algorithm}

## Labeling Examples for Review

| Verse | Text Snippet | Our Prediction | TBTA Value | Confidence | Notes |
|-------|-------------|----------------|------------|-----------|-------|
| {REF} | "{snippet}" | {value} | {TBTA value} | Low/Med/High | {reason} |

## Our Methodology
- Sample size: {n} verses per value
- Balanced: {OT/NT split}, {genre distribution}
- Algorithm: {brief description}
- Accuracy: {stated}% stated, {dominant}% dominant
- External validation: {if applicable}

## Translation Practitioner Impact

**Languages Tested**: {2-3 language families}
**Verses Translated**: {5-10 sample verses}

### What Worked for Translators:
1. {Annotation that prevented common error}

### What Confused Translators:
1. {Annotation that led to incorrect translation}

### Translation Mistakes Analysis:
- **Mistakes Avoided** (thanks to TBTA): {n} errors prevented
- **Mistakes Made** (despite TBTA): {n} errors introduced
- **Net Benefit**: {Assessment}

## Requested Feedback
1. Are our strategic questions addressing real TBTA annotation principles?
2. Do our observations match your understanding of TBTA methodology?
3. Are any "suspected errors" actually correct TBTA annotations we misunderstood?
4. Should we adjust our algorithm or document as valid divergence?
5. From translator testing: Are confusing cases actually correct annotations needing better documentation?
```

## Practical Application Testing

 - [ ] Create `experiments/TRANSLATOR-IMPACT.md` documenting real-world translation scenarios
 - [ ] Test with both marking and non-marking languages
 - [ ] Identify translation-critical issues
   - What mistakes would a translator make WITHOUT this data?
   - What mistakes might they make WITH this data?
   - What's the net benefit?

**TRANSLATOR-IMPACT.md Template**:
```markdown
# Translation Practitioner Impact Assessment: {Feature Name}

## Executive Summary
- Feature: {feature-name}
- Languages tested: {list 2-3 language families}
- Verses translated: {5-10 sample verses}
- Overall utility: {High/Medium/Low}
- Key findings: {1-sentence summary}

## Translation Scenarios

### Scenario 1: {Language} ({Family})
**Language Profile**:
- Grammatically marks {feature}? {Yes/No}
- Target audience: {context}

**Translation Test**:

| Verse | English | TBTA Value | My Translation | Helped | Confused | Avoided | Made |
|-------|---------|-----------|----------------|--------|----------|---------|------|
| {REF} | "{text}" | {value} | "{translation}" | {useful} | {unclear} | {errors prevented} | {errors introduced} |

**Overall Assessment**:
- **Useful**: {What annotations helped}
- **Confusing**: {What led astray}
- **Missing**: {What was needed}
- **Mistakes Avoided**: {Errors prevented by TBTA}
- **Mistakes Made**: {Errors despite TBTA}

## Cross-Language Patterns

### What Works Across All Languages:
1. {Universally helpful pattern}

### What Doesn't Work:
1. {What confused translators}

## Real Translation Mistakes Analysis

### Mistake Type 1: {Category}
**Example**: {Specific verse}
- **TBTA Value**: {value}
- **What I Translated**: {incorrect}
- **Why I Made Mistake**: {what confused me}
- **Correct Translation**: {should have been}
- **Fix Needed**: {improvement}

## Mistakes Successfully Avoided

### Avoidance 1: {Error type}
**Example**: {Verse}
- **Common Mistake**: {What translators typically get wrong}
- **TBTA Guidance**: {What prevented this}
- **Why TBTA Helped**: {Specific insight}

## Recommendations for Algorithm Improvement

### Critical (Would prevent translation errors):
1. {Specific improvement}

### Important (Would reduce confusion):
1. {Clarity improvement}

## Production Readiness from Translator Perspective

**Would I recommend this to translation teams?** {Yes/No/With caveats}
**Reasoning**: {Why or why not}
**Minimum Viable**: {What must be fixed}
**Ideal State**: {What would make this excellent}
```

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
 - [ ] Peer review complete (4 critical reviews passed)
   - [ ] Theological reviewer approval
   - [ ] Linguistic reviewer approval
   - [ ] Methodological reviewer approval
   - [ ] Translation practitioner approval
 - [ ] Error analysis documented (6-step process for all failures)
 - [ ] Locked predictions throughout (git commits present)
 - [ ] External validation conducted (if applicable)
 - [ ] Practical application testing complete (TRANSLATOR-IMPACT.md)
   - [ ] Tested with marking language(s)
   - [ ] Tested with non-marking language(s)
   - [ ] Net benefit is positive (more mistakes avoided than introduced)
   - [ ] Translation teams would recommend using this data
 - [ ] TBTA review feedback integrated (if applicable)
 - [ ] README.md updated with final status
 - [ ] Transferable insights added to `../learnings/README.md`

**Only when all above complete**: Mark feature as production ready
