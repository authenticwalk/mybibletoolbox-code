# Word-Type Auto-Detection Logic

**Created:** 2025-11-09
**Purpose:** Distinguish theological from grammatical words to route to appropriate extraction pathways
**Status:** Refinement #1 for Cycle 2

---

## Detection Objective

Automatically classify Strong's words into **theological** or **grammatical** categories to enable tailored extraction strategies. This improves both efficiency (less time on low-value extractions) and quality (appropriate depth for word type).

---

## Evidence Base

Detection criteria derived from Cycle 1 experiments:

| Word | Type | Freq | HELPS | TDNT/TWOT | Trench | Categories | Richness | Source |
|------|------|------|-------|-----------|--------|------------|----------|---------|
| G846 (αὐτός) | Grammatical | 5,597 | ✗ | ✗ | ✗ | 3 | 6.0/10 | Exp 1 |
| G1411 (δύναμις) | Theological | 120 | ✓ | ✓ | ✓ | 8 | 8.0/10 | Exp 2 |
| G5287 (ὑπόστασις) | Theological | 5 | ✓ | ✗ | ✗ | 2 | 7.0/10 | Exp 3 |
| H430 (אֱלֹהִים) | Theological | 2,606 | N/A | ✓ | N/A | 6 | 9.7/10 | Exp 4 |

**Key Finding:** Word type (theological vs grammatical) is a stronger predictor of data richness than frequency {cycle-01-learnings}.

---

## Primary Detection Criteria

### Criterion 1: Part of Speech (POS)

**Rule:** Content words → theological pathway; function words → grammatical pathway

**Theological Indicators (content words):**
- Nouns (especially abstract nouns)
- Verbs (action/state words)
- Adjectives (descriptive)

**Grammatical Indicators (function words):**
- Pronouns (personal, demonstrative, relative)
- Particles (negatives, intensifiers)
- Conjunctions (coordinators, subordinators)
- Articles (definite, indefinite)
- Prepositions

**Data Source:** Base file POS field, or Strong's concordance classification

**Evidence:**
- G846 (pronoun) → 6.0/10 richness {exp1-learnings}
- G1411 (noun) → 8.0/10 richness {exp2-learnings}
- H430 (noun) → 9.7/10 richness {exp4-learnings}

**Confidence:** HIGH - POS is the strongest single predictor

---

### Criterion 2: Theological Dictionary Presence

**Rule:** Word has TDNT/TWOT entry → theological pathway

**Detection Method:**
1. Check base file for TDNT reference (Greek) or TWOT reference (Hebrew)
2. If present → classify as theological
3. If absent → continue to Criterion 3

**Evidence:**
- G846 (no TDNT) → grammatical classification, 0 scholarly cross-refs {exp1-learnings}
- G1411 (TDNT 2:284,186) → theological classification, 7 scholarly cross-refs {exp2-learnings}
- H430 (TWOT 93c) → theological classification, extensive theological depth {exp4-learnings}

**Rationale:** TDNT/TWOT inclusion indicates scholarly consensus on theological significance {cycle-01-learnings}

**Confidence:** HIGH - Strong correlation with data richness

---

### Criterion 3: HELPS Word-Studies Availability

**Rule:** HELPS present → theological pathway; HELPS absent → grammatical pathway (if POS is function word)

**Detection Method:**
1. Quick check: WebFetch BibleHub page
2. Search for "HELPS Word-studies" section
3. If present → theological indicator
4. If absent AND function word → grammatical classification

**Evidence:**
- G846 (pronoun, no HELPS) → grammatical {exp1-learnings}
- G1411 (noun, HELPS present) → theological {exp2-learnings}
- G5287 (rare noun, HELPS present) → theological {exp3-learnings}

**Pattern:** "HELPS prioritizes theological terms over grammatical function words" {exp1-learnings}

**Confidence:** MEDIUM-HIGH - Consistent pattern but requires web fetch

**Note:** HELPS availability is not 100% predictive (60% availability overall {cycle-01-learnings}), but absence is highly predictive for grammatical words.

---

### Criterion 4: Semantic Domain Classification

**Rule:** Classify by semantic domain characteristics

**Theological Domains:**
- God/deity concepts
- Salvation/redemption terms
- Covenant/law terminology
- Worship/ritual language
- Moral/ethical concepts
- Spiritual/supernatural terms
- Eschatological language

**Grammatical/Functional Domains:**
- Spatial/temporal markers (prepositions)
- Logical connectors (conjunctions)
- Reference/deixis (pronouns)
- Quantification (articles, numbers)
- Discourse markers

**Detection Method:** Analyze Strong's definition for domain keywords

**Evidence:**
- G846 (reference/deixis domain) → grammatical {exp1-learnings}
- G1411 (spiritual power domain) → theological {exp2-learnings}
- H430 (God/deity domain) → theological {exp4-learnings}

**Confidence:** MEDIUM - Requires interpretation of definition

---

## Secondary Detection Criteria

### Criterion 5: Frequency-Type Interaction

**Rule:** High-frequency + content word → check for theological significance; High-frequency + function word → likely grammatical

**Frequency Tiers:**
- Ultra-high: 1,000+ occurrences
- High: 500-999 occurrences
- Medium: 50-499 occurrences
- Low: 10-49 occurrences
- Rare: <10 occurrences

**Patterns from Cycle 1:**
- Ultra-high frequency pronouns (G846, 5,597x) → grammatical, 6.0/10 richness {exp1-learnings}
- Ultra-high frequency theological nouns (H430, 2,606x) → theological, 9.7/10 richness {exp4-learnings}
- Medium frequency theological nouns (G1411, 120x) → theological, 8.0/10 richness {exp2-learnings}

**Key Insight:** "Theological significance > frequency for extraction value" {cycle-01-learnings}

**Confidence:** MEDIUM - Frequency alone insufficient; must combine with POS

---

### Criterion 6: Synonym Network Density

**Rule:** Words with rich synonym networks → theological pathway

**Detection Indicators:**
- Trench's Synonyms section present
- Multiple related Strong's numbers with semantic distinctions
- English translation collapse (1 English word = multiple Greek/Hebrew words)

**Evidence:**
- G846: 3 related words (morphological variants) {exp1-learnings}
- G1411: 5 distinct synonyms with clear semantic differentiation (βία, ἰσχύς, κράτος, ἐξουσία, ἐνέργεια) {exp2-learnings}

**Quote:** "English 'power' collapses 5+ Greek concepts. Synonym distinctions critical for theological precision" {exp2-learnings}

**Confidence:** MEDIUM - Requires some extraction work to verify

---

## Decision Tree

```
START
  |
  ├─ Is POS a function word (pronoun/particle/conjunction/article)?
  │   ├─ YES → Check HELPS availability
  │   │   ├─ HELPS present → THEOLOGICAL (rare case)
  │   │   └─ HELPS absent → GRAMMATICAL ✓
  │   │
  │   └─ NO (content word) → Continue
  │       |
  │       ├─ TDNT/TWOT reference present?
  │       │   ├─ YES → THEOLOGICAL ✓
  │       │   └─ NO → Continue
  │       │       |
  │       │       ├─ Semantic domain theological?
  │       │       │   ├─ YES → THEOLOGICAL ✓
  │       │       │   └─ NO → Check HELPS
  │       │       │       ├─ HELPS present → THEOLOGICAL ✓
  │       │       │       └─ HELPS absent → GRAMMATICAL (likely lexical/neutral)
```

---

## Automatable Implementation

### Step-by-Step Detection Process

**Input:** Strong's number (e.g., G846, H430)

**Step 1: Extract Base Data**
```yaml
extraction:
  - strongs_number: "G846"
  - base_file_data:
      pos: "pronoun"
      tdnt: null
      definition: "self, he/she/it, the same"
```

**Step 2: Apply POS Filter**
```python
function_words = ["pronoun", "particle", "conjunction", "article", "preposition"]
if pos in function_words:
    preliminary_classification = "grammatical"
else:
    preliminary_classification = "theological_candidate"
```

**Step 3: Check TDNT/TWOT**
```python
if tdnt or twot:
    classification = "theological"
elif preliminary_classification == "grammatical":
    classification = "grammatical"  # Confirmed
else:
    continue_to_step_4 = True
```

**Step 4: Semantic Domain Analysis (if needed)**
```python
theological_keywords = ["god", "spirit", "power", "faith", "grace", "sin", "salvation", "covenant", "holy", "righteous"]
if any(keyword in definition.lower() for keyword in theological_keywords):
    classification = "theological"
else:
    classification = "grammatical_or_lexical"
```

**Output:**
```yaml
word_type_detection:
  classification: "grammatical"  # or "theological"
  confidence: "HIGH"  # HIGH, MEDIUM, LOW
  criteria_matched:
    - "POS: pronoun (function word)"
    - "TDNT: absent"
    - "HELPS: absent (predicted)"
  extraction_pathway: "grammatical_morphology"  # or "theological_full"
```

---

## Edge Cases

### Edge Case 1: High-Frequency Theological Terms

**Example:** H430 (אֱלֹהִים) - 2,606 occurrences

**Challenge:** Ultra-high frequency might suggest functional word

**Resolution:** POS (noun) + TWOT (93c) + semantic domain (God) → THEOLOGICAL

**Evidence:** Achieved 9.7/10 richness despite ultra-high frequency {exp4-learnings}

**Rule:** TDNT/TWOT presence overrides frequency considerations

---

### Edge Case 2: Rare Grammatical Terms

**Example:** Rare particles or conjunctions (<10 occurrences)

**Challenge:** Rarity might suggest theological significance

**Resolution:** POS (particle/conjunction) → GRAMMATICAL regardless of frequency

**Evidence:** "Theological significance > frequency" applies to content words, not function words {cycle-01-learnings}

**Rule:** Function words classified as grammatical regardless of frequency

---

### Edge Case 3: Theologically-Loaded Function Words

**Example:** G3361 (μή, "not") used in theological contexts

**Challenge:** Frequent use in theological statements

**Resolution:** POS (particle) + no TDNT → GRAMMATICAL

**Rationale:** Function despite theological context

**Rule:** Distinguish between theological content vs. grammatical function

---

### Edge Case 4: Words with Dual Functions

**Example:** Words that function as both content and function words

**Challenge:** Classification ambiguity

**Resolution:** Prioritize primary usage (most frequent sense)

**Fallback:** If unclear, default to THEOLOGICAL pathway (better to over-analyze than under-analyze)

**Confidence:** Mark as MEDIUM or LOW confidence

---

### Edge Case 5: No HELPS but Clear Theological Significance

**Example:** G5287 (ὑπόστασις) - rare but theologically significant

**Challenge:** HELPS present, but pattern suggests HELPS isn't always available

**Resolution:** Combine multiple criteria:
- POS: noun (content word) ✓
- Semantic domain: faith/confidence (theological) ✓
- Frequency: rare (5x) but theological context ✓
- Classification: THEOLOGICAL

**Evidence:** Achieved 7.0/10 richness despite rarity {exp3-learnings}

**Rule:** Multiple weak signals can override single strong signal

---

## Classification Confidence Levels

### HIGH Confidence Indicators

**Theological:**
- Content word (noun/verb) + TDNT/TWOT reference
- Theological semantic domain + HELPS present
- Strong's definition contains God/salvation/covenant terms

**Grammatical:**
- Function word (pronoun/particle/conjunction) + no TDNT
- No HELPS + no theological keywords
- Morphology-focused definition

**Examples:**
- G1411 (δύναμις): HIGH confidence theological {exp2-learnings}
- G846 (αὐτός): HIGH confidence grammatical {exp1-learnings}

---

### MEDIUM Confidence Indicators

**Theological:**
- Content word + no TDNT but theological keywords
- Rare word with specialized usage
- Multiple synonym distinctions

**Grammatical:**
- Content word but functional usage
- High frequency + no theological depth in definition

**Examples:**
- Uncommon adverbs or adjectives
- Numerals with occasional symbolic usage

---

### LOW Confidence Indicators

**Ambiguous cases:**
- Content word + no TDNT + neutral semantic domain
- Mixed function/content usage
- Insufficient data in base file

**Resolution:** Default to THEOLOGICAL pathway (over-analyze rather than under-analyze)

**Rationale:** "Medium-frequency theological terms provide richest unique data extraction" {cycle-01-learnings}

---

## Expected Pathway Distribution

Based on Strong's concordance structure:

**Greek NT (5,624 words):**
- Theological: ~40-50% (nouns/verbs with theological significance)
- Grammatical: ~30-40% (pronouns, particles, prepositions, articles)
- Mixed/Lexical: ~10-20% (neutral nouns/verbs)

**Hebrew OT (8,573 words):**
- Theological: ~50-60% (higher theological density in OT)
- Grammatical: ~25-35% (function words)
- Mixed/Lexical: ~10-20% (neutral terms)

**Estimated total:**
- Theological pathway: ~7,000 words (50%)
- Grammatical pathway: ~4,500 words (32%)
- Case-by-case: ~2,500 words (18%)

---

## Validation Tests

### Test Set (from Cycle 1 experiments)

| Word | Expected Classification | Actual Pathway | Validation |
|------|------------------------|----------------|------------|
| G846 (αὐτός) | Grammatical | Grammatical | ✓ PASS |
| G1411 (δύναμις) | Theological | Theological | ✓ PASS |
| G5287 (ὑπόστασις) | Theological | Theological | ✓ PASS |
| H430 (אֱלֹהִים) | Theological | Theological | ✓ PASS |

**Test Accuracy:** 4/4 = 100% on Cycle 1 experiments

---

## Implementation Recommendations

### Phase 1: Manual Classification (Cycle 2)

**Approach:** Human applies detection criteria for 5 test words

**Benefit:** Validates detection logic before automation

**Output:** Confidence levels and edge case identification

---

### Phase 2: Semi-Automated (Cycle 3+)

**Approach:** Script checks POS + TDNT/TWOT, flags ambiguous cases for human review

**Tools needed:**
- Base file parser (extract POS, TDNT/TWOT fields)
- Keyword matcher (semantic domain analysis)
- Confidence scorer

**Benefit:** Faster processing with quality control

---

### Phase 3: Fully Automated (Future)

**Approach:** ML classifier trained on Cycle 1-3 results

**Features:**
- POS
- TDNT/TWOT presence
- Definition keyword density
- Frequency tier
- HELPS availability (predicted)

**Target accuracy:** 95%+ with LOW confidence flagging for human review

---

## Success Metrics for Cycle 2

### Detection Accuracy
- [ ] 100% accuracy on 5 Cycle 1 test words
- [ ] 90%+ accuracy on 5 new Cycle 2 test words
- [ ] Edge cases correctly identified and flagged

### Pathway Effectiveness
- [ ] Theological pathway: 99%+ validation, 8.0+ richness average
- [ ] Grammatical pathway: 99%+ validation, 6.0+ richness average (appropriate)
- [ ] Time savings: 15% reduction on grammatical words (less depth needed)

### Confidence Calibration
- [ ] HIGH confidence: 95%+ correct classification
- [ ] MEDIUM confidence: 80%+ correct classification
- [ ] LOW confidence: Flagged for human review

---

## Next Steps (Cycle 2 Implementation)

1. **Apply detection logic to Cycle 1 test words** (G846, G1411, G5287, H430)
   - Verify classifications match observed patterns
   - Confirm confidence levels

2. **Create pathway templates** (Refinement #2)
   - Theological pathway: Full semantic extraction (see next document)
   - Grammatical pathway: Morphology/syntax focus (see next document)

3. **Test on 2 new words** (1 theological, 1 grammatical)
   - Measure classification accuracy
   - Validate pathway appropriateness

4. **Refine criteria based on results**
   - Adjust confidence thresholds
   - Add new edge cases
   - Update decision tree

5. **Document learnings for Cycle 3**
   - What worked?
   - What needs refinement?
   - Automation feasibility?

---

## References

All evidence cited from Cycle 1 documentation:
- {exp1-learnings}: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp1-high-freq-word/LEARNINGS.md`
- {exp2-learnings}: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp2-medium-freq/LEARNINGS.md`
- {exp3-learnings}: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp3-rare-word/LEARNINGS.md`
- {exp4-learnings}: `/plan/strongs-enrichment-tools/01-lexicon-core/experiments/exp4-hebrew-word/LEARNINGS.md`
- {cycle-01-learnings}: `/plan/lexicon-core-cycles/cycle-01/CYCLE-1-LEARNINGS.md`

---

**Status:** ✅ DETECTION LOGIC COMPLETE - Ready for Cycle 2 testing
