# Number System Feature

## Feature Definition

The **Number System** feature identifies grammatical number distinctions beyond the basic singular/plural dichotomy. While English and Biblical Greek/Hebrew primarily distinguish singular (1) from plural (2+), many languages grammatically encode finer number distinctions:

- **Singular** (S): One entity
- **Dual** (D): Exactly two entities
- **Trial** (T): Exactly three entities (rare - often confused with paucal)
- **Paucal** (p): Small inexact group (typically 3-15, range varies by language)
- **Plural** (P): Multiple entities (more than paucal or unspecified)

**Linguistic Status**: These number distinctions are grammatically obligatory in languages that mark them - speakers cannot avoid choosing the correct number form when using nouns, pronouns, and verbs.

**Translation Impact**: Languages with these distinctions require translators to determine precise counts or groupings even when the source text (Hebrew/Greek) uses ambiguous plural forms.

---

## TBTA Tier 0 Encoding

**CRITICAL**: Position 2 of noun/pronoun character codes explicitly encodes number system:

| Position | Feature | Values |
|----------|---------|--------|
| **2** | **Number** | **S** (singular), **D** (dual), **T** (trial), **p** (paucal), **P** (plural) |

**Encoding Source**: TBTA DATA-STRUCTURE.md, Noun Codes table (10 positions)

**Implication**: When TBTA data exists, **ALWAYS check Position 2 first** before applying any algorithmic prediction. This is Tier 0 data - explicitly encoded in the source morphology.

**Example**:
```
Noun code: "MSNIADANP1"
Position 2: "S" → Singular (explicit)
```

**Algorithm Rule 1 (Tier 0 Check)**:
```
IF TBTA data exists for this noun/pronoun:
  RETURN Position 2 character (S/D/T/p/P)
ELSE:
  Proceed to hierarchical prompting algorithm
```

---

## Theological/Linguistic Context

### Biblical Example: Genesis 1:26 "Let Us Make"

**Hebrew Text**: `נַֽעֲשֶׂה אָדָם בְּצַלְמֵנוּ` (na'aseh adam b'tsalmenu - "Let us make man in our image")

**Grammatical Form**: Hebrew uses plural verb (`na'aseh` = "let us make") and plural suffix (`-enu` = "our")

**Number Ambiguity**: Hebrew plurals don't specify whether "us" = 2, 3, 4+, or many

**Translation Challenge for Trial Languages**:
- If translating into a language with **trial number** (exactly 3), the translator must choose:
  - **Trial**: "Let us-three make" → Implies Trinity (Father, Son, Holy Spirit)
  - **Plural**: "Let us-many make" → Implies divine council or angels
  - **Dual**: "Let us-two make" → Problematic for Trinitarian theology

**Scholarly Consensus** (2024):
- **Michael Heiser** (Trinitarian scholar): "Seeing the Trinity in Gen 1:26 is reading the New Testament back into the Old Testament."
- **Gordon J. Wenham** (World Biblical Commentary): "It is now universally admitted that this was not what the plural meant to the original author."
- **Main interpretations**: (1) Divine Council [scholarly consensus], (2) Plural of Majesty, (3) Trinity [Christian theological application], (4) Self-Deliberation

**Translation Implication**: While trial number *could* be used theologically to express Trinitarian doctrine in translation, this is a theological application rather than the original Hebrew meaning.

### Other Biblical Examples

**Dual Number Examples**:
- **Luke 24:13**: "Two of them" - requires dual in dual-marking languages
- **Acts 13:2**: "Set apart for me Barnabas and Saul" - dual reference to two missionaries
- **Genesis 19:1**: "Two angels came to Sodom" - dual number obligatory
- **Mark 6:7**: Jesus sent disciples "two by two" - dual emphasis

**Paucal Number Examples** (clarified with 2024 research):
- **Matthew 18:20**: "Where two or three gather" - paucal (small group, not large assembly)
- **John 2:6**: "Six stone water jars" - exact count, but paucal languages may categorize as "few"
- **Genesis 18:2**: "Three men" visiting Abraham - paucal (not trial - trial is extremely rare)

**Critical Distinction**: Most "trial" systems are actually **paucal** (minimum of 3, not exactly 3). True trial (exactly 3) is extremely rare in world languages.

---

## Language Family Analysis (Updated 2024)

### Stage 2: Languages Requiring Number System Feature

Based on typological research, TBTA analysis, and 2024 web research:

#### 1. **Austronesian Family** (176 languages in dataset)

**Dual Number**: Present in ~87 Oceanic languages (50% of Austronesian dataset)
- **Samoan**: `lāua` (they-two), `tāua` (we-two-inclusive), `māua` (we-two-exclusive)
- **Fijian**: Dual pronouns for exactly two referents
- **Hawaiian**: Marks singular-dual-plural (2024 Ka Baibala Hemolele Bible uses modern orthography)

**Paucal Number** (NOT trial): Present in multiple Oceanic languages
- **Fijian**: Personal pronouns distinguish four numbers: singular, dual, **paucal** (small number >2), plural
  - Paucal = "a small number of participants" (not exactly 3)
  - 2024 linguistic evidence: Fijian uses paucal derived from numeral 'three', but evolved semantically
- **Pattern**: May apply to numbers up to 5 in some languages
- **Etymology**: Many Austronesian paucals derived from Proto-Austronesian word for 'three' but expanded semantically

**True Trial** (exactly 3): **EXTREMELY RARE**
- **Tok Pisin**: Has trial pronouns (e.g., `mitripela` = we-three-exclusive) - one of few confirmed trials
- **Larike, Tolai, Raga, Wamesa**: Documented trial pronouns (facultative, not obligatory)
- **Scholarly consensus (2024)**: Most "trials" are actually paucals (minimum of 3, not exactly 3)

**Grammatical Obligatoriness**:
- Almost all trials are **facultative** (optional), not obligatory
- Some languages have facultative dual + facultative paucal/trial (Larike)
- Dual is often obligatory when present

**Translation Impact**: **HIGH**
- Dual: Required for paired disciples, two witnesses, etc.
- Paucal: Helps distinguish small groups from large crowds (Matthew 18:20 "two or three")
- Trial: Very rare - avoid assuming "trial" without linguistic evidence (likely paucal instead)

#### 2. **Indo-European Family** (135 languages in dataset)

**Dual Number**: Rare, preserved in only 4 Slavic languages
- **Slovenian**: Dual is obligatory for count 2, considered most distinctive feature
  - Singular: `hiša` (house)
  - Dual: `hiši` (two houses)
  - Plural: `hiše` (three or more houses)
- **Upper Sorbian**: Complete dual system (Bible translated 1728)
- **Lower Sorbian**: Dual preserved
- **Kashubian**: Dual preserved

**Historical Note**: Biblical Hebrew and Ancient Greek both had dual forms
- **Biblical Hebrew**: Dual endings `יִם-` (-ayim) for paired body parts (eyes, ears, hands, feet) and time periods
  - *Never found in adjectives, verbs, or pronouns* (nouns only)
  - **CRITICAL ERROR PATTERN**: Paired body parts are NOT always dual in context
    - Matthew 5:30 "if your RIGHT hand causes you to sin" → singular (one hand specified)
    - Context overrides morphology when injury/loss/specificity involved
- **Ancient Greek**: Had dual across nouns, verbs, adjectives (NOT in Koine Greek used in NT)
- **Pattern Divergence**: Hebrew used dual primarily for natural pairs; Slovenian uses dual *except* for natural pairs (opposite pattern!)

**Translation Impact**: Low-Medium (only 4 languages)
- Critical for Slovenian Bible (12th language with complete Bible, 1583)
- Important for translation accuracy but affects very few languages

#### 3. **Trans-New Guinea Family** (129 languages in dataset)

**Dual Number**: Very common across the family
- **Proto-TNG Reconstruction**: *-li, *-t (dual markers)
- **Pattern**: Three-way distinction common: Singular / Dual / Plural
- **Examples**:
  - **Wantoat**: Three-way (sg/dual/pl) in pronouns
  - **Yimas**: Four-way (sg/dual/paucal/pl) in pronouns
  - **Amele**: Plural marking (-el) restricted to kinship terms

**Paucal Number**: Present in some languages
- **Yimas**: Distinct paucal number (between dual and plural)
- **Range**: "A few" - typically 3-15 items
- **Murrinh-Patha**: Paucal extends up to 15 individuals

**Translation Impact**: **HIGH**
- Dual very significant for Scripture pairs (two disciples, two witnesses)
- Hebrew dual forms may map directly to TNG dual
- "Both" and "all" require careful distinction

#### 4. **Australian Family** (36 languages in dataset)

**Paucal Number**: Common feature
- **Range**: 3-15 items (varies by language)
- **Warlpiri**: Paucal + dual number system
- **Pattern**: Often combines with dual for fine-grained number distinctions

**Dual Number**: Varies by kinship
- Some languages have dual only for certain noun classes
- Kinship terms often trigger dual number

**Translation Impact**: **MEDIUM**
- Paucal helps distinguish small groups from large crowds
- Important for passages mentioning "a few" disciples or witnesses

#### 5. **Afro-Asiatic Family** (25 languages in dataset)

**Dual Number**: Classical Arabic and Hebrew only
- **Classical Hebrew**: Dual for paired body parts and time periods (nouns only)
- **Classical Arabic**: Full dual system (no longer in Modern Standard Arabic dialects)
- **Pattern**: Limited to nouns, not verbs or adjectives

**Translation Impact**: Low (historical languages only)
- Important for understanding source text morphology
- Modern varieties have lost dual

---

## Summary of Language Families Requiring Number System Feature

| Language Family | Languages (count) | Dual | Trial | Paucal | Priority |
|-----------------|-------------------|------|-------|--------|----------|
| **Austronesian** | 176 | ✅ (~87 Oceanic) | ⚠️ (very rare, mostly paucal) | ✅ (common in Oceanic) | **HIGH** |
| **Trans-New Guinea** | 129 | ✅ (very common) | ❌ | ✅ (some languages) | **HIGH** |
| **Indo-European** | 135 | ✅ (4 Slavic only) | ❌ | ❌ | **LOW** |
| **Australian** | 36 | ✅ (varies) | ❌ | ✅ (common) | **MEDIUM** |
| **Afro-Asiatic** | 25 | ✅ (Classical only) | ❌ | ❌ | **LOW** |
| **TOTAL** | **501+** | **~220+** | **<10 confirmed** | **~50-70** | — |

**Key Findings (Updated 2024)**:
- **Dual**: ~220+ languages require dual marking (44% of analyzed languages)
- **Trial**: <10 languages confirmed (mostly facultative, not obligatory) - MUCH RARER than previously thought
- **Paucal**: ~50-70 languages - often mistakenly labeled "trial" in older literature
- **Quadrial**: Extremely rare (possibly non-existent as true grammatical category per Michael Cysouw)

**Critical Correction**: The original mission statement mentioned "172 languages with trial number" - this is INCORRECT. The vast majority are **paucal** systems (minimum of 3, not exactly 3). True trial is found in <10 Austronesian languages and is usually facultative.

---

## Common Prediction Errors (Systematized from Archive)

### Error 1: Missing TBTA Semantic Expansions
**Pattern**: TBTA marks abstract/action nouns as entities with number
**Examples**: "all these things" → "things" is plural (referring to multiple events/items)
**Detection**: Look for demonstratives + abstract nouns
**Frequency**: ~15% of errors

### Error 2: Assuming Paired Body Parts Are Always Dual
**Pattern**: Naturally paired body parts (hands, eyes, feet)
**Problem**: Context may specify ONE of the pair
**Examples**:
- Matthew 5:30 "if your RIGHT hand causes you to sin" → **singular**, not dual
- "They washed their hands" → dual (both hands)
**Detection**: Look for "right/left" or injury contexts
**Frequency**: ~10% of errors
**Note**: Hebrew -ayim suffix indicates dual, but **context overrides**

### Error 3: Missing Trinity Trial in Subtle Contexts
**Pattern**: Trinity (Father, Son, Spirit) contexts
**Problem**: Not recognizing implicit Trinity references
**Examples**: "baptize in the name of Father, Son, Spirit" → "name" might be trial
**Detection**: Baptismal formulas, doxologies, theological passages
**Frequency**: ~5% of errors, but **theologically critical**
**Note**: Highest priority error to avoid

### Error 4: Confusing Generic Plural with Specific Count
**Pattern**: Generic types vs. specific groups
**Examples**:
- "the people rejoiced" → specific group (definite article + event)
- "people are like grass" → generic category
**Detection**: Check for articles, demonstratives, context specificity
**Frequency**: ~20% of errors

### Error 5: Ignoring Hebrew Morphological Signals
**Pattern**: Hebrew dual suffix -ayim (שְׁנַיִם, עֵינַיִם)
**Problem**: Missing clear morphological indicators
**Solution**: Always check Hebrew morphology for dual markers
**Frequency**: ~8% of errors when Hebrew source available

### Error 6: Confusing Paucal with Trial
**Pattern**: Small group indicators ("a few", "some", "several")
**Problem**: Assuming "trial" (exactly 3) when language actually has paucal (minimum of 3)
**Examples**: "a few disciples" → paucal (small group, typically 3-5), NOT trial
**Detection**: Check linguistic literature - most "trials" are actually paucals
**Frequency**: ~10% of classification errors
**Note**: **NEW ERROR PATTERN** (2024 research correction)

---

## Stage Checklist

### ✅ Stage 1: Research TBTA Documentation
- [x] Reviewed TBTA source materials
- [x] Verified Tier 0 encoding (Position 2: S/D/T/p/P)
- [x] Reviewed archived work (Stages 1-3 completed with peer review)
- [x] Generated updated README with Tier 0 encoding and 2024 research

### ✅ Stage 2: Language Study
- [x] Identified 501+ languages requiring this feature
- [x] Documented language families and obligatory vs. facultative distinctions
- [x] Corrected trial vs. paucal confusion (2024 update)
- [x] Listed target translation scenarios

### ✅ Stage 3: Scholarly and Internet Research
- [x] Reviewed typological databases (WALS, linguistic literature)
- [x] Updated with 2024 web research on trial/paucal distinction
- [x] Documented Fijian paucal system (NOT trial)
- [x] Verified Hawaiian dual-plural system
- [x] Confirmed scholarly consensus on Genesis 1:26 interpretations

### ⬜ Stage 4: Generate Test Set with Translation Data
- [ ] **CRITICAL**: Use subagent to prevent seeing answers
- [ ] Extract TBTA data with `extract_feature.py` (Position 2 values)
- [ ] Sample size: 100+ verses per value minimum
- [ ] Create translation database with:
  - **Fijian** (paucal system - verify against Nai Vola Tabu Vakavakadewa Vou)
  - **Hawaiian** (dual system - verify against Ka Baibala Hemolele 2018)
  - **Slovenian** (obligatory dual - verify against Dalmatinova Biblija)
  - **Tok Pisin** (trial system - verify against Nupela Testamen)
  - **Samoan** (dual system)
- [ ] Generate dual outputs: answer sheets (TBTA) + question sheets (translations)
- [ ] Split: train (40%), test (30%), validate (30%)
- [ ] Balance across OT/NT, genre, difficulty
- [ ] Include adversarial cases (paired body parts with injury/loss contexts)

### ⬜ Stage 5: Analyze Translations & Develop Algorithm
- [ ] **Rule 1 (Tier 0)**: Always check TBTA Position 2 first
- [ ] **Rule 2 (Translation Consensus)**: For non-TBTA verses, analyze what translators did
- [ ] Create ANALYSIS.md with hierarchical prompting approach
- [ ] Develop PROMPT1.md with locked predictions
- [ ] Apply 6-step error analysis from archived learnings
- [ ] Iterate until 95%+ accuracy (100% for stated values with n≥100)

### ⬜ Stage 6: Test Against Validate Set & Peer Review
- [ ] Blind subagent validation
- [ ] 4 critical peer reviews:
  1. **Theological**: Trinity contexts, baptismal formulas
  2. **Linguistic**: Trial vs. paucal distinction, Hebrew dual morphology
  3. **Methodological**: Tier 0 check priority, translation consensus
  4. **Translation Practitioner**: Test with Fijian, Hawaiian, Slovenian scenarios
- [ ] Create experiments/TRANSLATOR-IMPACT.md
- [ ] Address all critical feedback
- [ ] Production readiness verification

---

## Research Notes (Updated 2024)

### Critical Clarification: Trial vs. Paucal

**2024 Web Research Findings**:
- **Fijian** uses **paucal**, not trial: "a small number of participants" (not exactly 3)
- Most Austronesian "trials" are etymologically derived from numeral 'three' but evolved to paucal semantics
- **True trial** (exactly 3): <10 languages, mostly facultative
- **Paucal**: Minimum of 3, not exactly 3 (range typically 3-5 or 3-15)

**Translation Implication**: Genesis 1:26 in Fijian would use **paucal** (minimum of 3, theologically compatible with Trinity) rather than trial (exactly 3).

### External Validation Opportunities (2024 Bible Translations)

**Languages with Grammatical Number Distinctions**:
1. **Fijian** (paucal): Nai Vola Tabu - Vakavakadewa Vou (New Fijian Translation)
2. **Hawaiian** (dual): Ka Baibala Hemolele (2018 edition, modern orthography with ʻOkina and Kahakō)
3. **Slovenian** (obligatory dual): Dalmatinova Biblija (1583)
4. **Tok Pisin** (trial): Nupela Testamen
5. **Samoan** (dual): Test against dual pronouns

**Validation Strategy**: Compare TBTA Position 2 annotations against real Bible translations in these languages to verify translators made same number decisions.

---

## Next Steps

1. **Immediate**: Begin Stage 4 with subagent (test set generation)
2. **Priority**: Include Fijian paucal translations (not trial) in translation database
3. **Critical**: Implement Tier 0 check as Rule 1 in algorithm (Position 2 takes precedence)
4. **Key Focus**: Trinity contexts (Genesis 1:26, baptismal formulas) must achieve 100% accuracy
5. **Validation**: Test against Hawaiian, Fijian, Slovenian Bible translations

---

**Feature Status**: 🟨 Stage 3 (Scholarly Research) - **COMPLETE**

**Next Stage**: Stage 4 (Test Set Generation with Translation Data)

**Last Updated**: 2025-11-16
**Researcher**: Claude Code (Anthropic) - Number System Feature Development Agent
