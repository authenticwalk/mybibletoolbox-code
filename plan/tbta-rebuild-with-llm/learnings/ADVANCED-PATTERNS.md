# Patterns 9-10: Translation Validation & Discourse Context

**Sources**: Person-Systems Experiment, Participant Tracking Experiment

These advanced patterns address validation and discourse-level features.

---

## Pattern 9: Validation Against Real Translations

**Source**: Person-Systems Experiment (100% accuracy)
**Achievement**: 100% validation match (11/11) with Indonesian/Tagalog translations

### Core Insight

Testing predictions against actual Bible translations confirms accuracy and reveals gaps. Translations represent expert human judgment across languages.

### Why This Matters

- **Catches theoretical errors**: Framework must match translator intuitions
- **Builds confidence**: High accuracy validates approach
- **Reveals edge cases**: Mismatches show where framework needs refinement
- **LLM improvement**: Can feed back examples to improve future prompts
- **Cross-linguistic validation**: Multiple languages provide independent confirmation

### Prompt Template for Validation

```
Translation Validation Prompt:

I predicted {predicted_value} for {feature_name} in {verse reference}.

Here are actual translations:
- Indonesian: {translation} (uses: {grammatical_choice})
- Tagalog: {translation} (uses: {grammatical_choice})
- {other language}: {translation} (uses: {grammatical_choice})

Analysis questions:
1. Do the actual translations match my prediction?
2. If not, what did translators choose instead?
3. What might explain the difference?
   - Did I misunderstand the theological context?
   - Did I miss a discourse factor?
   - Is this an ambiguous case with multiple valid readings?
4. Should I revise my prediction or document as ambiguous?

Validation result:
- Matches translations: Yes/No
- If no, reason for difference: ...
- Revised prediction (if needed): ...
```

### Example Validation Table (Clusivity)

| Passage | Prediction | Indonesian | Tagalog | Match? | Notes |
|---------|------------|------------|---------|--------|-------|
| John 17:21 | INCLUSIVE | Kita ✓ | atin ✓ | ✅ | Believers in divine unity |
| Matt 6:9 | EXCLUSIVE | Kami ✓ | aming ✓ | ✅ | Prayer excludes God |
| Acts 2:32 | EXCLUSIVE | Kami ✓ | amin ✓ | ✅ | Apostolic witness |
| Rom 5:1 | INCLUSIVE | Kita ✓ | atin ✓ | ✅ | Shared peace with God |
| Gen 1:26 | EXCLUSIVE | Kami ✓ | amin ✓ | ✅ | Divine creation |
| 1 John 1:3 | EXCLUSIVE | Kami ✓ | amin ✓ | ✅ | Apostolic proclamation |

**Result**: 100% accuracy (11/11 test cases)

### Language Selection for Validation

**Choose languages that encode the target feature grammatically**:

**For Person (Clusivity)**:
- Indonesian: Kita (inclusive) vs Kami (exclusive)
- Tagalog: Atin/tayo (inclusive) vs Amin/kami (exclusive)
- Vietnamese: Chúng ta (inclusive) vs Chúng tôi (exclusive)

**For Aspect**:
- Russian: Perfective vs Imperfective verb pairs
- Greek: Aorist vs Present tense
- Spanish: Preterite vs Imperfect

**For Evidentiality**:
- Turkish: Direct (-DI) vs Indirect (-mIş) evidentials
- Bulgarian: Witnessed vs Reported forms
- Japanese: Direct vs Hearsay markers

**For Voice**:
- Any language: Active vs Passive constructions
- Turkish: Passive suffix -Il/-In
- Indonesian: Di- passive prefix

### Validation Workflow

**Step 1: Make Predictions**
```
Run predictions on test set WITHOUT looking at translations
→ Prevents bias
→ Ensures blind testing
```

**Step 2: Gather Translations**
```
For each test verse:
- Indonesian translation (if applicable)
- Tagalog translation (if applicable)
- Other relevant language translations
- Note: Use multiple translations per language if available
```

**Step 3: Compare and Analyze**
```
For each verse:
1. Does prediction match translation choice?
2. If no:
   - Is translation ambiguous? (some translators chose both)
   - Is this a known difficult case?
   - Did I miss a contextual factor?
```

**Step 4: Error Categorization**
```
Type 1: Theological misunderstanding
Type 2: Discourse factor missed
Type 3: Grammatical ambiguity
Type 4: Translation variant (both valid)
```

**Step 5: Refinement**
```
For Type 1-3 errors:
→ Revise prompts to address gap
→ Re-test on same verse
→ Validate improvement

For Type 4 (dual readings):
→ Document as ambiguous
→ Provide both readings with confidence levels
```

### Cross-Linguistic Validation Confidence

```
Agreement levels:
- 3+ languages agree with prediction → 99% confidence (virtually certain)
- 2 languages agree → 95% confidence (very high)
- 1 language confirms → 85% confidence (high)
- 0 languages match → Flag for review (likely error)
```

### Example: Dual Reading Case

**Verse**: Matthew 6:9 "Our Father"
**Prediction**: EXCLUSIVE (excludes God from "our")
**Indonesian**: Bapa kami (EXCLUSIVE) ✓
**Tagalog**: Ama namin (EXCLUSIVE) ✓
**Analysis**: 2/2 agree → 95% confidence
**Alternative reading**: Some interpret as INCLUSIVE (God + us in unity)
**Resolution**: Document as EXCLUSIVE (high confidence), note alternative reading exists

---

## Pattern 10: Discourse-Level Context Strategy

**Source**: Participant Tracking Experiment (90% accuracy)
**Key Learning**: Some features require discourse memory beyond single verse

### The Problem

**Verse-level processing is insufficient** for:
- Participant Tracking (9 states)
- NounListIndex (consistent indices)
- Surface Realization (zero anaphora)
- Topic/Focus Tracking
- Definiteness (first vs subsequent mention)
- Coreference Resolution
- Notional Structure (discourse units)

**Example Failure**:
```yaml
# Without context (WRONG):
MAT.024.046:
  - text: "servant"
    participant_tracking: "First Mention"  # ❌ Actually continues from 24:45

# With context (CORRECT):
MAT.024.046:
  - text: "servant"
    participant_tracking: "Routine"  # ✓ Continues from previous verse
```

### Approach 1: LLM Memory (Recommended First)

**Concept**: Leverage LLM's existing knowledge of Bible content from training data.

#### How It Works

```python
# Conceptual prompt (not actual code)

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

#### Prompt Template

```
Participant Tracking Analysis with LLM Memory:

Verse to analyze: {reference}

Based on your knowledge of {book} {chapter} from training:

DISCOURSE CONTEXT:
1. Who are the main participants in this chapter?
2. Where does each participant first appear?
3. Has "{entity_name}" been mentioned before in this chapter?
   - If YES: In which verse? What state (First Mention, Routine, Restaging)?
   - If NO: This is First Mention

For entity "{entity_name}" in current verse:
1. Is this the first mention of this entity in this discourse section?
   → If YES: First Mention (I)

2. Has this entity been mentioned recently (within 3-5 verses)?
   → If YES: Routine (D)

3. Has this entity been absent and now returns?
   → If YES: Restaging (R)

4. Is this entity about to leave the narrative permanently?
   → If YES: Exiting (E)

5. Can this entity be inferred from context without explicit mention?
   → If YES: Frame Inferable (F)

Predicted Participant Tracking value: ...
Reasoning based on discourse context: ...
Confidence: High/Medium/Low (based on LLM memory strength)
```

#### Expected Accuracy

- **Well-known books** (Gospels, Genesis, Romans): 85-90%
- **Moderately known** (Judges, Colossians): 75-85%
- **Obscure books** (Zephaniah, Chronicles): 60-75%

### Approach 2: Expanded Context Window (Fallback)

**Concept**: Load and process full chapters, maintaining entity registry across verse boundaries.

#### How It Works

```python
# Conceptual approach (not actual code)

class ChapterDiscourseContext:
    """Maintain discourse state across chapter"""
    def __init__(self, chapter_ref):
        self.chapter = chapter_ref
        self.entity_registry = {}      # text → Entity object
        self.verse_history = []        # Previous verses in order
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
```

#### Pros

✅ **100% accuracy potential** - Complete discourse history available
✅ **Explicit tracking** - Registry provides ground truth for entity states
✅ **Systematic** - Deterministic algorithm, not LLM-dependent
✅ **Debuggable** - Can inspect registry at each verse
✅ **Coreference chains** - Explicit pronoun → antecedent mappings

#### Cons

⚠️ **Infrastructure changes** - Requires processing pipeline refactor
⚠️ **Memory overhead** - Must load full chapter (50+ verses)
⚠️ **Token costs** - More context = more tokens per prediction
⚠️ **Complexity** - Registry management, state tracking

### Recommended Hybrid Strategy

**Use both approaches strategically**:

1. **Start with Approach 1 (LLM Memory)** for rapid deployment (2 weeks)
2. **Test accuracy** on well-known vs obscure books
3. **Add Approach 2 (Explicit Context)** only where LLM memory insufficient
4. **Result**: Hybrid system - fast for most books, accurate for all

#### Decision Criteria

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

### Discourse Context by Genre

**Minimum Context Window**:

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

---

## Integration: Validation + Discourse Context

### Combined Workflow

**Step 1: Implement discourse-aware prompts** (Approach 1)
```
Add LLM memory context to predictions
→ Test on 50 verses
→ Measure accuracy
```

**Step 2: Validate with translations**
```
Compare predictions to actual translations
→ Indonesian/Tagalog for Clusivity
→ Turkish for Evidentiality
→ etc.
```

**Step 3: Analyze errors**
```
Categorize mismatches:
→ LLM memory gap? (Add Approach 2)
→ Theoretical error? (Refine prompts)
→ Dual reading? (Document both)
```

**Step 4: Refine and deploy**
```
Update prompts based on errors
→ Re-validate
→ Deploy to production
```

### Expected Results

**With LLM Memory (Approach 1)**:
- Participant Tracking: 85-90% accuracy
- Validation match rate: 85-90%
- Implementation time: 2 weeks

**With Explicit Context (Approach 2) added selectively**:
- Participant Tracking: 95-100% accuracy
- Validation match rate: 95-100%
- Implementation time: 4-6 weeks total

---

## Conclusion

These advanced patterns (Translation Validation, Discourse Context) complement the core patterns to create a complete framework:

**Pattern 9 (Validation)**: Ensures predictions match human translator judgment
**Pattern 10 (Discourse)**: Enables features requiring context beyond single verse

Together with Patterns 1-8, these provide a comprehensive methodology for high-accuracy TBTA feature prediction using LLM prompting.

**Key Insight**: Always validate predictions against real translations, and use LLM memory for discourse context before building complex infrastructure.

---

## Quick Reference

### For Validation:
1. Make blind predictions (don't look at translations first)
2. Gather translations in languages that encode the feature
3. Compare and categorize errors
4. Refine prompts based on mismatches
5. Document dual readings as ambiguous

### For Discourse Context:
1. Try LLM memory approach first (fast, 2 weeks)
2. Test accuracy on well-known books
3. Add explicit context only where LLM memory fails
4. Use hybrid strategy for optimal results
5. Adjust context window by genre

---

**All patterns use LLM prompting, not Python code.**
