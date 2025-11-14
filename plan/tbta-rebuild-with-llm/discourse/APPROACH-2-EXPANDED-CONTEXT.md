# Approach 2: Expanded Context Window (Fallback/Hybrid)

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

