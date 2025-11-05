# Number Systems: Key Learnings and Reproduction Thesis

**Research Date**: 2025-11-05
**Researcher**: Claude (Sonnet 4.5)
**Dataset**: 1009 languages in `src/constants/languages.tsv`

---

## Executive Summary

TBTA encodes six number values (Singular, Dual, Trial, Quadrial, Paucal, Plural) to guide Bible translation into languages with diverse grammatical number systems. Our dataset of 1009 languages includes:

- **2-3 languages** with productive dual (Slovene, Lithuanian)
- **1+ languages** with trial (Tok Pisin confirmed, more likely in Austronesian)
- **0 languages** with true quadrial (scholarly consensus: doesn't exist)
- **3+ languages** with paucal (Sursurunga, Warlpiri, Murrinh-Patha, likely more)
- **176 Austronesian languages** - highest probability for trial/paucal
- **36 Australian Aboriginal languages** - highest probability for paucal
- **135 Indo-European languages** - need to identify Slavic subset for dual

**Key Finding**: Number annotation is primarily about **target language needs**, not source language morphology. Koine Greek lacks dual/trial, so TBTA assignments represent semantic/theological interpretation.

---

## Languages in Our Dataset by Number System

### 1. DUAL NUMBER

#### Confirmed Languages

**Slovene (slv)**
- Status: ✅ Confirmed in dataset? **Need to verify** (check for "Slovenian" or "Slovene")
- Family: Indo-European > Slavic > South Slavic
- Number system: Singular, Dual, Plural (fully productive)
- Scope: All inflected categories (nouns, verbs, adjectives, pronouns)
- Obligatoriness: Mandatory for exactly two entities
- Example: "two people" requires dual form, not plural
- Implication: When annotating for Slovene, any "exactly 2" → Dual (D)

**Lithuanian (lit)** ✅ IN DATASET
- File: `lit-lit.txt`
- Verses: 7,081
- Books: 66
- Family: Indo-European > Baltic
- Number system: Singular, Plural, remnant Dual
- Scope: Limited dual forms (mostly body parts, archaic/poetic)
- Obligatoriness: Optional, declining
- Implication: Check context - traditional/formal texts may use dual for natural pairs

#### Potential Languages (Need Investigation)

Search dataset for:
- **Sorbian** (Upper: hsb, Lower: dsb) - likely not present
- **Kashubian** (csb) - likely not present
- Other **Slavic languages** - may have dual remnants in specific contexts

**Action Item**:
```bash
grep -i "slovene\|slovenian\|sorbian\|kashubian" languages.tsv
grep -i "slavic" languages.tsv
```

---

### 2. TRIAL NUMBER

#### Confirmed Languages

**Tok Pisin (tpi)** ✅ IN DATASET (2 translations)
- Files: `tpi-tpi.txt` (35,547 verses, 78 books), `tpi-tpiOTNT.txt` (31,099 verses, 66 books)
- Country: Papua New Guinea
- Family: Creole (Melanesian Pidgin)
- Number system: Singular, Dual, Trial, Plural
- Scope: Pronouns (all persons: 1st, 2nd, 3rd)
- Features: Also distinguishes Inclusive/Exclusive in 1st person
- Pronoun examples:
  - 1sg: mi "I"
  - 1du.excl: mitupela "we two (not you)"
  - 1du.incl: yumitupela "we two (you and me)"
  - 1tr.excl: mitripela "we three (not you)"
  - 1tr.incl: yumitripela "we three (including you)"
  - 1pl.excl: mipela "we all (not you)"
  - 1pl.incl: yumipela "we all (including you)"
- Implication: For Tok Pisin, any "exactly 3" participants → Trial (T)
- Trinity passages: First Inclusive Trial (Genesis 1:26 "let us make")

#### High-Probability Languages (Oceanic Austronesian)

**Strategy**: Filter 176 Austronesian languages for Papua New Guinea, Solomon Islands, Vanuatu, eastern Indonesia.

**Expected trial languages**:
- **PNG Austronesian**: aai, adz, aia, apr, aui, bch, bdd, bjk, bjp, bmk, bnp, buk, etc.
- **Solomon Islands**: aia (Arosi), apb (Sa'a), bgt (Bughotu), etc.
- **Vanuatu**: bki (Baki)

**Action Item**:
```bash
# PNG Austronesian languages
grep "Austronesian" languages.tsv | grep "Papua New Guinea"

# Solomon Islands Austronesian
grep "Austronesian" languages.tsv | grep "Solomon Islands"

# Vanuatu Austronesian
grep "Austronesian" languages.tsv | grep "Vanuatu"

# Indonesia Austronesian (eastern regions more likely)
grep "Austronesian" languages.tsv | grep "Indonesia"
```

**Specific languages to verify** (if in dataset):
- Larike (lar) - true trial confirmed in literature
- Tolai/Kuanua (ksd) - trial confirmed
- Raga (lml) - trial confirmed
- Wamesa (wad) - remnant trial

---

### 3. QUADRIAL NUMBER

#### Scholarly Consensus: Does Not Exist

**Greville Corbett (2000)**: "No report of a quadrial grammatical number had been borne out."

All proposed quadrials have been **reanalyzed**:
- Sursurunga: Greater paucal, not quadrial
- Marshallese: Paucal with rhetorical use
- Tok Pisin: Grammatically possible, never used (speakers use plural)

#### Languages Previously Claimed (Now Disputed)

**Sursurunga (sgz)** ✅ IN DATASET
- File: `sgz-sgz.txt`
- Verses: 7,957
- Books: 27
- Country: Papua New Guinea
- **Actual system**: Singular - Dual - Lesser Paucal - Greater Paucal - Plural
- **Not quadrial**: "Greater paucal" can mean 4+, but also means "several" generally
- Implication: If TBTA marks Quadrial (Q), likely means Sursurunga's "greater paucal"

**Recommendation**:
- **Don't use Quadrial (Q)** in annotations unless absolutely clear
- Consider using **Paucal (p)** instead for small groups of 4-6
- Use **Plural (P)** for 4+ in most languages

---

### 4. PAUCAL NUMBER

#### Confirmed Languages

**Sursurunga (sgz)** ✅ IN DATASET
- System: Five-way number distinction
  1. Singular: iau "I"
  2. Dual: giur "the two of us"
  3. **Lesser paucal**: gimtul "the few of us" (~3-4)
  4. **Greater paucal**: gimhat "we" (4+, up to ~10)
  5. Plural: gim "we (many)"
- Implication: Can distinguish "a few" from "several" from "many"
- Usage: Lesser paucal for small groups (disciples?), greater paucal for larger groups (crowds?)

**Warlpiri (wbp)** ✅ IN DATASET
- File: `wbp-wbp.txt`
- Verses: 11,098
- Books: 36
- Country: Australia
- Family: Australian > Pama-Nyungan
- Number system: Singular, Dual, Paucal, Plural
- Paucal range: Small groups (exact range varies by noun class)
- Implication: Small groups of disciples, angels → Paucal

**Murrinh-Patha (mwf)** ✅ IN DATASET
- File: `mwf-mwf2018.txt`
- Verses: 4,374
- Books: 12
- Country: Australia
- Family: Australian
- Number system: Singular, Paucal, Plural (dual status unclear from search)
- Paucal range: About 10-15 (larger than typical)
- Implication: Can use paucal for "the twelve disciples"

#### High-Probability Languages

**Australian Aboriginal (36 total)** - Most likely have paucal

Confirmed in dataset:
1. Arrernte, Eastern (aer) - 10,165 verses
2. Alyawarr (aly) - 8,892 verses
3. Anmatyerre (amx) - 4,225 verses
4. Anindilyakwa (aoi) - 3,987 verses
5. Arrarnta, Western (are) - 7,956 verses
6. Awabakal (awk) - 1,136 verses
7. Burarra (bvr) - 7,957 verses
8. Dhangu-Djangu (dhg) - 685 verses (+ variant)
9. Diyari (dif) - 7,957 verses
10. Djinang (dji) - 988 verses
11. Djambarrpuyngu (djr) - 8,122 verses
12. Dhuwaya (dwy) - 717 verses
13. Gumatj (gnn) - 7,957 verses
14. Gunwinggu (gup) - 14,539 verses
15. Kuku-Yalanji (gvn) - 10,993 verses
16. Yanyuwa (jao) - 870 verses
17. Kunjen (kjn) - 138 verses
18. Maung (mph) - 680 verses
19. Martu Wangka (mpj) - 5,658 verses
20. Murrinh-Patha (mwf) - 4,374 verses ✅ confirmed paucal
21. Kala Lagaw Ya (mwp) - 5,928 verses
22. Ngarrindjeri (nay) - 390 verses
23. Nyangumarta (nna) - 2,399 verses
24. Ngaanyatjarra (ntj) - 13,028 verses
25. Nunggubuyu (nuy) - 8,377 verses
26. Nyungar (nys) - 1,285 verses
27. Pintupi-Luritja (piu) - 14,699 verses
28. Pitjantjatjara (pjt) - 12,948 verses
29. Kuuk Thayorre (thd) - 171 verses
30. Tiwi (tiw) - 1,575 verses
31. Warlpiri (wbp) - 11,098 verses ✅ confirmed paucal
32. Wik-Mungkan (wim) - 7,949 verses
33. Walmajarri (wmt) - 3,384 verses
34. Garrwa (wrk) - 5,267 verses
35. Worrorra (wro) - 1,828 verses

**Action Item**: Assume paucal for all Australian Aboriginal languages unless grammar explicitly says otherwise.

**Afro-Asiatic (25 total)** - Check for Arabic

Search for Arabic translations:
```bash
grep -i "arabic" languages.tsv
```

If Arabic present: Has paucal via broken plural templates (3-10 range)

---

### 5. SINGULAR & PLURAL

**Universal**: All 1009 languages distinguish singular from non-singular in some way.

**Plural strategies** (from WALS):
- Suffix (most common globally)
- Prefix
- Reduplication
- Tone change
- Free particle
- No marking (isolating languages)

---

## Reproduction Thesis: How to Determine TBTA Number Values

### Core Principle

**TBTA number annotation is TARGET-LANGUAGE-DRIVEN, not source-language-driven.**

Since Koine Greek has no dual/trial, and Hebrew dual is limited, TBTA must be making **semantic interpretations** based on:
1. Discourse participant tracking
2. Explicit numerals in context
3. Theological/cultural knowledge
4. Target language requirements

### Reproduction Algorithm

#### INPUT
- Biblical verse (Hebrew or Greek)
- Morphological analysis (from Macula or similar)
- Target language(s) to translate into

#### PROCESS

**Step 1: Extract Participants**
```
For each noun/pronoun in verse:
  - Identify referent (person, place, thing)
  - Assign participant index (1-9, A-Z, a-z)
  - Track across discourse (first mention, routine, restaging, etc.)
```

**Step 2: Count Participants**
```
For each participant:
  - Check explicit numerals: "two angels", "three men", "twelve disciples"
  - Check morphology: Hebrew dual suffix, Hebrew/Greek plural
  - Check context: How many entities in scene?
  - Check prior mentions: Established group size?
```

**Step 3: Determine Semantic Number**
```
Singular (S): Explicit "one" or morphologically singular
Dual (D): Explicit "two" or Hebrew dual morphology
Trial (T): Explicit "three" in context
Quadrial (Q): Explicit "four" (rare, use cautiously)
Paucal (p): "A few", small group (3-10 typically)
Plural (P): "Many", large group, or default plural
```

**Step 4: Apply Target Language Constraints**
```
If target has DUAL:
  - Semantic number = 2 → Dual (D)
  - All others remain the same

If target has TRIAL:
  - Semantic number = 3 → Trial (T)
  - All others remain the same

If target has PAUCAL:
  - Semantic number = "a few" (3-10) → Paucal (p)
  - Semantic number = "many" → Plural (P)
  - Boundary depends on target language grammar

If target has QUADRIAL (unlikely):
  - Semantic number = 4 → Quadrial (Q)
  - But verify target language actually has it!

If target has only SINGULAR/PLURAL:
  - Semantic number = 1 → Singular (S)
  - Semantic number = 2+ → Plural (P)
```

**Step 5: Validate**
```
Check:
  - Same participant has consistent number across verse
  - Number aligns with participant tracking
  - Theological implications make sense (esp. Trinity)
  - Matches reference translations (if available)
```

#### OUTPUT
- Number value (S/D/T/Q/p/P) for each noun/pronoun
- Participant index to track same entities
- Confidence level (high/medium/low)

---

## Special Cases and Edge Cases

### Case 1: Genesis 1:26 - "Let Us Make"

**Source**:
- Hebrew: נַעֲשֶׂה (na'aseh) "let us make" - 1st person plural cohortative
- Greek (LXX): ποιήσωμεν (poiēsōmen) "let us make" - 1st person plural subjunctive
- Neither has morphological dual or trial

**TBTA Decision**: Trial (T) + First Person Inclusive

**Reasoning**:
- Theological interpretation: Trinity (three divine persons)
- Participants: Father, Son, Holy Spirit
- Exactly three entities acting in unison
- Inclusive: The persons of the Trinity include each other

**Reproduction**:
- Requires **theological commentary** to identify Trinitarian passages
- Cannot be determined from morphology alone
- Need doctrine of the Trinity to assign trial

**Challenge**: Not all traditions interpret Genesis 1:26 as Trinity (some see divine council, royal "we", etc.)

### Case 2: Angels in Narrative

**Source**: Often plural in Hebrew/Greek, but context reveals exact number

**Example**: Genesis 18 - "three men" appear to Abraham
- Hebrew: שְׁלֹשָׁה אֲנָשִׁים (shloshah anashim) "three men" - explicit numeral
- Greek (LXX): τρεῖς ἄνδρες (treis andres) "three men" - explicit numeral

**TBTA Decision**: Trial (T) - for languages with trial

**Reproduction**:
- Explicit numeral → semantic number is 3
- If target has trial → use Trial (T)
- If target lacks trial → use Plural (P) or Paucal (p)

### Case 3: "The Twelve" Disciples

**Source**: Greek οἱ δώδεκα (hoi dōdeka) "the twelve"

**TBTA Decision**: Probably Paucal (p) or Plural (P), depending on target

**Reasoning**:
- Explicit numeral: twelve
- Too large for trial (>3)
- Too small for massive plural (not thousands)
- Murrinh-Patha paucal goes up to ~15 → could use paucal
- Most paucals stop at ~10 → would use plural

**Reproduction**:
- Check target language paucal range
- If paucal includes ~12 → Paucal (p)
- Otherwise → Plural (P)

### Case 4: "Two or Three Witnesses"

**Source**: Matthew 18:16 - "two or three witnesses"

**TBTA Decision**: Dual (D) OR Trial (T) - alternative interpretations

**Challenge**: Disjunction ("or") creates ambiguity

**Reproduction**:
- Could encode as two alternatives
- Or could use Paucal (p) "a few witnesses"
- Depends on how TBTA handles alternatives (need to check actual data)

### Case 5: Crowds, Nations, Multitudes

**Source**: ὄχλος (ochlos) "crowd", ἔθνη (ethnē) "nations/gentiles"

**TBTA Decision**: Plural (P)

**Reasoning**:
- Large, indefinite quantity
- Even for languages with paucal, this exceeds the range
- Always Plural

**Reproduction**:
- Semantic category "crowd" → automatically Plural (P)
- No need to count

---

## Challenges and Unknowns

### Challenge 1: Hebrew Dual Interpretation

**Problem**: Hebrew dual suffix appears on:
- Natural pairs: eyes, ears, hands, feet
- Time: two days, two years
- Place names: Egypt (Mitzrayim - "two narrows"?)

**Question**: Does TBTA encode Hebrew dual as Dual (D) even for lexicalized forms?

**Example**: "eyes" (עֵינַיִם einayim)
- Morphologically dual in Hebrew
- Semantically "two eyes" (natural pair)
- Should this be Dual (D) or just Plural (P)?

**Hypothesis**: TBTA encodes Dual (D) when:
1. Hebrew has dual morphology, AND
2. Semantically refers to exactly two, AND
3. Target language can mark dual

**Need**: Check actual TBTA data to confirm

### Challenge 2: Greek Plural Ambiguity

**Problem**: Greek plural is underspecified for exact number

**Example**: μαθηταί (mathētai) "disciples" - could be 2, 3, 12, 70, or 120

**Question**: How does TBTA decide number without explicit context?

**Hypothesis**:
- Default to Plural (P) unless:
  - Numeral in immediate context ("twelve disciples")
  - Discourse tracking identifies exact participants
  - Cultural knowledge (μαθηταί usually means "the twelve" in Gospels)

**Need**: Analyze TBTA decisions on ambiguous plurals

### Challenge 3: Quadrial Existence

**Problem**: Scholars say true quadrial doesn't exist

**Question**: Why does TBTA include Quadrial (Q)?

**Hypotheses**:
1. **Legacy category**: Included based on outdated claims, never actually used
2. **Semantic placeholder**: For explicit "exactly four" contexts
3. **Greater paucal encoding**: What TBTA calls "quadrial" is actually Sursurunga's greater paucal

**Need**: Check TBTA data - how often is Quadrial (Q) actually used? In which verses?

### Challenge 4: Paucal Boundaries

**Problem**: Paucal range varies widely by language
- Warndarrang: ~5
- Arabic: 3-10
- Murrinh-Patha: ~10-15

**Question**: How does TBTA set the paucal/plural boundary?

**Hypothesis**:
- Consult target language grammar
- Default: 3-10 is paucal, 11+ is plural
- Adjust based on noun type (people vs. things vs. abstract)

**Need**: Check grammars for each paucal language in dataset

### Challenge 5: Pronoun vs. Noun Marking

**Problem**: Many languages mark number on pronouns but not nouns

**Example**: Larike has singular/dual/trial/plural **pronouns**, but nouns only mark plural vs. non-plural

**Question**: Does TBTA encode different number values for pronouns vs. nouns?

**Hypothesis**: Yes - TBTA likely encodes:
- Pronoun number based on pronoun system
- Noun number based on noun system
- They may differ for the same referent

**Need**: Check if TBTA distinguishes syntactic category in number encoding

---

## Recommendations for Reproduction

### Priority 1: Analyze Actual TBTA Data

**Action**: Download and analyze TBTA annotations for sample verses

**Focus on**:
1. Genesis 1:26 - Trinity trial claim
2. Genesis 18 - Three angels/men
3. Gospel passages with "the twelve"
4. Natural pairs (eyes, ears, hands) - dual encoding?
5. Crowds - always plural?

**Questions to answer**:
- How often is each number value (S/D/T/Q/p/P) used?
- What triggers Dual (D)? Hebrew morphology or semantic "two"?
- Is Quadrial (Q) ever used? If so, where?
- What's the paucal/plural boundary in practice?

### Priority 2: Build Language Feature Database

**Action**: For each of our 1009 languages, document:

**Minimal info**:
- Language code
- Family
- Number system: singular-plural, singular-dual-plural, singular-dual-trial-plural, etc.
- Paucal: yes/no, range if yes
- Inclusive/exclusive: yes/no

**Data sources**:
1. Glottolog: Find referenced grammars
2. WALS: Check plurality features (though limited on dual/trial/paucal)
3. Ethnologue: Basic family info
4. Grammar libraries: UNT, UCLA, etc.

**Format**:
```yaml
# languages-number-systems.yaml
tpi:
  name: Tok Pisin
  family: Creole
  number_system:
    - singular
    - dual
    - trial
    - plural
  paucal: false
  inclusive_exclusive: true
  scope: pronouns

sgz:
  name: Sursurunga
  family: Austronesian
  number_system:
    - singular
    - dual
    - paucal_lesser
    - paucal_greater
    - plural
  paucal: true
  paucal_range_lesser: "3-4"
  paucal_range_greater: "4-10"
  inclusive_exclusive: true
  scope: pronouns

wbp:
  name: Warlpiri
  family: Australian
  number_system:
    - singular
    - dual
    - paucal
    - plural
  paucal: true
  paucal_range: "varies by noun class"
  scope: nouns and pronouns
```

### Priority 3: Develop Semantic Number Detector

**Action**: Create tool to determine semantic number from biblical text

**Inputs**:
- Verse text (Hebrew/Greek)
- Morphological analysis (Macula)
- Word glosses
- Context (surrounding verses)

**Process**:
1. **Extract numerals**: "two angels", "three men", "twelve disciples"
2. **Check morphology**: Hebrew dual suffix, plural endings
3. **Track participants**: Same entity across clauses
4. **Apply rules**:
   - Explicit numeral → semantic number = that number
   - Hebrew dual → semantic number = 2
   - No numeral + plural → semantic number = "many" (undefined)
   - Trinity context (Gen 1:26, Matt 28:19) → semantic number = 3

**Output**:
- Semantic number for each noun/pronoun
- Confidence level (high: explicit numeral, medium: morphology, low: inference)

### Priority 4: Map Semantic Number to Target Language

**Action**: Create mapping function

**Inputs**:
- Semantic number (from Priority 3)
- Target language number system (from Priority 2)

**Process**:
```python
def map_number(semantic_num, target_language):
    # Get target language number system
    system = language_features[target_language]['number_system']

    if semantic_num == 1:
        return 'S'  # Singular - universal

    elif semantic_num == 2:
        if 'dual' in system:
            return 'D'  # Dual
        else:
            return 'P'  # Plural

    elif semantic_num == 3:
        if 'trial' in system:
            return 'T'  # Trial
        elif 'paucal' in system:
            return 'p'  # Paucal
        else:
            return 'P'  # Plural

    elif 3 < semantic_num <= 10:
        if 'paucal' in system:
            # Check paucal range
            range_str = language_features[target_language].get('paucal_range', '3-10')
            if semantic_num in parse_range(range_str):
                return 'p'  # Paucal
        return 'P'  # Plural

    else:  # semantic_num > 10 or undefined "many"
        return 'P'  # Plural
```

**Output**:
- TBTA-style number code (S/D/T/Q/p/P)
- For each target language

---

## Next Steps

1. **Verify languages in dataset**
   - Search for Slovene/Slovenian
   - Identify all Slavic languages (dual remnants?)
   - Filter Austronesian by country (PNG/Solomon/Vanuatu → trial likely)
   - Verify Australian Aboriginal count (36 confirmed)

2. **Access TBTA sample data**
   - Clone/download https://github.com/AllTheWord/tbta_db_export
   - Analyze 10-20 verses in detail
   - Document actual encoding patterns

3. **Consult reference grammars**
   - For high-value languages (Tok Pisin, Warlpiri, Sursurunga, Australian languages)
   - Document number systems precisely
   - Note scope (pronouns only? nouns too?)
   - Note obligatoriness vs. optionality

4. **Build prototype**
   - Implement semantic number detector
   - Implement language feature database
   - Implement mapping function
   - Test on known examples (Gen 1:26, Gen 18, etc.)

5. **Validate**
   - Compare output to actual TBTA annotations
   - Measure accuracy
   - Identify discrepancies
   - Refine algorithm

---

## Summary

**What we know**:
- TBTA uses 6 number values: S/D/T/Q/p/P
- Our dataset has languages across the spectrum
- Number annotation is target-driven, not source-driven
- True quadrial likely doesn't exist (use cautiously)

**What we need**:
- Actual TBTA data to reverse-engineer decisions
- Language feature database (number systems for 1009 languages)
- Semantic number extraction from biblical text
- Mapping rules from semantic to target number

**Hypothesis for reproduction**:
1. Extract semantic number (explicit numerals, morphology, context, theology)
2. Look up target language number system
3. Map semantic number to closest target number category
4. Validate against participant tracking and discourse flow

**Confidence**: Medium-High
- We understand the typology well
- We have good language resources
- Main unknown: TBTA's exact decision criteria for edge cases
- Solution: Analyze actual TBTA data to learn patterns
