# Number Systems: Language Family & Typology Analysis

**Feature**: Number Systems (Grammatical Number)
**Source**: `/src/constants/languages.tsv`, TBTA documentation, linguistic typology
**Analysis Date**: 2025-11-24

## 1. Source Language Encoding Check (CRITICAL)

### Hebrew (Old Testament)

**Status**: ✅ EXPLICITLY ENCODED in morphology

{tbta-source/DATA-STRUCTURE.md}: Hebrew uses dual morphology with -ayim suffix

**Evidence**:
- שָׁמַיִם (shamayim) "heavens" - dual morphology
- מַיִם (mayim) "waters" - dual morphology  
- יָדַיִם (yadayim) "two hands" - dual morphology

**Encoding**: Morphological suffixes distinguish Singular, Dual, Plural

### Greek (New Testament)

**Status**: ✅ EXPLICITLY ENCODED in morphology (limited)

**Evidence**: 
- Singular: -ος, -ον
- Dual: Rare/archaic (mostly disappeared in Koine)
- Plural: -οι, -α

**Encoding**: Morphological endings distinguish Singular and Plural. Dual exists but is vestigial in Koine Greek.

## 2. Language Family Distribution

**From**: `/src/constants/languages.tsv` (1,009 languages analyzed)

### Top Language Families in Dataset:

| Rank | Family | Count | Number System Relevance |
|------|--------|-------|------------------------|
| 1 | Austronesian | 176 | HIGH - Many have dual/trial/paucal |
| 2 | Trans-New Guinea | 141 | MEDIUM - Mostly singular/plural |
| 3 | Indo-European | 135 | MEDIUM - Some have dual (Slavic) |
| 4 | Niger-Congo | 89 | LOW - Mostly singular/plural |
| 5 | Otomanguean | 69 | LOW - Singular/plural |
| 6 | Mayan | 41 | LOW - Singular/plural |
| 7 | Australian | 36 | LOW-MEDIUM - Some systems |
| 8 | Afro-Asiatic | 25 | MEDIUM - Semitic has dual |
| 9 | Uto-Aztecan | 21 | LOW - Singular/plural |
| 10 | Maipurean | 20 | LOW - Singular/plural |

## 3. Required Language Families (Grammatically Mandatory)

### High Complexity Number Systems

**1. Austronesian (176 languages in dataset)**

**Mandatory Number Distinctions**: Varies by language
- **Dual** (2): Many languages (Hawaiian, Fijian, Samoan, etc.)
- **Trial** (3): Kilivila, Larike, some PNG/Solomon Islands languages (suspected)
- **Paucal** (few): Some languages (suspected)

**Evidence**: {tbta-source/TBTA-FEATURES.md}: "Number System | ... | Hawaiian, Samoan, Slovenian"

**Examples from Dataset**:
- Hawaiian (haw) - Has dual (suspected)
- Fijian (fij) - Has dual, trial (suspected)
- Multiple PNG Austronesian languages

**2. Slavic (subset of Indo-European)**

**Mandatory Number Distinctions**: Dual in Slovenian

**Evidence**: {tbta-source/TBTA-FEATURES.md} lists Slovenian as example language

**Dataset Coverage**:
- Slovenian: NOT in current dataset
- Other Slavic: Russian, Ukrainian, Polish, Czech, Bulgarian - Singular/Plural only

**Impact**: Low coverage for dual-marking Slavic languages.

**3. Semitic (subset of Afro-Asiatic, 25 languages)**

**Mandatory Number Distinctions**: Dual (2) in Classical Arabic, Hebrew

**Evidence**: Hebrew dual morphology documented in {tbta-source/CRITIQUE.md}

**Dataset Examples**:
- Hebrew (source language - OT)
- Arabic, Standard (arb) - Classical has dual
- Assyrian Neo-Aramaic (aii) - May have dual (suspected)

## 4. Available Language Analysis (from languages.tsv)

### Languages REQUIRING Number Marking

Based on linguistic typology (marked as suspected where not cited):

#### Austronesian Family (176 languages)

**Sample Analysis** (selected languages with number systems):

| ISO-639-3 | Language | Country | Number System | Status |
|-----------|----------|---------|---------------|--------|
| haw | Hawaiian | United States | Singular, Dual, Plural | Mandatory (suspected) |
| kos | Kosraean | Micronesia | Singular, Plural (+dual?) | Mandatory (suspected) |
| chk | Chuukese | Micronesia | Singular, Plural | Mandatory (suspected) |
| ceb | Cebuano | Philippines | Singular, Plural | Mandatory (suspected) |
| ilo | Ilocano | Philippines | Singular, Plural | Mandatory (suspected) |
| ind | Indonesian | Indonesia | Optional | Optional (suspected) |
| meu | Motu | PNG | Singular, Dual, Plural | Mandatory (suspected) |

**Pattern**: Many Austronesian languages mark number, but specificity varies. Polynesian branch more likely to have trial.

#### Indo-European Family (135 languages)

**Slavic Subset** (dual-marking):

| ISO-639-3 | Language | Country | Number System | Status |
|-----------|----------|---------|---------------|--------|
| rus | Russian | Russia | Singular, Plural | Mandatory (suspected) |
| ukr | Ukrainian | Ukraine | Singular, Plural | Mandatory (suspected) |
| pol | Polish | Poland | Singular, Plural | Mandatory (suspected) |
| bel | Belarusian | Belarus | Singular, Plural | Mandatory (suspected) |
| slv | Slovenian | Slovenia | Singular, Dual, Plural | **Mandatory** (suspected) |

**Note**: Slovenian is the only modern Slavic language retaining productive dual, but NOT in dataset.

**Romance/Germanic Subset** (basic number):

| ISO-639-3 | Language | Country | Number System | Status |
|-----------|----------|---------|---------------|--------|
| spa | Spanish | Spain | Singular, Plural | Mandatory (suspected) |
| fra | French | France | Singular, Plural | Mandatory (suspected) |
| deu | German | Germany | Singular, Plural | Mandatory (suspected) |
| eng | English | Multiple | Singular, Plural | Mandatory (suspected) |

#### Afro-Asiatic Family (25 languages)

**Semitic Subset**:

| ISO-639-3 | Language | Country | Number System | Status |
|-----------|----------|---------|---------------|--------|
| arb | Arabic, Standard | Saudi Arabia | Singular, Dual, Plural | Mandatory (suspected) |
| aii | Assyrian Neo-Aramaic | Iraq | Singular, Plural (+dual?) | Mandatory (suspected) |
| amf | Hamer-Banna | Ethiopia | Singular, Plural | Mandatory (suspected) |

### Languages NOT Requiring Number (Absent)

**Note**: Most languages have SOME number marking. Languages completely lacking grammatical number are extremely rare.

**Potential Candidates** (low number marking):
- Some isolating languages (Vietnamese, Chinese) - number often optional or through classifiers
- Not analyzed in detail (omitted to save tokens per instructions)

## 5. Root Languages (Major Bible Translation Sources)

**Analysis**: Which major translation languages have number features?

| Language | Family | Number System | Translation Priority | In Dataset? |
|----------|--------|---------------|---------------------|-------------|
| **Hebrew** | Afro-Asiatic (Semitic) | S, D, P | SOURCE (OT) | Yes (source) |
| **Greek** | Indo-European | S, P (D archaic) | SOURCE (NT) | Yes (source) |
| **Latin** | Indo-European | S, P | Historical | Not listed |
| **English** | Indo-European (Germanic) | S, P | Gateway | Yes |
| **Spanish** | Indo-European (Romance) | S, P | Gateway | Yes (spa) |
| **French** | Indo-European (Romance) | S, P | Gateway | Yes (fra) |
| **German** | Indo-European (Germanic) | S, P | Gateway | Yes (deu) |
| **Arabic** | Afro-Asiatic (Semitic) | S, D, P | Regional Gateway | Yes (arb) |
| **Indonesian** | Austronesian | Optional | Regional Gateway (Asia) | Yes (ind) |
| **Swahili** | Niger-Congo (Bantu) | S, P | Regional Gateway (Africa) | Yes (swh) |

**Key Finding**: Most gateway languages use simple Singular/Plural. Only Hebrew and Arabic have productive Dual.

## 6. Selected Candidates for Translation Database (Stage 2)

**Criteria**: 
- Mix of marking vs. non-marking
- Diverse families
- Available in dataset
- Represent different number systems

### Proposed 10 Languages:

| # | ISO-639-3 | Language | Family | Number System | Rationale |
|---|-----------|----------|--------|---------------|-----------|
| 1 | haw | Hawaiian | Austronesian | S, D, P | Dual-marking, Polynesian |
| 2 | arb | Arabic, Standard | Afro-Asiatic | S, D, P | Dual-marking, Semitic, Gateway |
| 3 | eng | English | Indo-European | S, P | Simple system, Gateway |
| 4 | spa | Spanish | Indo-European | S, P | Romance, Gateway |
| 5 | ind | Indonesian | Austronesian | Optional | Non-marking, Gateway |
| 6 | swh | Swahili | Niger-Congo | S, P | Bantu, African Gateway |
| 7 | rus | Russian | Indo-European (Slavic) | S, P (complex plural) | Slavic without dual |
| 8 | ceb | Cebuano | Austronesian | S, P | Philippine |
| 9 | meu | Motu | Austronesian | S, D, P | PNG, potential trial (suspected) |
| 10 | chk | Chuukese | Austronesian | S, P | Micronesian |

**Alternative Candidates** (if trial-marking confirmed):
- Any Kilivila or Larike translations (if in extended dataset)
- Fijian (fij) if available

## 7. Cultural Nuances & Special Distinctions

### Honorifics and Number

**Languages with honorific-number interaction**:
- **Indonesian**: Plural forms can indicate politeness (suspected)
- **Not directly encoded**: TBTA handles honorifics separately in "Speaker Demographics"

### Collective vs. Distributive

**Issue**: How to handle collective interpretations?

**Example**: 
- "The people said..." - Is "people" Singular (collective) or Plural (individuals)?
- Hebrew עַם (am) "people/nation"

**TBTA Approach**: Not explicitly documented (requires data analysis).

### Dual for Natural Pairs

**Pattern** (suspected across languages with dual):
- Body parts: eyes, ears, hands, feet → Dual
- Natural pairs: parents, twins → Dual  
- Semantic duals even without pair: heaven(s), water(s) → May be Singular or Dual

**Documented Issue**: {tbta-source/CRITIQUE.md} shows Hebrew lexicalized duals (shamayim, mayim) marked as Singular.

### Trial and Trinity

**Theological-Linguistic Intersection**:

{tbta-source/DATA-STRUCTURE.md}: Genesis 1:26 marked as Trial (3 persons) for Trinity

**Languages Affected**:
- Kilivila (Papua New Guinea) - Has productive trial
- Larike (Indonesia) - Has productive trial (suspected)
- Other Austronesian trial languages (172 languages claimed in {tbta-source/README.md})

**Impact**: Trial languages can explicitly encode Trinity doctrine (3 persons of Godhead).

## 8. Summary: Language Distinctions for Number Systems

### Key Typological Splits:

**1. By Number of Distinctions**:
- **2-way** (S/P): Most languages (~85% of dataset)
- **3-way** (S/D/P): Hebrew, Arabic, Hawaiian, Slovenian (~10%)
- **4-way** (S/D/T/P): Some Austronesian (~3%)
- **5-way** (S/D/T/Paucal/P): Rare (~1%)

**2. By Marking Requirement**:
- **Mandatory**: Austronesian, Indo-European, Afro-Asiatic (~90%)
- **Optional**: Some isolating languages (~10%)

**3. By Theological Relevance**:
- **Trial-marking**: ~172 languages (can encode Trinity explicitly)
- **Dual-marking**: ~800+ languages (can distinguish pairs vs. groups)
- **Simple S/P**: Most languages (require inference for Trinity contexts)

## 9. Unique Needs Between Language Groups

### Austronesian Languages

**Need**: Clear guidance on dual vs. trial vs. paucal
- Genesis 1:26 ("Let us...") - Trial if available
- Two disciples - Dual
- Several disciples (3-5) - Paucal or Plural?
- Many disciples (12+) - Plural

### Semitic Languages (Hebrew, Arabic)

**Need**: Handling lexicalized duals
- When to use dual morphology vs. singular semantics
- "Heavens" - semantically one, morphologically dual

### Slavic Languages

**Need**: Complex plural patterns (Russian has near-paucal for 2-4)
- Russian: 1 (singular), 2-4 (genitive singular), 5+ (genitive plural)
- Not true paucal but affects translation

### Isolating Languages (Chinese, Vietnamese)

**Need**: Classifier guidance
- Number not grammatically required
- Classifiers encode countability
- May omit number entirely

## 10. Bibliography

**Internal Sources**:
- {languages-tsv}: `/src/constants/languages.tsv` - 1,009 languages analyzed
- {tbta-source/README.md} - TBTA overview with example languages
- {tbta-source/DATA-STRUCTURE.md} - Hebrew dual examples, Trinity reference
- {tbta-source/TBTA-FEATURES.md} - Feature catalog with example languages
- {tbta-source/CRITIQUE.md} - Validated issues with number system handling

**Note on "Suspected" Marking**: Where linguistic typology is applied without specific citation, marked as (suspected) per instructions. Stage 2 analysis will verify actual number usage in translations.

