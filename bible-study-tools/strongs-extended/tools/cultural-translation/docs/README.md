# Cultural Translation Challenges - Documentation

## Status
🔴 Stage 1 (Partial) - Test set and approach design needed before experimentation

**STAGES.md v2.0 Compliance:** 12.5% (1 of 8 stages)
**See:** AUDIT-REPORT.md and ACTION-PLAN.md in parent directory

## Overview
Document proven solutions for translating culturally non-existent concepts and taboo subjects using 900+ Bible translations.

**Data Source:** Same 900+ translation corpus as TBTA hints

**Timeline:** 4 months total
- Planning: 1 month ✅
- Pilot: 1 month
- Top 100: 1 month
- Expansion: 1 month

## Challenge Categories
1. **Non-existent Concepts** - Physical objects unknown in target culture
2. **Untranslatable Abstracts** - Theological concepts with no cultural equivalent
3. **Cultural Sensitivities** - Taboo subjects, offensive animals, sacred objects
4. **Semantic Gaps** - Missing distinctions or extra distinctions

## Extraction Approach
```python
# Identify cultural adaptations
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

## Priority Words
- Lamb/sheep (G721, H7716) - Arctic/desert cultures
- Snow (H7950, G5510) - Tropical cultures
- Bread (G740, H3899) - Rice cultures
- Agape (G26) - Love distinctions
- Grace (G5485) - Merit-based cultures
- Heart (H3820, G2588) - Different emotion-organs

## Example Solutions
**H7950 שֶׁלֶג (snow):**
- Hawaiian: "hau" (ice/frost metaphor)
- Tok Pisin: "ais bilong ren" (ice of rain)

**G721 ἀρνίον (lamb):**
- Inuktitut: "nattiq" (seal pup), preserves sacrifice imagery

**H3820 לֵב (heart):**
- Cultures using liver/kidneys for emotions

## Output Format
`.data/strongs/{num}/{num}-cultural.yaml`

## Complete Documentation
**See:** `/plan/strongs-cultural-translation/` for detailed planning, methodology, and pilot study design.

This documentation will be migrated here as the tool progresses through implementation phases.
