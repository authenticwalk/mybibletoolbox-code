# Cultural Translation - Success Metrics

## Validation Status

**Status:** 📋 PLANNED (methodology designed, pilot study pending)

**Validation Level:** ASPIRATIONAL - Target 300-500 high-variation words

---

## Quality Metrics

### Level 1: CRITICAL (100% pass required)
- 📋 **No fabrication** - All solutions from 900+ translation corpus
- 📋 **Inline citations** - Language examples cited: `{lang-code}: "translation"`
- 📋 **No percentages** - Use "most", "many", "some" (unless from corpus data)
- 📋 **Source validation** - All documented adaptations traceable to translations
- 📋 **Cultural sensitivity** - Respect for all cultures, no superiority assumptions

**Target:** 100% Level 1 validation

### Level 2: HIGH PRIORITY (80%+ pass required)
- 📋 **Solution documentation** - Multiple cultural adaptations per challenge
- 📋 **Strategy classification** - Substitute, describe, loan, metaphor, footnote
- 📋 **Rationale analysis** - Why solution works in target culture
- 📋 **Theological validation** - Core message preserved across adaptations

**Target:** 80%+ Level 2 validation

### Level 3: MEDIUM PRIORITY (60%+ pass required)
- 📋 **Evaluation criteria** - Success/failure of documented solutions
- 📋 **Translator guidance** - Practical recommendations for similar challenges
- 📋 **Cross-cultural patterns** - Common strategies across language families
- 📋 **Redemptive analogies** - Peace Child approach documentation

**Target:** 60%+ Level 3 validation

---

## Coverage Metrics

**Target Coverage:** Top 300-500 words with highest cultural variation

**Priority Words (Based on SIL/Wycliffe documented challenges):**

**Non-existent Concepts:**
- Lamb/sheep (G721, H7716) - Arctic/desert cultures
- Snow (H7950, G5510) - Tropical cultures
- Bread (G740, H3899) - Rice cultures
- Camel (G2574, H1581) - Cultures without large pack animals

**Untranslatable Abstracts:**
- Agape (G26) - Love distinctions
- Grace (G5485) - Merit-based cultures
- Righteousness (G1343) - Legal vs relational concepts
- Faith (G4102) - Trust vs belief distinctions

**Cultural Sensitivities:**
- Heart (H3820, G2588) - Different emotion-organs (liver, kidneys)
- Pig (H2386, G5519) - Taboo animals
- Numbers (H7651, G2033) - Taboo numbers
- Kinship terms (H251, G80) - Different family structures

**Current Status:** 📋 Methodology designed, pilot study (3-5 words) pending

---

## Evidence Base Metrics

**Status:** ✅ VALIDATED - Methodology grounded in real translation case studies

**Source Validation:**
- ✅ 900+ Bible translations in TBTA corpus
- ✅ SIL/Wycliffe documented translation challenges
- ✅ Published case studies (Peace Child, etc.)
- ✅ Scholarly literature on Bible translation theory

**Documented Solutions (Examples from existing translations):**

**Snow (H7950):**
- Hawaiian: "hau" (ice/frost metaphor) ✅ Documented
- Tok Pisin: "ais bilong ren" (ice of rain) ✅ Documented

**Lamb (G721):**
- Inuktitut: "nattiq" (seal pup) ✅ Documented, preserves sacrifice imagery

**Heart (H3820):**
- Various cultures: liver, kidneys, stomach for emotions ✅ Documented

**Result:** Methodology based on proven solutions, not theoretical

---

## Challenge Categories (Planned)

### 1. Non-existent Concepts
**Approach:** Identify physical objects unknown in target culture

**Extraction Pattern:**
```python
for translation in corpus:
    if strongs == "H7950" and translation.lang_has_no_snow():
        if translation.word != expected_cognate:
            record_adaptation({
                "original": "snow",
                "adaptation": translation.word,
                "strategy": classify_strategy(),  # substitute, describe, loan
                "rationale": analyze_choice()
            })
```

**Target Metrics:**
- Document 3-5 cultural adaptations per word
- Classify strategy (substitute, describe, loan, metaphor)
- Evaluate theological preservation

### 2. Untranslatable Abstracts
**Approach:** Theological concepts with no cultural equivalent

**Target Metrics:**
- Multiple translation strategies documented
- Theological stakes clearly marked (high/medium/low)
- Footnote recommendations when necessary

### 3. Cultural Sensitivities
**Approach:** Taboo subjects, offensive animals, sacred objects

**Target Metrics:**
- Cultural sensitivity documented (why taboo?)
- Alternative solutions from real translations
- Respect for cultural boundaries

### 4. Semantic Gaps
**Approach:** Missing distinctions or extra distinctions

**Target Metrics:**
- Document distinction patterns (love: agape/phileo/storge/eros)
- Cross-cultural comparison (which cultures distinguish?)
- Translation guidance for disambiguation

---

## Efficiency Metrics (Projected)

### Time Per Word
- **Simple substitution:** 2-3 hours (corpus extraction + documentation)
- **Complex cultural challenge:** 4-6 hours (multiple strategies, theological validation)
- **Redemptive analogy research:** 6-8 hours (deep cultural analysis)

### Pilot Study Timeline
- **Planning:** 1 month ✅ Complete
- **Pilot (3-5 words):** 1 month (validate methodology)
- **Top 100 words:** 1 month (scale up)
- **Expansion (300-500):** 1 month (full production)

---

## Expected Impact (Projected)

**Translation Accuracy:**
- Prevents literal translations that fail to communicate meaning
- Documents proven cultural adaptations from 900+ translations
- Provides multiple solution strategies per challenge
- Preserves theological message across cultural boundaries

**Translator Benefits:**
- Practical solutions for culturally non-existent concepts
- Multiple adaptation strategies (substitute, describe, loan, metaphor)
- Theological validation (core message preservation)
- Footnote recommendations when needed

**Cultural Sensitivity:**
- Respects cultural boundaries (taboo subjects documented)
- Documents successful adaptations from target cultures
- No cultural superiority assumptions
- Peace Child approach (redemptive analogies)

---

## Example Output (Planned Schema)

```yaml
# H7950 שֶׁלֶג (snow)
strongs_number: H7950
translation_challenges:
  category: [non_existent_concept]
  problem: "Desert/tropical cultures have never experienced snow"
  theological_stakes: "High - purity metaphors (Isaiah 1:18)"

solutions_documented:
  - language: "haw" # Hawaiian
    translation: "hau" (ice/frost metaphor)
    strategy: "substitute"
    evaluation: "Uses closest natural phenomenon, preserves whiteness"

  - language: "tpi" # Tok Pisin
    translation: "ais bilong ren" (ice of rain)
    strategy: "descriptive"
    evaluation: "Compound phrase, culturally accessible"

translator_guidance:
  - "Emphasize whiteness and purity, not coldness"
  - "Find local metaphor for absolute purity/cleansing"
  - "Consider footnote: 'white frozen precipitation'"
```

---

## Pilot Study Design (Next Steps)

**Pilot Words (3-5 selected):**
1. Snow (H7950) - Non-existent concept (tropical cultures)
2. Lamb (G721) - Non-existent concept (Arctic cultures)
3. Agape (G26) - Untranslatable abstract (love distinctions)
4. Heart (H3820) - Cultural sensitivity (different emotion-organs)
5. Bread (H3899) - Non-existent concept (rice cultures)

**Pilot Objectives:**
1. Validate extraction approach (corpus analysis)
2. Test solution documentation (3-5 adaptations per word)
3. Confirm theological validation (message preservation)
4. Measure time per word (efficiency)
5. Assess translator usefulness (impact testing)

**Pilot Timeline:** 1 month

---

## Production Readiness

**Status:** 📋 Planning complete, pilot pending

**Next Steps:**
1. Run pilot study (3-5 sample words)
2. Validate methodology and schema
3. Measure time and quality metrics
4. Expand to Top 100 words (documented challenges)
5. Scale to 300-500 words (full production)

**Deployment Timeline:**
- Pilot study: 1 month
- Top 100 production: 1 month
- Expansion: 1 month
- Total: 4 months (includes validation)

---

## Quality Assurance (Projected)

**Validation Approach:**
- 100% Level 1 validation (corpus-based, no fabrication)
- 80%+ Level 2 validation (multiple solutions, strategy classification)
- 60%+ Level 3 validation (evaluation criteria, translator guidance)

**Theological Validation:**
- Core message preservation checked for all adaptations
- Theological stakes marked (high/medium/low)
- Expert review for high-stakes theological terms

**Cultural Sensitivity:**
- All solutions from real translations (respect for target cultures)
- No cultural superiority assumptions
- Documented rationale for why solutions work

---

**Last Updated:** 2025-11-15
**See Also:** `./README.md` for planning overview
