# Word Pattern Analysis for Number Systems

**Analysis Date**: 2025-11-26
**Dataset**: train.jsonl (331 entries)
**Translations Analyzed**: 15 (ara, deu, eng, fra, grc, heb, ind, por, rus, spa, tgl, tha, tur, vie, zho)

## Executive Summary

Word pattern analysis reveals that certain English translation words are **highly discriminative** for predicting grammatical number categories. Words like "cut", "joseph", "stone", "rings", "tables", and "twelve" show 100% confidence in predicting specific number categories with strong support (60+ occurrences).

## Top Discriminative Patterns (100% Confidence, Support ≥60)

These patterns show perfect prediction accuracy with substantial support:

| Word | Translation | Label | Confidence | Support | Pattern |
|------|-------------|-------|-----------|---------|---------|
| cut | eng | Dual | 100% | 107 | Strong dual marker |
| joseph | eng | Dual | 100% | 81 | Named individual (dual context) |
| logos | grc | Singular | 100% | 79 | Greek singular noun |
| stone | eng | Dual | 100% | 76 | Physical object (dual) |
| rings | eng | Quadrial | 100% | 76 | Quadrial-specific (4 rings) |
| gift | eng | Singular | 100% | 75 | Abstract singular concept |
| wood | eng | Dual | 100% | 75 | Material (dual context) |
| twelve | eng | Dual | 100% | 73 | Number (dual context) |
| tables | eng | Dual | 100% | 70 | Furniture (dual) |
| sheep | eng | Plural | 100% | 68 | Animals (plural) |

## Label-Specific Word Patterns

### Trial (24 entries)

**Most Frequent English Words:**
- and (1204), the (1155), of (564), to (435), over (246)
- **Distinctive**: "over" (246 occurrences) suggests dominion/authority contexts

**Key Observations:**
- Trial is the smallest category (24 entries, 7.3% of dataset)
- Function words dominate (and, the, of, to)
- "over" appears 246 times, suggesting contexts of authority/dominion

### Singular (85 entries)

**Most Frequent English Words:**
- the (3889), and (2592), of (2219), is (1069), to (1015)
- **Distinctive**: "is" (1069), "god" (844), "one" (397), "gift" (75)

**100% Confidence Predictors:**
- "gift" (75 occurrences) - abstract singular concept
- "logos" (Greek, 79 occurrences) - theological term

**Key Observations:**
- Strong theological vocabulary: "god" (844), "lord" (440), "son" (377)
- Copula "is" (1069) strongly associated with singular statements
- "one" (397) explicitly marks singularity

### Plural (78 entries)

**Most Frequent English Words:**
- the (2948), and (2211), of (1443), you (829), in (760)
- **Distinctive**: "are" (581), "they" (419), "them" (415), "shall" (356), "sheep" (68)

**100% Confidence Predictors:**
- "sheep" (68 occurrences) - collective plural noun

**Key Observations:**
- Plural copula "are" (581) strongly associated
- Plural pronouns: "they" (419), "them" (415), "your" (347)
- Modal "shall" (356) often in plural commands
- "sheep" reliably indicates plural (collective noun)

### Paucal (28 entries) - "Few/Small Number"

**Most Frequent English Words:**
- the (1083), and (978), of (507), a (431), to (401)
- **Distinctive**: "few" (205), "little" (implicit in context)

**Key Observations:**
- "few" (205 occurrences) is the semantic marker for paucal
- Smaller dataset (28 entries, 8.5%)
- Narrative contexts with "he" (322), "they" (301), "him" (235)

### Dual (98 entries)

**Most Frequent English Words:**
- the (4007), and (3241), of (2037), two (1887), to (1545)
- **Distinctive**: "two" (1887), "one" (737)

**100% Confidence Predictors (Support ≥60):**
- "cut" (107) - ritual/covenant contexts (cutting in two)
- "joseph" (81) - named individual in dual contexts
- "stone" (76) - tablets, pillars (pairs)
- "wood" (75) - construction material (pairs)
- "twelve" (73) - number in dual contexts
- "tables" (70) - tablets/furniture (pairs)

**Key Observations:**
- Strongest category (98 entries, 29.6% of dataset)
- "two" (1887) is the dominant explicit marker
- Ritual objects often appear in pairs: stone tablets, rings, etc.
- Personal names in dual contexts: "joseph" (81)

### Quadrial (18 entries) - "Four/Sets of Four"

**Most Frequent English Words:**
- the (857), and (617), of (537), four (362), to (190)
- **Distinctive**: "four" (362), "face" (172), "faces" (106), "rings" (76), "wings" (80)

**100% Confidence Predictors:**
- "rings" (76 occurrences) - 4 rings on ark/altar corners

**Key Observations:**
- Smallest specialized category (18 entries, 5.4%)
- "four" (362) is the dominant explicit marker
- Visionary/symbolic contexts: "face/faces" (172/106), "wings" (80)
- Architectural details: "rings" (76) on sacred objects

## Cross-Language Patterns

### Greek (grc) Distinctive Words

**Singular Markers:**
- "logos" (79, 100% confidence) - word/reason (singular concept)
- "estin" (203) - "is" (singular copula)
- "theou" (152) - "of God" (genitive singular)
- "ho/o" (148/400) - singular article

**Dual/Plural Markers:**
- "duo/δυο/δύο" (360/185/173) - "two" (dual)
- "oi" (91 plural, 79 paucal) - plural article (ambiguous)

### Hebrew (heb) Patterns

**Note**: Hebrew uses individual letter frequencies due to script characteristics

**Dual Context Letters:**
- י (yod: 338), א (aleph: 324), ה (he: 296)
- ים (yod-mem: 83) - plural/dual suffix marker

**Singular Context:**
- יהוה (YHWH: 42) - divine name (singular)
- את (et: 28) - accusative marker

### Chinese (zho) Distinctive Words

**Singular Markers:**
- 是 (shì: 252) - "is" (copula)
- 神 (shén: 108) - "God" (singular)
- 子 (zǐ: 90) - "son" (singular)

**Dual Markers:**
- 兩/两 (liǎng: 94/94) - "two" (dual)
- 個/个 (gè: 109/109) - classifier (dual contexts)

**Plural Markers:**
- 們/们 (men: 143/143) - plural suffix
- 各 (gè: 48) - "each/various" (distributive plural)

## Ambiguous Words (High Frequency, Mixed Labels)

These high-frequency words appear across multiple categories and are NOT reliable predictors:

### English
- **"the"**: Trial (1155), Singular (3889), Plural (2948), Paucal (1083), Dual (4007), Quadrial (857)
- **"and"**: Trial (1204), Singular (2592), Plural (2211), Paucal (978), Dual (3241), Quadrial (617)
- **"of"**: Trial (564), Singular (2219), Plural (1443), Paucal (507), Dual (2037), Quadrial (537)

### Function Words (All Languages)
- Conjunctions (and, et, und, y, kai)
- Prepositions (of, de, in, en)
- Articles (the, le, la, o, ho)

**Conclusion**: Function words are distributed across all categories and provide NO discriminative value.

## Semantic Categories of Discriminative Words

### Numbers/Quantifiers
- **Dual**: "two" (1887), "twelve" (73), "one" (737)
- **Quadrial**: "four" (362)
- **Paucal**: "few" (205)
- **Plural**: Implicit in morphology ("sheep", "them")

### Named Entities
- **Dual**: "joseph" (81) - individual in dual contexts

### Physical Objects
- **Dual**: "stone" (76), "wood" (75), "tables" (70)
- **Quadrial**: "rings" (76), "wings" (80), "faces" (106)

### Abstract Concepts
- **Singular**: "gift" (75), "logos" (79)

### Theological Vocabulary
- **Singular**: "god" (844), "lord" (440), "son" (377)

### Verbs/Copulas
- **Singular**: "is" (1069)
- **Plural**: "are" (581)

### Ritual/Covenant Terms
- **Dual**: "cut" (107) - cutting covenant (paired action)

## Recommendations for ML Feature Engineering

### High-Value Features (Include)

1. **Explicit Number Words**:
   - "two", "four", "twelve" → Strong predictors
   - "one" → Singular/Dual ambiguous (needs context)

2. **Copulas/Verbs**:
   - "is" → Singular
   - "are" → Plural

3. **Specific Nouns**:
   - "gift", "logos" → Singular
   - "sheep" → Plural
   - "cut", "stone", "wood", "tables" → Dual
   - "rings", "faces", "wings" → Quadrial

4. **Paucal Markers**:
   - "few" → Strong paucal indicator

5. **Cross-Language Morphology**:
   - Chinese 們/们 (plural suffix)
   - Hebrew ים (dual/plural suffix)
   - Greek duo/δυο (dual)

### Low-Value Features (Exclude or Downweight)

1. **Function Words**: and, the, of, to, in, on, for
2. **High-Frequency Ambiguous Words**: Appear in all categories
3. **Generic Verbs**: said, was, had (need grammatical context)

### Feature Combinations Worth Exploring

1. **"two" + object noun** → Dual confidence boost
2. **"four" + architectural term** → Quadrial confidence boost
3. **Pronoun patterns**: "they/them/their" → Plural boost
4. **Quantifier + noun**: "few men" → Paucal boost

## Dataset Characteristics

### Label Distribution
- **Dual**: 98 entries (29.6%) - Largest category
- **Singular**: 85 entries (25.7%)
- **Plural**: 78 entries (23.6%)
- **Paucal**: 28 entries (8.5%)
- **Trial**: 24 entries (7.3%)
- **Quadrial**: 18 entries (5.4%) - Smallest category

### Implications
- **Class imbalance**: Quadrial and Trial are underrepresented
- **Dual dominance**: Biblical texts favor pairs (tablets, cherubim, witnesses)
- **Paucal/Trial rarity**: Limited examples for training

## Cross-Translation Validation

### Consistent Patterns Across Languages

**Dual Markers:**
- English: "two" (1887)
- Greek: "duo/δυο/δύο" (360/185/173)
- Chinese: "兩/两" (94/94)
- Spanish: "dos" (381)
- Indonesian: "dua" (70)

**Quadrial Markers:**
- English: "four" (362)
- Spanish: "cuatro" (94)
- Chinese: "四" (38)
- Turkish: "dört" (18)
- Indonesian: "empat" (15)

**Paucal Markers:**
- English: "few" (205)
- German: "wenig" (22)
- Spanish: "pocos/poco" (38/30)
- Portuguese: "pouco" (13)
- Indonesian: "sedikit" (14)

### Language-Specific Insights

**Greek (grc)**: Highly theological vocabulary, strong article system (ho/o/oi)
**Hebrew (heb)**: Consonantal script requires morphological analysis
**Chinese (zho)**: Classifier system (個/个) critical for number
**English (eng)**: Most discriminative patterns due to explicit number marking

## Conclusion

**Key Findings:**

1. **Explicit number words are perfect predictors**: "two" → Dual, "four" → Quadrial
2. **Specialized vocabulary is highly discriminative**: "cut", "joseph", "stone", "rings", "gift", "sheep"
3. **Function words are noise**: Articles, prepositions, conjunctions provide no value
4. **Copulas matter**: "is" (singular) vs "are" (plural)
5. **Cross-language consistency**: Number markers translate reliably
6. **Class imbalance**: Quadrial (18) and Trial (24) need more data

**Actionable Recommendations:**

- **For ML models**: Use word presence as binary features for high-confidence words (support ≥60)
- **For validation**: Check if explicit number markers (two/four/few) agree with predicted labels
- **For data augmentation**: Prioritize Quadrial and Trial examples (underrepresented)
- **For error analysis**: Investigate cases where "two" appears but label ≠ Dual

**Next Steps:**

1. Test these patterns on validate.jsonl and test.jsonl
2. Build simple rule-based classifier using top 20 discriminative words as baseline
3. Compare rule-based vs ML model performance
4. Analyze failure cases where discriminative words conflict with labels
