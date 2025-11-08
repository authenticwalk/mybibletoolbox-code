# TBTA Strong's Hints Approach

## Core Idea

Instead of annotating TBTA features verse-by-verse, annotate them **Strong's word-by-Strong's word** with translation hints based on cross-linguistic patterns.

### The Proposal

For each Strong's entry (~8,000 Greek/Hebrew words), add TBTA hints that encode patterns like:

```yaml
# Example: Strong's G846 (αὐτός - he/she/it/they)
strongs: G846
gloss: "he, she, it, they, same"
tbta_hints:
  person:
    - pattern: "when Japanese uses 彼ら (karera)"
      hint: "likely 3rd person plural, human"
    - pattern: "when Thai uses เขา (khao)"
      hint: "likely 3rd person singular"
    - pattern: "when Navajo uses different word than regular 3rd"
      hint: "likely 4th person (obviative)"

  number:
    - pattern: "when Samoan uses lāua (dual pronoun)"
      hint: "exactly 2 persons"
    - pattern: "when Hawaiian uses lākou (trial pronoun)"
      hint: "exactly 3 persons"

  surface_realization:
    default: "pronoun"
    note: "Pro-drop languages (Spanish, Japanese) may use zero"
```

### How It Works in Practice

**Step 1: Annotate Strong's Entries (One-Time)**
- Analyze how 900+ translations handle each Strong's word across all its occurrences
- Extract patterns: "Language X uses word Y in context Z → TBTA feature = value"
- Store hints on the Strong's entry

**Step 2: Use Hints for Translation (Per-Verse)**
- Load the verse to be translated
- Load all Strong's entries for words in that verse
- Strong's hints provide guidance based on proven translation patterns
- AI/translator makes final decision based on hints + context

### Key Advantages

1. **Reduced Annotation Workload**
   - ~8,000 Strong's entries vs ~31,000 verses
   - Patterns discovered once, applied many times

2. **Cross-Linguistic Wisdom**
   - Leverage existing translations as evidence
   - "Language family X consistently uses pattern Y for this word"

3. **Cumulative Learning**
   - Hints improve as more translations analyzed
   - Community contributions can refine hints

4. **Context-Aware When Needed**
   - Hints are suggestions, not rigid rules
   - Verse context overrides hints when appropriate

5. **Complementary to Macula**
   - Macula provides morphology/semantics
   - Strong's hints provide cross-linguistic translation patterns

### Example Scenario

**Translating Genesis 4:8 to Navajo (has 3rd vs 4th person distinction):**

```
Verse: "Cain said to Abel his brother, and he rose up and he killed him"
Problem: Which "he" is which? Navajo needs 3rd (subject) vs 4th (different subject)

Strong's Data Available:
- G846 (he) occurrence 1: hints suggest "subject continuation → 3rd person"
- G846 (he) occurrence 2: hints suggest "subject continuation → 3rd person"
- G846 (him) occurrence 3: hints suggest "object, different from subject → 4th person"

Plus Verse Context:
- NounListIndex: Cain=1, Abel=2
- Participant Tracking: Cain=routine subject, Abel=exiting

Combined Result:
- "he rose up" = 3rd person (Cain, subject continuation)
- "he killed" = 3rd person (Cain, still subject)
- "him" = 4th person (Abel, different from subject)
```

---

## Which TBTA Features Would Benefit?

### TIER 1: Strong Lexical Association (Hints are highly effective)

These features are inherent to the word itself and remain relatively stable across contexts:

| Feature | Strong's Benefit | Why It Works | Example |
|---------|-----------------|--------------|---------|
| **Number System** | ★★★★★ Excellent | Pronouns/nouns have inherent number; translations reveal it | G846 (αὐτός) → when Hawaiian uses lākou → trial (3 persons) |
| **Person System** | ★★★★★ Excellent | Pronouns encode person; clusivity visible in translations | G2249 (ἡμεῖς) → when Tagalog uses "kami" → exclusive, "tayo" → inclusive |
| **Proximity** | ★★★★★ Excellent | Demonstratives have spatial/temporal distance encoded | G3778 (οὗτος) → when Japanese uses これ → near speaker |
| **Polarity** | ★★★★☆ Very Good | Some words carry inherent negation | G3756 (οὐ) → always negative polarity |
| **Lexical Sense** | ★★★★★ Excellent | Polysemy is word-specific; translations disambiguate | G3056 (λόγος) → when used for "accounting" vs "speech" vs "Word of God" |
| **Surface Realization** | ★★★★☆ Very Good | Word class relatively stable | G1473 (ἐγώ) → defaults to pronoun, but pro-drop langs use zero |

**Implementation Pattern:**
```yaml
strongs: G2249
gloss: "we"
tbta_hints:
  person:
    baseline: "First person plural"
    clusivity_patterns:
      - context: "divine speech (Trinity addressing Trinity)"
        translations:
          - lang: "tgl"  # Tagalog
            word: "kami"
            hint: "exclusive (Trinity members only)"
      - context: "apostles addressing church"
        translations:
          - lang: "tgl"
            word: "kami"
            hint: "exclusive (apostles, not congregation)"
      - context: "church unity passages"
        translations:
          - lang: "tgl"
            word: "tayo"
            hint: "inclusive (all believers together)"
```

---

### TIER 2: Moderate Lexical Association (Hints provide useful baseline, context refines)

These features have a lexical component but are influenced by context:

| Feature | Strong's Benefit | Why It Works | Limitations |
|---------|------------------|--------------|-------------|
| **Aspect** | ★★★☆☆ Moderate | Verbs have aktionsart (lexical aspect) | Realized aspect depends on context/morphology |
| **Mood** | ★★★☆☆ Moderate | Some words signal modality | Context determines final mood |
| **Degree** | ★★★☆☆ Moderate | Some adjectives/adverbs are comparative/superlative | Degree can be constructional, not just morphological |
| **Reflexivity** | ★★★★☆ Very Good | Reflexive pronouns are lexically marked | Context shows reciprocal vs reflexive |
| **Semantic Role** | ★★★☆☆ Moderate | Verbs have argument structures (agent/patient) | Word order and case morphology matter |

**Implementation Pattern:**
```yaml
strongs: G4160
gloss: "to make, do"
tbta_hints:
  aspect:
    aktionsart: "accomplishment"  # lexical aspect
    note: "Tends toward perfective in completed actions, imperfective in ongoing"
    patterns:
      - context: "creation narrative"
        typical_aspect: "perfective (completive)"
      - context: "habitual actions"
        typical_aspect: "imperfective (habitual)"

  semantic_role:
    typical_frame: "Agent creates Patient"
    agent_patterns:
      - "Subject is typically agent (doer)"
    patient_patterns:
      - "Direct object is typically patient (thing created)"
```

---

### TIER 3: Weak Lexical Association (Hints provide general guidance, heavy context needed)

These features are more discourse/context-dependent than lexical:

| Feature | Strong's Benefit | Why It Works | Limitations |
|---------|------------------|--------------|-------------|
| **Time Granularity** | ★★☆☆☆ Limited | Verbs have default tense, but discourse time varies | "Said" in narrative (historic past) vs "said" in reported speech (may be recent) |
| **Participant Status** | ★★☆☆☆ Limited | Some words signal status (king, servant) | Social relationships are contextual |
| **Usage (Adj)** | ★★☆☆☆ Limited | Adjectives can be attributive/predicative | Syntactic position determines usage |

**Implementation Pattern:**
```yaml
strongs: G3004
gloss: "to say, speak"
tbta_hints:
  time:
    note: "Time granularity is highly context-dependent"
    genre_patterns:
      - genre: "narrative"
        typical_time: "historic past (remote)"
      - genre: "epistle"
        typical_time: "discourse present or recent past"
      - genre: "prophecy"
        typical_time: "prophetic future or prophetic perfect"
```

---

### TIER 4: No Lexical Association (Hints not effective, must annotate verse-level)

These features are entirely discourse/clause-level and cannot be predicted from individual words:

| Feature | Strong's Benefit | Why It Doesn't Work |
|---------|------------------|---------------------|
| **Participant Tracking** | ★☆☆☆☆ None | First mention vs routine vs exiting depends on narrative flow, not the word itself |
| **Noun List Index** | ★☆☆☆☆ None | Which entities are the same across clauses requires discourse analysis |
| **Salience Band** | ★☆☆☆☆ None | Foreground vs background is discourse structure, not word property |
| **Illocutionary Force** | ★☆☆☆☆ None | Declarative vs interrogative is clause-level, though some particles signal it |
| **Speaker Demographics** | ★☆☆☆☆ None | Who is speaking to whom changes verse by verse |
| **Topic NP** | ★☆☆☆☆ None | What is topical depends on information structure, not lexical |
| **Discourse Genre** | ★☆☆☆☆ None | Genre is passage-level, not word-level |
| **Implicit Information** | ★☆☆☆☆ None | What needs to be made explicit varies by context |
| **Alternative Analysis** | ★☆☆☆☆ None | Multiple valid interpretations are contextual |
| **Rhetorical Question** | ★☆☆☆☆ None | Whether a question is rhetorical is pragmatic, not lexical |

---

## Hybrid Approach: Strong's Hints + Verse Context

### Recommended Implementation

**Use Strong's hints for:**
- Number System
- Person System (including clusivity)
- Proximity
- Polarity
- Lexical Sense
- Surface Realization (baseline)
- Aspect (aktionsart baseline)
- Semantic Role (argument structure baseline)

**Use verse-level annotation for:**
- Participant Tracking
- Noun List Index
- Salience Band
- Illocutionary Force
- Speaker Demographics
- Topic NP
- Discourse Genre
- Implicit Information
- Alternative Analysis
- Rhetorical Question

**Use both (hints + context) for:**
- Time Granularity (genre hints + context)
- Mood (lexical modality + context)
- Degree (base form + constructional context)

---

## Benefits Breakdown

### Annotation Effort Reduction

**Strong's Hints Approach:**
- 8,000 Strong's entries × average 30 minutes = 4,000 hours

**Verse-by-Verse Approach:**
- 31,102 verses × average 15 minutes = 7,775 hours

**Hybrid Approach (Recommended):**
- 8,000 Strong's entries for Tier 1-2 features = 2,000 hours
- 31,102 verses for Tier 4 features only = 3,000 hours
- **Total: 5,000 hours (36% reduction)**

### Accuracy Improvements

**Strong's hints provide:**
1. **Cross-linguistic patterns** - "100+ Austronesian translations agree this is inclusive"
2. **Confidence scores** - "85% of ergative languages treat this as agent"
3. **Edge case warnings** - "Watch out: in poetic contexts, this word shifts meaning"

### Example Strong's Entry with Full Hints

```yaml
# Strong's G2249: ἡμεῖς (hēmeis) - "we"
strongs: G2249
lemma: "ἡμεῖς"
gloss: "we"
pos: "personal pronoun"

# TBTA Hints
tbta_hints:
  # Tier 1: Strong lexical association
  number:
    value: "plural"
    confidence: 1.0
    note: "Always plural in Greek"

  person:
    value: "first"
    confidence: 1.0
    clusivity:
      method: "analyze context + translations"
      patterns:
        - context: "divine speech (Trinity)"
          hint: "exclusive"
          evidence:
            - verse: "GEN.1.26"
              translations:
                - {lang: "tgl", word: "kami", meaning: "exclusive"}
                - {lang: "msa", word: "kami", meaning: "exclusive"}
              confidence: 0.95

        - context: "apostles to church"
          hint: "exclusive"
          evidence:
            - verse: "ACT.15.25"
              translations:
                - {lang: "tgl", word: "kami", meaning: "exclusive"}
              confidence: 0.90

        - context: "church unity passages"
          hint: "inclusive"
          evidence:
            - verse: "1CO.12.13"
              translations:
                - {lang: "tgl", word: "tayo", meaning: "inclusive"}
              confidence: 0.85

  surface_realization:
    default: "pronoun"
    variations:
      - lang_family: "Romance/Slavic pro-drop"
        typical: "zero anaphora when topic continuous"
      - lang_family: "Subject-obligatory (English)"
        typical: "must be expressed"

  proximity:
    value: "not_applicable"
    note: "Personal pronoun, not demonstrative"

  polarity:
    value: "affirmative"
    confidence: 1.0

  # Tier 2: Moderate association
  semantic_role:
    typical: "agent"
    note: "First person plural typically appears as subject/agent"
    exceptions:
      - "Can be patient in passive constructions"
      - "Can be experiencer with mental state verbs"

# Cross-Reference Data
usage_stats:
  total_occurrences: 864  # NT occurrences
  clusivity_breakdown:
    exclusive: 412  # estimated
    inclusive: 402   # estimated
    ambiguous: 50

translation_evidence:
  languages_analyzed: 156
  families_with_clusivity:
    - "Austronesian (47 languages)"
    - "Trans-New Guinea (23 languages)"
    - "Algic (8 languages)"

validation:
  last_updated: "2025-11-07"
  verified_by: "cross-linguistic analysis"
  confidence_overall: 0.88
```

---

## Discovery Process: How to Build Hints

### Step 1: Identify Translation Patterns

For each Strong's word:
1. Extract all verses containing that word
2. Load translations in 100+ languages with the target feature
3. Analyze which translation word is used in each context
4. Cluster contexts by translation pattern

**Example: G2249 (we) Clusivity Analysis**

```python
# Pseudo-code for pattern discovery
verses_with_G2249 = get_all_verses("G2249")

for verse in verses_with_G2249:
    tagalog_word = get_translation(verse, "tgl")

    if tagalog_word == "kami":
        contexts_exclusive.append(verse.context)
    elif tagalog_word == "tayo":
        contexts_inclusive.append(verse.context)

# Results:
# "kami" (exclusive) → divine speech, apostolic authority, speaker+others
# "tayo" (inclusive) → church unity, shared experience, speaker+listeners
```

### Step 2: Validate Patterns Across Language Families

Don't rely on one language:
- Check 5+ Austronesian languages for clusivity
- Check 3+ Native American languages
- Check patterns hold across language families

**Example: Validating "Inclusive" Pattern**

```yaml
verse: "1CO.12.13"
greek: "ἡμεῖς πάντες" (we all)
context: "church unity - all baptized into one body"

translations:
  - lang: "tgl"  # Tagalog
    word: "tayo"
    clusivity: "inclusive"

  - lang: "msa"  # Malay
    word: "kita"
    clusivity: "inclusive"

  - lang: "fij"  # Fijian
    word: "keda"
    clusivity: "inclusive"

pattern_confidence: 0.95  # 3/3 agree
```

### Step 3: Encode Hints with Confidence Scores

```yaml
clusivity_hint:
  context: "church unity passages (1CO.12.13, EPH.4.4-6)"
  hint: "inclusive"
  confidence: 0.95
  evidence_count: 8  # languages checked
  agreement: 8/8      # all agree
```

### Step 4: Flag Ambiguous Cases

```yaml
clusivity_hint:
  context: "apostle writing to church (general)"
  hint: "ambiguous - could be exclusive or inclusive"
  confidence: 0.40
  evidence_count: 12
  agreement: 6/12  # split between inclusive/exclusive
  note: "Requires theological interpretation of whether author includes readers"
```

---

## Implementation Roadmap

### Phase 1: Proof of Concept (2-3 weeks)
- [ ] Select 50 high-frequency Strong's words
- [ ] Build hints for Person/Number/Proximity (Tier 1 features)
- [ ] Test on 20 verses across 5 languages
- [ ] Measure accuracy improvement vs. no hints

### Phase 2: Tier 1 Features (6-8 weeks)
- [ ] Build hints for all 8,000 Strong's entries
- [ ] Focus on: Number, Person, Proximity, Polarity, Lexical Sense, Surface Realization
- [ ] Validate across 100+ languages
- [ ] Calculate confidence scores

### Phase 3: Tier 2 Features (4-6 weeks)
- [ ] Add hints for: Aspect (aktionsart), Mood, Semantic Role, Degree
- [ ] Encode context-dependent patterns
- [ ] Build hybrid hint+context decision trees

### Phase 4: Integration (3-4 weeks)
- [ ] Integrate hints into Macula Strong's files
- [ ] Build query interface: "Show me all Trial number instances"
- [ ] Create translation assistant that loads hints with verse
- [ ] Test end-to-end translation workflow

---

## Comparison: Verse-by-Verse vs Strong's Hints

| Aspect | Verse-by-Verse | Strong's Hints | Hybrid |
|--------|----------------|----------------|--------|
| **Annotation Effort** | 7,775 hours | 4,000 hours | 5,000 hours |
| **Best For** | Discourse features | Lexical features | All features |
| **Accuracy** | High (context-aware) | Medium-High (pattern-based) | High (both) |
| **Scalability** | Linear (1 verse = 1 unit) | Logarithmic (1 word = N verses) | Best of both |
| **Community Contribution** | Difficult (needs expertise per verse) | Easier (patterns discoverable) | Balanced |
| **Self-Improving** | Limited | High (more data = better patterns) | High |
| **Coverage** | Complete | Lexical features only | Complete |

---

## Key Insights

### What Makes Strong's Hints Powerful

1. **Leverage Existing Translations**
   - 900+ translations already made the hard decisions
   - Extract patterns: "When language X uses word Y → feature = Z"

2. **Cumulative Knowledge**
   - Each analysis of a Strong's word benefits all verses using that word
   - Community contributions improve hints over time

3. **Cross-Linguistic Validation**
   - If 50 Austronesian languages agree → high confidence
   - If languages disagree → flag as ambiguous, needs human review

4. **Complementary to Macula**
   - Macula: morphology, syntax, semantics (source language)
   - Strong's hints: translation patterns (target languages)
   - Together: comprehensive translation guidance

### Limitations

1. **Not All Features Are Lexical**
   - Participant Tracking, Salience Band, Speaker Demographics are discourse-level
   - These MUST be annotated verse-by-verse

2. **Context Can Override**
   - Even lexical features can shift in unusual contexts
   - Hints are probabilistic, not deterministic

3. **Requires Many Translations**
   - Pattern discovery needs 50-100+ languages with the feature
   - Rare features (e.g., 4th person) have limited evidence

---

## Recommendations

### Use Strong's Hints For (15 features - Tier 1 priority):
1. Number System ★★★★★
2. Person System ★★★★★
3. Proximity ★★★★★
4. Polarity ★★★★☆
5. Lexical Sense ★★★★★
6. Surface Realization ★★★★☆
7. Aspect (aktionsart) ★★★☆☆
8. Mood ★★★☆☆
9. Semantic Role ★★★☆☆
10. Degree ★★★☆☆
11. Reflexivity ★★★★☆

**Total: 15/59 features (25%) highly suitable for Strong's hints**

### Use Verse-Level Annotation For (10 features - Required):
1. Participant Tracking
2. Noun List Index
3. Salience Band
4. Illocutionary Force
5. Speaker Demographics
6. Topic NP
7. Discourse Genre
8. Implicit Information
9. Alternative Analysis
10. Rhetorical Question

### Hybrid Approach (3 features):
1. Time Granularity (genre hints + context)
2. Mood (lexical + context)
3. Semantic Role (argument structure + context)

---

## Next Steps

1. **Validate This Idea**
   - Get feedback from linguists, translators, Bible scholars
   - Test on 10 high-frequency words × 5 languages

2. **Proof of Concept**
   - Build hints for G846 (he/she/it), G2249 (we), G3778 (this)
   - Test accuracy on 20 verses

3. **If Successful, Scale Up**
   - Build hints for all 8,000 Strong's entries
   - Integrate into myBibleToolbox

---

**Status:** Proposal - Needs Validation
**Potential Impact:** 36% reduction in annotation effort for 25% of TBTA features
**Next:** Proof of concept with 3 pronouns (he, we, this)
