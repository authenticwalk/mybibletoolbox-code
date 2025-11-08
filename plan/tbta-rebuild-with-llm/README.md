# TBTA Reproduction Project

**Goal**: Reverse-engineer TBTA's linguistic annotation methodology to reproduce Bible translation annotations systematically.

**Status**: Training phase (2/17 features complete) | **Approach**: [Adversarial validation](METHODOLOGY-ADVERSARIAL.md)

---

## What is TBTA?

**TBTA (The Bible Translator's Assistant)** is a linguistic annotation dataset by SIL International that tags every constituent in all 31,102 Bible verses with **57 features** needed for translation into 1,000+ languages.

**Why it matters**: Most languages aren't like English. They need explicit features:
- **Clusivity** (176 languages): "We" = inclusive (including you) vs exclusive (excluding you)
  - Gen 1:26 "Let us make" = Exclusive (Trinity only, not humans)
- **Number** beyond singular/plural: Trial (3), dual (2), paucal (3-10)
  - Trinity references = Trial number
- **Participant tracking**: First mention vs routine vs presupposed
- **Theological patterns**: Divine speech differs from human speech

**The challenge**: Manual annotation by experts is expensive, slow, error-prone, and opaque.

**Our goal**:
1. Understand TBTA's annotation rules (reverse-engineering)
2. Reproduce annotations systematically
3. Validate/improve existing annotations
4. Extend to new features
5. Build self-improving annotation systems

---

## Three-Phase Approach

### Phase 1: Training (Current)
**Method**: Analyze TBTA to discover patterns
- 15-20 training verses per feature
- Study TBTA annotations freely
- Document decision rules
- Build algorithm v1.0

**Status**: 2/17 features complete
- ✅ Number systems (algorithm v1.0 locked, 91.4% initial prediction accuracy)
- ✅ Degree (ready for train/test split)

### Phase 2: Adversarial Validation (Next)
**Method**: Test on edge cases + typical cases
- Adversarial: 10-15 hard verses (target 60-70% accuracy)
- Random: 10-15 typical verses (target 80-90% accuracy)
- Predict BEFORE checking TBTA (no data leakage)

**Why adversarial?**: Edge cases find weaknesses faster than large random samples
- 2 weeks per feature vs months for comprehensive testing
- 65% hard + 85% easy > 90% all easy (more trustworthy)

**See**: [METHODOLOGY-ADVERSARIAL.md](METHODOLOGY-ADVERSARIAL.md)

### Phase 3: Comprehensive Validation (After Q1 2026)
**Method**: Large-scale after all features complete
- 200+ verses per feature
- Cross-validation, confidence intervals
- Ready for production

---

## Key Discoveries

### Universal Patterns (from number-systems analysis)

1. **Semantic over morphological**: TBTA marks meaning, not grammar form
   - Hebrew שָׁמַיִם (dual morphology) → Singular ("one sky")
2. **Theological context matters**: Trinity = Trial, divine speech gets special treatment
3. **Discourse role determines features**: Same entity, different values by role
4. **Ancient translations guide interpretation**: LXX/Vulgate show semantic meaning
5. **Rare values often absent**: Biblical text may lack theoretical values

**See**: [features/CROSS-FEATURE-LEARNINGS.md](features/CROSS-FEATURE-LEARNINGS.md)

### Methodology Lessons

- ❌ Training on test data → misleading "100% accuracy"
- ✅ Separate training (learn freely) from test (predict first, check after)
- ✅ Adversarial testing faster than large samples
- ✅ Locked predictions (git commit) before checking TBTA

**See**: [Critical review](../../tbta-experiment-critical-review.md) | [Methodology fixes](../../tbta-experiment-methodology-fixes.md)

---

## Current Status

**Completed (2)**:
- number-systems: 35 training verses, patterns documented, awaiting adversarial validation
- degree: 12 verses, ready for proper train/test split

**In progress (15)**:
- Semantic: person, participant-tracking, discourse-genre, time-granularity, proximity, polarity, surface-realization, honorifics-register, illocutionary-force, verb-tam
- Structural: 02-verbs, 07-phrasal-elements, 101-noun-phrases, 105-clauses, topic-np

**See**: [features/FEATURE-STATUS-SUMMARY.md](features/FEATURE-STATUS-SUMMARY.md)

---

## Timeline

**Q4 2025**: 5 features | **Q1 2026**: All 17 features | **Q2 2026**: Comprehensive validation | **Q3 2026**: Production | **Q4 2026**: Self-improving pipeline

---

## How to Join

### New Contributors: Read These in Order

1. **This README** (you are here) - 10 min
2. **[METHODOLOGY-ADVERSARIAL.md](METHODOLOGY-ADVERSARIAL.md)** - Testing protocol - 15 min
3. **[features/number-systems/](features/number-systems/)** - Completed example - 30 min
4. **[features/FEATURE-STATUS-SUMMARY.md](features/FEATURE-STATUS-SUMMARY.md)** - Pick a feature - 5 min

### Your First 2 Weeks

**Week 1: Training**
- Select 15-20 training verses
- Access TBTA for training set
- Analyze patterns, build algorithm v1.0
- Lock algorithm (git commit)

**Week 2: Validation**
- Design adversarial (10 hard) + random (10 typical) test sets
- Predict WITHOUT checking TBTA
- Lock predictions (git commit)
- Check TBTA, calculate accuracy
- Error analysis, algorithm v2.0

**Then**: Move to next feature or help others. Celebrate! 🎉

### Prerequisites

**You need**:
- Basic linguistics (morphology, semantics, syntax)
- Bible familiarity (Genesis, Gospels)
- Greek/Hebrew interlinear reading (tools provided)
- Systematic analysis skills

**You DON'T need**:
- Linguistics degree (we explain as we go)
- Greek/Hebrew fluency (lexicons provided)
- Machine learning expertise (rule-based, not ML)

---

## Quick Reference

### File Structure
`README.md` (overview) | `METHODOLOGY-ADVERSARIAL.md` (protocol) | `features/FEATURE-STATUS-SUMMARY.md` (status) | `features/CROSS-FEATURE-LEARNINGS.md` (patterns) | `features/[feature]/` (17 feature dirs)

### Success Metrics

**Per feature**:
- Adversarial: 60-70% (hard cases)
- Random: 80-90% (typical cases)
- Gap: Random > Adversarial by 15-25 points

**Overall**: 85%+ average across all features after comprehensive validation

### Key Links

- **Methodology**: [METHODOLOGY-ADVERSARIAL.md](METHODOLOGY-ADVERSARIAL.md)
- **Feature status**: [features/FEATURE-STATUS-SUMMARY.md](features/FEATURE-STATUS-SUMMARY.md)
- **Patterns**: [features/CROSS-FEATURE-LEARNINGS.md](features/CROSS-FEATURE-LEARNINGS.md)
- **Critical review**: [../../tbta-experiment-critical-review.md](../../tbta-experiment-critical-review.md)
- **Example feature**: [features/number-systems/](features/number-systems/)

### Resources

- **TBTA data**: `.data/tbta/` (local)
- **TBTA website**: [sil.org/tbta](https://www.sil.org/)
- **SIL resources**: [ethnologue.com](https://www.ethnologue.com/)

---

## FAQ

**Can we use TBTA data?** Yes! For training (learn freely). Predict BEFORE checking test data. | **Disagree with TBTA?** Flag as potential error after exhaustive analysis (1-5% expected). | **Time per feature?** 2 weeks (training + validation). | **Multiple features?** Yes, but validate one at a time.

---

## Contributing

**We need**: Feature validators (15 remaining), pattern analysts, documentation writers, theological researchers

**Start**: [features/FEATURE-STATUS-SUMMARY.md](features/FEATURE-STATUS-SUMMARY.md)

**Questions**: Check docs first, then create an issue

---

## Complementary Approaches

### Strong's Hints as Context Enhancement

**Alternative**: Supplement predictions with Strong's word-level translation patterns

Add cross-linguistic hints to Strong's entries extracted from 900+ translations:
- Pattern example: "When Tagalog uses 'kami' → exclusive, 'tayo' → inclusive"
- Expected gain: +7% overall accuracy, +25% on edge cases
- Best for: Lexical features (Number, Person, Proximity, Lexical Sense)

**See detailed analysis**:
- `../tbta-strongs-hints-summary.md` - Executive summary and decision guide
- `../tbta-strongs-hints-llm-enhancement.md` - Integration approaches
- `../tbta-strongs-hints-evaluation.md` - Feature-by-feature analysis

---

**Last Updated**: 2025-11-07 | **Next Milestone**: 5 features by end of Q4 2025
