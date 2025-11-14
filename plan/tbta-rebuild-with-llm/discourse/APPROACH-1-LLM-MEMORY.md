# Approach 1: LLM Memory (Recommended First)
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
