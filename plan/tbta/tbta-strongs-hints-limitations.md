# TBTA Strong's Hints: Limitations and Optimal Use Cases

## Executive Summary

While Strong's hints show promise for lexical features (Number, Person, Proximity), this analysis identifies critical limitations and explores when the approach is **not worthwhile** versus when it's **maximally valuable**.

**Key Finding:** Strong's hints work best for **high-frequency, high-variability pronouns** (top 50 words) but show rapidly diminishing returns for lower-frequency or semantically stable words.

---

## When Strong's Hints Are UNHELPFUL

### 1. Low-Frequency Words (The "Long Tail" Problem)

**Problem:** 80% of Strong's entries appear fewer than 50 times in the Bible

| Frequency Band | # of Words | Example | Why Hints Don't Help |
|----------------|-----------|---------|---------------------|
| 1-5 occurrences | ~5,000 words | G0016 ἀγαθοποιΐα (doing good) - 1x | Not enough data to establish patterns |
| 6-20 occurrences | ~2,000 words | G0026 ἀγάπη (love) - rare forms | Limited contexts, patterns unclear |
| 21-50 occurrences | ~500 words | G0037 ἁγιάζω (sanctify) - 29x | Some patterns, but high variance |

**Analysis:**

For G0016 (ἀγαθοποιΐα - "doing good", 1 occurrence in 1 Peter 4:19):
- Only appears once in entire NT
- Cannot establish cross-linguistic patterns
- Hints would be speculation, not evidence-based
- **Better approach:** Annotate the ONE verse directly

**Recommendation:** Only create hints for words with 50+ occurrences

**Impact:** This reduces worthwhile Strong's entries from 8,000 → **~500 words**

---

### 2. Semantically Stable Words (No Cross-Linguistic Variation)

**Problem:** Some words translate the same way in every language

**Examples:**

| Strong's | Gloss | Why Hints Are Useless |
|----------|-------|---------------------|
| G3962 | πατήρ (father) | Every language has "father" - no variation in Number, Person, etc. |
| G1135 | γυνή (woman) | Always singular feminine noun - stable across languages |
| G5207 | υἱός (son) | Always singular masculine - no ambiguity |
| G2250 | ἡμέρα (day) | Temporal noun, stable translation |

**Analysis:**

For G3962 (father):
```yaml
# Useless hints
tbta_hints:
  number: "singular"  # Always singular - obvious
  person: "third"     # Always third person - obvious
  surface_realization: "noun"  # Always a noun - obvious
```

**Why this is unhelpful:**
- Hints don't add value beyond what's obvious from morphology
- No cross-linguistic variation to capture
- Waste of annotation effort

**Recommendation:** Only create hints for words with **documented cross-linguistic variation**

---

### 3. Context-Dominant Words (Lexical Patterns Unreliable)

**Problem:** Some words have patterns that are completely overridden by context

**Example: G3004 λέγω (to say, speak)**

**Attempted Hints:**
```yaml
# G3004: λέγω (say)
tbta_hints:
  time_granularity:
    pattern: "Usually historic past in narrative"
    confidence: 0.60  # LOW - context overrides frequently
    exceptions:
      - "Recent past in reported speech"
      - "Discourse present in dialogue"
      - "Prophetic future in prophecy"
      - "Gnomic present in parables"
```

**Why this fails:**
- Context determines time granularity FAR more than the verb itself
- Hints give false confidence in unreliable patterns
- Better to analyze verse context directly

**Recommendation:** Skip hints for features with <70% pattern consistency

---

### 4. Over-Annotated Common Words (Noise Overwhelms Signal)

**Problem:** Very high-frequency words appear in so many different contexts that hints become unwieldy

**Example: G2532 καί (and)**

G2532 appears **9,161 times** in the NT. Attempted hints would be:

```yaml
# G2532: καί (and, also, even, but)
tbta_hints:
  lexical_sense:
    - sense: "A" (coordinating conjunction "and")
      contexts: [7,000+ occurrences]
    - sense: "B" (emphatic "even")
      contexts: [1,500+ occurrences]
    - sense: "C" (adversative "but")
      contexts: [500+ occurrences]
    - sense: "D" (adjunctive "also")
      contexts: [200+ occurrences]
```

**Why this is unhelpful:**
- Too many occurrences to analyze manually
- Context-dependent sense selection requires verse-level analysis anyway
- Hints would be vague generalities ("usually 'and', sometimes 'even'")

**Recommendation:** Cap hint creation at words with <1,000 occurrences for sense-based features

---

### 5. Features Already Clear from Morphology

**Problem:** Some hints just restate what Macula already provides

**Example: G3756 οὐ (not)**

```yaml
# Redundant with Macula
tbta_hints:
  polarity: "negative"  # Macula morphology already says this
  lexical_sense: "negation"  # Obvious from lemma
```

**Why this is unhelpful:**
- Macula already encodes morphological features
- Strong's hints should add NEW cross-linguistic insights, not duplicate existing data

**Recommendation:** Only create hints that provide **value beyond Macula**

---

## When Strong's Hints Are MOST HELPFUL

### 1. High-Frequency Pronouns (The "Sweet Spot")

**Why These Excel:**
- Appear hundreds/thousands of times → strong patterns emerge
- High cross-linguistic variation (clusivity, number systems, proximity)
- Context patterns are discoverable (divine speech, church unity, etc.)

**Prime Candidates (Top 20):**

| Rank | Strong's | Gloss | NT Occurrences | Hint Value | Features |
|------|----------|-------|----------------|------------|----------|
| 1 | G846 | αὐτός (he/she/it/they) | 5,597 | ★★★★★ | Number, Person, Surface Real |
| 2 | G3588 | ὁ (the) + pronouns | 19,870 | ★★★★☆ | Surface Real (when pronominal) |
| 3 | G2532 | καί (and) | 9,161 | ★★☆☆☆ | Too frequent, context-heavy |
| 4 | G1473 | ἐγώ (I) | 1,802 | ★★★★★ | Person, Surface Real |
| 5 | G3778 | οὗτος (this) | 1,388 | ★★★★★ | Proximity, Number |
| 6 | G4771 | σύ (you sg) | 1,069 | ★★★★☆ | Person, Surface Real |
| 7 | G2249 | ἡμεῖς (we) | 864 | ★★★★★ | Person, Clusivity, Number |
| 8 | G5210 | ὑμεῖς (you pl) | 844 | ★★★★☆ | Person, Number |
| 9 | G1565 | ἐκεῖνος (that) | 265 | ★★★★★ | Proximity, Number |
| 10 | G3745 | ὅσος (as many as) | 110 | ★★★☆☆ | Number (relative) |

**Optimal Range:** 100-5,000 occurrences with high cross-linguistic variation

**Recommendation:** Focus effort on **top 50 pronouns and demonstratives**

---

### 2. Theologically Significant Words with Distinct Senses

**Why These Excel:**
- Clear sense distinctions (abstract vs concrete, divine vs human)
- Theology provides context clustering
- Translations make distinctions visible

**Prime Candidates:**

| Strong's | Word | Senses | Why Hints Help |
|----------|------|--------|----------------|
| G3056 | λόγος (word/Word) | 3+ distinct | "Word" (Jesus) vs "word" (speech) vs "account" |
| G4151 | πνεῦμα (spirit/Spirit) | 2 main | Holy Spirit vs human spirit (often different words) |
| G2889 | κόσμος (world) | 3+ distinct | Creation vs fallen system vs humanity |
| G0932 | βασιλεία (kingdom) | 2 main | Kingdom of God vs earthly kingdoms |
| G0266 | ἁμαρτία (sin) | 2 main | Sin nature vs sins (acts) |

**Example: G3056 λόγος**

```yaml
# High-value hints because senses are CLEARLY distinct
tbta_hints:
  lexical_sense:
    - sense: "Divine Logos (John 1:1, 1:14)"
      translations:
        spanish: "Verbo" (special word!)
        tagalog: "Salita" (capitalized)
        japanese: "ことば" or "言"
      confidence: 0.98

    - sense: "Human speech, word spoken"
      translations:
        spanish: "palabra"
        tagalog: "salita"
        japanese: "言葉"
      confidence: 0.95

    - sense: "Accounting, reckoning, report"
      translations:
        spanish: "cuenta, razón"
        tagalog: "ulat, dahilan"
        japanese: "理由, 言い分"
      confidence: 0.90
```

**Why this is helpful:**
- Senses are theologically distinct
- Translations reliably use different words per sense
- Hints provide clear guidance

---

### 3. Grammatical Words with Systematic Patterns

**Why These Excel:**
- Small set of words (particles, conjunctions)
- Systematic functions
- Cross-linguistic patterns clear

**Prime Candidates:**

| Strong's | Word | Feature | Pattern |
|----------|------|---------|---------|
| G3361 | μή (not - subjunctive) | Polarity | Always negative, prohibitive contexts |
| G2228 | ἤ (or) | Lexical Sense | Alternative vs disjunctive |
| G1063 | γάρ (for, because) | Lexical Sense | Causal vs explanatory |
| G3767 | οὖν (therefore) | Lexical Sense | Inference vs transition |

**Recommendation:** Create hints for all ~100 particles and conjunctions

---

## Diminishing Returns Analysis

### Cost-Benefit by Word Frequency

| Frequency Band | # Words | Hours to Annotate | Value Score | ROI |
|----------------|---------|-------------------|-------------|-----|
| 1,000+ occurrences | ~20 words | 60 hours | ★★★★★ | **Excellent** |
| 100-999 occurrences | ~80 words | 160 hours | ★★★★☆ | **Very Good** |
| 50-99 occurrences | ~200 words | 200 hours | ★★★☆☆ | **Moderate** |
| 20-49 occurrences | ~500 words | 250 hours | ★★☆☆☆ | **Low** |
| 1-19 occurrences | ~7,000 words | 1,000+ hours | ★☆☆☆☆ | **Poor** |

**Recommendation:** Focus on top 300 words (covers 85% of text, 25% of annotation effort)

---

## Output Format Options: Pros and Cons

### Option 1: Simple YAML Hints (Current Proposal)

```yaml
# G2249: ἡμεῖς (we)
tbta_hints:
  person:
    clusivity:
      - context: "divine speech"
        hint: "exclusive"
        confidence: 0.98
```

**Pros:**
- ✅ Simple to parse programmatically
- ✅ Easy to maintain and update
- ✅ Clear confidence scores
- ✅ Machine-readable for AI systems

**Cons:**
- ❌ Lacks decision logic (when to apply which hint)
- ❌ Context descriptions are text, not structured
- ❌ Doesn't capture theological reasoning
- ❌ Hints can conflict (needs prioritization)

**Best For:** Simple features with 1-3 clear patterns

---

### Option 2: Logic Flow Diagram (Decision Tree)

```yaml
# G2249: ἡμεῖς (we) - Decision Tree
tbta_hints:
  person:
    clusivity:
      decision_tree:
        - question: "Is this divine speech (God speaking)?"
          yes:
            - question: "Is God addressing creation?"
              yes: "inclusive"  # GEN.1.26 - us and creation
              no: "exclusive"   # Trinity addressing Trinity
          no:
            - question: "Is speaker addressing listeners directly?"
              yes: "inclusive"  # "we all" passages
              no: "exclusive"   # "we apostles" vs "you readers"
```

**Pros:**
- ✅ Captures decision logic explicitly
- ✅ Helps AI/translator work through ambiguity
- ✅ Can be visualized as flowchart
- ✅ Transparent reasoning process

**Cons:**
- ❌ More complex to create
- ❌ Harder to maintain (multiple paths)
- ❌ Can become unwieldy for complex features
- ❌ Binary questions don't capture uncertainty well

**Best For:** Features with 2-4 clear decision points

---

### Option 3: Theological/Discourse Rules

```yaml
# G2249: ἡμεῖς (we) - Rule-Based
tbta_hints:
  person:
    clusivity:
      rules:
        - id: "trinity-exclusive"
          condition:
            speaker: "God"
            listener: ["Father", "Son", "Holy Spirit"]
            context: "divine council"
          hint: "exclusive"
          confidence: 0.98
          examples: ["GEN.1.26", "GEN.3.22", "GEN.11.7"]

        - id: "apostolic-authority"
          condition:
            speaker: ["apostle", "prophet"]
            listener: "church"
            genre: "epistle"
          hint: "exclusive"
          confidence: 0.90
          examples: ["ACT.15.25", "1TH.1.2"]

        - id: "church-unity"
          condition:
            speaker: "believer"
            listener: "believers"
            theme: ["unity", "baptism", "fellowship"]
          hint: "inclusive"
          confidence: 0.95
          examples: ["1CO.12.13", "EPH.4.4-6"]
```

**Pros:**
- ✅ Captures theological reasoning explicitly
- ✅ Structured conditions (can be evaluated programmatically)
- ✅ Examples provide validation
- ✅ Extensible (can add new rules as discovered)
- ✅ Confidence per rule

**Cons:**
- ❌ Requires theological analysis upfront
- ❌ Rules can overlap or conflict
- ❌ Condition matching requires external data (speaker, genre, theme)
- ❌ More complex to implement

**Best For:** Features with clear theological patterns (Person/Clusivity, Speaker Demographics)

---

### Option 4: Translation Pattern Matrix

```yaml
# G2249: ἡμεῖς (we) - Translation-Based
tbta_hints:
  person:
    clusivity:
      translation_patterns:
        # Pattern 1: Austronesian exclusive
        - languages: ["tgl", "msa", "fij", "haw", "smo"]
          exclusive_word: ["kami", "kami", "keirau", "mākou", "matou"]
          verses_using_exclusive: [
            "GEN.1.26", "GEN.3.22", "ACT.15.25", "1TH.1.2"
          ]

        # Pattern 2: Austronesian inclusive
        - languages: ["tgl", "msa", "fij", "haw", "smo"]
          inclusive_word: ["tayo", "kita", "keimami", "kākou", "tatou"]
          verses_using_inclusive: [
            "1CO.12.13", "EPH.4.4-6", "PHP.2.1-2"
          ]

      inference_method: "If 80%+ of languages with clusivity agree, use that value"
      confidence_formula: "agreement_rate * 0.95"
```

**Pros:**
- ✅ Evidence-based (grounded in actual translations)
- ✅ Can calculate confidence from agreement rate
- ✅ Identifies consensus patterns
- ✅ Flags ambiguous cases (low agreement)
- ✅ Validates hints against real data

**Cons:**
- ❌ Requires access to 50-100 translations
- ❌ Translation quality varies
- ❌ Some languages may have made wrong choice
- ❌ Doesn't capture WHY pattern exists

**Best For:** Validating patterns discovered through other methods

---

### Option 5: Hybrid: Theological Rules + Translation Validation

```yaml
# G2249: ἡμεῖς (we) - HYBRID APPROACH
tbta_hints:
  person:
    clusivity:
      # Step 1: Theological rules (hypothesis)
      rules:
        - id: "trinity-exclusive"
          theological_condition:
            speaker: "God"
            context: "divine council"
          hypothesis: "exclusive"

      # Step 2: Translation validation (evidence)
      validation:
        - rule_id: "trinity-exclusive"
          test_verses: ["GEN.1.26", "GEN.3.22", "GEN.11.7"]
          languages_checked: ["tgl", "msa", "fij", "haw", "smo"]
          results:
            GEN.1.26:
              tgl: "kami" # exclusive - ✓
              msa: "kami" # exclusive - ✓
              fij: "keirau" # exclusive - ✓
              haw: "mākou" # exclusive - ✓
              smo: "matou" # exclusive - ✓
            agreement: 5/5 (100%)
          confidence: 0.98
          status: "VALIDATED"

      # Step 3: Decision logic (application)
      decision_tree:
        - if: "speaker=God AND listener=Trinity"
          then: "exclusive"
          confidence: 0.98
          rule_reference: "trinity-exclusive"
```

**Pros:**
- ✅ Combines theological reasoning with empirical evidence
- ✅ Validates hypotheses against real translations
- ✅ Transparent: shows both theory and evidence
- ✅ Confidence scores grounded in agreement rates
- ✅ Identifies edge cases (low agreement → flag for review)

**Cons:**
- ❌ Most complex to create
- ❌ Requires theological expertise + translation corpus
- ❌ Time-intensive to build

**Best For:** High-value features (Person/Clusivity, Proximity) where investment is worthwhile

---

## Extending Beyond the Word: Context Integration

### Idea: Hints That Reference Verse Context

Instead of standalone hints, create **context-sensitive hints** that load additional data:

```yaml
# G2249: ἡμεῖς (we)
tbta_hints:
  person:
    clusivity:
      # Load verse context
      context_requirements:
        - speaker_demographics  # From verse annotation
        - discourse_participants  # From verse annotation
        - genre  # From passage annotation
        - theological_theme  # From commentary

      # Apply rules using context
      rules:
        - if: "speaker=God AND discourse_participants.includes('Trinity')"
          then: "exclusive"

        - if: "genre=epistle AND speaker=apostle AND theme=church_unity"
          then: "inclusive"

        - if: "speaker IN discourse_participants AND listener IN discourse_participants"
          then: "inclusive"
          else: "exclusive"
```

**Pros:**
- ✅ Leverages verse-level annotations for discourse features
- ✅ Handles complex context dependencies
- ✅ Can incorporate theological insights from commentaries
- ✅ More accurate than word-alone hints

**Cons:**
- ❌ Requires verse-level annotations to exist first (circular dependency)
- ❌ Complex implementation
- ❌ Blurs line between word hints and verse analysis

**Best For:** Hybrid system where some features annotated at verse level, others inferred from hints

---

### Idea: Theological Knowledge Graph

Create structured theological knowledge that hints can reference:

```yaml
# Theological Knowledge Graph
theological_entities:
  - id: "trinity"
    members: ["Father", "Son", "Holy Spirit"]
    characteristics:
      - "three persons, one God"
      - "co-equal, co-eternal"

  - id: "apostolic-band"
    members: ["Paul", "Peter", "John", ...]
    role: "church founders, authoritative teachers"

# Hints reference the graph
# G2249: ἡμεῖς (we)
tbta_hints:
  person:
    clusivity:
      rules:
        - if: "speaker IN theological_entities.trinity.members AND listener IN theological_entities.trinity.members"
          then: "exclusive"
          explanation: "Trinity members addressing each other, not creation"
```

**Pros:**
- ✅ Reusable theological knowledge across all Strong's entries
- ✅ Centralized expertise (update graph, all hints improve)
- ✅ Can incorporate scholarly consensus
- ✅ Extensible (add new entities/relationships)

**Cons:**
- ❌ Requires building comprehensive theological knowledge graph
- ❌ Theological disputes affect hints (whose theology?)
- ❌ Complex maintenance

**Best For:** Long-term vision if building comprehensive Bible knowledge system

---

## Recommended Hybrid Approach

### Tier 1: Simple YAML for Clear Cases (80% of hints)

```yaml
# G3756: οὐ (not)
tbta_hints:
  polarity: "negative"
  confidence: 1.0
```

### Tier 2: Decision Trees for 2-3 Decision Points (15% of hints)

```yaml
# G3778: οὗτος (this)
tbta_hints:
  proximity:
    decision_tree:
      - question: "Is referent physically present with speaker?"
        yes: "near_speaker"
        no:
          - question: "Is referent with listener?"
            yes: "near_listener"
            no: "remote"
```

### Tier 3: Theological Rules + Validation for Complex Cases (5% of hints)

```yaml
# G2249: ἡμεῖς (we)
tbta_hints:
  person:
    clusivity:
      rules: [theological rules as shown above]
      validation: [translation evidence]
      decision_tree: [application logic]
```

---

## Critical Limitations Summary

### When NOT to Create Strong's Hints:

1. **Low-frequency words** (<50 occurrences) - ❌ Not enough data
2. **Semantically stable words** (father, woman, day) - ❌ No variation to capture
3. **Context-dominant features** (Time Granularity, Participant Tracking) - ❌ Word-level hints unreliable
4. **Ultra-high-frequency words** (>5,000 occurrences) with high variance - ❌ Too many contexts
5. **Features already in Macula** (basic morphology) - ❌ Redundant

### When Strong's Hints Excel:

1. **High-frequency pronouns** (100-5,000 occurrences) - ✅ Clear patterns emerge
2. **Theologically significant words** with distinct senses - ✅ Translations distinguish
3. **Grammatical particles** with systematic functions - ✅ Small set, high value
4. **Demonstratives and deictics** - ✅ Cross-linguistic variation high
5. **Features NOT in Macula** (clusivity, proximity) - ✅ Adds new value

---

## Recommendations

### Focus Annotation Effort On:

**Tier 1 (Must-Have):** 50 words
- Top 20 pronouns (he, we, you, this, that)
- Top 10 demonstratives and deictics
- Top 20 particles with grammatical function

**Tier 2 (High Value):** 250 additional words
- High-frequency verbs with clear aktionsart
- Theologically significant nouns (5-10 senses)
- All conjunctions and particles

**Tier 3 (Diminishing Returns):** 500 additional words
- Medium-frequency words (100-500 occurrences)
- Only if clear cross-linguistic variation documented

**SKIP:** 7,000+ low-frequency words
- Better to annotate verses directly
- Insufficient data for reliable hints

### Use Output Format:

- **Simple YAML:** 80% of words (clear, unambiguous patterns)
- **Decision Trees:** 15% of words (2-3 decision points)
- **Theological Rules + Validation:** 5% of words (complex, high-value cases like clusivity)

---

**Status:** Critical Analysis Complete
**Key Finding:** Strong's hints are NOT a silver bullet - focus on top 300 words for 80% of value with 20% of effort
**Next:** Proof of concept with top 10 pronouns only
