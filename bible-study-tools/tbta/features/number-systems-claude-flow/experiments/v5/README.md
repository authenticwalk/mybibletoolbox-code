# V5: Translation Agreement with Trial-Marking Languages

**Status**: In progress
**Expected Accuracy**: 80-90% (hypothesis)
**Data Source**: eBible corpus (1079 languages)

## Hypothesis

Languages that grammatically MUST mark semantic number (dual, trial, paucal) will reveal TBTA's semantic annotations through their translation choices.

**Key Discovery from v4**: TBTA tracks **semantic participants** (who/what is being talked about), NOT Greek/Hebrew grammatical morphology.

## Trial-Marking Languages Available

From eBible corpus investigation:

### ✅ Confirmed in eBible
- **tpi** (Tok Pisin) - Has trial! "yumitripela" = "we three (including you)"
  - Full Bible available
  - 8 pronominal forms: sing/dual/trial/plural × inclusive/exclusive

### ❌ Not in eBible
- **smo** (Samoan) - Has trial (but not in eBible corpus)
- **fij** (Fijian) - Has trial (but not in eBible corpus)
- **slv** (Slovenian) - Has dual (but not in eBible corpus)
- **hsb** (Upper Sorbian) - Has dual (but not in eBible corpus)

## Approach

1. Extract Tok Pisin translations for all 236 train set verses
2. Analyze pronoun usage patterns:
   - Does Tok Pisin use "tripela" (trial) for TBTA Trial contexts?
   - Does Tok Pisin use "tupela" (dual) for TBTA Dual contexts?
   - What about Paucal contexts?

3. Check if translation agreement reveals semantic number

## Expected Challenges

- Tok Pisin trial might be compositional ("three-fellow") rather than pure grammatical category
- Only ONE trial-marking language available (need multiple for agreement)
- No dual-marking languages in eBible (Slovenian, Sorbian absent)

## Next Steps

1. Parse Tok Pisin corpus format
2. Extract translations for train set
3. Analyze pronoun patterns
4. Determine if sufficient signal for algorithm
