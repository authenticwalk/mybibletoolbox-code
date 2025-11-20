# LEARNINGS: Methodology for Reproducing TBTA Degree Annotations

## Executive Summary

This document synthesizes research findings into a practical methodology for reproducing TBTA's degree annotation decisions. The degree feature encodes 11 distinct values for adjectives, 8 for adverbs, and 8 for verbs, capturing comparison, intensification, and gradation across languages.

## Core Thesis

**TBTA's degree annotation is a two-layered system:**

1. **Source Language Analysis**: Understanding the morphological and syntactic degree marking in the original Greek/Hebrew
2. **Target Language Mapping**: Identifying how the translation renders degree in the target language

The annotation captures the **target language's expression of degree**, not necessarily a 1:1 mapping of source language forms. This reflects translation reality: a Greek synthetic comparative may become an English analytic comparative, Hebrew periphrastic comparison may become Spanish morphological comparison, etc.

## Foundational Principles

### Principle 1: Degree is Constructional, Not Just Morphological

Degree marking can be expressed through:
- **Morphology**: affixes (-er, -est, -τερος, -issimo)
- **Syntax**: multi-word constructions (more...than, as...as)
- **Lexical items**: separate degree words (very, extremely, μᾶλλον)
- **Context**: implicit comparison (Hebrew construct state)

**Implication**: Annotators must analyze the full construction, not just word forms.

### Principle 2: Part of Speech Determines Available Values

| Feature | Adjectives | Adverbs | Verbs |
|---------|-----------|---------|-------|
| Total values | 11 | 8 | 8 |
| Equality (q) | ✓ | ✗ | ✗ |
| Intensified Comparative (i) | ✓ | ✗ | ✗ |
| Superlative of 2 (s) | ✓ | ✗ | ✗ |
| Intensified (I vs V) | I | V | I |

**Implication**: Know the part of speech before annotating degree.

### Principle 3: Default is "No Degree" (N)

The vast majority of adjectives, adverbs, and verbs carry **N** (No Degree). Marked degree is the exception, not the norm.

**Implication**: Only annotate non-N values when clear morphological, syntactic, or lexical evidence exists.

### Principle 4: Language Typology Informs Expectations

Different language families have different degree-marking strategies:

- **Synthetic languages** (Slavic, Germanic, older Romance): Expect morphological comparison
- **Analytic languages** (Sino-Tibetan, many Niger-Congo): Expect separate degree words
- **Degree-neutral languages** (Motu, Fijian, Washo, Warlpiri): Expect conjoined or implicit comparison
- **Biblical Hebrew**: Always periphrastic (min, construct state)
- **Koine Greek**: Mixed synthetic and analytic

**Implication**: Familiarize yourself with the target language's degree-marking system before annotating.

## Annotation Decision Tree

### For Adjectives

```
START: Is this word an adjective?
│
├─ NO → Wrong part of speech, check again
│
└─ YES → Proceed
   │
   ├─ Does it have comparative morphology or syntax? (-er, more...than, plus...que, etc.)
   │  │
   │  ├─ YES → Is it intensified? (much more, far more, etc.)
   │  │  │
   │  │  ├─ YES → Code: i (Intensified Comparative)
   │  │  └─ NO → Code: C (Comparative)
   │  │
   │  └─ NO → Continue
   │
   ├─ Does it have superlative morphology or syntax? (-est, most, le plus, etc.)
   │  │
   │  ├─ YES → Is comparison explicitly between 2 items?
   │  │  │
   │  │  ├─ YES → Code: s (Superlative of 2 items)
   │  │  └─ NO → Code: S (Superlative)
   │  │
   │  └─ NO → Continue
   │
   ├─ Does it have equative construction? (as...as, aussi...que, tan...como, etc.)
   │  │
   │  ├─ YES → Code: q (Equality)
   │  └─ NO → Continue
   │
   ├─ Does it have downward comparison? (less than, least)
   │  │
   │  ├─ "less than" → Code: L
   │  ├─ "least" → Code: l
   │  └─ NO → Continue
   │
   ├─ Is it modified by intensifier?
   │  │
   │  ├─ Maximum intensifier (extremely, exceedingly, incredibly) → Code: E
   │  ├─ Standard intensifier (very, really, quite) → Code: I
   │  └─ NO → Continue
   │
   ├─ Does it express excessive degree? (too, trop, demasiado, etc.)
   │  │
   │  ├─ YES → Code: T
   │  └─ NO → Continue
   │
   └─ DEFAULT → Code: N (No Degree)
```

### For Adverbs

```
START: Is this word an adverb?
│
├─ NO → Wrong part of speech, check again
│
└─ YES → Proceed
   │
   ├─ Comparative morphology/syntax? → Code: C
   ├─ Superlative morphology/syntax? → Code: S
   ├─ "less than" → Code: L
   ├─ "least" → Code: l
   ├─ Intensifier present?
   │  ├─ Maximum (extremely, etc.) → Code: E
   │  └─ Standard (very, etc.) → Code: V  ← NOTE: V not I!
   ├─ Excessive (too) → Code: T
   └─ DEFAULT → Code: N
```

### For Verbs

```
START: Is this word a verb?
│
├─ NO → Wrong part of speech, check again
│
└─ YES → Proceed
   │
   ├─ Modified by comparative degree adverbial? → Code: C
   ├─ Modified by superlative degree adverbial? → Code: S
   ├─ Modified by "less" → Code: L
   ├─ Modified by "least" → Code: l
   ├─ Modified by intensifier?
   │  ├─ Maximum (extremely, exceedingly) → Code: E
   │  └─ Standard (very, really) → Code: I
   ├─ Excessive (too much) → Code: T
   └─ DEFAULT → Code: N
```

## Source Language-Specific Methodologies

### Greek (Koine/NT) Analysis

#### Step 1: Identify Greek Form

**Synthetic Comparative:**
- Endings: -τερος/-τέρᾱ/-τερον (regular)
- Irregular: -ῑ́ων/-ῑ́ᾱ/-ῐ́ον
- Examples: μείζων (greater), κρείττων (better)

**Synthetic Superlative:**
- Endings: -τατος/-τάτη/-τατον (regular)
- Irregular: -ιστος/-ιστη/-ιστον
- Examples: μέγιστος (greatest)

**Analytic Comparative:**
- μᾶλλον + positive adjective/adverb
- Example: μᾶλλον ἀγαθός (more good)

**Analytic Superlative:**
- μάλιστα + positive adjective/adverb
- Example: μάλιστα ἀγαθός (most good)

**Intensifiers:**
- λίαν (very, exceedingly)
- πάνυ (very much, entirely)
- σφόδρα (greatly, exceedingly)

#### Step 2: Predict Target Language Rendering

**If Greek has synthetic comparative/superlative:**
- Expect target language to render as comparative/superlative (how depends on target language typology)
- English: Usually synthetic for short adjectives, analytic for long
- Romance: Primarily analytic
- Germanic: Primarily synthetic

**If Greek has analytic μᾶλλον/μάλιστα:**
- Often context-specific (participles, compounds)
- Target may use standard comparison forms
- Check for why Greek used analytic (compound adjective? participle? stylistic?)

#### Step 3: Verify Translation Choice

Compare Greek source with target translation:
- Does target preserve degree marking?
- Is degree upgraded/downgraded?
- Is intensive interpretation added?

#### Step 4: Annotate Target

Based on target language form, not Greek form.

### Hebrew Analysis

#### Step 1: Identify Hebrew Construction

**Comparative with מִן (min):**
- Pattern: Adjective + מִן + standard
- Example: גָּדוֹל מִן = "great from" = "greater than"
- Annotate as: C

**Superlative: Construct State (Singular + Plural):**
- Pattern: Singular noun + plural of same noun
- Example: שִׁיר הַשִּׁירִים (Song of Songs)
- Annotate as: S

**Superlative: Construct State (Adjective + Noun):**
- Pattern: Adjective in construct + noun
- Example: "wise of men" = "wisest of men"
- Annotate as: S

**Superlative: Definite Article:**
- Adjective with article in specific contexts
- Often with partitive genitive
- Annotate as: S

**Intensifier מְאֹד (meod):**
- "very" or "greatly"
- Annotate as: I (or E if context suggests extreme)

#### Step 2: Recognize Hebrew Lacks Morphological Comparison

Hebrew never uses affixes for comparison. All comparison is periphrastic or contextual.

**Implication**: If translating FROM Hebrew:
- Source has no comparative morphology
- Target language must supply comparison form
- Translator interprets and renders appropriately

#### Step 3: Verify Translation Choice

Hebrew comparison is often implicit or contextual:
- Does context suggest comparison?
- Did translator make comparison explicit?
- Is superlative construct state rendered as superlative in target?

#### Step 4: Annotate Target

Based on how target language renders the Hebrew construction.

## Challenging Cases and Edge Decisions

### Case 1: Absolute vs. Relative Superlative

**Problem**: Some languages distinguish absolute superlative (elative) from relative superlative.

**Examples**:
- Italian: "bellissima" (elative: extremely beautiful) vs. "la più bella" (relative: the most beautiful)
- Spanish: "muy bueno" or "buenísimo" (elative) vs. "el más bueno" (relative)

**TBTA Decision**:
- If elative (intensive without comparison): Code **E** (Extremely Intensified)
- If relative (actual superlative comparison): Code **S** (Superlative)

**How to Distinguish**:
- Check for definite article (suggests relative)
- Check for comparison set ("of all", "in the group")
- Check for complements or context indicating comparison
- Elatives stand alone; superlatives compare

### Case 2: "Too" vs. "Very"

**Problem**: Distinguishing excessive (T) from intensive (E).

**Examples**:
- "too beautiful" (excessive, negative implicature) → T
- "extremely beautiful" (intensive, positive) → E

**TBTA Decision**:
- Code **T** only when excess/surplus meaning present
- Code **E** for maximum intensification without excess

**How to Distinguish**:
- Does it imply negative consequence or over-sufficiency?
- Could it be paraphrased with "excessively"?
- Is there a following consequence clause? ("too tall to fit")

### Case 3: Comparative of Two vs. Regular Comparative

**Problem**: English distinguishes "taller of the two" from "taller than X".

**Examples**:
- "He is the taller of the two brothers" → s (Superlative of 2 items)
- "He is taller than his brother" → C (Comparative)

**TBTA Decision**:
- Code **s** when explicit binary comparison with superlative syntax
- Code **C** for standard comparative

**How to Distinguish**:
- Look for "of the two" or equivalent
- Check for definite article ("the taller" vs. "taller")
- Context: Are exactly two entities being compared with one selected?

### Case 4: "Much More" / "Far More"

**Problem**: Enhanced comparatives with intensification.

**Examples**:
- "much more beautiful" → i (Intensified Comparative)
- "more beautiful" → C (Comparative)

**TBTA Decision**:
- Code **i** when comparative is itself intensified
- Code **C** for standard comparative

**How to Distinguish**:
- Check for degree adverbial modifying the comparative (much, far, significantly, way)
- "Much/far/way/significantly + comparative" → i
- Bare comparative → C

### Case 5: Positive Form with Comparative Meaning

**Problem**: Some contexts use positive forms with comparative meaning.

**Examples**:
- Latin: "audacior" (braver) but can appear as positive in some constructions
- Hebrew: Adjective alone with מִן implies comparison

**TBTA Decision**:
- Annotate based on **actual construction**, not morphological form
- If construction is comparative (syntax, context), code C
- If form is positive but meaning is comparative due to context, code C

**How to Distinguish**:
- Check for comparison particle/preposition (than, que, מִן)
- Check context for comparison
- Morphology alone is insufficient

### Case 6: Reduplication and Intensification

**Problem**: Some languages use reduplication for intensification.

**Examples**:
- Indonesian: "besar-besar" (very big)
- Hebrew: Repetition for emphasis
- Tagalog: Reduplication patterns

**TBTA Decision**:
- Reduplication for intensification → Code **I** or **E** depending on degree
- Full/complete reduplication suggesting maximum → E
- Partial reduplication or standard intensification → I

### Case 7: Equative vs. Similative

**Problem**: Some languages distinguish equality comparison from similarity.

**Examples**:
- English "as tall as" (equative) vs. "like" (similative)
- French "aussi...que" (equative) vs. "comme" (similative)

**TBTA Decision**:
- True equative (exact equality of degree) → Code **q**
- Similative (likeness/resemblance) → Code **N** (not a degree marking)

**How to Distinguish**:
- Equative: Compares degree on same scale ("as tall as")
- Similative: Compares manner or resemblance ("runs like a deer")
- Only equative receives q code

### Case 8: Contextual Degree Without Overt Marking

**Problem**: Some languages have implicit comparison/intensification.

**Examples**:
- Degree-neutral languages (Motu, Fijian, Washo)
- Conjoined comparison ("This big, that small")
- Contextual superlatives in Hebrew

**TBTA Decision**:
- Annotate based on **target language form**, not source implicature
- If target language has overt marking, code it
- If target language lacks overt marking, code **N**

**Rationale**: TBTA annotates observable linguistic forms, not semantic interpretations.

## Practical Workflow

### Stage 1: Preparation

1. **Identify verse/passage** to annotate
2. **Load source texts** (Greek NT, Hebrew OT)
3. **Load target translation**
4. **Research target language** degree-marking system if unfamiliar

### Stage 2: Source Analysis

**For Greek:**
1. Parse each adjective/adverb
2. Identify degree morphology (comparative/superlative suffixes)
3. Check for analytic μᾶλλον/μάλιστα
4. Note intensifiers (λίαν, πάνυ, σφόδρα)

**For Hebrew:**
1. Identify adjectives
2. Check for מִן constructions
3. Identify construct state patterns
4. Note מְאֹד or other intensifiers
5. Assess contextual comparison

### Stage 3: Target Language Analysis

1. **For each adjective/adverb/verb in target:**
   - Identify morphological form
   - Identify syntactic construction
   - Identify modifying degree words
   - Consult decision tree

2. **Compare with source:**
   - Does degree marking match source?
   - Is there degree upgrade/downgrade?
   - Is translation faithful or interpretive?

### Stage 4: Code Assignment

1. **Apply decision tree** for the part of speech
2. **Consult challenging cases** if uncertain
3. **Default to N** when ambiguous

### Stage 5: Quality Check

1. **Consistency check**: Similar constructions across passage receive same codes
2. **Source fidelity check**: Degree marking reflects source intent
3. **Typological check**: Codes match target language's degree system
4. **Documentation**: Note unusual decisions

## Language-Specific Quick References

### English

| Construction | Code | Example |
|-------------|------|---------|
| -er | C | taller, bigger |
| -est | S | tallest, biggest |
| more...than | C | more beautiful than |
| most | S | most beautiful |
| as...as | q | as tall as |
| very | I | very tall |
| extremely, incredibly | E | extremely tall |
| too | T | too tall |
| less...than | L | less tall than |
| least | l | least tall |
| much/far more | i | much taller |
| -er of the two | s | taller of the two |

### Spanish

| Construction | Code | Example |
|-------------|------|---------|
| más...que | C | más alto que |
| el/la más | S | el más alto |
| tan...como | q | tan alto como |
| muy | I | muy alto |
| sumamente, extremadamente | E | extremadamente alto |
| demasiado | T | demasiado alto |
| menos...que | L | menos alto que |
| el/la menos | l | el menos alto |
| mucho más | i | mucho más alto |
| -ísimo/-ísima | E | altísimo (elative) |

### French

| Construction | Code | Example |
|-------------|------|---------|
| plus...que | C | plus grand que |
| le/la plus | S | le plus grand |
| aussi...que | q | aussi grand que |
| très | I | très grand |
| extrêmement | E | extrêmement grand |
| trop | T | trop grand |
| moins...que | L | moins grand que |
| le/la moins | l | le moins grand |
| beaucoup plus | i | beaucoup plus grand |

### German

| Construction | Code | Example |
|-------------|------|---------|
| -er | C | größer |
| -ste(r/s) | S | größte |
| so...wie | q | so groß wie |
| sehr | I | sehr groß |
| äußerst, extrem | E | äußerst groß |
| zu | T | zu groß |
| weniger...als | L | weniger groß als |
| am wenigsten | l | am wenigsten groß |
| viel/weit -er | i | viel größer |

### Portuguese

| Construction | Code | Example |
|-------------|------|---------|
| mais...que/do que | C | mais alto que |
| o/a mais | S | o mais alto |
| tão...quanto/como | q | tão alto quanto |
| muito | I | muito alto |
| extremamente | E | extremamente alto |
| demasiado | T | demasiado alto |
| menos...que | L | menos alto que |
| o/a menos | l | o menos alto |
| muito mais | i | muito mais alto |
| -íssimo/-íssima | E | altíssimo (elative) |

### Italian

| Construction | Code | Example |
|-------------|------|---------|
| più...di/che | C | più alto di |
| il/la più | S | il più alto |
| così...come, tanto...quanto | q | così alto come |
| molto | I | molto alto |
| estremamente | E | estremamente alto |
| troppo | T | troppo alto |
| meno...di | L | meno alto di |
| il/la meno | l | il meno alto |
| molto più | i | molto più alto |
| -issimo/-issima | E | altissimo (elative) |

## Common Errors and How to Avoid Them

### Error 1: Confusing Source and Target

**Problem**: Annotating Greek comparative as C even when English uses positive form.

**Solution**: Always annotate the **target language form**, not the source.

### Error 2: Missing Analytic Constructions

**Problem**: Only looking for morphological markers (-er, -est), missing "more", "most".

**Solution**: Check for multi-word degree constructions, not just affixes.

### Error 3: Over-annotating Intensifiers

**Problem**: Marking every "very" as I, even when modifying non-gradable predicates.

**Solution**: Only annotate degree when modifying adjectives/adverbs that can be graded.

### Error 4: Ignoring Part of Speech Constraints

**Problem**: Using code 'q' for adverbs (not allowed).

**Solution**: Memorize which codes apply to which parts of speech.

### Error 5: Conflating Similative and Equative

**Problem**: Marking "like" constructions as q (Equality).

**Solution**: Only true degree-equative constructions get q. Similative ≠ equative.

### Error 6: Missing Downward Comparison

**Problem**: Annotating "less...than" as C instead of L.

**Solution**: Check for downward direction (less/least) and use L/l codes.

### Error 7: Defaulting to N Too Quickly

**Problem**: Missing subtle degree marking in unfamiliar languages.

**Solution**: Research target language's degree system; don't assume absence.

### Error 8: Inconsistent Intensifier Grading

**Problem**: Random assignment of I vs. E for intensifiers.

**Solution**: Establish hierarchy: E for maximum (extremely, exceedingly), I for standard (very, quite).

## Advanced: Cross-Linguistic Patterns Recognition

### Pattern 1: Synthetic → Analytic Shift

Many modern languages shift from synthetic to analytic comparison:
- Latin -ior → French plus
- English maintained both tracks
- Modern Greek πιο replaces classical -τερος in many contexts

**Annotation Implication**: Older translations may use more synthetic forms; modern translations more analytic. Code what's actually present.

### Pattern 2: Grammaticalization of Intensifiers

Intensifiers often grammaticalize from content words:
- English "very" < Latin vērus "true"
- French "très" < Latin trāns "across"
- Semantic bleaching over time

**Annotation Implication**: Historical translations may use different intensifiers than modern ones.

### Pattern 3: Superlative = Comparative + Article

Many languages form superlative from comparative + definite article:
- French: plus grand (comp) → le plus grand (superl)
- Spanish: más alto (comp) → el más alto (superl)
- Modern Greek: πιο ψηλός (comp) → ο πιο ψηλός (superl)

**Annotation Implication**: Check for article presence to distinguish C from S.

### Pattern 4: Elative in Romance

Romance languages preserve Latin -issimus as absolute superlative:
- Spanish: -ísimo
- Portuguese: -íssimo
- Italian: -issimo

**Annotation Implication**: Code as E (Extremely Intensified), not S (Superlative).

## Testing Your Annotations

### Self-Check Questions

1. **Have I identified the correct part of speech?**
   - Adjective, adverb, or verb?
   - Does my code match allowed values for this POS?

2. **Have I analyzed the full construction?**
   - Not just the adjective itself, but surrounding words?
   - Multi-word constructions (more...than, as...as)?

3. **Have I checked the source language?**
   - What degree does Greek/Hebrew express?
   - Is target faithful, upgraded, or downgraded?

4. **Have I consulted the decision tree?**
   - Worked through systematically?
   - Not skipped steps?

5. **Have I checked challenging cases?**
   - If uncertain, consulted edge cases section?
   - Applied proper distinction rules?

6. **Is my annotation consistent?**
   - Similar constructions receive similar codes?
   - Patterns across passage make sense?

### Validation Procedures

1. **Peer review**: Have another annotator check your codes
2. **Consistency check**: Run through passage looking for similar constructions
3. **Source alignment**: Verify degree markings align with source intent
4. **Typological check**: Ensure codes match target language grammar
5. **Documentation**: Write notes on unusual decisions

## Future Research Directions

### Questions Remaining

1. **Adverb-specific patterns**: Why does TBTA use 'V' for adverb intensification instead of 'I'?
2. **Verb degree**: How commonly do verbs receive non-N codes? What patterns exist?
3. **Translation variation**: Do different Bible translations show systematic differences in degree rendering?
4. **Diachronic changes**: Do older vs. newer translations differ in degree strategies?

### Areas for Further Investigation

1. **Actual TBTA data sampling**: Access complete TBTA database to find verses with all 11 degree values
2. **Language family coverage**: Systematic analysis of degree in each language family represented
3. **Source-target alignment**: Statistical analysis of Greek/Hebrew → target language mappings
4. **Annotation inter-rater reliability**: Testing consistency across annotators

### Tools to Develop

1. **Degree annotation helper**: Interactive tool implementing decision trees
2. **Language-specific guides**: Detailed references for top 20 Bible translation languages
3. **Pattern database**: Searchable database of constructions → codes
4. **Quality assurance checker**: Automated consistency verification

## Conclusion

TBTA's degree annotation system is sophisticated and cross-linguistically grounded. Successful annotation requires:

1. **Linguistic knowledge**: Understanding degree typology
2. **Source language competence**: Greek and Hebrew degree systems
3. **Target language analysis**: Identifying degree in diverse languages
4. **Systematic methodology**: Following decision trees and validation
5. **Attention to detail**: Distinguishing subtle contrasts

This document provides the foundation. Practical application and continuous refinement will build expertise.

---

**Document Version**: 1.0
**Created**: 2025-11-05
**Author**: Research synthesis by Claude (Sonnet 4.5)
**Status**: Initial methodology thesis - subject to refinement based on actual TBTA data sampling

## Appendix: TBTA Code Reference Table

| Code | Full Name | POS | Description |
|------|-----------|-----|-------------|
| N | No Degree | Adj, Adv, Vrb | Base/positive form |
| C | Comparative | Adj, Adv, Vrb | "more X than Y" |
| S | Superlative | Adj, Adv, Vrb | "most X of all" |
| I | Intensified | Adj, Vrb | "very X", "really X" |
| V | Intensified | Adv | "very X" (adverb-specific) |
| E | Extremely Intensified | Adj, Adv, Vrb | "extremely X", "exceedingly X" |
| T | 'too' | Adj, Adv, Vrb | "too X", excessive degree |
| L | 'less' | Adj, Adv, Vrb | "less X than Y" |
| l | 'least' | Adj, Adv, Vrb | "least X of all" |
| q | Equality | Adj only | "as X as Y" |
| i | Intensified Comparative | Adj only | "much more X than Y" |
| s | Superlative of 2 items | Adj only | "the X-er of the two" |
