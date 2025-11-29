# V5 Conclusion: Translation Agreement Approach

**Status**: Abandoned
**Reason**: Insufficient trial-marking language coverage in eBible

## Investigation Summary

### Languages Checked

**✅ In eBible (1079 languages total)**:
- **tpi** (Tok Pisin) - Has trial grammatically, but limited pronoun usage in Bible

**❌ Not in eBible**:
- **smo** (Samoan) - Has trial
- **fij** (Fijian) - Has trial
- **slv** (Slovenian) - Has dual
- **hsb** (Upper Sorbian) - Has dual

### Tok Pisin Analysis

**Trial pronouns theoretically available**:
- yumitripela = we three (inclusive)
- mitripela = we three (exclusive)
- yutripela = you three

**Actual usage in Tok Pisin Bible**:
- **Dual pronouns**: Frequent (mitupela, yutupela appear ~15+ times in Genesis alone)
- **Trial pronouns**: Rare (only 2 instances found: JOB 13:2, 13:4 "yutripela")
- **Trinity context (GEN 1:26)**: Uses "yumi" (ambiguous), NOT "yumitripela" (trial)

**Problem**: Even if pronouns appear, need MULTIPLE languages for agreement

## Why V5 Fails

1. **Only 1 trial language** in eBible (Tok Pisin) - can't establish agreement
2. **No dual languages** in eBible (Slovenian, Sorbian missing)
3. **Translator inconsistency** - GEN 1:26 uses "yumi" (ambiguous) not "yumitripela" (trial)
4. **Optional marking** - Trial may be grammatically possible but pragmatically rare

## Lessons from V5

1. **eBible != World's trial/dual languages** - Most Oceanic/Slavic languages absent
2. **Translation != Grammar** - Translators may not use available distinctions
3. **Need multiple languages** - Single language insufficient for agreement threshold
4. **Source morphology remains best bet** - Hebrew/Greek when they have it

## Recommendation

**ABANDON v5**. Return to v2 (PROMPT2) as best achievable with English-only data:
- 42.1% overall accuracy
- 89.5% high-confidence (Tier 1)
- Deploy Tier 1 only until morphology integration available

## Path Forward

To exceed 42.1% ceiling, need ONE of:
1. **Hebrew/Greek morphology** (but v4 showed this tracks grammar, not TBTA semantics)
2. **TBTA annotation guidelines** (understand their semantic criteria)
3. **Multiple trial/dual languages** (Samoan, Fijian, Slovenian not in eBible)
4. **Statistical ML** (accept 70-80% ceiling)

**Next action**: Document v5 as abandoned, finalize experiments folder
