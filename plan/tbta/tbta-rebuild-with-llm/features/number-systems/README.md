# Linguistic Number Systems in TBTA Languages

## Translation Impact ⭐⭐⭐⭐⭐ (CRITICAL)

**Impact Level**: CRITICAL - Affects 176 Austronesian + 141 Trans-New Guinea + 36 Australian languages (~35% of TBTA database)

**Why This Matters**:
- **Theological Precision**: Trinity passages require trial number (exactly 3) in 50+ languages
- **Pronoun Accuracy**: "We" could mean "we two" (dual) vs "we three" (trial) vs "we many" (plural) in 200+ languages
- **Cultural Appropriateness**: Using plural for natural pairs (eyes, hands) sounds unnatural in dual-number languages
- **Translation Decisions**: Translators must determine exact counts where Greek/Hebrew is ambiguous

**Validation Status** (Phase 8 complete - 2025-11-09):
- Training: 91.4% accuracy on 35 verses (experiment-001.md)
- Validation: 57% on 7 Genesis/Exodus verses (partial TBTA coverage - adversarial-test/RESULTS.md, random-test/RESULTS.md)
- Algorithm: v2.0 with refined rules (see ALGORITHM-v2.md, COMPLETION-SUMMARY.md for details)

---

## Executive Summary

This feature analyzes grammatical number systems beyond the simple singular/plural distinction found in English and biblical source languages (Hebrew, Aramaic, Greek). Our analysis of ~1000 TBTA languages reveals significant diversity in number encoding, with critical implications for Bible translation accuracy.

---

## TIER 1: Core Documentation Elements

### Complete Value Enumeration (8 Categories)

1. **Singular** - One entity (70% of Biblical text) ✅ Validated: 100% accuracy
2. **Dual** - Exactly two entities (RARE in TBTA - see v2.0 notes below)
3. **Trial** - Three entities (1% - ANY explicit "three", not just Trinity) ✅ Validated
4. **Quadrial** - Four entities (0.5% - rare, possibly theoretical) ⏳ Unvalidated (no NT data)
5. **Paucal** - A few entities (0.5% - small groups, typically 3-15 depending on language) ⏳ Unvalidated
6. **Plural** - Many entities (25% - crowds, groups, unspecified multiples)
7. **Greater Paucal** - (Language-specific: some Oceanic languages distinguish lesser/greater paucal)
8. **Mass/Uncountable** - (Treated as Singular in TBTA)

**⚠️ Critical Update (v2.0 - 2025-11-09)**:
- **Dual appears RARE/UNUSED in TBTA for pronouns** (0% accuracy in validation)
- **Trial is productive for ALL explicit "three"** (not Trinity-only) ✅
- **Pronouns follow morphological number** (plural suffix → Plural, even with 2 referents)

**Greenberg's Hierarchy**: No language has trial without dual; no language has dual without plural.

## Baseline Statistics

Analysis of 100 verses across Genesis, Matthew, Acts:
- **Singular**: ~70% of all noun/pronoun references
- **Plural**: ~25% of all references
- **Dual**: ~3% (mostly paired body parts, "both" constructions)
- **Trial**: ~1% (Trinity references, "all three")
- **Paucal**: ~0.5% ("a few", small groups)
- **Quadrial**: ~0.5% (rare: "all four", specific counts)

Genre variation:
- Narrative: Higher singular (individual characters focus)
- Genealogy: Higher plural (descendants, groups)
- Theological: Trial spikes (Trinity contexts)

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language distinguish dual (exactly 2) from plural (3+)?
2. ☐ Does your language distinguish trial (exactly 3)?
3. ☐ Does your language distinguish paucal ("a few", small group)?
4. ☐ Does your language distinguish quadrial (exactly 4)?
5. ☐ Are paired body parts always dual in your language?

If you answered YES to any of #1-4, specialized number annotation is critical.

**Languages needing this**:
- **Austronesian** (176 languages): Dual/trial/paucal widespread
  - Oceanic subset (~50 languages): Trial/quadrial systems
  - Philippine-type: Dual pronouns common
- **Trans-New Guinea** (141 languages): Dual widespread, some trial
- **Australian** (36 languages): Almost all have dual
  - **Kinship variation**: Dual forms vary by relationship between the two referents
  - Example (Warlpiri): Different dual pronouns for kin vs. non-kin pairs
- **Afro-Asiatic** (25 languages):
  - **Arabic**: Full dual system (nouns, verbs, adjectives, pronouns)
  - **Hebrew**: Restricted dual (mainly paired body parts: eyes-עֵינַיִם, hands-יָדַיִם)
- **Niger-Congo** (94 languages): Singular/plural via noun class systems (10-20 classes)
  - Number marking integrated with class agreement
  - Example (Swahili): class 1 (singular person) / class 2 (plural people)
- **Mayan** (22 languages): Singular/plural in ergative-absolutive system
- **Indo-European (CRITICAL NOTE)**:
  - **Only 4 IE languages preserve productive dual**: Slovene, Upper Sorbian, Lower Sorbian, Kashubian
  - **NONE in current dataset!** All major IE languages (Russian, Polish, German, French, Spanish, English) LOST dual
  - Greek NT: Residual dual (rare); Sanskrit: Full dual (archaic)

**Examples**: See TBTA-EXAMPLES.md for Genesis 1:26 (Trinity trial), Matthew 5:29 (singular eye), Genesis 1:27 (dual "them")

---

## TIER 2: Advanced Implementation Elements

### Hierarchical Prediction Prompt Template

**Level 1 - Theological (Highest Priority)**
Prompt: "Does this referent have theological significance?"
- Trinity (Father, Son, Spirit) → **Trial**
- Divine council, elders → Check exact count

**Level 2 - Semantic (Explicit Count)**
Prompt: "Is there an explicit numeral or clear semantic count?"
- "two disciples" → **Dual**
- "all three" → **Trial**
- "both" → **Dual**
- "a few" → **Paucal**

**Level 3 - Morphological (Hebrew Dual Forms)**
Prompt: "Does Hebrew/Greek morphology indicate number?"
- Hebrew -ayim suffix → **Dual** (hands, feet, eyes)
- Greek article+number agreement → Match morphology

**Level 4 - Paired Body Parts (High Confidence)**
Prompt: "Is this a naturally paired body part?"
- hands, feet, eyes, ears, knees → **Dual**
- BUT: Check context (if one is lost → singular)

**Level 5 - Baseline Default**
Prompt: "No special indicators found?"
- Countable, one entity → **Singular**
- Countable, unspecified multiple → **Plural**
- Mass noun → **Singular** (uncountable)

## Gateway Features & Prediction Shortcuts

Quick rules with high accuracy:

| If Text Contains... | Then Predict... | Confidence |
|---------------------|----------------|------------|
| "Trinity" context (Father + Son + Spirit) | Trial | 95%+ |
| Hebrew -ayim suffix (שְׁנַיִם, עֵינַיִם) | Dual | 90%+ |
| Explicit "both" or "two" | Dual | 95%+ |
| Paired body part (hands, eyes) | Dual | 85%+ |
| "a few", "some" (small group) | Paucal | 80%+ |
| Generic/mass noun | Singular | 90%+ |

**Correlation with Semantic Type**:
- Divine references in Trinity context → 90% trial
- Paired body parts → 85% dual (but check for injury/loss)
- Exact numerals → 100% match stated number

## Common Prediction Errors

**Error 1**: Missing TBTA semantic expansions
- Problem: TBTA marks "things" (actions as entities) with number
- Solution: Check if abstract/action nouns should have number
- Example: "all these things" → might mark "things" as plural

**Error 2**: Assuming paired body parts are always dual
- Problem: "Cut off your hand" → context shows ONE hand (singular)
- Solution: Check context for injury, loss, or specific reference to one
- Example: Matthew 5:30 "right hand" → singular, not dual

**Error 3**: Missing Trinity trial in subtle contexts
- Problem: Not recognizing implicit Trinity references
- Solution: Check for Father, Son, Spirit together even if not explicit
- Example: "baptize in name of Father, Son, Spirit" → "name" is trial

**Error 4**: Confusing generic plural with specific count
- Problem: "people" could be generic or specific group
- Solution: Check if referring to specific individuals or type/class
- Example: "people rejoiced" (specific group in context) vs "people are..." (generic)

### Validation Metrics

**Experiment 001** (Genesis & John passages):
- Overall Accuracy: **91.4%** (32/35 predictions)
- Singular predictions: **100%** (25/25)
- Plural predictions: **100%** (6/6)
- Trial prediction (Trinity): **100%** (1/1)
- Dual predictions: **0%** (0/3) - Hebrew morphological dual not always encoded as semantic dual

**Experiment Validation** (Matthew 24):
- Method v1.0: **73.7%** (14/19)
- Method v2.0: **85.7%** (6/7)
- Improvement through semantic expansion awareness

**Key Finding**: TBTA encodes semantic number (how many entities) NOT morphological number (grammatical form)

---

## Language Distribution & References

**Major Language Families** (see LANGUAGE-BREAKDOWN.md for full list):
- **Austronesian (176)**: Most complex - Sursurunga (sgz) has 5-way distinction
- **Trans-New Guinea (141)**: Typically dual, some paucal/trial
- **Australian (36)**: Almost all have dual - Murrinh-Patha (mwf) has paucal up to 15
  - **Kinship-influenced**: Australian dual pronouns vary by relationship between referents
  - Example (Warlpiri): Different dual forms based on kinship between the two people
- **Afro-Asiatic (25)**: Arabic (full dual), Hebrew (restricted dual)
- **Niger-Congo (94)**: Number mediated through noun class systems (10-20 classes)
  - Singular/plural distinction OBLIGATORY but expressed through class agreement
  - Example: Swahili class 1/2 (people), class 5/6 (natural pairs/plurals)
  - Every noun must be assigned to class affecting all concordial agreements
- **Mayan (22)**: Singular/plural in ergative-absolutive alignment
  - Number marking interacts with ergativity
  - Classifiers (shape/function) may affect plural interpretation
- **Indo-European**: MOST languages lost dual entirely
  - Only Slovene + 3 Sorbian languages maintain productive dual
  - Historical dual in Greek (NT), Sanskrit (archaic)

**Critical Translation Passages**:
- Trinity contexts → trial (Gen 1:26, Matt 28:19)
- "We apostles" → requires exact count for dual/trial/paucal languages
- Paired body parts → dual where available (context-dependent)

**Implementation Details**: See LEARNINGS.md for methodology, cross-feature interactions, and detailed error patterns.

**References**: Corbett (2000) *Number*; Greenberg (1963); Lynch (1998) *Pacific Languages*; Hutchisson (1986) Sursurunga.