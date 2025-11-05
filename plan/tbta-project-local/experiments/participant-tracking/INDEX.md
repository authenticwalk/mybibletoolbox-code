# Participant Tracking Experiment - Complete Index

**Test Subject**: Matthew 24:46-47 (Master/Servant Relationships)
**Feature**: Participant Tracking (9 values)
**Status**: Initial predictions complete, ready for TBTA validation
**Date**: 2025-11-04

---

## Document Quick Reference

### 1. README.md - START HERE
**Purpose**: Overview and quick start guide
**Contains**:
- Quick start instructions
- File directory overview
- Key findings summary
- Test case summary
- Running instructions

**Read this for**: Understanding the full experiment scope and how to run it

### 2. experiment-001.md - DETAILED METHODOLOGY
**Purpose**: Complete experimental protocol
**Contains**:
- Objective and background
- All 9 participant tracking values explained
- Test verses (MAT 24:46-47) with full analysis
- Detailed predictions for each entity with reasoning
- Expected TBTA patterns
- Validation criteria
- Testing phases

**Key Tables**:
- "Predicted Participant Tracking Values" (MAT 24:46)
- "Predicted Participant Tracking Values" (MAT 24:47)
- "Expected TBTA Patterns" with YAML examples

**Read this for**: Understanding WHY each prediction was made and WHAT the features mean

### 3. PREDICTION-METHODS.md - THREE APPROACHES
**Purpose**: Comparing different prediction methodologies
**Contains**:
- Method 1: Discourse Position & Narrative Flow
- Method 2: Syntactic Surface Realization
- Method 3: Information Structure & Discourse Grounding
- Comparative analysis showing 100% agreement
- Strengths/weaknesses of each approach
- Implementation recommendations

**Key Tables**:
- "Comparative Analysis" - All three methods on MAT 24:46-47
- "Method Strengths & Weaknesses Summary"
- "Syntactic Decision Table" (Method 2)
- "Information Grounding Decision Table" (Method 3)

**Read this for**: Understanding HOW we arrive at predictions and validating reasoning

### 4. predictor.py - IMPLEMENTATION
**Purpose**: Automated prediction engine
**Contains**:
- Python classes for entity tracking
- 5-step prediction algorithm
- Main execution for MAT 24:46-47
- Results formatting

**Key Components**:
- `ParticipantTrackingValue` - Enum of 9 values
- `Entity` - Data class for discourse entities
- `EntityReference` - Prediction with confidence/reasoning
- `ParticipantTrackingPredictor` - Main prediction engine

**Run with**: `python3 predictor.py`

**Read this for**: Understanding implementation details and extending the system

---

## The Three Prediction Methods Explained Simply

### Method 1: Narrative Flow
**Question**: Is this entity new to the story, continuing, returning, or leaving?
**Approach**: Track entities through narrative timeline
**Example**: Servant introduced (First Mention) → continues in next verse (Routine)

### Method 2: Surface Realization
**Question**: How is the entity expressed? (noun, pronoun, possessive, etc.)
**Approach**: Analyze syntactic form
**Example**: Pronoun "he" → always Routine. Possessive "his goods" → Frame Inferable

### Method 3: Information Structure
**Question**: Is the entity explicitly mentioned, inferrable, or completely new?
**Approach**: Ground entities in discourse context
**Example**: "his goods" not explicitly mentioned but inferrable from master's role → Frame Inferable

**Result**: All three methods predict identically on MAT 24:46-47

---

## Participant Tracking Values At-a-Glance

| Value | Meaning | Example from MAT 24:46-47 |
|-------|---------|--------------------------|
| **First Mention** | New entity introduced | (None predicted in this passage) |
| **Routine** | Established, continuing | "servant", "lord", "he", "him" |
| **Integration** | Becoming part of narrative | (Not applicable here) |
| **Exiting** | Leaving the narrative | (Not applicable here) |
| **Restaging** | Reintroduced after absence | (Not applicable here) |
| **Offstage** | Mentioned but not present | (Not applicable here) |
| **Generic** | Non-specific reference | (Not applicable here) |
| **Interrogative** | In question context | (Not applicable here) |
| **Frame Inferable** | Understood from context | "goods" (understood to belong to master) |

---

## Predictions Summary

### MAT 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

```
servant    → Routine      (HIGH confidence)
lord       → Routine      (HIGH confidence)
he         → Routine      (HIGH confidence)
```

### MAT 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."

```
he         → Routine      (HIGH confidence)
him        → Routine      (HIGH confidence)
goods      → Frame Inferable (MEDIUM confidence)
```

**Total**: 6 entities analyzed, 5 Routine, 1 Frame Inferable, 100% method agreement

---

## Next Steps for Validation

### Immediate (Required)
1. Obtain TBTA annotations for MAT 24:45-51
2. Compare predictions to actual data
3. Calculate accuracy metrics
4. Document discrepancies

### Short-term (Recommended)
1. Test on Luke 12:37-38 (similar master/servant theme)
2. Test on Genesis 19:31 (family relationships)
3. Test cross-verse participant tracking
4. Refine confidence thresholds

### Long-term (Future)
1. Test complete feature interactions
2. Apply to other language families
3. Build comprehensive prediction system
4. Create translator guidance documents

---

## Key Insights From This Experiment

### Finding 1: Pronouns Always Predict Routine
All pronouns ("he", "him") reliably predicted as Routine because they refer to previously established entities.

### Finding 2: Possessive Constructions Indicate Frame Inferable
"his goods" - not explicitly introduced but understood through master's role and wealth.

### Finding 3: Method Agreement Validates Predictions
Three independent methods (Narrative Flow, Surface Realization, Information Structure) all predict identical values. This 100% agreement increases confidence.

### Finding 4: Master/Servant Relationships Show Predictable Patterns
Hierarchical relationships (master→servant→objects) follow consistent participant tracking patterns:
- Master = established (Routine)
- Specific servant = introduced (or Routine if continuing)
- Master's possessions = implied (Frame Inferable)

---

## Why Participant Tracking Matters for Translation

### Languages That Need It

**Switch-Reference Languages**
- Native American languages (Navajo, Apache, etc.)
- Many Papua New Guinea languages
- Need to mark explicitly when subject/agent changes

**Topic-Marking Languages**
- Japanese (wa particle marks topic)
- Korean (neun particle)
- Chinese (topic-comment structure)

**Definiteness-Marking Languages**
- Semitic languages (marked article systems)
- Slavic languages (aspect-definiteness interaction)
- Need to distinguish new from known information

**Honorific Systems**
- Korean, Japanese, Thai
- Determine politeness level based on entity status
- Need to know if entity is established/respected

### Translation Implications for MAT 24:46-47

**For Indonesian/Malay**
- "servant" vs "that servant" affects determiner selection
- "lord" (established) uses different form than first mention
- Pronoun reference patterns (kami/kita/dia) depends on tracking

**For Tagalog**
- Participant tracking determines mood/focus markers
- "ang" (agent focus) vs "ng" (non-focus) depends on entity status
- Aspect selection may depend on whether entity is routine

**For Switch-Reference Languages**
- "he cometh" (still master from previous clause) vs new subject
- Verb suffix marks same/different subject
- Tracking prevents ambiguity in complex clauses

---

## File Navigation

### By Task

**Want to understand the predictions?**
1. Read: README.md (overview)
2. Read: experiment-001.md (detailed analysis)
3. Check: PREDICTION-METHODS.md (validation)

**Want to implement predictions?**
1. Study: predictor.py (implementation)
2. Review: PREDICTION-METHODS.md (Method 2 for automation)
3. Extend: Add new verses to `step1_context_analysis()`

**Want to validate the experiment?**
1. Check: experiment-001.md (methodology)
2. Compare: Predictions vs TBTA actual annotations
3. Calculate: Accuracy, precision, recall, F1 scores

**Want to apply to translation?**
1. Read: experiment-001.md (linguistic reasoning)
2. Review: PREDICTION-METHODS.md (Information Structure method)
3. Apply: Feature values to target language

### By Interest

**Linguistics Students**
- Start with: PREDICTION-METHODS.md (all three methods explained)
- Then read: experiment-001.md (application to real Bible text)

**Software Developers**
- Start with: README.md (overview)
- Code is in: predictor.py
- Extend by adding: New verses to entity detection

**Bible Translators**
- Start with: README.md (why this matters)
- Focus on: PREDICTION-METHODS.md (Method 3: Information Structure)
- Apply: Predictions to your target language

**Researchers**
- Start with: experiment-001.md (methodology)
- Expand: PREDICTION-METHODS.md (comparative approaches)
- Validate: Run predictor.py and compare to TBTA

---

## Experiment Statistics

| Metric | Value |
|--------|-------|
| Verses Analyzed | 2 |
| Entities Found | 6 |
| Participant Tracking Values Used | 2 (Routine, Frame Inferable) |
| Prediction Methods | 3 |
| Method Agreement | 100% |
| High Confidence Predictions | 5 |
| Medium Confidence Predictions | 1 |
| False Negatives Expected | 0 |
| False Positives Expected | 0 |

---

## Key References

### Internal Documentation
- **FRAMEWORK.md** - Overall TBTA feature reproduction methodology
- **ALL-FEATURES.md** - Complete participant tracking value definitions
- **STANDARDIZATION.md** - File naming and data structure standards
- **SCHEMA.md** - Output data format specifications

### Related Experiments
- Noun Index tracking (companion feature)
- Proximity distinctions (demonstrative/deictic)
- Speaker demographics (honorifics and register)
- Person/Number features (inclusive/exclusive distinctions)

### External References
- Discourse analysis in Bible translation (TBTA documentation)
- Information structure linguistics (Prince 1992, Gundel et al. 1993)
- Switch-reference systems (Fauconnier 1985, Donohue 2012)
- Topic/focus marking (Li & Thompson 1976, Lambrecht 1994)

---

## How to Use These Documents Effectively

### For Reading
1. Start with README.md for quick overview
2. Dive into experiment-001.md for detail
3. Compare approaches in PREDICTION-METHODS.md
4. Review predictor.py for implementation

### For Understanding
1. Focus on prediction tables in experiment-001.md
2. Compare "Expected TBTA Patterns" to actual data
3. Study the three methods side-by-side in PREDICTION-METHODS.md
4. Note the 100% agreement between approaches

### For Implementation
1. Study predictor.py classes and methods
2. Understand the 5-step algorithm
3. Extend `step1_context_analysis()` for new verses
4. Add new entity detection logic

### For Validation
1. Get TBTA annotations for MAT 24:45-51
2. Compare to predictions in this experiment
3. Calculate accuracy metrics
4. Document any discrepancies and revise algorithm

### For Application
1. Map participant tracking values to target language
2. Use Method 3 (Information Structure) for reasoning
3. Consider switch-reference, topic-marking, definiteness needs
4. Create translator guidance documents

---

## Checklist for Using This Experiment

- [ ] Read README.md for overview
- [ ] Understand all 9 participant tracking values
- [ ] Review MAT 24:46-47 predictions and reasoning
- [ ] Run predictor.py to see automation in action
- [ ] Study the three prediction methods
- [ ] Verify 100% agreement between methods
- [ ] Obtain TBTA annotations for validation
- [ ] Compare predictions to actual data
- [ ] Calculate accuracy metrics
- [ ] Document lessons learned
- [ ] Plan next experiments (other verses, languages)

---

## Questions & Troubleshooting

**Q: Why only 2 participant tracking values predicted (Routine, Frame Inferable)?**
A: MAT 24:46-47 is a focused narrative with established main characters (master, servant). First Mention doesn't apply because these entities are introduced earlier in the parable framework. Other values (Exiting, Restaging, Interrogative) don't apply to this specific text.

**Q: Why is "goods" medium confidence while others are high?**
A: "Goods" is never explicitly mentioned. The Frame Inferable classification is inferenced from context (master's implied wealth). If TBTA data shows a different value, we may need to reconsider our inferencing rules.

**Q: How would predictions differ in another language?**
A: Participant tracking VALUES are universal (they describe discourse structure), but how languages express them varies. A switch-reference language would mark "he cometh" vs "he said" differently. A topic-marking language would use different particles.

**Q: Can I use this for verses other than MAT 24:46-47?**
A: Yes! The algorithm is general. Add entities to `step1_context_analysis()` and run. Start with verses from the same parable (MAT 24:45, 24:48-50, 24:51) for best results.

**Q: How accurate is this system?**
A: Currently untested against TBTA annotations. The three methods show 100% agreement on this test case, suggesting high reliability, but external validation is needed.

---

## Document Statistics

| Document | Lines | Purpose |
|----------|-------|---------|
| README.md | 400+ | Overview & quick start |
| experiment-001.md | 450+ | Detailed methodology |
| PREDICTION-METHODS.md | 500+ | Three approaches explained |
| predictor.py | 300+ | Python implementation |
| INDEX.md | 400+ | This navigation document |

**Total**: ~2000 lines of documentation and code

---

## Version & Maintenance

**Current Version**: 1.0
**Date Created**: 2025-11-04
**Status**: Initial experiment complete, ready for validation
**Next Review**: After TBTA data comparison
**Maintainer**: TBTA Feature Reproduction Project

---

## See Also

- **Parent Directory**: `/plan/tbta-project-local/experiments/`
- **Framework**: `/plan/tbta-project-local/experiments/FRAMEWORK.md`
- **Features**: `/plan/tbta-project-local/features/ALL-FEATURES.md`
- **Related Experiments**: `noun-index/` directory

---

**Last Updated**: 2025-11-04
**Ready for Review**: Yes ✓
**Validation Pending**: TBTA annotations for MAT 24:45-51
