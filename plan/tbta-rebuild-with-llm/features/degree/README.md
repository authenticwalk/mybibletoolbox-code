# TBTA Feature: Degree

## Translation Impact

Degree marking determines how languages express comparison ("more than"), superlatives ("most"), and intensification ("very"). Languages vary dramatically: some use synthetic morphology (English "-er/-est", Greek "-τερος/-τατος"), others use analytic constructions (Mandarin "更/最", French "plus/le plus"), while degree-neutral languages (Motu, Fijian, Washo, Warlpiri) lack degree semantics entirely and use conjoined comparison. Without accurate degree annotation, translations will fail to select appropriate comparative forms, misuse intensifiers, or incorrectly apply degree marking in degree-neutral languages, producing unnatural or ungrammatical output across diverse comparison systems.

## Complete Value Enumeration

TBTA encodes degree at different positions by part of speech:

### Adjectives (Position 4) - 11 values

| Code | Meaning | Description |
|------|---------|-------------|
| `N` | No Degree | Positive/base form, unmarked |
| `C` | Comparative | "more X than Y" |
| `S` | Superlative | "most X (of all)" |
| `I` | Intensified | "very X", "extremely X" |
| `E` | Extremely Intensified | "exceedingly X", maximum intensification |
| `T` | 'too' | Excessive degree ("too X") |
| `L` | 'less' | Downward comparison ("less X than Y") |
| `l` | 'least' | Downward superlative ("least X of all") |
| `q` | Equality | Equative comparison ("as X as Y") |
| `i` | Intensified Comparative | "much more X than Y" |
| `s` | Superlative of 2 items | "the X-er of the two" |

### Adverbs (Position 4) - 8 values

Uses: `N`, `C`, `S`, `V` (=Intensified), `E`, `T`, `L`, `l`
(Lacks: `q`, `i`, `s`)

### Verbs (Position 9) - 8 values

Uses: `N`, `C`, `S`, `I`, `E`, `T`, `L`, `l`
(Lacks: `q`, `i`, `s`)

## Baseline Statistics

Expected distribution in Biblical texts (estimates based on degree morphology frequency):

| Code | Estimate | Context |
|------|----------|---------|
| `N` (Unmarked) | ~70% | Base form, no degree marking |
| `C` (Comparative) | ~15% | Explicit comparison constructions |
| `S` (Superlative) | ~5% | Superlative forms (less common than comparative) |
| `I` (Intensified) | ~5% | Intensifiers ("very", μᾶλλον, מְאֹד) |
| `E`, `T`, `L`, `l`, `q`, `i`, `s` | ~5% | Specialized degree marking (combined) |

**Source Language Patterns:**
- Greek NT: Synthetic comparative/superlative common (μείζων, μέγιστος)
- Hebrew OT: No synthetic forms, exclusively periphrastic (מִן construction)
- Epistles: Higher intensification frequency
- Narrative: More base forms, occasional comparative

## Quick Translator Test

**Critical questions to determine degree annotation needs:**

1. **Does your language mark comparative (more X than Y)?**
   - Synthetic: Morphological (English -er, Latin -ior) → Code morphology
   - Analytic: Degree word (English "more", Mandarin 更) → Code degree word
   - Conjoined: Parallel clauses (Amele, Motu) → Degree-neutral
   - None: Context-based (Washo, Fijian) → Degree-neutral

2. **Does your language mark superlative (most X)?**
   - Synthetic: Suffix (English -est, Greek -τατος)
   - Analytic: Degree word (English "most", Mandarin 最)
   - Periphrastic: Construct state (Hebrew)
   - None: Degree-neutral

3. **Is your language degree-based or degree-neutral?**
   - Degree-based: Gradable adjectives introduce degree arguments (most languages)
   - Degree-neutral: No degree semantics, uses conjoined comparison (Motu, Fijian, Washo, Warlpiri)

4. **Does your language have multiple intensifiers?**
   - Many intensifiers: Track levels (I = "very", E = "extremely")
   - Few intensifiers: Simple distinction sufficient
   - Morphological: Reduplication, prefixes, augmentative

5. **What comparison construction type does your language use?**
   - Exceed comparative: Standard NP as object of "exceed" verb (Duala, African)
   - Locational: Standard takes case (Estonian "from", Maasai "to")
   - Conjoined: Parallel clauses (Amele, Australian)
   - Particle: Comparative particle + standard (English "than")

**Critical Indicators:**

- **Degree-neutral languages** → Do NOT use C/S codes, use conjoined comparison
- **Synthetic morphology** → Code forms directly (C for -er, S for -est)
- **Rich intensifier systems** → Distinguish I (general) from E (extreme)
- **Exceed/Locational comparatives** → Pay attention to case/verb, not just degree

## Examples

**Example 1: John 15:13** - Comparative
```yaml
Greek: μείζονα ταύτης ἀγάπην (meizona tautēs agapēn)
English: "Greater love than this"
Degree: C (Comparative)
Reason: Synthetic comparative form μείζων (greater) from μέγας (great)
```

**Example 2: Matthew 22:36** - Superlative
```yaml
Greek: ποία ἐντολὴ μεγάλη (poia entolē megalē)
English: "Which is the greatest commandment?"
Degree: S (Superlative) - if using μεγίστη form
Note: Greek may use positive form contextually for superlative meaning
```

**Example 3: Song of Solomon 1:2** - Comparative (Hebrew)
```yaml
Hebrew: טוֹבִים דֹּדֶיךָ מִיָּיִן (tovim dodeka miYayin)
English: "Your love is better than wine"
Degree: C (Comparative)
Reason: מִן (min) construction creates comparative meaning
```

**Example 4: John 3:29** - Intensified
```yaml
Greek: χαρᾷ χαίρει (chara chairei) - "rejoices with joy"
English: "Greatly rejoices" or "rejoices exceedingly"
Degree: I or E (Intensified)
Reason: Cognate accusative creates intensification
```

**Example 5: 2 Corinthians 4:17** - Intensified Superlative
```yaml
Greek: καθ' ὑπερβολὴν εἰς ὑπερβολὴν (kath hyperbolēn eis hyperbolēn)
English: "Far more exceeding / beyond all comparison"
Degree: E (Extremely Intensified)
Reason: Double hyperbole construction, maximum intensification
```

## Hierarchical Prompt Template (5-Level)

### Level 1: Check for Degree Marking

```
Does this adjective/adverb/verb show degree marking?

Source: [Greek/Hebrew text]
Translation: [English]

Check for:
- Comparative forms (English -er, "more", Greek -τερος, Hebrew מִן)
- Superlative forms (English -est, "most", Greek -τατος, Hebrew construct)
- Intensifiers (very, extremely, Greek λίαν/σφόδρα, Hebrew מְאֹד)
- Excessive markers ("too")
- Equative ("as...as")

Answer: YES or NO
```

**Decision:** NO → `N` (No Degree), STOP | YES → Continue to Level 2

### Level 2: Identify Degree Type

```
What type of degree marking is present?

Options:
A. Comparative: "more X than Y", comparison between entities
B. Superlative: "most X", highest degree in set
C. Intensified: "very X", degree enhancement without comparison
D. Excessive: "too X", beyond acceptable threshold
E. Equative: "as X as Y", equality of degree
F. Downward: "less X" or "least X", inferiority comparison

Source indicators:
- Greek synthetic: -τερος (comp), -τατος (sup), -ῑ́ων (irreg comp)
- Greek analytic: μᾶλλον (more), μάλιστα (most)
- Hebrew: מִן (comparative), construct state (superlative), מְאֹד (very)

Identified type: [A-F]
```

**Decision:** Continue to Level 3 with type

### Level 3: Determine Degree Subtype

```
Refine the degree marking based on context.

For Comparative (A):
- Standard comparative → C
- Intensified comparative ("much more") → i (adjectives only)

For Superlative (B):
- General superlative → S
- Superlative of two items → s (adjectives only)
- Absolute/Elative (no comparison set) → Consider E

For Intensified (C):
- General intensification ("very") → I
- Maximum intensification ("exceedingly") → E

For Excessive (D):
- Excess marking ("too") → T

For Equative (E):
- Equality construction ("as...as") → q (adjectives only)

For Downward (F):
- Comparative of inferiority → L
- Superlative of inferiority → l

Identified code: [Specific TBTA code]
```

### Level 4: Validate Against Source Language

```
Verify degree marking against source language form.

Greek validation:
- Synthetic comparative present? → C
- Synthetic superlative present? → S
- μᾶλλον used? → C (analytic comparative)
- μάλιστα used? → S (analytic superlative)
- Intensifier (λίαν, σφόδρα, πάνυ)? → I or E

Hebrew validation:
- מִן construction present? → C (comparative)
- Construct state pattern? → Check if superlative (S)
- מְאֹד present? → I (intensified)
- Definite article on adjective? → May indicate S

Does source support predicted degree? YES/NO
If NO, revise prediction based on source.
```

### Level 5: Check Target Language Requirements

```
Validate against target language comparison system.

Target language questions:
1. Is target language degree-neutral?
   - If YES, do NOT use C/S codes, use conjoined comparison
2. Does target use synthetic or analytic comparison?
   - Synthetic: Ensure proper morphological form
   - Analytic: Select appropriate degree word
3. Does target have exceed/locational comparative?
   - Adjust case marking and verb choice accordingly
4. Does target distinguish multiple intensifier levels?
   - If YES, apply I vs E distinction
   - If NO, collapse to single intensifier

Final degree code: [Code with justification]
```

## Gateway Features (Correlations)

High-confidence quick predictions:

| Context | Predict | Confidence | Notes |
|---------|---------|------------|-------|
| No degree marking | `N` | 95%+ | Base form, default |
| Greek -τερος/-τέρᾱ/-τερον | `C` | 95%+ | Synthetic comparative |
| Greek -τατος/-τάτη/-τατον | `S` | 95%+ | Synthetic superlative |
| Greek μᾶλλον + adjective | `C` | 90%+ | Analytic comparative |
| Greek μάλιστα + adjective | `S` | 90%+ | Analytic superlative |
| Hebrew מִן + adjective | `C` | 90%+ | Comparative construction |
| Hebrew construct state pattern | `S` | 75%+ | Check context for superlative |
| English "more" + adjective | `C` | 90%+ | Analytic comparative |
| English "most" + adjective | `S` | 90%+ | Analytic superlative |
| English "very" + adjective | `I` | 85%+ | General intensification |
| English "extremely/exceedingly" | `E` | 85%+ | Maximum intensification |
| English "too" + adjective | `T` | 95%+ | Excessive degree |

**Cross-feature correlations:**
- Teaching discourse → Higher intensification (I/E)
- Comparative constructions → Often with "than" particle
- Superlatives → Usually with definite article
- Degree-neutral target → Never use C/S codes

## Common Prediction Errors

### Error 1: Applying Degree to Degree-Neutral Languages (~40% in affected languages)

**Problem:** Using C/S codes for languages lacking degree semantics

**Example:**
- Motu, Fijian, Washo, Warlpiri all lack degree arguments
- Wrong: Code "bigger" as C (Comparative)
- Right: Use conjoined comparison ("X big, Y small")

**Solution:** Check target language typology first, identify degree-neutral languages

### Error 2: Missing Synthetic vs. Analytic Distinction (~15-20% of errors)

**Problem:** Not recognizing morphological degree marking

**Example:**
- Greek μείζων (synthetic comparative) vs. μᾶλλον μέγας (analytic)
- Both mean "greater" but different constructions
- Must code both as C, but construction type matters for target

**Solution:** Check source language morphology, identify synthetic forms

### Error 3: Confusing Intensification Levels (~20% of errors)

**Problem:** Not distinguishing general (I) from extreme (E) intensification

**Example:**
- "Very good" → I (Intensified)
- "Exceedingly good" → E (Extremely Intensified)
- Wrong: Coding both as I
- Right: Use E for maximum intensification

**Solution:** Check intensifier strength (very/quite = I, exceedingly/incredibly = E)

### Error 4: Hebrew Comparative Misidentification (~10-15% in Hebrew texts)

**Problem:** Missing מִן (min) construction for comparative

**Example:**
- טוֹב מִן "good from" = "better than"
- Wrong: Code as N (unmarked)
- Right: Code as C (comparative via מִן construction)

**Solution:** Always check for מִן with adjectives, indicates comparative

### Error 5: Absolute vs. Relative Superlative Confusion (~10% of errors)

**Problem:** Confusing elative (absolute) with superlative (relative)

**Example:**
- Latin/Greek superlative can mean "very X" (elative) or "most X" (superlative)
- "Most holy" (elative = extremely holy) → E
- "Most holy (of all)" (superlative) → S
- Context determines meaning

**Solution:** Check for comparison set; if absent, may be E not S

## Validation Approach

**How to test degree predictions:**

1. **Source Language Validation**
   - Greek: Check for -τερος/-τατος or -ῑ́ων/-ιστος suffixes
   - Greek: Identify μᾶλλον/μάλιστα + adjective
   - Hebrew: Look for מִן construction or construct state
   - Hebrew: Check for מְאֹד (very)

2. **Morphological Analysis**
   - Synthetic forms: Identify affixes directly
   - Analytic forms: Identify degree words
   - Mixed systems: Determine which strategy applies (adjective length, type)

3. **Cross-Feature Validation**
   - Comparative + "than" particle → Confirms C
   - Superlative + definite article → Confirms S
   - Intensifier + no comparison → Confirms I or E
   - Excessive + negative implicature → Confirms T

4. **Target Language Check**
   - Degree-neutral: Never use C/S
   - Synthetic target: Ensure morphological compatibility
   - Analytic target: Verify degree word availability
   - Exceed/Locational: Adjust case and verb selection

5. **Sample Testing**
   - Test 50-100 adjectives/adverbs across genres
   - Compare to TBTA gold standard
   - Calculate error rate by degree type
   - Target: <10% error with methodology

**Error Rate Expectations:**
- Without methodology: 30-40% error rate
- With source checking: <10% error rate
- Degree-neutral languages: 0% if typology checked first

## Detailed Documentation

For comprehensive linguistic analysis, see:
- **[typology.md](typology.md)** - Cross-linguistic comparison systems, WALS data, degree-neutral languages
- **[biblical-languages.md](biblical-languages.md)** - Greek and Hebrew degree systems in detail
- **[constructions.md](constructions.md)** - Comparative, superlative, and intensification constructions

## Summary

Degree is essential for accurate comparison and intensification across diverse languages. TBTA's 11-value system (adjectives) covers synthetic/analytic comparative (C), superlative (S), intensification (I/E), excessive (T), equative (q), and downward comparison (L/l). Critical considerations include degree-neutral languages (Motu, Fijian, Washo) requiring conjoined comparison, synthetic vs. analytic morphology (Greek vs. Mandarin), and Hebrew's exclusively periphrastic system. Validation requires checking source language forms (Greek synthetic forms, Hebrew מִן construction), target language typology (degree-based vs. degree-neutral), and comparison construction types (exceed, locational, conjoined, particle).
