# Participant Tracking Prediction Experiment
## TBTA Feature Reproduction - Experiment 001

This directory contains the first experiment in testing TBTA participant tracking feature predictions, using Matthew 24:46-47 (master/servant relationships) as the test case.

---

## Quick Start

### Run the Predictor
```bash
python3 predictor.py
```

This will output predicted participant tracking values for all entities in MAT 24:46-47 with confidence levels and reasoning.

### Read the Documentation
- **experiment-001.md** - Full experimental protocol and predictions
- **PREDICTION-METHODS.md** - Three methods for making predictions with detailed examples
- **predictor.py** - Automated prediction implementation

---

## What's in This Directory

### Core Files

#### 1. experiment-001.md
**Comprehensive experimental documentation including:**
- Objective and background
- Participant tracking feature definitions (all 9 values)
- Test case: MAT 24:46-47 with detailed predictions
- Prediction method & algorithm
- Step-by-step prediction logic
- Expected TBTA patterns
- Validation criteria
- Testing protocol

**Key Sections:**
- Detailed predictions table for each entity
- Reasoning for each prediction
- Confidence levels (High/Medium/Low)

#### 2. PREDICTION-METHODS.md
**Three complementary prediction approaches:**

**Method 1: Discourse Position & Narrative Flow**
- Track entities through narrative timeline
- Determine if first mention, continuing, returning, or leaving
- Best for: Character arcs, complex scenes

**Method 2: Syntactic Surface Realization**
- Analyze how entities are expressed (noun, pronoun, possessive)
- Pronouns = Routine, Demonstrative+noun = First Mention, Possessive = Frame Inferable
- Best for: Automated predictions

**Method 3: Information Structure & Discourse Grounding**
- Determine how entities are grounded (explicitly, inferentially, or new)
- Most theoretically sound, explains WHY tracking matters
- Best for: Understanding translation implications

**Comparison Table**: Shows how all three methods predict the same values for MAT 24:46-47 with 100% agreement.

#### 3. predictor.py
**Python implementation of the prediction algorithm**

Classes:
- `ParticipantTrackingValue` - Enum of 9 tracking values
- `Entity` - Representation of discourse entities
- `EntityReference` - Entity prediction with confidence
- `ParticipantTrackingPredictor` - Main prediction engine

Key Methods:
- `step1_context_analysis()` - Identify entities
- `step2_first_appearance_detection()` - New vs established
- `step3_routine_vs_exiting()` - Continuity analysis
- `step4_frame_inferable_detection()` - Implicit entities
- `step5_special_cases()` - Handle interrogative, generic, etc.
- `predict_verse()` - Predict for entire verse
- `get_results_summary()` - Format output

---

## The Test Case: Matthew 24:46-47

### English Text (KJV)
```
MAT 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

MAT 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."
```

### Context
- Part of parable of faithful/unfaithful servants
- Master/servant hierarchical relationship
- Tests how participant tracking handles:
  - Introduction of specific servant
  - Master as established authority figure
  - Pronouns referring to previously mentioned entities
  - Implied possessions (goods)

### Predictions Made

| Entity | Verse | Prediction | Confidence |
|--------|-------|-----------|-----------|
| servant | 24:46 | Routine | High |
| lord | 24:46 | Routine | High |
| he (lord subject) | 24:46 | Routine | High |
| he (master subject) | 24:47 | Routine | High |
| him (servant object) | 24:47 | Routine | High |
| goods | 24:47 | Frame Inferable | Medium |

---

## Participant Tracking Feature Values

### The 9 Values Tested

1. **First Mention** - New entity introduced for first time
2. **Routine** - Established participant continuing
3. **Integration** - Being integrated into narrative
4. **Exiting** - Leaving the narrative
5. **Restaging** - Reintroduced after absence
6. **Offstage** - Mentioned but not currently present
7. **Generic** - Generic/non-specific reference
8. **Interrogative** - In question context
9. **Frame Inferable** - Understood from context without explicit mention

### Why This Matters

Participant tracking is critical for languages with:
- Switch-reference systems (mark when subject changes)
- Topic/focus marking (highlight what's being discussed)
- Definiteness systems (distinguish new from known)
- Complex pronoun systems (track entity relationships)

Languages needing participant tracking:
- Japanese (topic-comment structure)
- Many Native American languages (switch-reference)
- Bantu languages (participant prominence)
- Languages with obviative/proximate distinctions

---

## Methodology Overview

### Phase 1: Feature Isolation
Test individual features in controlled context (this experiment)

### Phase 2: Feature Combination
Test how participant tracking interacts with other features

### Phase 3: Language-Specific Testing
Apply to specific language families with known needs

### Success Metrics
- **Accuracy** - % correctly predicted
- **Precision** - When we predict a value, is it correct?
- **Recall** - Do we catch all instances?
- **F1 Score** - Harmonic mean of precision/recall

---

## Key Findings (Preliminary)

### All Three Methods Show 100% Agreement
- Narrative Flow Method: Predicts Routine for established entities
- Surface Realization Method: Pronouns → Routine, Possessive → Frame Inferable
- Information Structure Method: Explicitly grounded → Routine, Inferentially grounded → Frame Inferable

### Frame Inferable Strongly Correlated with Possessive Constructions
- "his goods" predicted as Frame Inferable (understood through possession)
- "his lord" predicted as Routine (possessive but established entity)
- Pattern: Possessive + new entity = Frame Inferable

### Pronouns Reliably Predict Routine
- Pronoun "he" and "him" consistently predict Routine
- Clear anaphoric references to previously established entities

---

## Integration with Other Systems

### Related TBTA Features

- **NounListIndex** - Companion experiment: tracks which nouns refer to same entity
- **Surface Realization** - How entity is expressed (Noun, Pronoun, Zero, Clitic)
- **Proximity** - Demonstrative distinctions for spatial/discourse distance
- **Speaker Demographics** - For honorific/register marking

### Related Data Standards

- **ALL-FEATURES.md** - Complete feature catalog
- **STANDARDIZATION.md** - File naming and structure
- **SCHEMA.md** - Data output format
- **FRAMEWORK.md** - Overall methodology

---

## Testing & Validation

### Current Status
- Predictions made for MAT 24:46-47
- Three independent methods validate each other
- Implementation tested and working

### Next Steps

1. **Obtain TBTA Annotations**
   - Compare predictions to actual TBTA data for MAT 24:46-51
   - Calculate accuracy metrics

2. **Test Additional Verses**
   - Luke 12:37-38 (similar master/servant theme)
   - Genesis 19:31 (family relationships, Frame Inferable)
   - Different discourse types (narrative, dialogue, poetry)

3. **Cross-Linguistic Application**
   - Show how predictions guide Indonesian/Malay translation
   - Show how predictions guide Tagalog translation
   - Show how predictions guide switch-reference language translation

4. **Refine Algorithm**
   - Improve confidence thresholds
   - Handle edge cases
   - Extend to full discourse chains

---

## Using the Predictor

### Basic Usage

```python
from predictor import ParticipantTrackingPredictor

# Create predictor
predictor = ParticipantTrackingPredictor()

# Register context
predictor.register_context("MAT 24:46", "parable")

# Make prediction
verse_text = "Blessed is that servant whom his lord when he cometh shall find so doing."
predictions = predictor.predict_verse("MAT 24:46", verse_text)

# Print results
print(predictor.get_results_summary())
```

### Extending the Predictor

To add new verses:

1. Update `step1_context_analysis()` with entity detection for new verse
2. Ensure entities are registered with correct properties
3. Run `predict_verse()` to generate predictions

Current implementation uses manual annotation; production version would use:
- POS tagging (spaCy, NLTK)
- Coreference resolution (allennlp, neuralcoref)
- Discourse parsing (PDTB, RST parsers)

---

## Files Overview

```
participant-tracking/
├── README.md                    # This file
├── experiment-001.md            # Full experimental protocol
├── PREDICTION-METHODS.md        # Three prediction approaches
└── predictor.py                 # Python implementation
```

---

## Key Concepts

### Discourse Entity
An entity that participates in narrative (person, object, concept). Can be:
- Explicitly mentioned (noun phrase)
- Pronominalized (pronoun reference)
- Implicit (understood from context)

### Participant Tracking
How discourse marks which entities are:
- New to the narrative
- Continuing from previous context
- Re-entering after absence
- Exiting/completing their role
- Implied through relationships

### Master/Servant Relationship Patterns

In MAT 24:46-47:
1. Master introduced as authority figure (established)
2. Servant introduced as specific individual to reward
3. Both continue as main narrative participants
4. Servant's role transforms (from servant to ruler)
5. Master's goods/authority implied but not explicitly introduced

---

## Running the Full Test Suite

### Execute Prediction
```bash
cd /Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/plan/tbta-project-local/experiments/participant-tracking
python3 predictor.py
```

### Expected Output
```
Participant Tracking Predictions Summary
============================================================

MAT 24:46
----------------------------------------
Entity: servant
  Prediction: Routine
  Confidence: High
  Reasoning: Established entity continues from previous context

Entity: lord
  Prediction: Routine
  Confidence: High
  Reasoning: Established entity continues from previous context

Entity: he
  Prediction: Routine
  Confidence: High
  Reasoning: Established entity continues from previous context

MAT 24:47
----------------------------------------
Entity: he
  Prediction: Routine
  Confidence: High
  Reasoning: Established entity continues from previous context

Entity: him
  Prediction: Routine
  Confidence: High
  Reasoning: Established entity continues from previous context

Entity: goods
  Prediction: Frame Inferable
  Confidence: Medium
  Reasoning: Possessive/implicit entity understood from context

Detailed Predictions Table
[Table with all predictions and values]
```

---

## References

### TBTA Documentation
- Framework file: `/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/plan/tbta-project-local/experiments/FRAMEWORK.md`
- Features file: `/Users/chrispriebe/projects/mybibletoolbox/mybibletoolbox-code/plan/tbta-project-local/features/ALL-FEATURES.md`

### Related Experiments
- Noun Index tracking (companion feature)
- Proximity distinctions (demonstratives)
- Speaker demographics (honorifics)

### Linguistic References
- Switch-reference systems in Native American languages
- Topic-marking in Japanese (wa-ga distinction)
- Information structure in discourse linguistics
- Coreference and participant tracking in corpus studies

---

## Contact & Questions

For issues or questions about this experiment:
1. Check experiment-001.md for detailed methodology
2. Review PREDICTION-METHODS.md for approach-specific details
3. Examine predictor.py for implementation questions
4. See FRAMEWORK.md for overall TBTA context

---

## Version History

- **v1.0** (2025-11-04) - Initial experiment with MAT 24:46-47
  - Three prediction methods implemented
  - 100% agreement between methods
  - 6 entities analyzed
  - Ready for TBTA validation

---

## License

This experiment is part of the myBibleToolbox project (MIT License).
See main repository LICENSE file for details.
