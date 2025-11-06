# Experiment 001: Participant Tracking in Master/Servant Relations
## Testing TBTA Participant Tracking Feature Prediction

**Date**: 2025-11-04
**Test Verses**: Matthew 24:46-47
**Feature Being Tested**: Participant Tracking
**Focus**: Master/Servant relationships and entity reintroduction patterns

---

## Objective

Test whether we can accurately predict Participant Tracking values (First Mention, Routine, Restaging, Exiting, Frame Inferable) for entities in a narrative involving master/servant hierarchical relationships.

---

## Background: Participant Tracking Values

From ALL-FEATURES.md, Participant Tracking has these possible values:

| Value | Meaning | Usage |
|-------|---------|-------|
| **First Mention** | New entity introduced | Initial appearance in narrative |
| **Routine** | Established participant continuing | Entity already known, appearing again |
| **Integration** | Being integrated into narrative | Becoming part of active participants |
| **Exiting** | Leaving the narrative | Ceasing to be active in the story |
| **Restaging** | Reintroduced after absence | Returning after being absent |
| **Offstage** | Not currently present but referenced | Mentioned but not in scene |
| **Generic** | Generic/non-specific reference | Not specific individual |
| **Interrogative** | In question context | Within interrogative structure |
| **Frame Inferable** | Can be inferred from context | Not explicitly mentioned but implied |

---

## Test Case: Matthew 24:46-47

### English Text
**MAT 24:46** (KJV): "Blessed is that servant whom his lord when he cometh shall find so doing."

**MAT 24:47** (KJV): "Verily I say unto you, That he shall make him ruler over all his goods."

### Discourse Context
- Matthew 24:45-51 is the parable of the faithful and unfaithful servants
- Jesus is teaching about the return and final judgment
- Master/Servant relationship is central to the theological point
- Multiple references to entities with implied relationships

---

## Predicted Participant Tracking Values

### For MAT 24:46

| Constituent | Part of Speech | Tracking Prediction | Reasoning |
|-------------|-----------------|-------------------|-----------|
| **servant** (main) | Noun | First Mention | New character introduced (hypothetical servant in parable) |
| **lord/his lord** | Noun | First Mention | Master introduced (new in immediate context, though established earlier in parable) |
| **he** (pronoun ref: lord) | Pronoun | Routine | Referring back to already-mentioned lord |

### For MAT 24:47

| Constituent | Part of Speech | Tracking Prediction | Reasoning |
|-------------|-----------------|-------------------|-----------|
| **he** (subject: servant) | Pronoun | Routine | Servant still in focus, continuing action from v.46 |
| **him** (object: servant) | Pronoun | Routine | Same servant, continuing discussion |
| **his goods/all his goods** | Noun Phrase | Frame Inferable | Goods belong to master, implied but not explicitly introduced |

---

## Prediction Method & Hypothesis

### Prediction Hypothesis

**H1: First Mention vs. Routine**
- Servants in parables follow "first mention" pattern for main focus character
- The master follows first mention if genuinely new, or routine if established
- Pronouns referring to already-mentioned entities = Routine

**H2: Restaging vs. Exiting**
- "Exiting" appears when an entity leaves the narrative focus
- "Restaging" applies when an entity returns after being backgrounded
- Master-servant parables typically show Restaging if master reappears after being absent

**H3: Frame Inferable**
- Possessive constructions (his goods, their house) should show Frame Inferable
- Family/relational nouns (father, daughter, lord's slave) often Frame Inferable
- Implicit agents in passive constructions = Frame Inferable

### Test Strategy

1. **Baseline**: Predict participant tracking WITHOUT seeing TBTA data
2. **Hypothesis Validation**: Check if predictions match the framework
3. **Error Analysis**: Identify why predictions fail or succeed
4. **Pattern Recognition**: Extract rules about narrative structure

---

## Implementation: Prediction Algorithm

### Step 1: Context Analysis

**Input**: Verse text + surrounding narrative context

```
Step 1a: Identify all noun phrases and pronouns
Step 1b: Build entity reference chain (coreference)
Step 1c: Mark narrative position (first appearance, repeated, backgrounded, etc.)
Step 1d: Note semantic relationships (possession, agency, modification)
```

### Step 2: First Appearance Detection

```
For each noun/pronoun:
  IF entity is appearing for the first time in the discourse unit
     → PREDICT: First Mention
  ELSE IF entity is continuing from previous mentions
     → PREDICT: Routine (go to Step 3)
  ELSE IF entity is reappearing after absence
     → PREDICT: Restaging (go to Step 4)
```

### Step 3: Routine vs Exiting Decision

```
For Routine entities:
  IF entity is being actively referenced/acted upon
     → CONFIRM: Routine
  ELSE IF entity's role is diminishing in narrative
     → PREDICT: Exiting
  ELSE IF entity's role is increasing/being highlighted
     → CONFIRM: Routine
```

### Step 4: Frame Inferable Detection

```
For implicit/inferred entities:
  IF entity is possessed/owned by another entity
     → PREDICT: Frame Inferable (possessive construction)
  ELSE IF entity is implied through kinship/relationship
     → PREDICT: Frame Inferable
  ELSE IF entity is agent of passive construction
     → PREDICT: Frame Inferable
  ELSE IF entity is understood from cultural/situational context
     → PREDICT: Frame Inferable
```

### Step 5: Special Cases

```
Check for:
  - Interrogative context → Interrogative marker
  - Generic/non-specific use → Generic
  - Offstage/mentioned but not present → Offstage
  - Restaging conditions → Restaging
```

---

## Detailed Predictions with Reasoning

### Matthew 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

#### Entity: "that servant"
- **Part**: NP (main subject)
- **Prediction**: First Mention
- **Reasoning**:
  - This is the first time this particular servant is introduced
  - Though servants were mentioned earlier (24:45), this specific servant is being singled out ("that servant")
  - The demonstrative "that" helps distinguish this particular servant as distinct
  - Parable introduces hypothetical example → First Mention pattern

#### Entity: "his lord" (within 24:46)
- **Part**: NP (possessive phrase)
- **Prediction**: Routine (with Frame Inferable nuance)
- **Reasoning**:
  - "Lord" has been established in the parable framework (24:45: "whom his lord hath made ruler")
  - This is a reappearance of the master figure
  - Possessive "his" indicates the relationship is understood/established
  - Could argue Restaging if master was truly backgrounded, but more likely Routine with Frame Inferable for the implied goods/authority

#### Entity: "he" (subject of "cometh")
- **Part**: Pronoun
- **Prediction**: Routine
- **Reasoning**:
  - Clearly refers to the just-mentioned lord
  - Same-clause pronoun reference = Routine continuation

---

### Matthew 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."

#### Entity: "he" (subject)
- **Part**: Pronoun
- **Prediction**: Routine
- **Reasoning**:
  - Continues reference to the master from 24:46
  - Direct continuation of narrative action (master blessing the servant)

#### Entity: "him" (object)
- **Part**: Pronoun
- **Prediction**: Routine
- **Reasoning**:
  - Refers back to the servant from 24:46
  - Direct continuation of description about that same servant

#### Entity: "his goods" / "all his goods"
- **Part**: NP (noun phrase with possessive)
- **Prediction**: Frame Inferable
- **Reasoning**:
  - The "goods" are not explicitly introduced
  - They are implied through the master's wealth/authority (frame-inferrable)
  - Possessive construction indicates relationship understood in context
  - Belongs to implied master's estate/household

---

## Expected TBTA Patterns

### Pattern 1: Character Introduction
```yaml
- Constituent: "servant"
  Participant Tracking: First Mention
  NounListIndex: "1"  # First entity in this specific scene

- Constituent: "lord"
  Participant Tracking: Routine  # Established in frame
  NounListIndex: "2"  # Second distinct entity
```

### Pattern 2: Pronoun Continuity
```yaml
- Constituent: "he"
  Person: Third
  Participant Tracking: Routine
  Surface Realization: Pronoun
```

### Pattern 3: Implicit/Frame Elements
```yaml
- Constituent: "goods"
  Participant Tracking: Frame Inferable
  Polarity: Affirmative
  Surface Realization: Noun
```

---

## Validation Criteria

### Success Metrics

- **Accuracy**: % of participant tracking values predicted correctly
- **Precision**: When we predict "First Mention", is it actually First Mention?
- **Recall**: Do we catch all instances that should be marked?
- **Specificity**: Do we distinguish Frame Inferable from other categories?

### Minimum Success Threshold

- **80% accuracy** on MAT 24:46-47 would validate basic approach
- **100% accuracy** on character introduction/exit patterns
- **High precision** on Frame Inferable (few false positives)

---

## Testing Protocol

### Phase 1: Blind Prediction
1. Make predictions without access to TBTA data
2. Document reasoning for each prediction
3. Record confidence level (High/Medium/Low)

### Phase 2: Comparison
1. Compare predictions to actual TBTA annotations
2. Record matches and mismatches
3. Analyze error patterns

### Phase 3: Analysis
1. Identify which rules worked
2. Identify which rules failed
3. Refine hypothesis

### Phase 4: Re-test
1. Apply refined rules
2. Test on different verses
3. Build patterns library

---

## Results (To Be Updated)

### Initial Predictions Summary

| Entity | Prediction | Confidence | Status |
|--------|-----------|-----------|--------|
| servant (24:46) | First Mention | High | Pending validation |
| lord (24:46) | Routine | High | Pending validation |
| he (24:46 subject) | Routine | High | Pending validation |
| he (24:47 subject) | Routine | High | Pending validation |
| him (24:47 object) | Routine | High | Pending validation |
| goods (24:47) | Frame Inferable | Medium | Pending validation |

---

## Lessons Learned (To Be Updated)

### Key Insights
- [ ] Master/servant relationships show predictable participant tracking patterns
- [ ] Pronouns reliably predict Routine tracking
- [ ] Frame Inferable best identified through possessive/relational structures
- [ ] Parable context affects first mention vs routine decisions

### Refined Rules
- [ ] Rule for demonstrative + noun = First Mention
- [ ] Rule for same-clause pronoun reference = Routine
- [ ] Rule for possessive NP with implicit agent = Frame Inferable
- [ ] Rule for reappearing characters in same passage = Routine vs Restaging

---

## Cross-Reference

**Related Experiments**:
- noun-index: Testing NounListIndex tracking (companion feature)
- [Future] proximity: Testing demonstratives and spatial distinctions
- [Future] speaker-demographics: Testing honorific contexts

**Related Standards**:
- See STANDARDIZATION.md for file naming conventions
- See SCHEMA.md for data output format
- See ALL-FEATURES.md for complete feature definitions

---

## Notes for Next Phase

1. **Data Source**: Need to obtain actual TBTA annotations for MAT 24:45-51 to validate
2. **Scope Expansion**: Test on additional verses with master/servant themes (Luke 12:37-38, etc.)
3. **Language Variation**: Consider how this would be realized in languages with:
   - Switch-reference systems
   - Evidentiality markers
   - Topic-focus distinctions
4. **Integration**: Link participant tracking predictions with NounListIndex and Surface Realization

---

## Document Metadata

- **Framework Version**: 1.0 (FRAMEWORK.md)
- **Feature Set**: ALL-FEATURES.md (Participant Tracking section)
- **Experiment Type**: Feature Isolation (Phase 1)
- **Expected Duration**: Single verse pair testing
- **Success Criteria**: 80%+ accuracy on participant tracking
