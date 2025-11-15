The following summarizes the correct stages to build a new feature. If you are improving a feature you should validate that it has done all of these stages.

# 1. Research TBTA Documentation

Review the source documentation of TBTA for this feature:
- Official TBTA documentation: See `../tbta-source/README.md` for links to source materials
- Check existing feature directory for this feature

Generate the README.md for the feature with the information learnt:
- Include: Feature definition, theological/linguistic context, TBTA encoding details
- Add stage checklist (copy from this file)

# 2. Language Study

Review language families to determine which languages need this feature:
- Check: `../languages/` directory
- Reference: Language codes and families
- Consider: Which language families grammatically encode this feature?

Update README.md with language analysis:
- List: Language families that require this feature
- Note: Languages where feature is grammatically obligatory vs optional
- Example: Target translation scenarios

# 3. Scholarly and Internet Research

- Look for scholarly articles about this subject to get the latest research into it
- Look into general web information
- Update the README

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

## External Validation Preparation (Thesis Approach)

**During data construction**, build the foundation for discovering answers from real translations:
- For features with observable translation differences (clusivity, tense, etc.):
  - **Primary**: List which languages/language families grammatically mark this feature
  - **Priority**: Identify Bible translations in those languages, preferring:
    1. Same language family as target translation
    2. Translations from same source lineage (e.g., all derived from Indonesian, Swahili, French, etc.)
    3. Translations from source text (Greek/Hebrew) by local translators
  - **Translation Database**: For each marking language, document:
    - Which Bible translations exist (name, version, year)
    - Source lineage (derived from what language/translation?)
    - Language family classification
    - Availability/access method
  - **Thesis Application**: This enables DISCOVERING the answer by analyzing what real translators did, not just validating accuracy
- Store this information in train.yaml metadata for cross-linguistic validation

## Data Extraction Process

A subagent should extract TBTA data and create stratified samples:

**TBTA Analysis Script responsibilities**:
- Clone/access TBTA data repository
- Loop through all TBTA files looking for this feature
- Filter to verses with complete TBTA data only
- Generate frequency counts for each VALUE this feature can have

**LLM responsibilities** (subagent with access to train data only):
- Sample with stratification across Testament (OT/NT), Genre (narrative/poetry/prophecy/epistle/etc.), and Difficulty (typical + adversarial)
- Identify which languages/families mark this feature
- Classify verses by genre and difficulty
- Add explanatory notes for adversarial cases
- Split into train (40%), test (30%), validate (30%)
- 

**Output YAML structure**:
```yaml
feature: {feature-name}
value:
  - specific_value: {specific-value}
    total_verses: {count}
    distribution:
      OT: {count}
      NT: {count}
      Books: [list of counts per book]
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

**Main agent**: Receives only file paths, never sees test/validate data. Files stored in: `features/{feature}/experiments/train.yaml`, `test.yaml`, `validate.yaml`

# 5. Propose your Hypothesis and First Prompt

## Analysis Phase
- Review the train.yaml file and the source TBTA files for the training verses
- Review `../learnings/README.md` for transferable patterns from other features
- Create `experiments/ANALYSIS.md` with up to 12 different approaches
  - Weight pros and cons of each approach
  - Consider: theological factors, grammatical cues, discourse patterns, genre signals
  - Identify which approaches might work best for this feature

## First Prompt Development
- Given the top methods, create `experiments/PROMPT1.md` with most likely approach
- **LOCKED PREDICTIONS**: Before testing against TBTA, commit predictions to git
  ```bash
  # Create predictions file first
  # Commit: "feat({feature}): lock PROMPT1 predictions before TBTA check"
  # Push to remote
  # Record commit SHA in LEARNINGS.md
  ```
- Apply prompt to each verse in test set, predicting main value
  - If one clear option: predict only the value
  - If multiple good options: predict dominant with rationale (which may include language family preferences)

## Success Criteria & Iteration

**Accuracy Targets** (with sufficient sample size ≥100 verses):
- **Stated values** (single answer): 100% accuracy goal
  - The text is God's inerrant word - less than 100% means we're missing something
  - **Caveat**: Small datasets (<50 verses) cannot reliably demonstrate 100% - need larger samples
- **Dominant values** (primary + rationale): 95% accuracy goal

## Systematic Error Analysis (6-Step Process)

For EVERY error, follow this rigorous debugging process:

**Step 1: Verify Data Accuracy**
- Check TBTA annotation is correct for this verse
- Verify verse reference matches (no transcription errors)
- Confirm value encoding is what you think it is

**Step 2: Re-analyze Source Text**
- Read Greek/Hebrew if applicable
- Check multiple translations
- Look for linguistic details missed initially

**Step 3: Re-analyze Context**
- Read surrounding verses (±3 verses minimum)
- Check chapter context
- Consider book-level patterns

**Step 4: Cross-Reference Sources**
- Check 3+ Bible translations
- Review LXX/Vulgate if OT
- Consult commentaries if available
- **ATTRIBUTION**: URL-templatable sources go in ATTRIBUTION.md (BibleHub, StudyLight, etc.)
- **One-off sources**: Add citation at bottom of individual YAML file (unique articles, specific blog posts)

**Step 5: Test Hypotheses**
- Why did algorithm predict X when answer is Y?
- What rule/pattern led to wrong prediction?
- What should algorithm have noticed?
- Would a different approach have succeeded?

**Step 6: Final Determination**
- Is TBTA annotation correct? (95%+ of time: yes)
- Is this a valid perspective difference? (rare, document carefully)
- Is this a potential TBTA annotation error? (very rare, flag for review)
- What algorithmic change would fix this without overfitting on this error

Document analysis in `experiments/LEARNINGS.md` with:
- Verse reference
- Predicted vs. actual
- Error category
- Root cause
- Proposed fix

## Iterative Refinement

- **PROMPT2.md**: Focus on different approaches first (try alternatives before refining)
- **PROMPT3+.md**: Refine winning approach using:
  - Prompt engineering (clearer language)
  - Examples (few-shot learning)
  - Logic flowcharts (decision trees)
  - Minimal prompt optimization (remove unnecessary complexity)
- Repeat until you cannot achieve better results
- Each iteration: Lock predictions → Test → Analyze errors → Refine
- Typical iterations: 3-5 prompts (v1.0 → v2.0 → v2.1 etc.)
- Stop when: Accuracy plateaus or reaches target

## Cross-Linguistic Translation Validation (Thesis Approach)

**Philosophy**: "There is nothing new under the sun" - with ~1000 Bible translations, someone has already dealt with your unique linguistic feature. The key is analyzing those translations to discover which ones reveal the answer.

**For features with observable translation differences** (clusivity, tense, number distinctions, etc.):

### Step 1: Identify Marking Languages (from Stage 2/4)
- Which languages grammatically require this feature?
- Which language families share this requirement?
- Example: Dual number → many Austronesian, Polynesian languages

### Step 2: Find & Prioritize Bible Translations
**Preference order for target language X:**
1. **Same language family** (share grammatical patterns)
2. **Same source lineage** (translated from same intermediate language)
   - Example: Many minority languages translate from Indonesian, Swahili, French, German
   - Shared source → similar translation decisions
3. **Direct from source text** (Greek/Hebrew by local translators)

**Build translation database:**
- Translation name, version, year
- Language family classification
- Source lineage (from Greek/Hebrew? Or from Indonesian/Swahili/etc.?)
- Access method (online, physical copy, API)

### Step 3: Cross-Linguistic Analysis Per Test Verse
For each verse in test/validate set:

**a. Check what real translators did:**
- Query all marking-language translations for this verse
- Extract how each translation handled this feature
- Document the translation decisions

**b. When translations AGREE (90%+ consensus):**
- **High confidence**: This is likely the correct answer
- **Document**: List which translations agree + their language families
- **Use as validation**: Does our algorithm match this consensus?

**c. When translations DISAGREE (split decision):**
- **Analyze WHY** using these factors:
  - **Cultural context**: Different cultures may interpret differently
  - **Linguistic structure**: Language family differences
  - **Source lineage**: Did they translate from different sources?
  - **Theological tradition**: Different Christian traditions
  - **Genre understanding**: Different narrative vs. poetry interpretation
- **Document divergence patterns**: Which families agree? Which disagree?
- **Make informed decision**: Based on analysis, which translation is most likely correct for THIS context?

**d. When translations are UNAVAILABLE or UNCLEAR:**
- Flag for manual review
- Document what languages/families are missing
- Note limitations of validation for this verse

### Step 4: Document Results in `experiments/CROSS-LINGUISTIC-VALIDATION.md`

```markdown
# Cross-Linguistic Translation Validation: {Feature Name}

## Translation Database
- Total translations analyzed: {count}
- Language families represented: {list}
- Source lineages: {Greek/Hebrew direct: X, Indonesian-derived: Y, etc.}

## Test Verse Results (Sample)

### High Agreement Verses (90%+ consensus)
| Verse | Our Prediction | Translation Consensus | Agreement Rate | Validating Translations |
|-------|----------------|---------------------|----------------|------------------------|
| {REF} | {value} | {value} | 95% (19/20) | Fijian, Samoan, Tongan, Māori... |

### Divergence Verses (split decision)
| Verse | Our Prediction | Translation Split | Analysis | Decision |
|-------|----------------|------------------|----------|----------|
| {REF} | {value} | Austronesian: {valueA}, Mayan: {valueB} | Different cultural context for kinship terms | Prefer Austronesian (same family as target) |

## Overall Validation Metrics
- **Agreement rate**: {X}% (our predictions match translation consensus)
- **High-confidence verses** (90%+ translation agreement): {Y}%
- **Divergence verses** (requiring analysis): {Z}%
- **Unavailable/unclear**: {W}%

## Patterns Discovered
- **Cultural factors**: {What cultural differences affected translations?}
- **Language family patterns**: {Which families consistently agreed?}
- **Source lineage effects**: {Did Indonesian-derived differ from Greek-derived?}

## Thesis Application Success
- **Answers discovered from translations**: {count of verses where translations revealed the answer}
- **Algorithm improvements**: {How translation analysis improved our algorithm}
- **Remaining uncertainties**: {Verses where even translations disagreed}
```

### Step 5: Integrate Learnings into Algorithm
- **When translations agree with TBTA**: Confirms our approach
- **When translations disagree with TBTA**: Investigate carefully
  - Is TBTA correct but translations got it wrong?
  - Is this a valid perspective difference?
  - Does this reveal an algorithm blind spot?
- **When translations reveal patterns we missed**: Update algorithm to capture this

### Success Criteria
- **Translation agreement rate**: 90%+ (our predictions match real translator decisions)
- **High-confidence coverage**: 80%+ of verses have clear translation consensus
- **Divergence understanding**: All disagreements analyzed and documented
- **Net benefit**: Translation analysis improved algorithm accuracy

**Purpose**: Not just validation, but DISCOVERY - let the wisdom of 1000+ translations guide us to the correct answer.

## Documentation

Summarize top learnings in `experiments/LEARNINGS.md`:
- What worked best and why
- Common error patterns
- 6-step analysis results for failures
- Algorithm evolution (v1 → v2 → v3...)

Update `../learnings/README.md` with transferable patterns:
- Successful approaches reusable for other features
- Error analysis techniques
- Validation strategies
- If learnings README exceeds 400 lines, apply progressive disclosure - try reducing duplicates aggregating first then (split into topic files if still too large)

# 6. Test Against Validate Set & Peer Review

## Subagent Validation (Blind Testing)

**Subagent 1**: Apply best prompt to validate.yaml (blind - never sees answers)
- Generate predictions file
- Lock predictions with git commit
- Return only predictions file path to main agent

**Subagent 2**: Score predictions against TBTA
- Load validate.yaml (has TBTA answers)
- Load predictions file
- Calculate accuracy (stated values, dominant values)
- Identify errors for analysis
- Return only: accuracy percentages + list of error verse references (NOT the answers)

**Main agent**: Analyze errors using 6-step process
- If accuracy < 95%: return to Stage 5, refine prompt
- If accuracy ≥ 95%: proceed to peer review

## Critical Peer Review (4 Subagents)

Launch 4 subagents for independent critical review:

**Subagent 3 (Theological Reviewer)**: Assume junior wrote this with theological blind spots
- Review prompt for theological soundness
- Check if prompt handles key doctrinal distinctions
- Look for oversimplifications or category errors
- Consider how translators might accidentally create theological issues
- Test edge cases: Does prompt handle divine speech correctly? Prayer contexts? Prophetic literature?

**Subagent 4 (Linguistic Reviewer)**: Assume junior missed linguistic nuances
- Review prompt for linguistic accuracy
- Check if prompt handles genre differences
- Look for grammar vs. semantics confusion
- Apply best practices, standards, edge cases in linguistics
- Consider for what languages will this not work and why?
- Test discourse complexity: Quoted speech? Multiple speakers? Narrative vs. direct address?

**Subagent 5 (Methodological Reviewer)**: Assume junior cut corners
- Check sample size adequacy (is n=100+ per value?)
- Verify balanced sampling (OT/NT, genres)
- Review error analysis rigor (6-step process followed?)
- Check locked predictions discipline (git commits present?)
- Verify external validation attempted (if applicable)

**Subagent 6 (Translation Practitioner)**: Assume role of Bible translator in target language
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

When significant confusion or divergence exists, create a concise `experiments/TBTA-REVIEW.md` focusing only on specific unclear cases:

```markdown
# TBTA Review Request: {Feature Name}

**Feature**: {feature-name}
**Algorithm Accuracy**: {stated}% / {dominant}%

## Key Questions

1. **Annotation Philosophy**: {Specific unclear scenario}
   - Example: {verse reference}
   - Question: {specific question about annotation approach}

2. **Edge Cases**: {List 2-3 most confusing cases}
   - {Verse + specific question}

## Divergence Examples

| Verse | Our Prediction | TBTA Value | Question |
|-------|----------------|------------|----------|
| {REF} | {our value} | {TBTA value} | {Why we're uncertain} |

## Translator Impact

**What confused translators**: {Brief summary of translation testing issues}
**Question**: Are these annotations correct but need better documentation?

---
**Contact**: {Your information}
**Date**: {YYYY-MM-DD}
```

## Practical Application Testing

Create `experiments/TRANSLATOR-IMPACT.md` documenting real-world translation scenarios:

```markdown
# Translation Practitioner Impact Assessment: {Feature Name}

## Executive Summary
- Feature: {feature-name}
- Languages tested: {list 2-3 language families}
- Verses translated: {5-10 sample verses}
- Overall utility: {High/Medium/Low}
- Key findings: {1-sentence summary}
- **Note**: AI simulation using {model-name-and-version}

## Translation Scenarios

### Scenario 1: {Language Name} ({Language Family})
**Language Profile**:
- Does this language grammatically mark {feature}? {Yes/No}
- If yes: How? {brief description}
- Target audience: {Bible translation project context}

**Translation Test** (Pick 3-5 verses from validate set):

| Verse | English Text | TBTA Value | My Translation | What Helped | What Confused | Mistakes Avoided | Mistakes Made |
|-------|-------------|------------|----------------|-------------|---------------|------------------|---------------|
| {REF} | "{snippet}" | {value} | "{my translation}" | {What was useful} | {What was unclear} | {Errors prevented} | {Errors introduced} |

**Overall Assessment**:
- **Useful**: {What annotations helped most}
- **Confusing**: {What led me astray}
- **Missing**: {What I needed but didn't have}
- **Mistakes Avoided**: {Specific translation errors prevented by TBTA data}
- **Mistakes Made**: {Errors I made despite (or because of) TBTA data}

### Scenario 2: {Different Language} ({Different Family})
[Repeat structure above]

### Scenario 3: Non-Marking Language (e.g., English, Spanish)
**Question**: If my language doesn't grammatically mark this feature, is TBTA data still useful?

**Translation Test**:
[Test how annotations help even when language doesn't require explicit marking]

## Cross-Language Patterns

### What Works Across All Languages:
1. {Pattern 1: What was universally helpful}
2. {Pattern 2: What avoided common mistakes}
3. {Pattern 3: What clarified ambiguity}

### What Doesn't Work:
1. {Issue 1: What confused translators}
2. {Issue 2: What led to mistakes}
3. {Issue 3: What was irrelevant or misleading}

## Real Translation Mistakes Analysis

### Mistake Type 1: {Category}
**Example**: {Specific verse where translator made error}
- **TBTA Value**: {what TBTA said}
- **What I Translated**: {incorrect translation}
- **Why I Made Mistake**: {What in TBTA data confused me or what was missing}
- **Correct Translation**: {what it should have been}
- **Fix Needed**: {How algorithm/annotations should improve}

### Mistake Type 2: {Category}
[Repeat structure]

## Mistakes Successfully Avoided

### Avoidance 1: {Specific error type}
**Example**: {Verse where TBTA data prevented common error}
- **Common Mistake**: {What translators typically get wrong}
- **TBTA Guidance**: {What annotation prevented this}
- **My Translation**: {Correct result}
- **Why TBTA Helped**: {Specific insight that made difference}

## Recommendations for Algorithm Improvement

### Critical (Would prevent translation errors):
1. {Specific improvement to prevent Mistake Type 1}
2. {Specific improvement to prevent Mistake Type 2}

### Important (Would reduce confusion):
1. {Clarity improvement}
2. {Additional context needed}

### Nice-to-have (Would enhance usability):
1. {Convenience feature}

## Production Readiness from Translator Perspective

**Would I recommend this to translation teams?** {Yes/No/With caveats}

**Reasoning**: {Why or why not, what needs to change}

**Minimum Viable**: {What must be fixed before this is usable}

**Ideal State**: {What would make this truly excellent for translators}
```

Test with both marking and non-marking languages:
- Marking language: Language that grammatically requires this feature
- Non-marking language: Language that doesn't grammatically distinguish this feature
- Document whether annotations are useful for both

Identify translation-critical issues:
- What mistakes would a translator make WITHOUT this data?
- What mistakes might they make WITH this data?
- What's the net benefit?

## Integration & Iteration

Review all peer review feedback and categorize:
- **Critical**: Must fix before production
- **Important**: Should fix if possible
- **Nice-to-have**: Consider for future iterations

If material feedback exists: Return to Stage 5
- Refine prompt based on feedback
- Re-test on validate set
- Repeat peer review

When peer reviewers are satisfied (non-material feedback only):
- Mark Stage 6 complete
- Document final accuracy
- Update README.md with production status

## Production Readiness Checklist

- Accuracy ≥ 100% on validate set for claims (≥100 verses)
- Peer review complete (4 critical reviews passed)
  - Theological reviewer approval
  - Linguistic reviewer approval
  - Methodological reviewer approval
  - Translation practitioner approval
- Error analysis documented (6-step process for all failures)
- Locked predictions throughout (git commits present)
- **Cross-Linguistic Translation Validation complete (Thesis Approach)**
  - Translation database built (language families, source lineages documented)
  - Test verses analyzed against real translations
  - Agreement rate ≥ 90% (our predictions match translator consensus)
  - High-confidence coverage ≥ 80% (verses with clear translation consensus)
  - Divergences analyzed (cultural, linguistic, source lineage factors documented)
  - Learnings integrated into algorithm (translation patterns incorporated)
  - Results documented in `experiments/CROSS-LINGUISTIC-VALIDATION.md`
- Practical application testing complete (TRANSLATOR-IMPACT.md)
  - Tested with marking language(s)
  - Tested with non-marking language(s)
  - Net benefit is positive (more mistakes avoided than introduced)
  - Translation teams would recommend using this data
- TBTA review feedback integrated (if applicable)
- README.md updated with final status
- Transferable insights added to `../learnings/README.md`

**Only when all above complete**: Mark feature as production ready
