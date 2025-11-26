# TBTA Label Quality Review: Number Systems Feature

**Date**: 2025-11-26
**Reviewer**: AI Analysis
**Data Sources**:
- train.jsonl (331 curated entries)
- leftovers.jsonl (171,260 entries)
- HIGH-LEVEL-REVIEW.md (baseline testing results)

## Executive Summary

This review examines the quality and consistency of TBTA's number system labels across 171,591 total annotations. While the majority of labels appear sound, we identified **four categories of concerns** that warrant TBTA team review:

1. **Trinity Passage Inconsistency**: Mixed Trial/Plural labeling for identical theological contexts
2. **Quadrial Linguistic Validity**: 180 instances of a grammatically unattested category
3. **Lexicalized Dual Handling**: Inconsistent treatment of Hebrew dual morphology
4. **Paucal Boundary Ambiguity**: Unclear criteria for Paucal vs. Plural distinction

Overall Assessment: **Generally high quality with specific areas requiring clarification**

## Label Distribution

### Train.jsonl (331 entries, stratified sample):
```
Dual        :   98 (29.6%)  - Oversampled for testing
Singular    :   85 (25.7%)
Plural      :   78 (23.6%)
Paucal      :   28 (8.5%)
Trial       :   24 (7.3%)
Quadrial    :   18 (5.4%)
```

### Leftovers.jsonl (171,260 entries, full dataset):
```
Singular    :  113,531 (66.3%)  - Natural distribution
Plural      :   55,477 (32.4%)
Dual        :    1,629 (1.0%)
Trial       :      456 (0.3%)
Quadrial    :      162 (0.1%)
Paucal      :        5 (0.0%)   - Extremely rare
```

**Observation**: The train set is intentionally stratified to oversample rare categories (Dual, Trial, Quadrial, Paucal). In natural distribution, Singular/Plural dominate 98.7% of cases.

## Issue 1: Trinity Passage Inconsistency

### Problem Statement

Trinity passages with identical theological contexts (God using plural pronouns "us/our") receive **inconsistent** number labels across the dataset.

### Evidence

#### GEN.001.026 "Let us make man in our image":
```
Constituent  Label      Count    Observation
God          Trial      3        Majority labeling
God          Singular   1        Inconsistent minority
person       Plural     1        (Not the issue - different constituent)
```

#### GEN.003.022 "Man has become like one of us":
```
Constituent  Label      Count    Observation
God          Trial      1        Consistent with GEN.1.26 majority
God          Singular   1        Still has inconsistency
```

#### GEN.011.007 "Let us go down":
```
Constituent  Label      Count    Observation
Yahweh       Plural     2        DIFFERENT from GEN.1.26!
we           Plural     1        Uses Plural, not Trial
```

#### ISA.006.008 "Who will go for us?":
```
Constituent  Label      Count    Observation
us           Plural     1        Uses Plural, not Trial
```

### Analysis

**Expected Pattern**: All Trinity references (God speaking in plural first person) should use **Trial** to represent the three persons of the Godhead (Father, Son, Holy Spirit). This is theologically critical per the research documentation.

**Actual Pattern**:
- GEN.1.26 "God": Mostly Trial (3/4 instances)
- GEN.3.22 "God": Mixed Trial/Singular (1/1)
- GEN.11.7 "Yahweh/we": **Plural** (not Trial!)
- ISA.6.8 "us": **Plural** (not Trial!)

### Questions for TBTA Team

1. **Is this intentional theological nuance?** Does TBTA distinguish between:
   - Direct Trinity references (GEN.1.26) → Trial
   - Ambiguous plural contexts (GEN.11.7, ISA.6.8) → Plural

2. **Or is this a data quality issue?** Should all these passages consistently use Trial?

3. **What about the Singular label** in GEN.1.26 and GEN.3.22? Is this:
   - A different constituent (e.g., "God" as subject vs. object)?
   - An annotation error?
   - Representing a different theological interpretation?

### Recommendation

**Document the policy clearly**: Either:
- **Option A**: All Trinity contexts → Trial (requires fixing GEN.11.7, ISA.6.8)
- **Option B**: Only explicit "us/our" with clear 3-person context → Trial; ambiguous cases → Plural (requires documentation)

## Issue 2: Quadrial - Linguistically Unattested Category

### Problem Statement

TBTA includes "Quadrial" (exactly 4 entities) as a grammatical number category, but **no natural language has been documented with true grammatical quadrial** (Corbett 2000, cited in research documentation).

### Usage Statistics

- Train.jsonl: 18 instances (5.4% of sample)
- Leftovers.jsonl: 162 instances (0.1% of full dataset)
- **Total: 180 Quadrial labels across entire dataset**

### Sample Cases

All Quadrial instances involve **explicit count of 4**:

| Verse | Constituent | Text Snippet |
|-------|-------------|--------------|
| EXO.025.012 | ring | Moses attach ring **4 leg** ark-of-the-covenant |
| LUK.009.028 | man | **man** go-up mountain to pray (Peter, James, John, Jesus) |
| DAN.003.025 | man | I see **4 man** walking (furnace miracle) |
| EZK.01.006 | wing | each had **4 wing** |
| DAN.008.022 | kingdom | **4 kingdom** arise from nation |

### Analysis

**TBTA's approach is SEMANTIC, not morphological**: The label "Quadrial" means "exactly 4 entities are referenced semantically" rather than "the language has grammatical quadrial morphology."

**This is consistent** with TBTA's documented policy of prioritizing semantic meaning over morphological form (e.g., Hebrew "shamayim" [dual morphology] → labeled Singular because semantically one sky).

### Linguistic Context

From research documentation:
> "Corbett (2000): No natural language has true quadrial; Dual in ~88 languages, Trial in ~172"
> "Greenberg Universal 34: No trial without dual (hierarchical: S < D < T < P)"

The linguistic typology hierarchy is: Singular < Dual < Trial < Paucal < Plural

Quadrial **violates** this universal by skipping from Trial (3) directly to a specific number (4) without Paucal as an intermediary.

### Questions for TBTA Team

1. **Why include Quadrial?** If it's purely semantic (counting contexts with exactly 4 items), why not:
   - Use "Paucal" (few items, 3-10) which IS linguistically attested?
   - Create a separate annotation for "exact count" vs. "grammatical number"?

2. **Utility for translation**: How does Quadrial help translators?
   - No target language will have quadrial morphology to translate into
   - The context already specifies "4 men" or "4 beasts" explicitly

3. **Is this confusing the boundary** between:
   - **Grammatical number** (linguistic categories: S/D/T/p/P)
   - **Numerical reference** (semantic counting: 1, 2, 3, 4, 5, etc.)

### Recommendation

**Three options**:

1. **Keep Quadrial as semantic category** - Document clearly that it's semantic counting, not grammatical morphology
2. **Reclassify as Paucal** - Merge all Quadrial → Paucal (covers 3-10 entities)
3. **Remove Quadrial entirely** - Use Plural for all unspecified counts >3

Our preference: **Option 2 (merge to Paucal)** because:
- Aligns with linguistic typology
- Still preserves "small specific group" meaning
- Reduces complexity (one less rare category to train ML models on)

## Issue 3: Lexicalized Dual Handling

### Problem Statement

Hebrew has grammatical dual morphology (suffix -ayim) for certain nouns, particularly "shamayim" (heavens) and "mayim" (waters). TBTA policy states these **should be marked Singular** when semantically referring to one entity, but the data shows inconsistency.

### Evidence

#### "heaven/heavens" labeling:

**In leftovers.jsonl** (natural Hebrew contexts):
```
GEN.003.015  heaven   Singular  ✓ Correct (lexicalized dual → Singular)
GEN.021.017  heaven   Singular  ✓ Correct
[...hundreds more...]
1KI.022.019  heaven   Singular  ✓ Correct
```

**In train.jsonl** (sample):
```
PSA.019.001  heaven   Plural    ✗ INCONSISTENT
PSA.019.001  heavens  Plural    ✗ INCONSISTENT
```

#### "waters" labeling:

**In leftovers.jsonl** (GEN.1 creation account):
```
GEN.001.002  water    Singular  ✓ Correct (mostly)
GEN.001.006  water    Dual      ✗ One instance marked Dual!
GEN.001.006  water    Singular  ✓ Other instances Singular
GEN.001.007  water    Singular  ✓ Correct (4 instances)
```

### Analysis

**Research documentation states**:
> "Lexicalized duals (Hebrew 'heavens', 'waters') → Marked as Singular (semantically one entity)"
> "Policy: Semantic meaning prioritized over morphological form"

**Actual data**:
- Hundreds of "heaven" instances correctly labeled Singular
- PSA.19.1 has 2 instances labeled **Plural** (inconsistent)
- GEN.1.6 has 1 "water" instance labeled **Dual** (inconsistent)

This appears to be **annotation errors** rather than systematic policy differences.

### Questions for TBTA Team

1. **Are PSA.19.1 and GEN.1.6 errors?** Should they be:
   - PSA.19.1 "heaven/heavens" → Singular
   - GEN.1.6 "water" (one instance) → Singular

2. **Is there context where lexicalized duals SHOULD be marked Dual?** For example:
   - When explicitly contrasting "waters above" vs. "waters below" (GEN.1.6-7)?
   - When the plural morphology is semantically significant?

### Recommendation

**Audit and fix**:
1. Search all instances of "heaven/heavens/water/waters"
2. Verify each follows the "semantic-over-morphological" policy
3. Document any exceptions with clear criteria

## Issue 4: Paucal Boundary Ambiguity

### Problem Statement

The boundary between **Paucal** (few, 3-10 entities) and **Plural** (many entities) is **unclear and inconsistently applied**.

### Evidence from Baseline Testing

From HIGH-LEVEL-REVIEW.md, the **largest error category** (41.7% of all errors) was:
> "LLM labeled Plural when TBTA labeled Paucal"

Examples:
```
LUK.005.019  man     TBTA: Paucal  LLM: Plural  "man could not enter house"
MAT.025.021  thing   TBTA: Paucal  LLM: Plural  "master entrust thing"
LUK.008.013  month   TBTA: Paucal  LLM: Plural  "believe for month"
```

### Paucal Usage Analysis

**Total Paucal cases in train.jsonl: 28**

#### Cases WITH explicit numbers (2 cases, 7.1%):
```
GEN.029.020  day     "7 year seem **day**"          (7 days)
MAT.015.034  fish    "7 loaf and small **fish**"    (small amount)
```

#### Cases WITHOUT explicit numbers (26 cases, 92.9%):
These are **semantic Paucal** - context implies "a few" without stating exact count:

**Time expressions** (9 cases):
```
GEN.018.003  hour    "stay for **hour** with Abraham"
RUT.002.007  minute  "rest for **minute** in shelter"
RUT.001.001  year    "live in Moab for **year**"
2SA.015.020  day     "Ittai come ago **day**"
LUK.008.013  month   "believe for **month**"
DAN.002.016  hour    "wait for **hour**"
```

**People/groups** (12 cases):
```
JOS.010.020  man     "**man** Amorite be able run city"
1SA.004.004  man     "leader send **man** Shiloh"
NEH.002.012  person  "Nehemiah and **person** go during night"
MAT.007.014  person  "only **person** find gate"
LUK.005.002  person  "Jesus see **person** catch fish"
LUK.005.018  man     "**man** carry paralyzed man"
LUK.005.019  man     "**man** could not enter house"
LUK.010.002  worker  "**worker** are few"
```

**Things/objects** (5 cases):
```
EXO.016.017  flake   "gather **flake**" (small amount)
MAT.025.021  thing   "master entrust **thing**"
MRK.008.007  fish    "small **fish**"
LUK.005.003  meter   "move boat **meter** from shore"
```

### Analysis

**TBTA's Paucal criteria appears to be**:
1. Context implies "not many" or "a few"
2. Indefinite plural without large-scale quantification
3. Words like "few", "small", "short time", etc.

**The problem**: This is **highly interpretive** and context-dependent:
- "men carrying paralyzed man" (LUK.5.18) → How many? 2? 4?
- "man could not enter house" (LUK.5.19) → Same men as 5.18?
- "believe for month" (LUK.8.13) → How long is "a while"?

**LLM baseline got this wrong 41.7% of the time** because:
- No clear numeric boundary (is it 3-10? 3-20? "less than a crowd"?)
- Requires deep contextual understanding beyond the snippet
- Depends on narrative knowledge (e.g., 4 men typically carry a stretcher)

### Questions for TBTA Team

1. **What are the Paucal criteria?** Please specify:
   - Numeric range (3-10? 3-20? other?)
   - Contextual clues (words like "few", "small", "short"?)
   - Narrative knowledge (cultural assumptions about group sizes?)

2. **Why is Paucal so rare in leftovers.jsonl** (only 5 instances in 171K entries)?
   - Is it intentionally conservative (only label Paucal when very clear)?
   - Were most Paucal candidates labeled as Plural instead?
   - Is Paucal primarily a NT phenomenon?

3. **How should translators use this distinction?**
   - What target languages have Paucal morphology that would benefit?
   - Is this distinction theologically/semantically significant, or just linguistic precision?

### Recommendation

**Document Paucal policy explicitly** with:
1. **Numeric guidance**: "3-10 entities" or "small countable group"
2. **Keyword list**: "few", "small", "short time", etc. trigger Paucal consideration
3. **Examples**: Positive cases (clear Paucal) and negative cases (should be Plural)
4. **Uncertainty handling**: When unsure → default to Plural (conservative approach)

**Consider**: Given its rarity (0.0% of natural data) and high error rate, evaluate whether Paucal adds sufficient value for ML training. Could it be merged with Plural for practical purposes?

## Issue 5: Additional Edge Cases

### MAT.18.020 - "2 or 3" Ambiguity

**Text**: "For where **two** or three are gathered in my name"
**TBTA Label**: "two" → Plural (!)
**Expected**: Dual (since "two" is explicitly 2)

**Analysis**: The constituent is the word "two" itself, not "people". TBTA labeled it Plural, possibly because:
- It's part of a disjunctive phrase "two **or** three"
- The number is uncertain (could be 2 OR 3)
- Greek δύο (duo) is an adjective/cardinal number, not a noun

**Question**: Should numerals be labeled by their semantic value (two → Dual) or by their grammatical function in the sentence?

### MAT.26.037 - Peter + 2 Sons = 3 Total

**Text**: "Jesus walk-away with Peter and 2 son Zebedee"

**TBTA Labels**:
```
Jesus    Singular
Peter    Singular
son      Dual      (2 sons = James & John)
Zebedee  Singular
```

**Total people**: Peter (1) + 2 sons (2) = 3 people going with Jesus

**Analysis**: TBTA correctly labeled each constituent separately:
- "son" is Dual (exactly 2 sons)
- Total group is not labeled (no "disciple/group" constituent)

**Observation**: This is consistent and correct. The baseline review questioned why this wasn't Trial, but TBTA labeled the **constituent** (2 sons = Dual), not the total group.

### LUK.9.28 - Transfiguration Quadrial

**Text**: "man go-up mountain to pray"
**TBTA Label**: Quadrial (4 men: Peter, James, John, Jesus)

**Analysis**: This is a valid Quadrial case IF we accept Quadrial as a semantic category. The narrative context specifies exactly 4 people ascending the mountain.

**Alternative**: Could be Paucal (small specific group) if Quadrial is removed.

## Summary of Concerns

| Issue | Severity | Instances | Impact on ML | Recommendation |
|-------|----------|-----------|--------------|----------------|
| Trinity Inconsistency | HIGH | ~10 | Low (rare cases) | Clarify & fix policy |
| Quadrial Validity | MEDIUM | 180 | Medium (confuses training) | Merge to Paucal |
| Lexicalized Duals | LOW | ~5 | Very Low | Audit & fix errors |
| Paucal Boundary | HIGH | ~1000s? | **Very High** (41% error rate) | Document criteria clearly |

## Positive Observations

1. **Consistent Dual labeling**: Body parts (hands, feet, eyes) correctly marked Dual when referring to pairs
2. **Majority of Trinity cases use Trial**: GEN.1.26 predominantly labeled Trial (3/4 instances)
3. **Semantic-over-morphological policy generally followed**: "heaven" (Hebrew dual form) mostly labeled Singular
4. **Explicit counts handled well**: "4 beasts", "3 men", "2 sons" correctly identified
5. **Large dataset coverage**: 171K annotations provide robust coverage

## Recommendations for TBTA Team

### Immediate Actions

1. **Review and reconcile Trinity passages**:
   - Decide: Trial or Plural for GEN.11.7, ISA.6.8?
   - Fix inconsistencies in GEN.1.26, GEN.3.22
   - Document the theological reasoning

2. **Document Paucal criteria explicitly**:
   - Numeric range or contextual criteria
   - Example lists (positive and negative cases)
   - Default rules when uncertain

3. **Decide on Quadrial**:
   - Keep and document as semantic (not morphological)
   - OR merge into Paucal
   - OR remove entirely

4. **Audit lexicalized duals**:
   - Fix PSA.19.1 "heavens" → Singular
   - Fix GEN.1.6 "water" inconsistency
   - Search for other instances

### Documentation Improvements

Create a "Number System Annotation Guide" covering:
1. **Morphological vs. Semantic distinction**
2. **Trinity passage policy** (Trial? Plural? Both?)
3. **Lexicalized dual handling** (shamayim, mayim)
4. **Paucal vs. Plural boundary** (with examples)
5. **Quadrial rationale** (if kept)
6. **Edge case decision tree** (collective nouns, numerals, etc.)

### For ML Training

Given the findings, we recommend:

1. **Start with 4-category system**: Singular, Dual, Plural, Trial
   - Merge Quadrial → Paucal (or Plural)
   - Treat Paucal as Plural initially (too rare and ambiguous)

2. **After resolving inconsistencies**, retry with full 6-category system

3. **Stratified sampling**: Ensure Trinity passages appear in all splits (train/validate/test)

## Respectful Closing

This review is offered in a spirit of collaboration and quality improvement. TBTA represents an enormous scholarly effort, and the overall quality is impressive. The issues raised here are:

- **Mostly edge cases** affecting <1% of the dataset
- **Opportunities for clarification** rather than fundamental flaws
- **Expected challenges** in any large-scale annotation project

We recognize that TBTA may have **good reasons** for decisions that appear inconsistent from a purely linguistic typology perspective. We respectfully request clarification on these points to:

1. Train more accurate ML models
2. Help translators understand the distinctions
3. Ensure theological precision in critical passages

Thank you for your consideration.

---

**Files Referenced**:
- `/workspace/bible-study-tools/tbta/features/number-systems/analysis/data/train.jsonl`
- `/workspace/bible-study-tools/tbta/features/number-systems/analysis/data/leftovers.jsonl`
- `/workspace/bible-study-tools/tbta/features/number-systems/analysis/HIGH-LEVEL-REVIEW.md`
- `/workspace/bible-study-tools/tbta/features/number-systems/research/README.md`

**Analysis Methodology**:
- Systematic pattern analysis across 171,591 annotations
- Cross-reference with linguistic typology literature (Corbett 2000)
- Comparison with baseline ML testing results
- Focus on theological significance and translation utility
