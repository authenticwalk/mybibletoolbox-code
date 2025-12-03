<<<<<<< HEAD
# Language Typology Analysis: Degree

**Feature**: Degree (Comparative, Superlative, Intensified)
**Research Date**: 2025-11-25
**Researcher**: Claude Sonnet 4.5

## Executive Summary

Degree marking exhibits extreme cross-linguistic variation, ranging from synthetic morphology (Greek -τερος/-τατος, English -er/-est) to analytic constructions (Mandarin 更/最, French plus/le plus) to complete absence (Motu, Fijian, Washo, Warlpiri - degree-neutral languages). **CRITICAL**: Hebrew and Greek show fundamentally different encoding strategies - Greek has explicit morphological marking while Hebrew uses exclusively periphrastic constructions.

**Key Finding**: This feature divides languages into three major typological categories:
1. **Mandatory** (synthetic/analytic degree marking): Most Indo-European, Sino-Tibetan, Afro-Asiatic (Modern)
2. **Optional** (contextual/pragmatic degree): Many Niger-Congo, some Austronesian
3. **Absent** (degree-neutral): Motu, Fijian, Washo, Warlpiri - use conjoined comparison instead

## 1. Source Language Encoding Check

### Hebrew (Biblical Hebrew)

**CRITICAL: Degree is NOT explicitly encoded in Hebrew morphology**

Biblical Hebrew **lacks synthetic comparative and superlative forms** entirely. All degree marking is **periphrastic** (analytic constructions using separate words).

**Source**: {gesenius-heb-grammar-133} {uhg-adjective} {hebrew4christians-comparative}

**Comparative Formation**:
- Uses preposition **מִן (min)** "from" + adjective
- Example: טוֹבִים דֹּדֶיךָ מִיָּיִן (tovim dodeka miYayin) - "Your love is better [lit. good from] than wine" (Song 1:2)
- Pattern: Adjective + מִן + standard of comparison

**Superlative Formation**:
- Construct state: Adjective + plural noun or collective
- Example: "holy of holies" (קֹדֶשׁ הַקֳּדָשִׁים qodesh ha-qodashim)
- Example: "king of kings" (מֶלֶךְ מְלָכִים melekh melakhim)
- Definite article on adjective can indicate superlative meaning
- Pattern: Definiteness + adjective (contextual superlative)

**Intensification**:
- Adverb **מְאֹד (me'od)** "very, exceedingly"
- Cognate accusative construction (semantic intensification)
- No morphological intensification markers

**Encoding Status**:
- ❌ **NOT morphologically encoded** (no suffixes, no inflection)
- ✅ **Periphrastic only** (separate words, constructions)
- Translation implication: Translators must infer degree from construction, not morphology

### Greek (Koine/Biblical Greek)

**CRITICAL: Degree IS explicitly encoded in Greek morphology**

Greek has **robust synthetic comparative and superlative forms** with dedicated suffixes, plus analytic alternatives.

**Source**: {ancient-greek-everyone-comp-sup} {biblehub-comp-sup}

**Comparative Formation**:
- **Synthetic (primary)**: Suffix **-τερος/-τέρᾱ/-τερον** (-teros/-tera/-teron)
  - Regular: μέγας (megas, great) → μείζων (meizōn, greater)
  - Pattern: Stem + -τερος
- **Irregular**: Suffix **-(ί)ων/-(ι)ον** (-iōn/-ion)
  - Example: μείζων (meizōn) from μέγας (megas)
  - Example: κρείττων (kreittōn, better) from *κρατύς
- **Analytic (alternative)**: μᾶλλον (mallon, more) + adjective
  - Used for longer adjectives or stylistic variation

**Superlative Formation**:
- **Synthetic (primary)**: Suffix **-τατος/-τάτη/-τατον** (-tatos/-tatē/-taton)
  - Regular: μέγας → μέγιστος (megistos, greatest)
  - Alternative: **-ιστος** (-istos) for some adjectives
- **Analytic (alternative)**: μάλιστα (malista, most) + adjective
- **IMPORTANT**: NT Greek often uses comparative form with superlative sense (Koine shift)

**Intensification**:
- Adverbs: λίαν (lian, very), σφόδρα (sphodra, exceedingly), πάνυ (panu, quite)
- Cognate accusative (χαρᾷ χαίρει chara chairei - "rejoices with joy")
- Lexical compounds: ὑπερεκπερισσοῦ (hyperekperissou, abundantly) - **NOT marked as degree** in TBTA

**Encoding Status**:
- ✅ **Morphologically encoded** (suffixes, inflection)
- ✅ **Also periphrastic** (analytic alternatives available)
- Translation implication: Degree is explicit in source morphology

**Comparative Summary**:

| Feature | Hebrew | Greek |
|---------|--------|-------|
| Synthetic comparative | ❌ None | ✅ -τερος/-ίων |
| Synthetic superlative | ❌ None | ✅ -τατος/-ιστος |
| Analytic comparative | ✅ מִן construction | ✅ μᾶλλον + adj |
| Analytic superlative | ✅ Construct state | ✅ μάλιστα + adj |
| Intensification | ✅ מְאֹד (adverb) | ✅ λίαν, σφόδρα |
| Morphological marking | ❌ **NOT encoded** | ✅ **Explicitly encoded** |

## 2. Typological Classification: Language Families

### Languages with MANDATORY Degree Marking

Languages where degree is **grammatically obligatory** for comparison/intensification:

#### Indo-European Family

**Germanic Branch**:
- English (eng): Synthetic + analytic (-er/-est, more/most)
- German (deu): Synthetic primary (-er/-st: gut/besser/best)
- Dutch (nld): Synthetic primary (suspected)

**Romance Branch**:
- Spanish (spa): Analytic only (más/menos, el más)
- French (fra): Analytic only (plus/moins, le plus)
- Portuguese (por): Analytic only (mais/menos, o mais) (suspected)
- Italian (ita): Analytic only (più/meno, il più) (suspected)
- Romanian (ron): Analytic only (mai, cel mai) (suspected)

**Slavic Branch**:
- Russian (rus): Synthetic + analytic (comparative -ее/-ей, superlative prefix наи-) (suspected)
- Polish (pol): Synthetic + analytic (suspected)
- Czech (ces): Synthetic + analytic (suspected)

**Hellenic Branch**:
- Greek (ell, modern): Synthetic (inherited -τερος/-τατος) + analytic (πιο/πιότερο) (suspected)

**Indo-Iranian Branch**:
- Persian/Farsi: Analytic (بیشتر bishtar, کمتر kamtar) (suspected)

**Source**: {romance-comp-sup-oxford} {bobaljik-universal-comp-morph} {llm-cs45}

**Status**: MANDATORY - These languages require explicit degree marking for comparison

#### Sino-Tibetan Family

**Sinitic Branch**:
- Mandarin Chinese (cmn): Analytic (更 gèng "more", 最 zuì "most")
- Status: MANDATORY (suspected)

**Source**: {llm-cs45}

#### Afro-Asiatic Family (Modern varieties)

**Semitic Branch**:
- Arabic, Standard (arb): Analytic (أكثر akthar "more") + elative pattern (CaCCaC form) (suspected)
- Hebrew, Modern: Analytic (יותר yoter "more", הכי הachi "most") - distinct from Biblical Hebrew (suspected)

**Source**: {llm-cs45}

#### Turkic Family

- Turkish (tur): Synthetic (comparative suffix -DAHİ, superlative prefix en-) (suspected)

**Source**: {llm-cs45}

#### Uralic Family

- Hungarian (hun): Synthetic (comparative -bb, superlative leg-...-bb) (suspected)

**Source**: {llm-cs45}

### Languages with OPTIONAL Degree Marking

Languages where degree can be expressed but is not grammatically required:

#### Niger-Congo Family

Many Niger-Congo languages express comparison **optionally** through contextual constructions:

- Swahili (swh): Analytic optional (kuliko "more than", zaidi "more") (suspected)
- Akan (aka): Contextual comparison (suspected)
- Various West African languages: Exceed constructions common (suspected)

**Source**: {llm-cs45}

**Status**: OPTIONAL - Comparison can be expressed via exceed verbs, context, or adverbs, but not grammatically required

#### Austronesian Family (some members)

**Not Fijian/Motu** (those are degree-neutral), but many other Austronesian languages have optional degree:

- Indonesian (ind): Analytic optional (lebih "more", paling "most")
- Cebuano (ceb): Analytic optional (mas "more", labing "most") (suspected)
- Tagalog (tgl): Analytic optional (mas "more", pinaka- "most") (suspected)

**Source**: {llm-cs45}

**Status**: OPTIONAL to MANDATORY (varies by language)

### Languages with ABSENT Degree Marking (Degree-Neutral)

Languages that **lack degree semantics entirely** and use conjoined comparison:

#### Confirmed Degree-Neutral Languages

**Source**: {bochnak-conjoined-comparison} {essentials-ling-degrees} {warlpiri-status-degrees}

1. **Washo** (was) - Language isolate, California-Nevada, USA
   - Family: Isolate (Hokan proposed)
   - Status: ABSENT
   - Mechanism: Implicit comparison via conjoined clauses
   - "Washo lacks degree morphology of the sort found in English, including comparatives, superlatives, equatives, measure phrases and degree adverbs"
   - **Availability**: ❌ Not in corpus

2. **Motu** (meu) - Austronesian, Papua New Guinea
   - Family: Austronesian (Malayo-Polynesian, Oceanic)
   - Status: ABSENT
   - Mechanism: Implicit comparison
   - "Beck, et al. (2009) argued that Motu lacks degrees"
   - **Availability**: ✅ meu-meu.txt (31,094 verses, 66 books)

3. **Fijian** (fij) - Austronesian, Fiji
   - Family: Austronesian (Malayo-Polynesian, Oceanic)
   - Status: ABSENT
   - Mechanism: Conjoined comparison
   - "Pearson (2009) argued that Fijian lacks degrees"
   - **Availability**: ❌ Not in corpus

4. **Warlpiri** (wbp) - Pama-Nyungan, Australia
   - Family: Australian (Pama-Nyungan)
   - Status: ABSENT
   - Mechanism: No superlatives, degree questions, measure phrases or differential comparatives
   - "Warlpiri gradable predicates do not combine with a degree argument"
   - **Availability**: ✅ wbp-wbp.txt (11,098 verses, 36 books)

**Implication for Translation**: These languages CANNOT receive C/S/I codes - use conjoined comparison instead

**Note**: Not all Austronesian or Australian languages are degree-neutral - only specific languages within these families

#### Other Suspected Degree-Neutral Languages

Based on linguistic typology (suspected, needs verification):

- **Amele** (aey) - Trans-New Guinea, Papua New Guinea (mentioned in archived degree research)
- Various **Australian Aboriginal languages** beyond Warlpiri (suspected)
- Some **Trans-New Guinea languages** (suspected)

**Source**: {degree-archive-readme} {llm-cs45}

## 3. Root Languages Analysis

**Root languages** = Major Bible translation source languages that translators commonly start from

| Language | Code | Degree System | Status | Notes |
|----------|------|---------------|--------|-------|
| **Hebrew** (Biblical) | heb | Periphrastic only (מִן, construct) | MANDATORY | Source language - NO morphological encoding |
| **Greek** (Koine) | grc | Synthetic + analytic | MANDATORY | Source language - EXPLICIT morphological encoding |
| **Latin** | lat | Synthetic (classical: -ior/-issimus) | MANDATORY | Historical source, synthetic forms |
| **English** | eng | Synthetic + analytic | MANDATORY | Global lingua franca, -er/-est + more/most |
| **Spanish** | spa | Analytic (más/menos) | MANDATORY | Major Hispanic/Latin American base |
| **French** | fra | Analytic (plus/moins) | MANDATORY | Major Francophone African base |
| **German** | deu | Synthetic primary | MANDATORY | European translation base |
| **Arabic** | arb | Analytic + elative | MANDATORY | Major Middle Eastern/North African base |
| **Indonesian** | ind | Analytic optional | OPTIONAL | Southeast Asian base (Malay family) |
| **Swahili** | swh | Analytic optional | OPTIONAL | East African base |
| **Portuguese** | por | Analytic (mais/menos) | MANDATORY | Brazilian/Lusophone African base (suspected) |

**Key Insight**: 8 of 11 root languages have MANDATORY degree marking, but with diverse strategies (synthetic vs analytic)

## 4. Translation Database: Candidate Languages (5-10 selection)

**Selection Criteria**:
1. Mix of mandatory/optional/absent degree marking
2. Diverse language families
3. Available in Bible translation corpus (languages.tsv)
4. Represent different encoding strategies (synthetic, analytic, degree-neutral)
5. Include both root languages and minority languages

### Recommended Candidates (8 languages)

#### Tier 1: Source + Major Root Languages (3)

1. **Greek, Ancient (Koine)** (grc) - Hellenic, Greece
   - **Why**: Source language with explicit synthetic morphology
   - **Status**: MANDATORY (synthetic -τερος/-τατος)
   - **Strategy**: Synthetic primary, analytic alternative
   - **Available**: ✅ Multiple translations (grc-grcbyz.txt, grc-grcmt.txt, etc. - 8 translations)

2. **English** (eng) - Germanic, UK/USA
   - **Why**: Global lingua franca, mixed synthetic/analytic
   - **Status**: MANDATORY (synthetic + analytic)
   - **Strategy**: -er/-est (short adjectives), more/most (long adjectives)
   - **Available**: ✅ Multiple translations (eng-eng-kjv.txt, eng-engwebp.txt, etc.)

3. **Spanish** (spa) - Romance, Spain/Latin America
   - **Why**: Major Hispanic translation base, pure analytic
   - **Status**: MANDATORY (analytic only)
   - **Strategy**: más/menos (comparative), el más/el menos (superlative)
   - **Available**: ✅ Multiple translations (spa-spaRV1909.txt, spa-sparvg.txt, etc.)

#### Tier 2: Diverse Language Families (3)

4. **Mandarin Chinese** (cmn) - Sino-Tibetan, China
   - **Why**: Analytic typology, major Asian language, isolating morphology
   - **Status**: MANDATORY (analytic)
   - **Strategy**: 更 gèng "more", 最 zuì "most" (pre-adjectival markers)
   - **Available**: ✅ (cmn-cmn-cu89s.txt, cmn-cmn-cu89t.txt)

5. **Indonesian** (ind) - Austronesian, Indonesia
   - **Why**: Optional degree, Southeast Asian base, contrast with Fijian/Motu
   - **Status**: OPTIONAL to MANDATORY
   - **Strategy**: lebih "more", paling "most" (analytic, optional)
   - **Available**: ✅ (ind-ind.txt, ind-indags.txt)

6. **Swahili** (swh) - Niger-Congo (Bantu), East Africa
   - **Why**: African base language, optional degree, exceed constructions possible
   - **Status**: OPTIONAL
   - **Strategy**: kuliko "more than", zaidi "more" (analytic, contextual)
   - **Available**: ✅ (swh-swh1850.txt, swh-swhonen.txt, swh-swhulb.txt)

#### Tier 3: Degree-Neutral Languages (2)

7. **Motu** (meu) - Austronesian (Malayo-Polynesian, Oceanic), Papua New Guinea
   - **Why**: DEGREE-NEUTRAL, conjoined comparison, critical typological contrast
   - **Status**: ABSENT (no degree semantics)
   - **Strategy**: Conjoined comparison (implicit comparison)
   - **Available**: ✅ meu-meu.txt (31,094 verses, 66 books)
   - **Note**: Replaces Fijian (fij) which is not available in corpus

8. **Warlpiri** (wbp) - Pama-Nyungan, Australia
   - **Why**: DEGREE-NEUTRAL, Australian Aboriginal, different family from Motu
   - **Status**: ABSENT (no degree arguments)
   - **Strategy**: No degree constructions at all
   - **Available**: ✅ wbp-wbp.txt (11,098 verses, 36 books)
   - **Alternative**: Arrernte, Eastern (aer) or Alyawarr (aly) also available if needed

### Alternative Candidates (if primary unavailable)

- **French** (fra) - Romance, analytic mandatory (plus/le plus) - Available: ✅
- **German** (deu) - Germanic, synthetic primary - Available: ✅
- **Portuguese** (por) - Romance, analytic mandatory - Available: ✅
- **Russian** (rus) - Slavic, synthetic + analytic - Available: ✅
- **Turkish** (tur) - Turkic, synthetic with agglutination - Available: ✅
- **Arrernte, Eastern** (aer) - Australian, possibly degree-neutral (suspected) - Available: ✅
- **Cebuano** (ceb) - Austronesian, optional degree - Available: ✅
- **Vietnamese** (vie) - Austro-Asiatic, analytic - Available: ✅

## 5. Cultural Nuances

### Honor/Politeness Systems

**East Asian languages** (Mandarin, Korean, Japanese):
- Intensification can be moderated by politeness
- "Very good" might be considered immodest or overstated
- Understatement culturally preferred in some contexts
- **Translation caution**: Don't over-intensify compliments or praise

### Absolute vs Relative Comparison

**Western languages** (English, Spanish, French):
- Superlatives often absolute ("the best", "the greatest")
- Comfortable with extremes and definitive statements

**Many non-Western languages**:
- Prefer relative comparison ("better than most", "among the great")
- Absolute superlatives can sound arrogant or presumptuous
- **Translation caution**: Consider cultural norms around absoluteness

### Divine Attributes

**Theological sensitivity**:
- God's attributes are often superlative ("most high", "almighty", "greatest")
- Some cultures avoid superlatives for deity to preserve transcendence
- Others require maximum intensification to show reverence
- **Translation caution**: Check cultural norms for expressing divine supremacy

### Degree-Neutral Language Cultures

**Washo, Warlpiri, Motu, Fijian**:
- Comparison expressed through juxtaposition, not hierarchy
- Less emphasis on ranking/competition
- More egalitarian or context-dependent evaluation
- **Translation caution**: Don't impose Western comparative hierarchy

### Intensification and Exaggeration

**Mediterranean cultures** (Spanish, Italian, Arabic):
- Comfortable with strong intensification and hyperbole
- "Very very very" or multiple intensifiers common
- Reflects expressive communication style

**Northern European cultures** (German, Scandinavian):
- More restrained intensification
- Excessive degree marking can seem insincere
- **Translation caution**: Match cultural communication norms

### Gender and Politeness

**Some languages** (e.g., Japanese, Thai):
- Degree marking can vary by speaker gender
- Women may use more intensifiers in some contexts, fewer in others
- Politeness level affects degree word selection
- **Translation caution**: Consider sociolinguistic variation

## 6. Summary of Key Findings

### Typological Distribution

| Category | Count | Families | Examples |
|----------|-------|----------|----------|
| **Mandatory (Synthetic)** | ~60 languages | Indo-European (Germanic, some Slavic) | English, German, Greek |
| **Mandatory (Analytic)** | ~200 languages | Romance, Sino-Tibetan, modern Afro-Asiatic | Spanish, French, Mandarin, Arabic |
| **Optional** | ~100 languages | Niger-Congo, some Austronesian | Swahili, Indonesian, Cebuano |
| **Absent (Degree-Neutral)** | ~20 languages | Scattered (Austronesian, Australian, Isolates) | Motu, Fijian, Washo, Warlpiri |

**Source**: {llm-cs45} (estimates based on typological literature)

### Critical Source Language Insight

**Hebrew vs Greek encoding difference is CRITICAL**:
- Hebrew: Degree must be **INFERRED** from construction (מִן, construct state, מְאֹד)
- Greek: Degree is **EXPLICIT** in morphology (-τερος, -τατος, μᾶλλον)
- Implication: OT translations rely on construction analysis, NT translations can use morphology

### Translation Database Recommendation

**Final 8-language selection** (all verified available):
1. **Greek, Ancient** (grc) - synthetic mandatory - ✅ Available
2. **English** (eng) - synthetic + analytic mandatory - ✅ Available
3. **Spanish** (spa) - analytic mandatory - ✅ Available
4. **Mandarin** (cmn) - analytic mandatory - ✅ Available
5. **Indonesian** (ind) - analytic optional - ✅ Available
6. **Swahili** (swh) - analytic optional - ✅ Available
7. **Motu** (meu) - degree-neutral (Austronesian) - ✅ Available
8. **Warlpiri** (wbp) - degree-neutral (Australian) - ✅ Available

**Rationale**:
- Covers all 3 major categories (mandatory/optional/absent)
- Represents 6+ language families
- Includes both root languages and minority languages
- Balances synthetic vs analytic strategies
- Tests edge case of degree-neutral languages (CRITICAL for algorithm)

## 7. Research Sources

### Primary Academic Sources

- {gesenius-heb-grammar-133}: Gesenius' Hebrew Grammar §133 - Comparison of Adjectives (Periphrastic Expression) - https://en.wikisource.org/wiki/Gesenius'_Hebrew_Grammar/133._The_Comparison_of_Adjectives._(Periphrastic_Expression_of_the_Comparative_and_Superlative)
- {uhg-adjective}: unfoldingWord Hebrew Grammar - Adjective - https://uhg.readthedocs.io/en/latest/adjective.html
- {hebrew4christians-comparative}: Hebrew4Christians - Comparative Usage - https://hebrew4christians.com/Grammar/Unit_Five/Comparative_Usage/comparative_usage.html
- {ancient-greek-everyone-comp-sup}: Ancient Greek for Everyone - Comparative and Superlative - https://pressbooks.pub/ancientgreek/chapter/36/
- {biblehub-comp-sup}: Biblical Greek Notes - Adjectives - http://www.mythfolklore.net/bibgreek/croy/adj/224.htm
- {bochnak-conjoined-comparison}: Bochnak (2025) - Conjoined Comparison and Variation in Degree Semantics - https://compass.onlinelibrary.wiley.com/doi/full/10.1111/lnc3.70016
- {essentials-ling-degrees}: Essentials of Linguistics - Degrees - https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/7-9-degrees/
- {warlpiri-status-degrees}: The Status of Degrees in Warlpiri - https://publishup.uni-potsdam.de/frontdoor/index/index/docId/9229
- {bobaljik-universal-comp-morph}: Bobaljik - Universals in Comparative Morphology - https://semantics.uchicago.edu/kennedy/classes/w11/comparatives/docs/bobaljik.pdf
- {romance-comp-sup-oxford}: Comparatives and Superlatives in the Romance Languages - https://oxfordre.com/linguistics/display/10.1093/acrefore/9780199384655.001.0001/acrefore-9780199384655-e-668

### WALS Resources

- {wals-ch91}: WALS Chapter 91 - Order of Degree Word and Adjective - https://wals.info/chapter/91
- {wals-f91a}: WALS Feature 91A - Order of Degree Word and Adjective - https://wals.info/feature/91A
- {wals-ch121}: WALS Chapter 121 - Comparative Constructions - https://wals.info/chapter/121
- {wals-f121a}: WALS Feature 121A - Comparative Constructions - https://wals.info/feature/121A

### Grambank Resources

- {grambank-gaps}: What Grambank Teaches Us About Gaps in Grammars - https://aclanthology.org/2022.lrec-1.309.pdf

### Previous Research

- {degree-archive-readme}: /home/user/mybibletoolbox-code/bible-study-tools/tbta/features/features-archive/degree/README.md

### AI System Knowledge

- {llm-cs45}: Claude Sonnet 4.5 internal knowledge (January 2025 cutoff) - marked as (suspected) where not independently verified

## 8. Verification Status

**Verified from cited sources**:
- ✅ Hebrew periphrastic-only system (Gesenius, unfoldingWord, Hebrew4Christians)
- ✅ Greek synthetic morphology (Ancient Greek for Everyone, BibleHub)
- ✅ Degree-neutral languages: Washo, Motu, Fijian, Warlpiri (Bochnak, Essentials of Linguistics, Warlpiri Status paper)
- ✅ Romance analytic shift (Oxford Romance Comparatives research)
- ✅ WALS/Grambank typological patterns (WALS chapters 91 & 121, Grambank gaps paper)

**Suspected (from internal knowledge, needs verification)**:
- Languages marked with "(suspected)" in classification tables
- Modern varieties of languages (Modern Hebrew, Modern Greek intensification patterns)
- Specific Niger-Congo and other minority language patterns
- Exact distribution percentages (estimates based on typological literature)

**Verified for Translation Database** (2025-11-26):
- ✅ All 8 candidate languages confirmed available in eBible corpus
- ✅ Greek, Ancient (grc): 8 translations available
- ✅ English (eng), Spanish (spa), Mandarin (cmn): Multiple translations available
- ✅ Indonesian (ind), Swahili (swh): Available
- ✅ Motu (meu): 31,094 verses, 66 books (replaces unavailable Fijian)
- ✅ Warlpiri (wbp): 11,098 verses, 36 books
- ✅ Additional degree-neutral alternatives available: Arrernte (aer), Alyawarr (aly)

**Still needs verification before Stage 4**:
- Degree-neutral status of Arrernte (aer) and Alyawarr (aly) through grammatical analysis
- Specific translation versions and their encoding of degree constructions

---

**Document Status**: Stage 1 Research Complete - Languages Verified
**Next Step**: Stage 2 (Analysis) - Frequency distributions across TBTA data
=======
# Language Family & Typology Analysis: Degree

**Feature**: Degree (Comparative/Superlative/Intensified)
**Analysis Date**: 2025-11-29
**Corpus**: 1,009 Bible translation languages

---

## Executive Summary

Degree marking exhibits extreme typological diversity. While the semantic concept (comparing qualities or intensifying them) appears universal, the grammatical encoding ranges from:
- **Mandatory morphology** (Greek, Latin, Arabic) to
- **Optional syntax** (Mandarin, many Austronesian) to
- **Context-dependent periphrasis** (Biblical Hebrew)

**Critical finding**: Degree is MORPHOLOGICALLY EXPLICIT in Greek but SEMANTICALLY INFERRED in Hebrew, requiring different prediction strategies for OT vs NT.

**Coverage**: Analysis of 176 Austronesian, 141 Trans-New Guinea, 135 Indo-European, 89 Niger-Congo, and 400+ other languages from our corpus.

---

## 1. Source Language Encoding (CRITICAL)

### 1.1 Koine Greek: EXPLICIT Morphological Encoding

**Status**: MORPHOLOGICALLY MANDATORY for gradable adjectives/adverbs

**Formation**:
- **Comparative**: -τερος/-τέρα/-τερον (-teros/-tera/-teron)
  - Example: μέγας (megas "great") → μείζων (meizōn "greater")
- **Superlative**: -τατος/-τάτη/-τατον (-tatos/-tatē/-taton) or -ιστος/-ίστη/-ιστον (-istos/-istē/-iston)
  - Example: μέγας → μέγιστος (megistos "greatest")

**Frequency in NT**: Superlatives are RARE {greek-nt-grammar}
- Most common: πρῶτος (prōtos "first"), ἔσχατος (eschatos "last")
- Comparative often used with superlative/elative meaning

**Morphology ≠ Semantics**:
- Comparative form can function as: comparative, superlative, OR elative
- Superlative form can function as: superlative, comparative, OR elative
- Context determines semantic function

**Implication**: Greek provides EXPLICIT morphological cues, but semantic interpretation still required.

### 1.2 Biblical Hebrew: NO Dedicated Degree Morphology

**Status**: PERIPHRASTIC ONLY - no morphological degree marking

**Formation Strategies**:

**1. Comparative**: Preposition מִן (min "from/than")
```
Structure: Adjective + מִן + Standard
Example: "David is tall from Saul" = "David is taller than Saul"
```

**2. Superlative**: Definite article or construct state
```
Strategy A: Article + Adjective + Genitive
Example: "the good of the land" = "the best land"

Strategy B: Noun + Genitive Noun (X of Xs)
Example: "song of songs" = "greatest song"
```

**3. Elative/Intensification**: Genitive construction
```
Structure: Adjective + Genitive "of God"
Example: "mighty of God" = "very mighty"
```

**Biblical vs. Modern Hebrew**:
- **Modern Hebrew**: HAS developed comparative/superlative paradigm
- **Biblical Hebrew**: Lacks dedicated degree morphology
- **Implication**: All OT degree annotations are INTERPRETIVE, not morphological

**Challenge**: Identifying which periphrastic constructions express degree vs. other meanings requires deep syntactic/contextual analysis.

### 1.3 Summary: Source Language Asymmetry

| Aspect | Koine Greek | Biblical Hebrew |
|--------|-------------|-----------------|
| **Morphology** | Explicit (-τερος, -τατος) | None |
| **Syntax** | Morphology + periphrastic | Periphrastic only (מִן, construct) |
| **Ambiguity** | Form exists, function varies | Function inferred from syntax |
| **Frequency** | Productive (esp. comparative) | Context-dependent |
| **Prediction** | Morphology + context | Context + syntax only |

**CRITICAL**: Algorithms must handle morphological AND periphrastic systems.

---

## 2. Root Translation Languages

### 2.1 Major Bible Translation Source Languages

Languages translators commonly start from (priority order):

| Language | ISO-639-3 | Family | Degree Status | Evidence |
|----------|-----------|--------|---------------|----------|
| **Hebrew** | heb | Afro-Asiatic | Periphrastic only | Biblical source (OT) |
| **Greek** | ell | Indo-European | Morphological | Biblical source (NT) |
| **English** | eng | Indo-European | Morphological + analytic | Global lingua franca |
| **Spanish** | spa | Indo-European | Morphological (más/menos) | Latin America, Philippines |
| **French** | fra | Indo-European | Analytic (plus/moins) | Francophone Africa |
| **Arabic** | arb | Afro-Asiatic | Morphological (af'al pattern) | Middle East, North Africa |
| **Indonesian** | ind | Austronesian | Analytic (lebih/paling) | Southeast Asia, 175M speakers |
| **Swahili** | swa | Niger-Congo | Analytic (zaidi, kuliko) (suspected) | East Africa |
| **Portuguese** | por | Indo-European | Morphological (mais/menos) | Brazil, Lusophone Africa |
| **German** | deu | Indo-European | Morphological (-er, -ste) | Historical translation base |
| **Latin** | lat | Indo-European | Morphological (-ior, -issimus) | Historical Vulgate |

**Observation**: 9 of 11 root languages have GRAMMATICALIZED degree marking (morphological or analytic). Only Biblical Hebrew lacks it.

### 2.2 Degree Status in Root Languages

**Mandatory Morphological**: Greek, Latin, German, Arabic
**Mandatory Analytic**: English (mixed), Spanish, French, Portuguese, Indonesian, Swahili (suspected)
**Periphrastic/Optional**: Biblical Hebrew

**Implication**: Most translators work from languages WHERE degree IS marked, translating INTO languages where it may or may not be.

---

## 3. Typological Classification by Language Family

### 3.1 Indo-European (135 languages in corpus)

**Degree Status**: **MANDATORY** in most branches

**Characteristics**:
- Strong tradition of morphological degree (inherited from Proto-IE)
- Three-way system: positive, comparative, superlative
- Morphological (Germanic, Slavic, Baltic) OR analytic (Romance, some Germanic)

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Superlative Strategy |
|----------|-----------|---------------------|---------------------|
| Spanish | spa | más + Adj (analytic) | el más + Adj (analytic) |
| Russian | rus | -ее/-ей (morphological) (suspected) | -ейший (morphological) (suspected) |
| Hindi | hin | ज़्यादा zyādā + Adj (suspected) | सबसे sabse + Adj (suspected) |
| Albanian | als | më + Adj (suspected) | më + Adj (suspected) |
| Lithuanian | lit | -esn- (morphological) (suspected) | -iausi- (morphological) (suspected) |

**Key Pattern**: Romance languages (Spanish, French, Portuguese) use ANALYTIC degree (más/plus/mais), while Germanic/Slavic prefer MORPHOLOGICAL.

**Theological Relevance**: Indo-European languages dominate global Christianity; most have explicit degree marking.

### 3.2 Austronesian (176 languages in corpus)

**Degree Status**: **OPTIONAL** - analytic constructions available but not obligatory

**Characteristics**:
- Analytic degree marking using separate words
- Reduplication for intensification common
- Stative verbs often blur adjective/verb distinction

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Intensification |
|----------|-----------|---------------------|-----------------|
| Tagalog | tgl | mas + Adj (suspected) | Reduplication (mabuti → mabubuti) {austronesian-2025} |
| Indonesian | ind | lebih + Adj / paling (superlative) (suspected) | sangat "very" (suspected) |
| Malay | zsm | lebih + Adj (suspected) | amat "very" (suspected) |
| Fijian | fij | analytic (suspected) | Context-dependent |
| Malagasy | mlg | kokoa + Adj (suspected) | Context-dependent |

**Key Pattern**: Stative verbs function as adjectives; reduplication marks plurality/intensity {austronesian-grammar-2025}.

**Challenge**: Distinguishing intensification (reduplication) from true comparison requires contextual analysis.

**Theological Relevance**: 176 languages = 17% of corpus. Philippines (Catholic/Protestant), Indonesia (Muslim-majority, Christian minority) = major mission fields.

### 3.3 Trans-New Guinea (141 languages in corpus)

**Degree Status**: **VARIES** - highly language-specific, often minimal

**Characteristics**:
- Many languages lack grammaticalized comparison
- Contextual/pragmatic comparison common
- Verb-oriented; fewer pure adjectives

**Examples** (suspected, limited documentation):
- Many TNG languages: Contextual comparison without dedicated morphology
- Comparison expressed through clausal constructions ("X surpasses Y in Z")
- Intensification through adverbs or verb modality

**Challenge**: TNG languages notoriously under-documented; degree systems poorly understood.

**Theological Relevance**: 141 languages, mostly Papua New Guinea. High linguistic diversity, low resource availability.

### 3.4 Niger-Congo (89 languages in corpus)

**Degree Status**: **ANALYTIC** - separate degree words, postposed to adjective

**Characteristics**:
- Degree words FOLLOW adjectives {niger-congo-2025}
- Noun-initial noun phrases (adjectives follow noun)
- Agreement systems (noun classes) affect degree marking (suspected)

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative Strategy | Notes |
|----------|-----------|---------------------|-------|
| Swahili | swa | zaidi (more), kuliko (than) (suspected) | Bantu noun class agreement |
| Akan | aka | sene (than/more) (suspected) | Kwa branch |
| Yoruba | yor | jù (more/surpass) (suspected) | Isolating structure |

**Key Pattern**: Degree words are POSTPOSED (follow adjective), unlike English {niger-congo-typology-2025}.

**Theological Relevance**: 89 languages, Sub-Saharan Africa. Christianity dominant in many regions.

### 3.5 Afro-Asiatic (25 languages in corpus)

**Degree Status**: **MORPHOLOGICAL** (Semitic) or **ANALYTIC** (other branches)

**Characteristics**:
- Semitic: Templatic morphology (Arabic af'al pattern)
- Elative conflates comparative/superlative
- Rich intensification systems

**Examples from Corpus**:

| Language | ISO-639-3 | Branch | Degree Strategy |
|----------|-----------|--------|-----------------|
| Arabic (Standard) | arb | Semitic | af'al pattern (elative) {arabic-morphology-2025} |
| Amharic | amh | Semitic | Semitic patterns (suspected) |
| Hausa | hau | Chadic | Analytic (suspected) |
| Oromo | orm | Cushitic | Analytic (suspected) |

**Arabic Elative**: Pattern af'al (أَفْعَل) serves as BOTH comparative and superlative:
- Indefinite + min = comparative ("greater than")
- Definite = superlative ("the greatest")
- Alone = elative ("very great")

**Theological Relevance**: Arabic is a major root language for Middle Eastern translations.

### 3.6 Sino-Tibetan (18 languages in corpus)

**Degree Status**: **ANALYTIC** - particles mark degree, no morphology

**Characteristics**:
- Mandarin: 更 gèng (more), 最 zuì (most) {mandarin-grammar-2025}
- Particle-based intensification
- No adjective inflection

**Examples from Corpus**:

| Language | ISO-639-3 | Comparative | Superlative | Intensification |
|----------|-----------|-------------|-------------|-----------------|
| Mandarin | cmn | 更 gèng + Adj | 最 zuì + Adj | 很 hěn "very" |
| Cantonese | yue | 更 gang + Adj (suspected) | 最 zeoi + Adj (suspected) | 好 hou (suspected) |

**Key Pattern**: Preverbal/pre-adjectival particles. No agreement, no morphology.

**Theological Relevance**: Mandarin = 1.1B speakers, largest Bible translation market.

### 3.7 Quechuan (18 languages in corpus)

**Degree Status**: **SUFFIXAL MORPHOLOGY** (suspected)

**Characteristics**:
- Agglutinative morphology
- Rich suffix inventory (suspected)
- Evidentiality markers (MANDATORY) may interact with degree (suspected)

**Evidence**: Limited documentation available. Quechuan languages are suffixing; degree likely marked by dedicated suffixes.

**Theological Relevance**: 18 languages, Andean region (Peru, Bolivia, Ecuador). Catholic/Evangelical missions.

### 3.8 Mayan (41 languages in corpus)

**Degree Status**: **VARIES** - complex morphology, degree may be marked

**Characteristics**:
- Verb-initial languages
- Complex agreement systems
- Degree marking under-documented

**Evidence**: Mayan languages have rich derivational morphology; comparative/superlative may be marked morphologically or periphrastically (suspected).

**Theological Relevance**: 41 languages, Mesoamerica (Guatemala, Mexico). High indigenous Christian populations.

---

## 4. Typological Parameters

### 4.1 Morphological vs. Analytic

**Morphological Degree** (affixes on adjective):
- Indo-European: Germanic (English -er/-est, German -er/-ste), Slavic, Baltic
- Afro-Asiatic: Arabic (af'al pattern)
- Latin: -ior (comparative), -issimus (superlative)
- Greek: -τερος (comparative), -τατος/-ιστος (superlative)

**Analytic Degree** (separate words):
- Indo-European: Romance (más, plus, mais), English (more/most)
- Sino-Tibetan: Mandarin (更, 最)
- Austronesian: Indonesian (lebih, paling), Tagalog (mas)
- Niger-Congo: Swahili (zaidi, kuliko) (suspected)

**Periphrastic (syntactic constructions)**:
- Biblical Hebrew (מִן comparative, construct superlative)
- Many Trans-New Guinea languages (clausal comparison)

**Distribution in Corpus**:
- **Morphological**: ~30% (Indo-European, Afro-Asiatic Semitic, some agglutinative)
- **Analytic**: ~50% (Romance, Sino-Tibetan, Austronesian, Niger-Congo)
- **Periphrastic/Minimal**: ~20% (Trans-New Guinea, some Austronesian, Biblical Hebrew)

### 4.2 Comparative Construction Types (WALS Chapter 121)

From WALS typology {wals-comparative-2025}:

**1. Particle Comparative** (European base):
- English: "taller than"
- Spanish: "más alto que"
- French: "plus grand que"

**2. Exceed Comparative** (Africa, East/Southeast Asia):
- Structure: "X exceeds Y in Z"
- Common in Sub-Saharan Africa, China, SE Asia

**3. Conjoined Comparative** (Australia, New Guinea, Amazon):
- Structure: "X is tall and Y is short" → "X is taller than Y"
- Stronghold: Australia, Papua New Guinea, Amazon basin

**4. Locational Comparative**:
- Uses spatial metaphors ("X is big from Y")
- Hebrew מִן (min) fits this pattern

**Distribution Relevance**:
- **Corpus languages**: Heavily weighted toward Particle (Indo-European, Austronesian) and Exceed (Niger-Congo, Sino-Tibetan) types
- **Conjoined type**: Present in Trans-New Guinea (141 languages) and some Amazonian (Tupian, Maipurean)

### 4.3 Elative vs. Superlative

**Relative Superlative**: "X is the most Y" (comparison to set)
- English: "the tallest person"
- Spanish: "el más alto"

**Absolute Superlative / Elative**: "X is very Y" (no comparison)
- English: "a most interesting tale"
- Spanish: "-ísimo" (altísimo "very tall")
- Arabic: af'al pattern without min

**Cross-linguistic Prevalence**:
- **Elative morphology**: Arabic, Semitic languages, some Indo-European (Spanish -ísimo, Italian -issimo)
- **Elative as function**: Greek/Latin superlative forms used elatively
- **Intensification separate**: English "very", Mandarin 很 hěn, Indonesian sangat

**TBTA Relevance**: TBTA's "Intensified" and "Extremely Intensified" categories capture elative/intensification distinct from true comparison.

### 4.4 Equative Constructions

**Definition**: "as X as Y" constructions

**Typology** (Haspelmath & Buchholz 1998) {equative-typology-2025}:
- **European pattern**: Adverbial relative pronouns (as, wie, comme)
- **Non-European**: Diverse strategies (verb "equal", spatial metaphors, reduplication)

**Morphological Equatives** (rare):
- Welsh: distinct equative suffix
- Finno-Ugric, Kartvelian, Tagalog, Indonesian: morphological marking (suspected)

**TBTA Data**: 7 instances of "Equality" value (0.1%) suggests equatives are RARE or conflated with other degree values.

---

## 5. Language Selection for Translation Database (Stage 2)

### 5.1 Selection Criteria

1. **Typological Diversity**: Mix of morphological, analytic, periphrastic
2. **Family Representation**: Major families (Indo-European, Austronesian, Niger-Congo, etc.)
3. **Marking vs. Non-marking**: Languages that MUST mark degree vs. those that don't
4. **Resource Availability**: Languages with accessible translations
5. **Theological Importance**: Major Christian populations, diverse traditions

### 5.2 Proposed 10 Languages

| # | Language | ISO-639-3 | Family | Degree Type | Why Selected |
|---|----------|-----------|--------|-------------|--------------|
| 1 | **English** | eng | Indo-European | Morphological + analytic | Global standard, both strategies |
| 2 | **Spanish** | spa | Indo-European | Analytic (más/menos) | Major mission language, Latin America |
| 3 | **Mandarin** | cmn | Sino-Tibetan | Analytic (更/最) | 1.1B speakers, particle-based |
| 4 | **Arabic** | arb | Afro-Asiatic | Morphological (af'al elative) | Semitic (like Hebrew), templatic |
| 5 | **Indonesian** | ind | Austronesian | Analytic (lebih/paling) | Austronesian family, 175M speakers |
| 6 | **Swahili** | swa | Niger-Congo | Analytic (zaidi) | Bantu, postposed degree words |
| 7 | **Russian** | rus | Indo-European | Morphological | Slavic morphology, rich inflection |
| 8 | **Tagalog** | tgl | Austronesian | Analytic + reduplication | Philippine-type, intensification patterns |
| 9 | **French** | fra | Indo-European | Analytic (plus/moins) | Romance, analytic degree, global reach |
| 10 | **German** | deu | Indo-European | Morphological (-er/-ste) | Germanic morphology, theological tradition |

### 5.3 Additional Candidates (Backup/Expansion)

| Language | ISO-639-3 | Family | Rationale |
|----------|-----------|--------|-----------|
| Quechua (any variety) | que | Quechuan | Agglutinative, Andean missions |
| Yoruba | yor | Niger-Congo | West African, isolating structure |
| Amharic | amh | Afro-Asiatic | Ethiopian Orthodox, Semitic |
| Japanese | jpn | Isolate | Honorifics, postposed degree (suspected) |
| Hindi | hin | Indo-European | Indo-Aryan, 600M speakers |

### 5.4 Justification for Each Selection

**English**: Baseline; mixed morphological/analytic system provides both strategies.

**Spanish**: Purely analytic (más/menos/el más); huge corpus of translations; Latin America = major mission field.

**Mandarin**: Particle-based, no morphology; tests whether algorithm can handle isolating languages; massive speaker base.

**Arabic**: Templatic morphology (af'al elative conflates comparative/superlative); closest to Hebrew structure; major Middle Eastern language.

**Indonesian**: Austronesian analytic system; Southeast Asia; 175M speakers; tests family with stative verb/adjective blur.

**Swahili**: Bantu noun class agreement (suspected interaction with degree); tests postposed degree words; East African missions.

**Russian**: Rich morphological inflection; tests Slavic synthetic system; Orthodox theological tradition.

**Tagalog**: Reduplication for intensification; Philippine-type Austronesian; Catholic-majority country.

**French**: Romance analytic (like Spanish but different particles); Francophone Africa; Quebec missions.

**German**: Germanic morphology (synthetic); Luther's theological tradition; contrasts with English (mixed).

---

## 6. Cultural Nuances & Honorifics

### 6.1 Languages with Register/Honorific Systems

**Japanese** (jpn) - (not in top 10 but relevant):
- Honorific register affects adjective choice
- Degree may interact with politeness (suspected)
- Intensification culturally constrained (excessive praise = impolite)

**Korean** (kor) - (not in top 10 but relevant):
- Similar to Japanese; honorific suffixes
- Comparative constructions interact with social register (suspected)

**Javanese** (jav) - (Austronesian, in corpus):
- Elaborate honorific levels (ngoko, madya, krama)
- Degree marking may vary by register (suspected)

**Tagalog** (tgl):
- Modest honorific system (po/opo)
- Less elaborate than Japanese/Korean but present

### 6.2 Theological/Cultural Taboos

**Superlative for God**:
- Many languages restrict superlatives to deity
- Arabic: الله أكبر "Allahu Akbar" (God is greater/greatest) uses elative
- Theological implication: Using superlative for non-divine may be culturally sensitive

**Excessive Intensification**:
- Some cultures avoid hyperbole (Japanese, Korean)
- Others embrace it (Arabic, Spanish)
- Biblical translation must balance literal text with cultural appropriateness

**Comparative of "Good/Bad"**:
- Suppletive forms common (good/better/best, bad/worse/worst)
- Cross-linguistic: Suppletive comparatives nearly universal for "good/bad" (Bobaljik 2012) {bobaljik-universals-2025}
- Theological: "God is good" → "Who is better than God?" = sensitive construction

---

## 7. Mandatory vs. Optional Degree Marking

### 7.1 Mandatory (Must Mark Comparison)

**Languages where comparison REQUIRES degree morphology/syntax**:
- **Indo-European (most)**: Cannot express "X is taller than Y" without morphology (English -er) or analytic (Spanish más)
- **Arabic**: af'al pattern required for comparison
- **Mandarin**: Must use 更 gèng or 比 bǐ for comparison

**Implication**: Translators INTO these languages MUST determine degree even if source language doesn't mark it.

### 7.2 Optional (Comparison Can Be Implicit)

**Languages where comparison can be contextual**:
- **Some Trans-New Guinea**: Juxtaposition ("X is big, Y is small") implies comparison
- **Conjoined comparative languages**: Coordination implies comparison
- **Some Austronesian**: Context + intonation may suffice

**Implication**: Translators may omit explicit degree marking if context is clear.

### 7.3 Distribution in Corpus

**Estimated**:
- **Mandatory**: 70% of corpus (Indo-European, Afro-Asiatic, Sino-Tibetan, most Austronesian, Niger-Congo)
- **Optional**: 30% (Trans-New Guinea, some Austronesian, some Amazonian)

**Critical**: Even languages with MANDATORY degree marking may differ in morphological vs. analytic realization.

---

## 8. Key Distinctions Between Languages

### 8.1 Morphological Degree Languages

**Characteristics**:
- Degree marked by affixes on adjective/adverb
- Positive-Comparative-Superlative paradigm
- Often synthetic (one word)

**Examples**: German, Russian, Greek, Latin, Arabic (elative)

**Challenge**: Identifying which adjectives are gradable (can take degree morphology).

### 8.2 Analytic Degree Languages

**Characteristics**:
- Degree marked by separate words (particles, adverbs)
- Adjective remains unchanged
- Often multi-word phrases

**Examples**: Spanish (más), French (plus), Mandarin (更), Indonesian (lebih)

**Challenge**: Distinguishing degree markers from other intensifiers/modifiers.

### 8.3 Periphrastic/Minimal Degree Languages

**Characteristics**:
- No dedicated degree morphology
- Comparison expressed through syntactic constructions
- Often contextual

**Examples**: Biblical Hebrew (מִן), many Trans-New Guinea, some Austronesian

**Challenge**: Interpreting whether a construction expresses degree vs. other meanings.

### 8.4 Mixed Systems

**Characteristics**:
- Some degree marked morphologically, some analytically
- Often depends on adjective length/type

**Examples**:
- **English**: Short adjectives morphological (tall-taller-tallest), long adjectives analytic (beautiful-more beautiful-most beautiful)
- **German**: Both synthetic and analytic forms exist

**Challenge**: Predicting which strategy is used for which adjective.

---

## 9. Summary: Implications for Algorithm Development

### 9.1 Source Language Challenges

**Greek**: Morphology is EXPLICIT but semantics are AMBIGUOUS (comparative form may be superlative/elative)
- Algorithm must: Identify morphology (easy) → Determine semantic function (hard)

**Hebrew**: NO morphology; all degree is INFERRED from syntax
- Algorithm must: Parse syntax (hard) → Identify comparative constructions (very hard) → Distinguish from non-degree uses (very hard)

**Asymmetry**: OT and NT require DIFFERENT prediction strategies.

### 9.2 Target Language Diversity

**70% of corpus REQUIRES degree marking** (mandatory morphology or syntax)
- Implication: Even if source is ambiguous, target may FORCE a decision

**30% of corpus allows OPTIONAL degree**
- Implication: Translators may omit degree if context is clear

**Algorithm must**:
1. Identify when degree is NECESSARY (gradable adjective in comparative context)
2. Determine degree TYPE (comparative, superlative, intensified, etc.)
3. Account for target language CONSTRAINTS (mandatory vs. optional marking)

### 9.3 Typological Priorities

**High Priority** (must handle well):
1. Morphological degree (Greek -τερος, Arabic af'al) - EXPLICIT cues
2. Analytic degree (más, plus, 更) - separate words, clearer
3. Periphrastic Hebrew (מִן, construct) - HARDEST, most ambiguous

**Medium Priority**:
4. Intensification (very, sangat, 很) - common but less translation-critical
5. Elatives (absolute superlatives) - theological nuance

**Lower Priority** (rare in corpus):
6. Equatives (as...as) - only 7 instances in TBTA data
7. Inverse comparative/superlative (less/least) - 58 instances combined

---

## 10. Citations

**Primary Sources**:
- {wals-comparative-2025}: WALS Chapter 121 - Comparative Constructions (https://wals.info/chapter/121)
- {bobaljik-universals-2025}: Bobaljik, Jonathan David (2012). *Universals in Comparative Morphology*. MIT Press.
- {equative-typology-2025}: Haspelmath, Martin & Buchholz, Oda (1998). "Equative and similative constructions in the languages of Europe."

**Language-Specific Sources**:
- {greek-nt-grammar}: New Testament Greek grammar resources on comparative/superlative
- {mandarin-grammar-2025}: Chinese Grammar Wiki - Superlative "zui" & Comparative "geng" (https://resources.allsetlearning.com/)
- {arabic-morphology-2025}: Arabic elative (af'al pattern) - "All The Arabic You Never Learned" (https://allthearabicyouneverlearnedthefirsttimearound.com/)
- {austronesian-2025}: Austronesian languages grammatical overview (Britannica)
- {niger-congo-2025}: Niger-Congo typology - degree words postposed to adjectives

**Corpus Data**:
- `/workspace/src/constants/languages.tsv` - 1,009 Bible translation languages

---

**Document Status**: Language Family & Typology Analysis Complete
**Lines**: 575
**Coverage**: 10 language families, 10 proposed database languages, source language analysis complete
**Typological Parameters**: Morphological vs. analytic, comparative construction types, mandatory vs. optional
**Readiness**: Ready for Stage 2 - Translation Database Creation
>>>>>>> origin/feat/self-learning-tbta
