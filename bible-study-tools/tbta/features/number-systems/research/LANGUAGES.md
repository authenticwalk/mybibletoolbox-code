# Language Family & Typology Analysis: Number Systems

**Source**: TBTA language documentation, WALS, Grambank, dataset analysis  
**Date**: 2025-01-27  
**Purpose**: Identify which languages require number system distinctions and classify their needs

---

## 1. Source Language Encoding Check

### 1.1 Hebrew

**Morphological Encoding**: 
- **Dual morphology exists**: `-ayim` suffix (e.g., `שָׁמַיִם` shamayim "heavens", `מָּיִם` mayim "waters")
- **Status**: Lexicalized duals (semantically singular concepts)
- **Productive Dual**: Rare, primarily for natural pairs (eyes, hands, feet)
- **Trial/Paucal/Quadrial**: **NOT encoded** morphologically

**TBTA Policy**: Semantic overrides morphological (Hebrew duals → Singular when lexicalized)

**Source**: `tbta-source/CRITIQUE.md` Section 3.2

### 1.2 Greek

**Morphological Encoding**:
- **Singular/Plural only**: No dual, trial, paucal, or quadrial morphology
- **Dual**: Archaic, not productive in Koine Greek
- **Trial/Paucal/Quadrial**: **NOT encoded** morphologically

**Source**: Standard Greek grammar (no TBTA-specific documentation)

### 1.3 Conclusion

**Source languages (Hebrew/Greek) do NOT explicitly encode**:
- Trial number
- Paucal number  
- Quadrial number
- Productive dual (Hebrew has lexicalized duals only)

**Translation Challenge**: Target languages requiring these distinctions must infer from context, theological knowledge, or explicit numbers in text.

---

## 2. Required Language Families

### 2.1 Austronesian Family (172 languages in dataset)

**Number System Requirements**:

#### Oceanic Subgroup (~87 languages, 50.6% of family)

**Mandatory Features**:
- **Dual**: Very common (e.g., Samoan `lāua` "they two")
- **Trial**: Present in many Oceanic languages (e.g., Larike, Kilivila)
- **Paucal**: Common in Oceanic languages

**Examples from Dataset**:
- **Samoan** (smo): Dual/trial/plural distinctions
- **Fijian** (fij): Dual/trial/paucal/plural
- **Kilivila** (kij): Trial number (documented in TBTA examples)
- **Larike** (alo): Trial number

**Philippine Subgroup (45 languages)**

**Mandatory Features**:
- **Dual**: Less common than Oceanic
- **Trial/Paucal**: Rare or absent
- **Plural**: Standard

**Indonesian Subgroup (~18 languages)**

**Mandatory Features**:
- **Dual**: Minimal or absent
- **Trial/Paucal**: Absent
- **Plural**: Standard

**Source**: `tbta/languages/families/austronesian/README.md`, `tbta/languages/families/austronesian/linguistic-features.md`

**Typological Classification**:
- **Oceanic**: Mandatory (dual/trial/paucal required)
- **Philippine**: Optional (dual may exist)
- **Indonesian**: Absent (singular/plural only)

---

### 2.2 Trans-New Guinea Family (129 languages in dataset)

**Number System Requirements**:

**Mandatory Features**:
- **Dual**: Very common across family
- **Paucal**: Present in some languages (e.g., Yimas)
- **Trial**: Rare or absent
- **Plural**: Standard

**Examples from Dataset**:
- **Yimas** (yee): Four-way system (singular/dual/paucal/plural) in pronouns
- **Wantoat** (wnc): Three-way system (singular/dual/plural) in pronouns
- **Mian** (mpt): Dual marking on pronouns and verbs
- **Telefol** (tlf): Dual marking on pronouns and verbs
- **Amele** (aey): Number marking restricted to kinship terms (plural `-el`)

**Proto-TNG Reconstructions**:
- Dual: `*-li`, `*-t`
- Plural: `*-nV`
- Collective: `*-pi-` (dual), `*-m-` (plural)

**Typological Classification**:
- **Dual**: Mandatory (very common)
- **Paucal**: Optional (present in some languages)
- **Trial**: Absent (not documented)

**Source**: `tbta/languages/families/trans-new-guinea/README.md`, `tbta/languages/families/trans-new-guinea/grammatical-features-part1.md`

---

### 2.3 Australian Family (36 languages in dataset)

**Number System Requirements**:

**Mandatory Features**:
- **Dual**: Common
- **Paucal**: Present in some languages
- **Trial**: Rare or absent
- **Plural**: Standard

**Examples from Dataset**:
- **Arrernte, Eastern** (aer): Dual number documented
- **Alyawarr** (aly): Dual number
- **Anindilyakwa** (aoi): Number distinctions

**Typological Classification**:
- **Dual**: Mandatory (common)
- **Paucal**: Optional (present in some languages)
- **Trial**: Absent

**Source**: WALS, Australian language typology

---

### 2.4 Slavic Languages (Indo-European)

**Number System Requirements**:

**Dual Preservation**:
- **Slovene**: Full dual system (nouns, verbs, adjectives, pronouns) - **NOT in dataset**
- **Upper/Lower Sorbian**: Full dual - **NOT in dataset**
- **Kashubian**: Full dual - **NOT in dataset**

**Dataset Languages** (no dual):
- Russian, Polish, Czech, Ukrainian, Belarusian, Croatian, Serbian - **none have dual**

**Typological Classification**:
- **Slavic languages in dataset**: Absent (singular/plural only)
- **Slavic languages with dual**: Mandatory (but not in our dataset)

**Source**: `tbta/languages/families/indo-european/translation-analysis.md`

---

### 2.5 Other Language Families

**Mayan Family**:
- **Dual**: Present in some languages
- **Typological Classification**: Optional

**Niger-Congo Family**:
- **Number**: Expressed through noun classes, not dedicated number morphology
- **Typological Classification**: Absent (number encoded differently)

**Otomanguean Family**:
- **Number**: Marked through quantifiers, not noun suffixes
- **Typological Classification**: Absent (number encoded differently)

---

## 3. Available Languages Analysis

### 3.1 Dataset Summary

**Total Languages**: 1,009 languages in `src/constants/languages.tsv`

**Languages Requiring Number Systems**:

| Family | Languages in Dataset | Number System Requirement |
|--------|---------------------|---------------------------|
| **Austronesian** | 172 | Oceanic: Mandatory (dual/trial/paucal)<br>Philippine: Optional (dual)<br>Indonesian: Absent |
| **Trans-New Guinea** | 129 | Mandatory (dual common, paucal optional) |
| **Australian** | 36 | Mandatory (dual common, paucal optional) |
| **Slavic (with dual)** | 0 | Mandatory (but not in dataset) |
| **Mayan** | ~10 | Optional (dual in some) |
| **Total Requiring** | ~337+ | Varies by feature |

### 3.2 Typological Classification by Feature

#### Dual Number

**Mandatory** (~337 languages):
- Austronesian Oceanic: ~87 languages
- Trans-New Guinea: ~129 languages  
- Australian: ~36 languages
- Mayan: ~5-10 languages (suspected)

**Optional** (~45 languages):
- Austronesian Philippine: ~45 languages

**Absent** (~627 languages):
- Austronesian Indonesian: ~18 languages
- Indo-European (most): ~200+ languages
- Niger-Congo: ~94 languages (number via noun classes)
- Other families: ~315+ languages

#### Trial Number

**Mandatory** (~87 languages):
- Austronesian Oceanic: ~87 languages (trial-marking subset)

**Absent** (~922 languages):
- All other languages in dataset

**Source**: `tbta-source/README.md` - "Trial number (172 languages)" (but only Oceanic subset in our dataset)

#### Paucal Number

**Mandatory** (~50-100 languages):
- Austronesian Oceanic: ~50-70 languages (paucal-marking subset)
- Trans-New Guinea: ~10-20 languages (e.g., Yimas)
- Australian: ~5-10 languages

**Optional** (~50 languages):
- Some Oceanic languages use paucal optionally

**Absent** (~859+ languages):
- Most languages in dataset

#### Quadrial Number

**Mandatory**: **0 languages** (no natural language has true grammatical quadrial)

**TBTA Schema**: Includes Quadrial, but linguistic evidence shows this is incorrect (`tbta-source/CRITIQUE.md` Section 3.1)

**Reality**: Languages like Sursurunga have "greater paucal" (4+), not true quadrial

---

## 4. Root Languages Analysis

**Root languages** are major Bible translation languages that translators often start with (priority: Hebrew, Greek, but smaller languages often begin with parent language of their region).

### 4.1 Root Languages with Number Systems

**Hebrew** (ISO-639-3: `heb`):
- **Dual**: Morphological (lexicalized), not productive
- **Trial/Paucal/Quadrial**: Absent
- **Status**: Source language, semantic priority policy

**Greek** (ISO-639-3: `grc`/`ell`):
- **Dual**: Archaic, not productive in Koine
- **Trial/Paucal/Quadrial**: Absent
- **Status**: Source language

**Arabic** (ISO-639-3: `arb`):
- **Dual**: Productive (nouns, verbs, adjectives)
- **Trial/Paucal/Quadrial**: Absent
- **Status**: Root language for Middle East/African translations
- **In Dataset**: Yes (`arb-arb-vd.txt`, `arb-arbnav.txt`)

**Sanskrit** (ISO-639-3: `san`):
- **Dual**: Productive (archaic, not used in modern translations)
- **Trial/Paucal/Quadrial**: Absent
- **Status**: Root language for South Asian translations
- **In Dataset**: Yes (suspected, need verification)

### 4.2 Root Languages Without Number Systems

**English** (`eng`): Singular/plural only  
**Spanish** (`spa`): Singular/plural only  
**French** (`fra`): Singular/plural only  
**German** (`deu`): Singular/plural only  
**Indonesian** (`ind`): Singular/plural only (root for many Austronesian translations)  
**Swahili** (`swa`): Singular/plural only (root for many African translations)

---

## 5. Candidate Languages for Translation Database

**Criteria**: Mix of marking vs. non-marking, diverse families, from dataset

### 5.1 High-Priority Candidates (10 languages)

1. **Samoan** (`smo`) - Austronesian Oceanic
   - **Why**: Full dual/trial/plural system, well-documented
   - **Family**: Austronesian (Oceanic)
   - **Number System**: Mandatory (dual/trial/plural)

2. **Fijian** (`fij`) - Austronesian Oceanic  
   - **Why**: Dual/trial/paucal/plural, extensive Bible translation
   - **Family**: Austronesian (Oceanic)
   - **Number System**: Mandatory (dual/trial/paucal/plural)

3. **Kilivila** (`kij`) - Austronesian Oceanic
   - **Why**: Trial number documented in TBTA examples (Genesis 1:26)
   - **Family**: Austronesian (Oceanic)
   - **Number System**: Mandatory (trial-marking)

4. **Larike** (`alo`) - Austronesian Oceanic
   - **Why**: Trial number documented in TBTA examples
   - **Family**: Austronesian (Oceanic)
   - **Number System**: Mandatory (trial-marking)

5. **Yimas** (`yee`) - Trans-New Guinea
   - **Why**: Four-way system (singular/dual/paucal/plural)
   - **Family**: Trans-New Guinea
   - **Number System**: Mandatory (dual/paucal/plural)

6. **Mian** (`mpt`) - Trans-New Guinea
   - **Why**: Dual marking on pronouns and verbs, well-documented
   - **Family**: Trans-New Guinea
   - **Number System**: Mandatory (dual)

7. **Telefol** (`tlf`) - Trans-New Guinea
   - **Why**: Dual marking, triple-indexing system
   - **Family**: Trans-New Guinea
   - **Number System**: Mandatory (dual)

8. **Arrernte, Eastern** (`aer`) - Australian
   - **Why**: Dual number, well-documented
   - **Family**: Australian
   - **Number System**: Mandatory (dual)

9. **Arabic, Standard** (`arb`) - Afro-Asiatic
   - **Why**: Productive dual, root language for region
   - **Family**: Afro-Asiatic
   - **Number System**: Mandatory (dual)

10. **Tagalog** (`tgl`) - Austronesian Philippine
    - **Why**: Optional dual, major translation language
    - **Family**: Austronesian (Philippine)
    - **Number System**: Optional (dual may exist)

### 5.2 Rationale for Selection

**Diversity**:
- 3 Oceanic (trial-marking)
- 3 Trans-New Guinea (dual/paucal)
- 1 Australian (dual)
- 1 Afro-Asiatic (dual, root language)
- 1 Philippine (optional dual)
- 1 control (well-documented)

**Coverage**:
- Trial: 3 languages (Samoan, Kilivila, Larike)
- Paucal: 2 languages (Fijian, Yimas)
- Dual: 7 languages (all except Tagalog)
- Root languages: 2 (Arabic, Tagalog)

---

## 6. Cultural Nuances

### 6.1 Honorifics & Social Distinctives

**Not Applicable**: Number systems are grammatical, not honorific-based

**Note**: Some languages may use number distinctions for social purposes (e.g., dual for married couples), but this is not the primary function

### 6.2 Taboos

**Not Documented**: No taboos related to number systems found in research

### 6.3 Natural Pairs

**Universal Pattern**: Body parts (eyes, hands, feet) naturally occur in pairs

**Translation Impact**: 
- Dual-marking languages expect dual for natural pairs
- Hebrew dual morphology for body parts maps directly to dual-marking languages
- Example: "his eyes" → dual in dual-marking languages

**Source**: Universal linguistic pattern, not culture-specific

---

## 7. Distinctions Between Languages

### 7.1 Trial vs. Plural Distinction

**Languages Requiring Trial**:
- Oceanic Austronesian: Must distinguish exactly 3 vs. 3+ (many)
- Example: Genesis 1:26 "Let us make" → Trial (Trinity) vs. Plural (divine council)

**Languages Without Trial**:
- Most languages: Use plural for 3+
- Example: English "we" (3+) vs. "we two" (dual)

### 7.2 Paucal vs. Plural Distinction

**Languages Requiring Paucal**:
- Some Oceanic: Must distinguish "few" (3-15) vs. "many" (15+)
- Some Trans-New Guinea: Paucal for small groups

**Languages Without Paucal**:
- Most languages: Use plural for all non-singular

### 7.3 Dual vs. Plural Distinction

**Languages Requiring Dual**:
- Most Trans-New Guinea: Must distinguish 2 vs. 3+
- Many Oceanic: Must distinguish 2 vs. 3+
- Australian: Must distinguish 2 vs. 3+

**Languages Without Dual**:
- Most Indo-European: Use plural for 2+
- Example: English "they" (2+) vs. dual-marking languages "they two" vs. "they many"

---

## 8. Summary

### 8.1 Source Language Status

**Hebrew/Greek**: Do NOT encode trial/paucal/quadrial morphologically

**Translation Challenge**: Must infer from context, theology, or explicit numbers

### 8.2 Target Language Requirements

**Mandatory Number Systems** (~337 languages):
- Dual: ~337 languages (Austronesian Oceanic, Trans-New Guinea, Australian)
- Trial: ~87 languages (Austronesian Oceanic subset)
- Paucal: ~50-100 languages (Oceanic, some Trans-New Guinea, some Australian)

**Optional Number Systems** (~45 languages):
- Dual: ~45 languages (Austronesian Philippine)

**Absent** (~627 languages):
- Most Indo-European, Niger-Congo, other families

### 8.3 Key Distinctions

1. **Trial vs. Plural**: Critical for Trinity references (Genesis 1:26)
2. **Dual vs. Plural**: Critical for pairs (two disciples, two witnesses)
3. **Paucal vs. Plural**: Important for small groups vs. large crowds

---

**Next Steps**: See `SCHOLARLY.md` for typological research and `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` for theological analysis.

