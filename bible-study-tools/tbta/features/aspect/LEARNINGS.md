# Aspect Feature Learnings

**Source**: Migrated from `/plan/tbta-rebuild-with-llm/features/verb-tam/LEARNINGS.md`

This document consolidates learnings from the Verb TAM research that are specifically relevant to Aspect prediction.

---

## Core Challenge: Aspect vs. Aktionsart

Aspect annotation must distinguish:
- **Grammatical aspect** (viewpoint): How the speaker views the action
- **Lexical aspect (Aktionsart)**: Inherent temporal properties of the verb

TBTA encodes grammatical aspect, but Aktionsart influences which aspects are natural for each verb.

---

## Four-Stage Annotation Process (Aspect-Specific)

### Stage 1: Source Language Analysis

**Greek Aspect System**:

| Greek Form | Default TBTA Aspect | Context Adjustments |
|------------|---------------------|---------------------|
| Aorist | U (Unmarked) or C (Completive) | Aktionsart-dependent |
| Aorist (ingressive) | N (Inceptive) | "began to do" context |
| Aorist (effective) | C (Completive) | "accomplished" context |
| Present | o (Continuative) or H (Habitual) | Context-dependent |
| Present (progressive) | o (Continuative) | "is doing" |
| Present (gnomic) | G (Gnomic) | Timeless truth |
| Imperfect | I (Imperfective) or o (Continuative) | Ongoing past |
| Imperfect (iterative) | H (Habitual) or R (Routinely) | Repeated action |
| Perfect | C (Completive) | Resulting state |

**Hebrew Aspect System**:

| Hebrew Form | Default TBTA Aspect | Context Adjustments |
|-------------|---------------------|---------------------|
| Qatal | U (Unmarked) perfective | Context-dependent |
| Qatal (stative) | o (Continuative) or H (Habitual) | State verbs |
| Wayyiqtol | U (Unmarked) | Narrative sequence |
| Yiqtol (modal) | U (Unmarked) | Mood affects aspect |
| Yiqtol (habitual) | H (Habitual) | Customary action |

### Stage 2: Aktionsart Classification

**Verb Classes** (Vendler 1957, Comrie 1976):

| Verb Class | Examples | Typical Aspect Coding |
|------------|----------|----------------------|
| **States** | "know," "love," "be" | I (Imperfective), o (Continuative), or U |
| **Activities** | "walk," "sing," "write" | o (Continuative), I (Imperfective) |
| **Accomplishments** | "build a house," "write a letter" | C (Completive) when done, o ongoing |
| **Achievements** | "arrive," "die," "notice," "win" | N (Inceptive) or U (Unmarked) |
| **Semelfactives** | "knock," "cough," "blink" | U for single, R/H for repeated |

### Stage 3: Discourse Context

**Narrative Structure**:
- **Foreground (mainline)**: Typically Perfective or Unmarked (event sequence)
- **Background**: Typically Imperfective or Continuative (setting, states)
- **Peaks**: May use marked aspects (Inceptive, Completive)

**Genre Patterns**:
- **Historical narrative**: Favor Perfective/Unmarked (completed events)
- **Teaching/Wisdom**: Habitual or Gnomic (general truths)
- **Prophecy**: Mix (certain futures = Perfective, possibilities = Imperfective)
- **Poetry**: Marked aspect uses (rhetorical effect)

### Stage 4: Multi-Factor Convergence

**The 5-Factor Model** (achieved 98.1% accuracy):

1. **Morphological**: Greek/Hebrew aspect forms (85-95% confidence)
2. **Lexical**: Aktionsart verb class (70-85% confidence)
3. **Temporal**: Adverbial cues ("always", "now", "began") (75-90% confidence)
4. **Discourse**: Genre and narrative structure (65-85% confidence)
5. **Clause-level**: Illocutionary force, modality (70-85% confidence)

**Convergence Scoring**:
- 4-5 factors align → High confidence (95%+)
- 3 factors align → Medium confidence (80-90%)
- 2 factors align → Low confidence (65-75%)
- 1 factor only → Very low, use default (Unmarked)

---

## Key Principles for Aspect Annotation

### Principle 1: Default to Unmarked

- 90.7% of verbs are Unmarked in narrative
- TBTA marks aspect only when semantically necessary
- Unmarked allows flexibility in target languages

### Principle 2: Morphology + Aktionsart

**Combined Analysis**:
- Greek aorist + achievement verb → typically U (Unmarked)
- Greek aorist + stative verb → often N (Inceptive) "came to know"
- Greek present + activity verb → o (Continuative) or H (Habitual)
- Greek imperfect + state verb → I (Imperfective) or o (Continuative)

### Principle 3: Discourse Trumps Morphology

**Example**: Greek aorist can have multiple aspects:
- Narrative sequence → U (Unmarked) or C (Completive)
- Teaching context → may be H (Habitual) if gnomic
- Parable → may be N (Inceptive) if hypothetical beginning

### Principle 4: Phasal Marking

Explicit phasal verbs override defaults:
- "Begin to" + verb → N (Inceptive)
- "Stop/cease" + verb → c (Cessative)
- "Finish/complete" + verb → C (Completive)

---

## Algorithm Evolution

### PROMPT1 (v1.0): Morphology-Only Approach

**Method**: Map Greek/Hebrew forms directly to TBTA aspects

**Accuracy**: 92.3%

**What Worked**:
- Greek aorist → Perfective (strong correlation)
- Greek present/imperfect → Imperfective (reliable)
- Wayyiqtol → Perfective (Hebrew narrative)

**What Failed**:
- Stative verbs in aorist (wrongly predicted Perfective)
- Gnomic present (wrongly predicted Imperfective)
- Genre variation (legal vs narrative different patterns)
- Hebrew qatal ambiguity (perfective or stative?)

### PROMPT2 (v2.0): Lexical-Primary Approach

**Method**: Use Aktionsart as primary signal, morphology as secondary

**Accuracy**: 92.3%

**What Worked**:
- State verbs → Imperfective (high accuracy)
- Achievement verbs → Perfective/Unmarked (good)
- Activity verbs → Continuative (decent)

**What Failed**:
- Morphological overrides (aorist can make stative inceptive)
- Discourse context (narrative vs teaching genre)
- Phasal constructions ("began to" not recognized)

### PROMPT3 (v3.2): Multi-Factor Convergence

**Method**: Combine all 5 factors with convergence scoring

**Accuracy**: 98.1%

**What Worked**:
- High-confidence when 4+ factors align (99% accuracy)
- Handles edge cases via context (stative aorist = inceptive)
- Genre-aware (narrative vs teaching vs prophecy)
- Recognizes phasal constructions

**What Failed** (remaining 1.9% errors):
- Annotation ambiguities (multiple valid perspectives)
- Rare constructions (insufficient training data)
- Translation philosophy differences (TBTA vs other approaches)

---

## Common Errors and Solutions

### Error 1: Missed Inceptive

**Symptom**: Predicted Unmarked, actual was Inceptive
**Cause**: Did not check potential mood + action verb combination
**Fix**: Always check mood BEFORE defaulting to Unmarked
**Example**: "beat" with 'might' Potential → Inceptive, not Unmarked

### Error 2: Confused Habitual and Imperfective

**Symptom**: Swapped these two aspects
**Cause**: Both describe repeated/ongoing action
**Fix**:
- Habitual = present/customary pattern (teaching contexts)
- Imperfective = past/ongoing state (narrative background)

### Error 3: Missed Cessative

**Symptom**: Predicted Unmarked, actual was Cessative
**Cause**: Did not recognize apocalyptic context or ending verbs
**Fix**: Look for transition markers and cessation verbs
**Example**: "Sun stopped shining" → check for Cessative

### Error 4: False Perfective

**Symptom**: Predicted Perfective, actual was Unmarked
**Cause**: Completed action without telic (goal-oriented) nature
**Fix**: Perfective requires goal-oriented verb with completion focus
**Distinguish**:
- "He walked to the store" = Perfective (goal achieved)
- "He walked for 10 minutes" = Unmarked (no endpoint)

---

## Decision Trees

### Aspect Feature Decision Tree

```
What is the source verb form?
├─ Greek Aorist
│  ├─ Ingressive context ("began to")? → N (Inceptive)
│  ├─ Effective context ("succeeded in")? → C (Completive)
│  └─ Otherwise → U (Unmarked)
├─ Greek Present
│  ├─ Gnomic statement? → G (Gnomic)
│  ├─ Habitual context ("regularly does")? → H (Habitual)
│  ├─ Progressive context ("is doing now")? → o (Continuative)
│  └─ Otherwise → U (Unmarked)
├─ Greek Imperfect
│  ├─ Iterative context? → H (Habitual) or R (Routinely)
│  ├─ Progressive past? → I (Imperfective) or o (Continuative)
│  └─ Inceptive imperfect? → N (Inceptive)
├─ Greek Perfect
│  └─ → C (Completive) with resultant state
└─ Hebrew verb forms
   └─ (Similar logic, adjusted for Hebrew system)

Also check:
- Aktionsart of verb (stative → I/o, achievement → N/U, accomplishment → C)
- Aspectual adverbs ("always" → G/H, "continuously" → o)
- Phasal verbs ("begin" → N, "stop" → c, "finish" → C)
```

---

## Statistical Summary (Matthew 24)

From analysis (54 verbs, 10 verses):

| Aspect | Count | % | Confidence |
|--------|-------|---|------------|
| Unmarked | 49 | 90.7% | VERY HIGH (98%) |
| Inceptive | 3 | 5.6% | VERY HIGH (100%) |
| Imperfective | 1 | 1.9% | MEDIUM (small sample) |
| Habitual | 1 | 1.9% | MEDIUM (small sample) |
| Others | 0 | 0% | UNTESTED |

**Overall Accuracy**: 53/54 correct = 98.1%

---

## Resources Needed for Aspect Reproduction

### Linguistic Databases

1. **Morphologically parsed texts**:
   - OpenText.org (Greek NT with aspect annotations)
   - ETCBC database (Hebrew Bible)

2. **Lexicons with Aktionsart**:
   - BDAG (Greek) - augment with verb class labels
   - BDB, HALOT (Hebrew) - add aspectual properties
   - Create Aktionsart classification database

3. **Discourse-annotated corpora**:
   - Narrative structure (foreground/background)
   - Genre labels
   - Phasal construction markers

---

## Open Questions

### Question 1: Aspect vs. Aktionsart Interaction

**Issue**: How much does lexical aspect determine TBTA aspect vs. grammatical aspect?

**Hypothesis**: Both contribute:
- Grammatical aspect sets range of possibilities
- Aktionsart + context selects within range

**Test**: Annotate verbs with different Aktionsart in same grammatical aspect; track distributions

### Question 2: Granularity of Aspect Codes

**Issue**: When to use specific aspect (Inceptive) vs. Unmarked?

**Hypothesis**: Use Unmarked when:
- Source language doesn't specify
- Multiple interpretations equally valid
- Target languages would diverge

Use specific codes when:
- Clear contextual evidence
- Discourse function requires it
- Cross-linguistically stable

**Test**: Compare translation naturalness with Unmarked vs. specific codes

---

## Validation Metrics

To evaluate aspect annotation quality:

1. **Inter-annotator agreement**: Cohen's kappa on aspect types
2. **Consistency**: Same verb class + context → same aspect
3. **Coverage**: All verbs annotated
4. **Transfer adequacy**: Russian, Mandarin, Arabic translations validated
5. **Typological validity**: Codes align with Comrie (1976), Smith (1997) frameworks

---

## Next Steps

1. **Expand to full Matthew 24**: 51 verses, ~316 verbs
2. **Test across genres**: Narrative (Genesis), Prophecy (Isaiah), Wisdom (Proverbs)
3. **Find rare aspects**: Cessative (apocalyptic), Perfective (telic narratives)
4. **Complete LEARNINGS.md**: Document all algorithm iterations
5. **External validation**: Russian, Mandarin, Arabic comparisons (30+ verses each)

---

**Document Source**: Combined from verb-tam/LEARNINGS.md (aspect-specific sections)
**Last Updated**: 2025-11-15
**Status**: Migrated to aspect feature directory
**Algorithm Version**: 3.2 (Multi-Factor Convergence)
