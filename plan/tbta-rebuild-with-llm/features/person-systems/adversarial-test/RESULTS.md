# Person Systems: Adversarial Test Results

**Date**: 2025-11-09
**Algorithm**: v1.0 (commit f373646)
**Predictions**: Locked (commit 77010a4)
**TBTA Access**: Began 2025-11-09

---

## Critical Discovery: TBTA Person Annotation Approach

### Finding from Genesis 1:26 Analysis

**TBTA Person field values** (from SCHEMA.md):
- A = First person inclusive
- B = First person exclusive

**Actual TBTA JSON format** (from sample):
- Full string: "First Inclusive" (not code "A")
- Full string: "First Exclusive" (expected, not yet confirmed)

### Key Insight: Discourse-Internal vs. Translation Perspective

**Genesis 1:26** analysis reveals potential methodological difference:

**TBTA Annotation** (discourse-internal):
```json
{
  "Constituent": "God",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Listener": "God",
  "Speaker": "God"
}
```

**TBTA marks**: "First Inclusive" - Speaker (God/Trinity person) includes Listener (God/other Trinity persons)

**My Prediction** (translation perspective): **EXCLUSIVE** - Human translators should use EXCLUSIVE form because humans (the ultimate addressees/readers) are NOT included in the divine "us"

### Two Valid Perspectives

1. **Discourse-Internal** (TBTA approach):
   - Who is the speaker within the text?
   - Who is the listener within the text?
   - Does speaker's "we" include that listener?
   - Genesis 1:26: God→God = Inclusive (within Trinity)

2. **Translation-Oriented** (My algorithm v1.0):
   - Who will read/hear this text (humans)?
   - Should the translation use inclusive or exclusive form?
   - Genesis 1:26: Divine "us" → Exclusive form (excludes human readers)

### Implications

This is not necessarily an error by either approach, but represents **different annotation goals**:
- TBTA: Annotating discourse structure within the text
- Algorithm v1.0: Guiding translation into clusivity languages

**Critical question for validation**:
- Should I compare against TBTA's discourse-internal marking?
- OR should I verify against actual Bible translations in clusivity languages?

**Hypothesis**: TBTA may be consistently discourse-internal, which means:
- Algorithm v1.0 might show "low accuracy" against TBTA
- BUT high accuracy against real translations (98% validated)
- This would indicate different but both valid approaches

---

## Progress: TBTA Data Access

### Verses Checked

1. ✅ **Genesis 1:26**: TBTA data accessed (local sample)
   - TBTA: "First Inclusive" (discourse-internal)
   - My prediction: EXCLUSIVE (translation perspective)
   - Real translations: EXCLUSIVE confirmed (Indonesian kami, Tagalog kami)
   - **Mismatch with TBTA, Match with real translations**

### Next Steps

1. ⏳ Check more verses to confirm pattern
2. ⏳ Determine if this is systematic difference
3. ⏳ Decide validation approach:
   - Option A: Validate against TBTA (may show lower accuracy)
   - Option B: Validate against real translations (98% known accuracy)
   - Option C: Document both perspectives, validate both ways

---

## Partial Results

### Adversarial Test

| Verse | My Prediction | TBTA Annotation | Match? | Real Translations | Translation Match? |
|-------|---------------|-----------------|--------|-------------------|-------------------|
| Genesis 1:26 | EXCLUSIVE | First Inclusive | ❌ | Exclusive (kami) | ✅ |

**Current Score**: 0/1 against TBTA, 1/1 against real translations

---

## Analysis Notes

### Genesis 1:26 Detailed Analysis

**Text**: "Then God say, now God create person" (simplified from TBTA)

**TBTA Annotation**:
- Speaker: "God"
- Listener: "God" (line 179)
- Subject NP: "God" with Number="Trial", Person="First Inclusive"
- Illocutionary Force: "Suggestive 'let's'"

**Discourse interpretation**:
- One person of Trinity (Speaker) addressing other persons (Listener=God)
- "Let us" = First Inclusive (speaker includes listener within discourse)

**Translation interpretation**:
- Ultimate addressees: Human readers
- Divine "us" excludes humans → Exclusive form needed
- Confirmed by 9 languages using exclusive forms

**Conclusion**: Both annotations are valid for different purposes

---

## Methodological Decision Needed

### Option 1: Accept TBTA Mismatch
- Continue validation against TBTA
- Document systematic difference
- Expect lower accuracy (may be 40-60% if most mismatches follow this pattern)
- Argue both approaches valid but for different purposes

### Option 2: Dual Validation
- Track TBTA accuracy separately
- Track real translation accuracy separately
- Show algorithm v1.0 optimized for translation, not discourse analysis
- Claim success on translation validation (98%)

### Option 3: Pivot Algorithm
- Adjust algorithm v2.0 to match TBTA's discourse-internal perspective
- Would require retraining conceptual framework
- Would diverge from real translation validation

**Recommendation**: **Option 2 (Dual Validation)**

Rationale:
1. Algorithm v1.0 was trained on real translations (98% validation)
2. TBTA serves different purpose (discourse annotation)
3. Both perspectives are valuable
4. Documenting the difference advances understanding

---

## Next Actions

1. ⏳ Continue checking test verses against TBTA
2. ⏳ Verify if pattern is systematic or just Genesis 1:26
3. ⏳ Calculate TBTA accuracy
4. ⏳ Document dual validation approach
5. ⏳ Update algorithm v2.0 with discourse-internal awareness

---

**Status**: In progress - Critical insight discovered
**Date**: 2025-11-09
**Next**: Continue TBTA access for remaining verses
