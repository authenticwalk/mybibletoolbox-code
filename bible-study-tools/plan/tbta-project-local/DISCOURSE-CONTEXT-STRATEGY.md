# TBTA Discourse-Level Context Strategy

**Date**: 2025-11-05
**Status**: Proposed
**Priority**: HIGH - Affects multiple core features
**Context**: Addresses verse-level scope limitation identified in ANALYSIS-SUMMARY.md

---

## Executive Summary

Current TBTA implementation processes verses in isolation, but multiple critical features require **discourse-level context** beyond single verse boundaries. This document proposes three approaches to address this limitation, recommends a preferred solution, and outlines validation methodology.

**Recommendation**: Start with **Approach 1 (LLM Memory)** for immediate implementation, with **Approach 2 (Expanded Context Window)** as fallback for accuracy-critical features.

---

## 1. Problem Statement

### 1.1 Current Limitation: Verse-Level Scope

The existing TBTA feature extraction pipeline processes one verse at a time:

```python
# Current approach
for verse_ref in chapter:
    verse_data = load_verse(verse_ref)
    features = extract_features(verse_data)  # ❌ No context from other verses
    save_features(verse_ref, features)
```

**Impact**: Features requiring discourse history **cannot be accurately predicted** without context.

### 1.2 Features Requiring Discourse Context

Based on experimental analysis (TRANSFERABLE-LEARNINGS.md, lines 323-371):

#### Critical Dependencies (HIGH Priority)

1. **Participant Tracking** (9 states)
   - **Problem**: Cannot distinguish "First Mention" vs "Routine" without tracking prior appearances
   - **Example**: Matthew 24:46 - "servant" continues from 24:45, not a new entity
   - **Impact**: 100% error rate on state classification without context

2. **NounListIndex**
   - **Problem**: Cannot assign consistent indices across verses
   - **Example**: Same entity needs same index throughout discourse unit
   - **Impact**: Pronouns cannot inherit indices from antecedents

3. **Surface Realization**
   - **Problem**: Zero anaphora requires discourse history to resolve
   - **Example**: "Ø went home" - who went? Need prior context
   - **Impact**: Cannot determine what is elided

4. **Topic/Focus Tracking**
   - **Problem**: Topic continuity requires tracking across boundaries
   - **Example**: Topic shift detection requires knowing previous topic
   - **Impact**: Cannot identify thematic structure

#### Medium Dependencies

5. **Notional Structure**
   - **Problem**: Discourse structure spans multiple clauses/verses
   - **Needs**: Paragraph and episode-level boundaries

6. **Coreference Resolution**
   - **Problem**: Pronouns reference entities mentioned earlier
   - **Needs**: Registry of entities across verses

7. **Definiteness**
   - **Problem**: First mention vs subsequent mention distinction
   - **Needs**: History of what has been introduced

### 1.3 Concrete Failure Example

**Without Context** (WRONG):
```yaml
MAT.024.046:
  entities:
    - text: "servant"
      participant_tracking: "First Mention"  # ❌ Wrong!
      noun_index: 7                          # ❌ Inconsistent!
    - text: "lord"
      participant_tracking: "First Mention"  # ❌ Wrong!
      noun_index: 8                          # ❌ Inconsistent!
```

**With Chapter Context** (CORRECT):
```yaml
# Context from MAT.024.045:
#   - "master" introduced (index 5)
#   - "servant" introduced (index 6)

MAT.024.046:
  entities:
    - text: "servant"
      participant_tracking: "Routine"        # ✓ Continues from 24:45
      noun_index: 6                          # ✓ Inherits from first mention
      antecedent: "MAT.024.045:servant"
    - text: "lord"
      participant_tracking: "Routine"        # ✓ Same as "master"
      noun_index: 5                          # ✓ Coreference with master
      antecedent: "MAT.024.045:master"
```

**Accuracy Impact**: 0% → 100% with proper context

---

## 2. Proposed Solutions

### Approach 1: LLM Memory (Recommended First)

**Concept**: Leverage LLM's existing knowledge of Bible content from training data instead of re-extracting everything.

#### How It Works

```python
def predict_with_llm_memory(verse_ref, verse_text, feature):
    """Use LLM's built-in Bible knowledge for discourse context"""

    prompt = f"""
    You know Genesis 4:1-16 from your training data.

    For verse {verse_ref}: "{verse_text}"

    Based on your knowledge of the full chapter context:
    1. Which entities have been mentioned previously in this chapter?
    2. Which entities are appearing for the first time?
    3. What relationships were established earlier?

    Predict {feature} for each entity.
    """

    return llm.predict(prompt)
```

#### Pros

✅ **Zero infrastructure changes** - Works with existing verse-by-verse pipeline
✅ **Immediate implementation** - No data restructuring required
✅ **Leverages existing knowledge** - Bible is heavily represented in training data
✅ **Natural discourse understanding** - LLMs excel at narrative comprehension
✅ **Handles all genres** - Narrative, poetry, epistles equally well
✅ **Cost-effective** - No additional data loading/processing

#### Cons

⚠️ **Accuracy uncertainty** - Need to validate LLM memory is sufficient
⚠️ **Less well-known books** - Minor prophets, Numbers may have sparse coverage
⚠️ **Version variations** - LLM may mix translations (NIV/KJV/ESV)
⚠️ **Rare verses** - Obscure passages may lack detailed training
⚠️ **No ground truth verification** - Cannot check against explicit data

#### Validation Test

**Test LLM memory sufficiency**:
```yaml
test_cases:
  well_known:
    - reference: "Genesis 1:26-27"
      question: "Who are the participants across these verses?"
      expected: "God (continuing), man (new in 27)"

  moderately_known:
    - reference: "Matthew 24:45-47"
      question: "Track the master/servant through these verses"
      expected: "Master (45), servant (45), both continue to 46-47"

  obscure:
    - reference: "Zephaniah 2:8-10"
      question: "Which entities continue from verse 8 to 9?"
      expected: [Test if LLM knows this passage]
```

**Success Criteria**: 90%+ accuracy on well-known passages, 70%+ on moderately known

#### Implementation Plan

**Phase 1: Validate** (1-2 days)
1. Test 50 verses across well-known/moderate/obscure books
2. Measure accuracy against known ground truth
3. Identify books/genres where LLM memory fails

**Phase 2: Implement** (2-3 days)
1. Add discourse-aware prompts to existing feature extractors
2. Structure prompts to reference "your knowledge of the full chapter"
3. Test on Participant Tracking first (highest priority)

**Phase 3: Refine** (1 week)
1. Build prompt library for different features
2. Calibrate by book/genre (Genesis high confidence, Zephaniah lower)
3. Flag low-confidence predictions for manual review

**Estimated Timeline**: 2 weeks to production-ready

---

### Approach 2: Expanded Context Window (Fallback/Hybrid)

**Concept**: Load and process full chapters instead of individual verses, maintaining entity registry across verse boundaries.

#### How It Works

```python
class ChapterDiscourseContext:
    """Maintain discourse state across chapter"""
    def __init__(self, chapter_ref):
        self.chapter = chapter_ref
        self.entity_registry = {}      # text → Entity object
        self.verse_history = []        # Previous verses in order
        self.coreference_chains = []   # Pronoun → antecedent mappings
        self.noun_index_counter = 0    # Consistent indexing

    def process_chapter(self):
        """Process all verses maintaining context"""
        for verse_ref in self.get_verses():
            # CRITICAL: Context includes all previous verses
            context = {
                'previous_verses': self.verse_history,
                'known_entities': self.entity_registry,
                'noun_indices': self.get_current_indices()
            }

            # Predict with full context
            features = self.predict_verse(verse_ref, context)

            # Update registry for next verse
            self.update_registry(features)
            self.verse_history.append(verse_ref)

        return self.get_all_features()
```

#### Architecture

```
Before (verse-level):
  Load MAT.024.045 → Process → Save
  Load MAT.024.046 → Process → Save  ❌ No memory of 045
  Load MAT.024.047 → Process → Save  ❌ No memory of 045-046

After (chapter-level):
  Load MAT.024 (all verses)
  → Process 045 (initialize registry)
  → Process 046 (use registry from 045)  ✓ Knows about prior entities
  → Process 047 (use registry from 045-046)  ✓ Full history
  Save all verse outputs
```

#### Pros

✅ **100% accuracy potential** - Complete discourse history available
✅ **Explicit tracking** - Registry provides ground truth for entity states
✅ **Systematic** - Deterministic algorithm, not LLM-dependent
✅ **Debuggable** - Can inspect registry at each verse
✅ **Coreference chains** - Explicit pronoun → antecedent mappings
✅ **Cross-feature consistency** - Same registry for Participant Tracking, NounIndex, Surface Realization

#### Cons

⚠️ **Infrastructure changes** - Requires processing pipeline refactor
⚠️ **Memory overhead** - Must load full chapter (50+ verses)
⚠️ **Token costs** - More context = more tokens per prediction
⚠️ **Complexity** - Registry management, state tracking
⚠️ **Chapter boundaries** - Need to determine appropriate context units

#### Implementation Details

**Entity Registry Structure**:
```python
class Entity:
    def __init__(self, text, first_verse):
        self.text = text
        self.first_appearance = first_verse
        self.noun_index = None  # Assigned on first appearance
        self.mentions = []      # All verses where mentioned

    def get_tracking_state(self, current_verse):
        """Determine participant tracking state"""
        if current_verse == self.first_appearance:
            return "First Mention"
        elif self.is_returning_after_gap(current_verse):
            return "Restaging"
        else:
            return "Routine"
```

**Minimum Context Window** (by genre):
```yaml
narrative_prose:
  minimum: "Current chapter"
  optimal: "Discourse unit (2-3 chapters if continuous)"
  example: "Matthew 24 (Olivet Discourse = continuous)"

dialogue_heavy:
  minimum: "Current dialogue span + narrative frame"
  optimal: "Full dialogue section"
  example: "John 3 (Nicodemus conversation)"

poetry:
  minimum: "Current poem/oracle"
  optimal: "Full book section"
  example: "Psalm 119 (single acrostic poem)"

epistolary:
  minimum: "Current argument section"
  optimal: "Full letter section"
  example: "Romans 5-8 (single argument flow)"
```

#### Implementation Plan

**Phase 1: Prototype** (1 week)
1. Build DiscourseContext class with entity registry
2. Implement chapter-level processing for Matthew 24
3. Test Participant Tracking accuracy vs verse-level

**Phase 2: Integrate** (2 weeks)
1. Refactor processing pipeline to support chapter-level
2. Implement context window detection by genre
3. Add registry persistence (save/load between sessions)

**Phase 3: Scale** (2 weeks)
1. Process all narrative books (Gospels, Acts, OT narrative)
2. Validate accuracy on 10+ chapters
3. Optimize memory usage

**Estimated Timeline**: 5 weeks to production-ready

---

### Approach 3: Two-Pass Processing (Comprehensive)

**Concept**: First pass extracts chapter-level discourse structure, second pass uses that structure for verse-level feature prediction.

#### How It Works

**Pass 1: Discourse Analysis** (Chapter-level)
```python
def pass1_discourse_analysis(chapter_ref):
    """Extract discourse-level structures"""
    chapter_text = load_full_chapter(chapter_ref)

    discourse_structure = llm.analyze(f"""
    Analyze discourse structure of {chapter_ref}:

    1. Participant Registry:
       - List all entities (people, things, concepts)
       - Mark first appearance verse for each
       - Track which verses each appears in

    2. Notional Structure:
       - Identify discourse units (scenes, sections)
       - Mark boundaries

    3. Topic Flow:
       - What is the topic in each section?
       - Where do topic shifts occur?

    4. Coreference Chains:
       - Map all pronouns to antecedents

    Output as structured data.
    """)

    save_discourse_structure(chapter_ref, discourse_structure)
    return discourse_structure
```

**Pass 2: Verse Feature Extraction** (Uses discourse structure)
```python
def pass2_feature_extraction(verse_ref):
    """Extract features using discourse context"""
    # Load discourse structure from Pass 1
    chapter = get_chapter(verse_ref)
    discourse = load_discourse_structure(chapter)

    verse_data = load_verse(verse_ref)

    # Now predict with full context
    features = predict_features(
        verse_data,
        participant_registry=discourse.participants,
        coreference_chains=discourse.coreferences,
        topic_context=discourse.topics
    )

    return features
```

#### Pros

✅ **Best accuracy** - Combines LLM discourse understanding + systematic extraction
✅ **Separation of concerns** - Discourse analysis separate from feature extraction
✅ **Reusable structure** - Pass 1 output used by all features
✅ **Cacheable** - Discourse structure computed once, reused many times
✅ **Human reviewable** - Can manually verify Pass 1 output
✅ **Incremental improvement** - Refine discourse analysis without re-running extraction

#### Cons

⚠️ **Most complex** - Two separate processing pipelines
⚠️ **Highest cost** - LLM analysis of full chapters + verse-level processing
⚠️ **Dependencies** - Pass 2 blocked on Pass 1 completion
⚠️ **Error propagation** - Pass 1 errors affect all Pass 2 predictions
⚠️ **Storage overhead** - Must store intermediate discourse structures

#### Implementation Plan

**Phase 1: Design** (1 week)
1. Define discourse structure schema
2. Design prompt for Pass 1 discourse analysis
3. Create validation tests

**Phase 2: Pass 1 Implementation** (2 weeks)
1. Build chapter-level discourse analyzer
2. Test on 5 chapters (diverse genres)
3. Validate output quality

**Phase 3: Pass 2 Integration** (2 weeks)
1. Modify feature extractors to consume discourse structure
2. Test accuracy improvement vs verse-only
3. Build caching layer

**Phase 4: Scale** (3 weeks)
1. Process discourse structure for all books
2. Human review of discourse structures
3. Refine based on errors

**Estimated Timeline**: 8 weeks to production-ready

---

## 3. Comparison Matrix

| Criterion | Approach 1: LLM Memory | Approach 2: Expanded Context | Approach 3: Two-Pass |
|-----------|----------------------|---------------------------|---------------------|
| **Implementation Time** | 2 weeks | 5 weeks | 8 weeks |
| **Accuracy (est.)** | 80-90% | 95-100% | 95-100% |
| **Infrastructure Change** | None | Moderate | Significant |
| **Token Cost** | Low (verse-level) | Medium (chapter context) | High (2x passes) |
| **Debuggability** | Low (LLM black box) | High (explicit registry) | High (structured output) |
| **Scalability** | Excellent | Good | Good |
| **Failure Handling** | Graceful degradation | Deterministic | Intermediate caching |
| **Human Review** | Hard to verify | Registry inspectable | Pass 1 reviewable |
| **Best For** | Rapid deployment | Accuracy-critical | Long-term comprehensive |

---

## 4. Recommended Strategy

### 4.1 Primary Recommendation: Hybrid Approach

**Start with Approach 1 (LLM Memory)**, then **selectively apply Approach 2** for accuracy-critical features.

#### Rationale

1. **Immediate value** - Approach 1 can be deployed in 2 weeks
2. **Low risk** - No pipeline changes, easy to test and iterate
3. **Validates need** - Proves discourse context improves accuracy
4. **Identifies gaps** - Testing reveals which books/features need explicit tracking
5. **Incremental investment** - Only build Approach 2 where Approach 1 fails

#### Implementation Sequence

**Milestone 1: LLM Memory Baseline** (Weeks 1-2)
- Implement discourse-aware prompts
- Test on Participant Tracking (highest priority)
- Measure accuracy on 50 test verses
- **Go/No-Go Decision**: If >85% accuracy → Deploy broadly, If <85% → Add Approach 2

**Milestone 2: Selective Expansion** (Weeks 3-4)
- For books with <85% accuracy → Implement Approach 2 (chapter context)
- Likely candidates: Minor prophets, Numbers, Chronicles
- Build hybrid system: LLM Memory for most books, Explicit Context for difficult ones

**Milestone 3: Feature Rollout** (Weeks 5-8)
- Apply to NounListIndex (second priority)
- Apply to Surface Realization
- Apply to Topic/Focus Tracking
- Measure accuracy improvements

**Milestone 4: Optimization** (Weeks 9-12)
- Refine prompts based on error analysis
- Add Approach 2 where needed
- Build confidence calibration (by book/genre)
- Consider Approach 3 for future enhancement

### 4.2 Decision Criteria

**When to use Approach 1 (LLM Memory)**:
- ✓ Well-known books (Gospels, Genesis, Psalms, Romans)
- ✓ Features with clear discourse patterns (Participant Tracking)
- ✓ Development speed is priority
- ✓ Acceptable accuracy: 80-90%

**When to use Approach 2 (Expanded Context)**:
- ✓ Accuracy-critical features (NounListIndex consistency)
- ✓ Features with complex state (coreference chains)
- ✓ Obscure books where LLM memory uncertain
- ✓ Required accuracy: 95-100%

**When to use Approach 3 (Two-Pass)**:
- ✓ Long-term comprehensive solution
- ✓ Multiple features benefit from same discourse analysis
- ✓ Human review of discourse structure desired
- ✓ Computational cost acceptable

---

## 5. Validation Methodology

### 5.1 Test Corpus Design

**Stratified Sampling** across three dimensions:

#### Dimension 1: Book Familiarity
```yaml
high_familiarity:
  books: [Matthew, Genesis, Psalms, Romans]
  test_verses: 20
  expected_llm_memory: "Excellent"

medium_familiarity:
  books: [Judges, Ezra, Colossians, James]
  test_verses: 15
  expected_llm_memory: "Good"

low_familiarity:
  books: [Numbers, Chronicles, Zephaniah, Philemon]
  test_verses: 15
  expected_llm_memory: "Uncertain"
```

#### Dimension 2: Feature Type
```yaml
participant_tracking:
  test_cases: 20
  success_metric: "State classification accuracy"

noun_list_index:
  test_cases: 20
  success_metric: "Index consistency across verses"

surface_realization:
  test_cases: 10
  success_metric: "Pronoun resolution accuracy"
```

#### Dimension 3: Genre
```yaml
narrative: [Genesis 4, Matthew 24, Acts 2]
dialogue: [John 3, Job 38-39]
poetry: [Psalm 23, Isaiah 53]
epistolary: [Romans 5, Ephesians 4]
```

**Total Test Set**: 50 verses × 3 features = 150 test predictions

### 5.2 Ground Truth Sources

1. **Existing TBTA annotations** - For Participant Tracking ground truth
2. **Manual annotation** - Expert linguist labels 50 verses
3. **Translation comparison** - Indonesian/Tagalog for clusivity, Turkish for evidentials
4. **Academic grammars** - Wallace, Porter for Greek; GKC, IBHS for Hebrew

### 5.3 Success Metrics

**Tier 1 (Production Ready)**:
- Accuracy: ≥95%
- Precision: ≥90% (minimize false positives)
- Recall: ≥90% (minimize false negatives)
- Confidence calibration: High confidence cases ≥98% accurate

**Tier 2 (Acceptable)**:
- Accuracy: 85-95%
- Precision: ≥85%
- Recall: ≥85%
- Confidence calibration: High confidence ≥95%, Medium ≥85%

**Tier 3 (Needs Improvement)**:
- Accuracy: 70-85%
- Use for research only, not production
- Flag all predictions for human review

### 5.4 Error Analysis Framework

**Categorize errors** to identify patterns:

```yaml
error_type_1_semantic_gap:
  description: "LLM lacks specific discourse knowledge"
  example: "Obscure minor prophet reference"
  solution: "Add Approach 2 for this book"

error_type_2_ambiguity:
  description: "Legitimately ambiguous (multiple valid readings)"
  example: "Dual reading in Pauline letter"
  solution: "Flag as dual-reading, provide both"

error_type_3_complex_coreference:
  description: "Pronoun resolution requires deep context"
  example: "Multiple possible antecedents"
  solution: "Add Approach 2 for coreference chains"

error_type_4_structural:
  description: "Feature requires explicit tracking"
  example: "NounListIndex consistency"
  solution: "Add Approach 2 for this feature"
```

**Action based on error distribution**:
- >50% Type 1 → Approach 2 needed for this book
- >50% Type 2 → Document ambiguities, acceptable
- >50% Type 3 → Implement coreference module
- >50% Type 4 → Approach 2 required for feature

---

## 6. Impact on Existing Features

### 6.1 Features Requiring Updates

**Critical Updates** (blocked without discourse context):

| Feature | Current State | Update Required | Priority |
|---------|--------------|----------------|----------|
| Participant Tracking | 90% accuracy (limited test) | Add discourse context | P0 |
| NounListIndex | Not implemented | Build with context from start | P0 |
| Surface Realization | Partial | Add zero anaphora resolution | P1 |
| Topic NP | Not implemented | Requires topic tracking | P1 |

**Medium Updates** (degraded without context):

| Feature | Current State | Impact | Priority |
|---------|--------------|--------|----------|
| Definiteness | Rule-based | First mention detection improves | P2 |
| Notional Structure | Not implemented | Discourse units needed | P2 |
| Coreference | Implicit | Make explicit | P2 |

**Low/No Impact** (verse-level sufficient):

| Feature | Reason |
|---------|--------|
| Mood | Explicit in TBTA (Tier 0) |
| Aspect | Explicit in TBTA (likely Tier 0) |
| Time | Explicit in TBTA (likely Tier 0) |
| IlLocutionary Force | Explicit in TBTA |
| Number (basic) | Mostly explicit |
| Person (basic) | Mostly explicit |

### 6.2 Feature-Specific Recommendations

#### Participant Tracking
**Current**: 90% accuracy with manual discourse analysis
**With Approach 1**: 85-90% expected (sufficient for production)
**With Approach 2**: 95-100% (matches experiment results)
**Recommendation**: Start with Approach 1, add Approach 2 if <90%

#### NounListIndex
**Current**: Not implemented
**Requirement**: MUST have consistent indices across verses (100% requirement)
**Recommendation**: **Use Approach 2** from start - cannot compromise on consistency

#### Surface Realization
**Current**: Partial implementation
**Challenge**: Zero anaphora (Ø) resolution
**Recommendation**: Approach 1 for most, Approach 2 for pro-drop languages (Greek, Hebrew)

#### Topic/Focus
**Current**: Not implemented
**Challenge**: Topic shifts require knowing previous topic
**Recommendation**: Approach 1 sufficient - topic shifts are salient discourse features LLMs handle well

### 6.3 Integration Points

**Code modifications needed**:

```python
# Before (verse-only)
def extract_participant_tracking(verse_data):
    entities = get_entities(verse_data)
    for entity in entities:
        state = predict_state(entity)  # ❌ No context
    return results

# After (with discourse context) - Approach 1
def extract_participant_tracking(verse_ref, verse_data):
    chapter = get_chapter(verse_ref)

    # Add discourse-aware prompt
    prompt = f"""
    Based on your knowledge of {chapter},
    previous verses have introduced these entities: [context]

    For verse {verse_ref}, classify each entity's participant tracking state.
    """

    state = llm.predict_with_context(prompt, verse_data)
    return results

# After (with explicit registry) - Approach 2
def extract_participant_tracking(verse_ref, verse_data, discourse_context):
    entities = get_entities(verse_data)
    for entity in entities:
        # Check registry
        if entity in discourse_context.entity_registry:
            state = "Routine"
        else:
            state = "First Mention"
            discourse_context.register_entity(entity, verse_ref)
    return results
```

---

## 7. Risk Assessment

### 7.1 Approach 1 Risks

**Risk**: LLM memory insufficient for obscure books
**Likelihood**: Medium
**Impact**: Medium (accuracy drops to 70-80%)
**Mitigation**: Test early, add Approach 2 for problematic books

**Risk**: LLM mixes Bible versions
**Likelihood**: Low
**Impact**: Low (verse identification still accurate)
**Mitigation**: Include version specification in prompts

**Risk**: High token costs at scale
**Likelihood**: Low (verse-level prompts are small)
**Impact**: Low
**Mitigation**: Monitor costs, batch processing

### 7.2 Approach 2 Risks

**Risk**: Pipeline refactor introduces bugs
**Likelihood**: Medium
**Impact**: High (blocks all processing)
**Mitigation**: Extensive testing, gradual rollout

**Risk**: Memory overhead for long chapters
**Likelihood**: Low (most chapters <50 verses)
**Impact**: Medium
**Mitigation**: Lazy loading, registry pruning

**Risk**: Discourse unit boundaries unclear
**Likelihood**: Medium (especially in epistles)
**Impact**: Medium (suboptimal context window)
**Mitigation**: Genre-specific rules, human review

### 7.3 Approach 3 Risks

**Risk**: Pass 1 errors propagate to all features
**Likelihood**: Medium
**Impact**: High
**Mitigation**: Human review of Pass 1 output, confidence thresholds

**Risk**: High complexity delays deployment
**Likelihood**: High
**Impact**: High (opportunity cost)
**Mitigation**: Use Approach 1/2 for interim solution

---

## 8. Success Criteria & Next Steps

### 8.1 Definition of Success

**Phase 1 Success** (Approach 1 validation):
- ✓ 50 test cases evaluated
- ✓ Participant Tracking accuracy ≥85%
- ✓ Clear understanding of where LLM memory succeeds/fails
- ✓ Decision made: Deploy broadly OR add Approach 2

**Phase 2 Success** (Production deployment):
- ✓ Participant Tracking deployed for all books
- ✓ NounListIndex implemented with consistent indices
- ✓ Surface Realization updated with discourse context
- ✓ Overall feature accuracy ≥90%

**Phase 3 Success** (Comprehensive):
- ✓ All discourse-dependent features implemented
- ✓ Hybrid system optimized (Approach 1 + selective Approach 2)
- ✓ Documentation updated
- ✓ Ready for Approach 3 evaluation

### 8.2 Immediate Next Steps

**Week 1: Validation**
1. Design test corpus (50 verses across 3 dimensions)
2. Manually annotate ground truth for Participant Tracking
3. Implement Approach 1 prototype for Participant Tracking
4. Run validation tests

**Week 2: Analysis**
1. Analyze results by book/genre/feature
2. Categorize errors (4 types)
3. Calculate accuracy metrics
4. Make go/no-go decision

**Week 3-4: Implementation** (if validation succeeds)
1. Refine prompts based on error analysis
2. Implement for NounListIndex (Approach 2 required)
3. Build hybrid system
4. Deploy to production

**Week 5-8: Expansion**
1. Roll out to Surface Realization
2. Roll out to Topic/Focus
3. Monitor accuracy
4. Iterate based on user feedback

### 8.3 Decision Points

**Decision Point 1** (End of Week 2):
- IF Approach 1 achieves ≥85% accuracy on well-known books → Deploy broadly
- ELSE IF 70-85% → Deploy with confidence flags + add Approach 2 for difficult books
- ELSE IF <70% → Abandon Approach 1, fully implement Approach 2

**Decision Point 2** (End of Week 4):
- IF Approach 2 needed for >30% of books → Consider Approach 3 for long-term
- ELSE → Continue with hybrid Approach 1 + selective Approach 2

**Decision Point 3** (End of Week 8):
- Evaluate ROI of Approach 3 for comprehensive solution
- Decide if worth 8-week investment

---

## 9. Conclusion

### Key Insights

1. **Discourse context is essential** for 7+ TBTA features (high priority)
2. **Verse-level processing is fundamentally insufficient** for Participant Tracking, NounListIndex, Surface Realization
3. **Three viable approaches** exist with different trade-offs
4. **Hybrid strategy recommended**: Start with LLM Memory (fast), add Explicit Context (accurate) where needed

### Strategic Recommendation

**Implement Approach 1 (LLM Memory) immediately** to:
- Prove discourse context value in 2 weeks
- Deploy Participant Tracking improvements quickly
- Identify books/features needing Approach 2

**Reserve Approach 2 (Expanded Context)** for:
- NounListIndex (consistency requirement)
- Books where LLM memory insufficient
- Features requiring 95%+ accuracy

**Consider Approach 3 (Two-Pass)** for:
- Long-term comprehensive solution
- After Approach 1+2 hybrid proves value
- When multiple features benefit from shared discourse analysis

### Expected Outcomes

**Short-term** (2-4 weeks):
- Participant Tracking accuracy: 85-90%
- NounListIndex implemented: 95%+ index consistency
- 2-3 discourse-dependent features deployed

**Medium-term** (8-12 weeks):
- 7+ features using discourse context
- Hybrid system optimized
- Accuracy calibration by book/genre

**Long-term** (6+ months):
- Full TBTA feature coverage
- Approach 3 implemented for comprehensive solution
- Human review workflows integrated

---

**Document Status**: READY FOR REVIEW
**Next Action**: Validate Approach 1 with 50-verse test corpus
**Owner**: TBD
**Timeline**: Start validation in Week 1
