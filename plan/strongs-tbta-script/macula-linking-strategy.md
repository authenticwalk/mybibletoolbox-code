# Macula-TBTA Linking Strategy

## Analysis Date
2025-11-15

## Executive Summary

Macula Greek dataset provides a clean, position-based word-by-word structure with Strong's numbers already assigned. TBTA provides semantic tree structures with English glosses. The key challenge is that **TBTA uses English words and semantic structures** while **Macula uses Greek words with positions**. There is no direct word-position mapping between them.

## Macula Data Structure Overview

### File Metadata
```yaml
source: macula-greek
version: 1.0.0
language: grc
verse: "BOOK C:V"
text: "Full Greek text"
```

### Word Array Structure
Each word in the `words` array contains:

```yaml
- position: 1                    # Sequential position in verse (1-based)
  text: "Ἐν"                     # Surface form (actual Greek text)
  lemma: "ἐν"                    # Dictionary/lexicon form
  normalized: "Ἐν"               # Normalized form
  ids:
    ref: "JHN 1:1!1"             # Unique reference (BOOK C:V!position)
    wordID: "n43001001001"       # Macula word ID (n{book}{chapter}{verse}{word})
  translation:
    gloss: "In [the]"            # English gloss
  morphology:
    class: prep                  # Word class (prep, noun, verb, det, conj, etc.)
    morph: "PREP"                # Morphology code
    # Additional fields vary by class:
    # - Nouns: gender, number, case, type (common/proper)
    # - Verbs: number, person, tense, voice, mood
    # - Adjectives: has_article
  lexical:
    strong: "1722"               # ⭐ Strong's number (string, no G/H prefix)
  semantic:
    semanticDomain: "067002"     # Louw-Nida domain
    ln: "67.33"                  # Louw-Nida reference
  syntax:                        # Optional syntactic role
    role: "vc"                   # e.g., "vc" (verbal copula), "p" (predicate)
```

## Strong's Number Format

### In Macula Files
- **Format**: String of digits only (no G/H prefix)
- **Examples**: `"1722"`, `"746"`, `"3588"`, `"2316"`
- **Storage**: `lexical.strong` field
- **Consistency**: Present for ALL words in the dataset

### Standard Strong's Format
- **Greek**: G{number:04d} → `G1722`, `G0746`, `G3588`, `G2316`
- **Hebrew**: H{number:04d} → `H0430`, `H7225`

### Conversion Required
```python
# Macula → Standard
macula_strong = "1722"
standard_strong = f"G{int(macula_strong):04d}"  # → "G1722"

# Handle edge case: Macula might already have G/H prefix in some tools
if not macula_strong.startswith(('G', 'H')):
    standard_strong = f"G{int(macula_strong):04d}"
```

## Word Identification System

### Primary Identifiers

1. **Position** (Most Reliable for Linking)
   - Sequential 1-based position in verse
   - Simple, predictable, stable
   - **Limitation**: TBTA doesn't have position numbers

2. **Reference ID** (`ids.ref`)
   - Format: `BOOK C:V!position`
   - Example: `JHN 1:1!1`, `MAT 1:1!5`
   - Combines verse and position

3. **Word ID** (`ids.wordID`)
   - Format: `n{book:02d}{chapter:03d}{verse:03d}{word:03d}`
   - Example: `n43001001001` (John 1:1 word 1)
   - Unique across entire NT

### Linguistic Identifiers

4. **Lemma** (`lemma`)
   - Dictionary form of the word
   - Example: `εἰμί` for all forms of "to be"
   - **Issue**: Same lemma appears multiple times in a verse

5. **Surface Text** (`text`)
   - Actual Greek word as it appears
   - Example: `Ἐν`, `ἦν`, `Λόγος`
   - **Issue**: Same word can appear multiple times

## TBTA Data Structure

### Key Characteristics
- **No position numbers**: TBTA uses hierarchical tree structure
- **English-based**: Uses English glosses (Constituent field)
- **Semantic organization**: Words organized by clause/phrase structure, not linear order
- **Multiple clauses per verse**: A single verse has multiple clause trees

### Example from JHN 1:1 TBTA
```yaml
clauses:
- children:
  - children:
    - Constituent: word          # English gloss, not Greek
      Part: Noun
      NounListIndex: '1'
    Part: NP
  - children:
    - Constituent: become
      Part: Verb
    Part: VP
  - children:
    - Constituent: human
      Part: Noun
      NounListIndex: '2'
    Part: NP
  Part: Clause
```

### Critical Observation
TBTA represents **semantic meaning**, not **word-by-word Greek text**. One TBTA clause may:
- Reorder Greek words for English clarity
- Combine multiple Greek words into one concept
- Split one Greek word into multiple English words
- Use different English words for the same Greek lemma

## The Linking Challenge

### Why Direct Mapping Is Difficult

1. **Different Representational Systems**
   - Macula: Linear sequence of Greek words
   - TBTA: Hierarchical semantic tree of English concepts

2. **No Shared Position Index**
   - Macula has `position: 1, 2, 3...`
   - TBTA has `NounListIndex`, `Part`, `Constituent` (English words)

3. **One-to-Many Relationships**
   - One Greek word → Multiple TBTA nodes (e.g., "τὸν Θεόν" → "the" + "God")
   - Multiple Greek words → One TBTA node (e.g., compound expressions)

4. **Word Order Differences**
   - Greek: "ὁ Λόγος ἦν" (the Word was)
   - TBTA restructures for English semantics

### Example Mismatch: JHN 1:1

**Macula** (17 Greek words in order):
1. Ἐν (in) - G1722
2. ἀρχῇ (beginning) - G0746
3. ἦν (was) - G1510
4. ὁ (the) - G3588
5. Λόγος (Word) - G3056
6. καὶ (and) - G2532
...

**TBTA** (Multiple clause trees with English):
- Clause 1: "word" (Noun) + "become" (Verb) + "human" (Noun)
- Clause 2: "word" + "be" + "in" + "beginning"
- Clause 3: "before" + "God" + "create" + "any" + "thing" + ...

The TBTA structure is **semantic interpretation**, not word-for-word mapping.

## Recommended Linking Algorithms

### Option 1: Lemma-Based Matching (Simplest, Less Accurate)

**Approach**: Match TBTA English words to Macula Greek lemmas via translation glosses

**Steps**:
1. Extract all Macula words with their `translation.gloss` and `lexical.strong`
2. For each TBTA Constituent (English word), search Macula glosses
3. Create mapping: `{tbta_word} → [{macula_position, strong_number}]`

**Pros**:
- Simple to implement
- Works for unique words in a verse

**Cons**:
- Many false matches (e.g., "the" appears 4+ times in JHN 1:1)
- Ambiguous for common words (ἦν "was" appears 3 times)
- Glosses are translations, not exact equivalents

**Accuracy**: ~60-70% for content words (nouns/verbs), <30% for function words

### Option 2: NounListIndex Tracking (Moderate Accuracy)

**Approach**: Use TBTA's `NounListIndex` to track specific noun references

**Steps**:
1. Extract all TBTA nouns with `NounListIndex: '1', '2', '3'...`
2. Extract all Macula nouns (where `morphology.class == 'noun'`)
3. Match by order: NounListIndex '1' → first Macula noun, '2' → second, etc.

**Pros**:
- Works well for nouns
- Leverages TBTA's noun tracking system

**Cons**:
- Only covers nouns (~40% of words)
- Doesn't help with verbs, prepositions, articles, conjunctions
- Assumes TBTA noun order matches Macula noun order (may not always be true)

**Accuracy**: ~85-90% for nouns, 0% for other parts of speech

### Option 3: Hybrid Semantic + Position Heuristic (Best Practical Approach)

**Approach**: Combine multiple signals to find best matches

**Algorithm**:
```python
def link_tbta_to_macula(tbta_word, macula_words):
    """
    Match TBTA word to Macula word(s) using multiple signals.

    Returns: List of (position, strong_number, confidence) tuples
    """
    candidates = []

    # Signal 1: Gloss matching (case-insensitive)
    tbta_lower = tbta_word['Constituent'].lower()
    for m in macula_words:
        gloss_lower = m['translation']['gloss'].lower()
        if tbta_lower in gloss_lower or gloss_lower in tbta_lower:
            candidates.append({
                'position': m['position'],
                'strong': m['lexical']['strong'],
                'score': calculate_similarity(tbta_lower, gloss_lower),
                'match_type': 'gloss'
            })

    # Signal 2: Part of speech matching
    tbta_pos = tbta_word.get('Part', '').lower()
    pos_map = {'noun': 'noun', 'verb': 'verb', 'adjective': 'adj',
               'adposition': 'prep', 'conjunction': 'conj'}
    macula_pos = pos_map.get(tbta_pos)

    if macula_pos:
        for m in macula_words:
            if m['morphology']['class'] == macula_pos:
                # Boost score if already in candidates
                for c in candidates:
                    if c['position'] == m['position']:
                        c['score'] *= 1.5

    # Signal 3: NounListIndex for nouns
    if 'NounListIndex' in tbta_word:
        noun_index = int(tbta_word['NounListIndex'])
        noun_positions = [m['position'] for m in macula_words
                         if m['morphology']['class'] == 'noun']
        if noun_index <= len(noun_positions):
            expected_pos = noun_positions[noun_index - 1]
            for c in candidates:
                if c['position'] == expected_pos:
                    c['score'] *= 2.0  # Strong boost

    # Signal 4: Lemma matching (if available in TBTA)
    # This would require adding Greek lemmas to TBTA data

    # Rank by score and return
    candidates.sort(key=lambda x: x['score'], reverse=True)

    # Return top matches with confidence
    results = []
    for c in candidates[:3]:  # Top 3
        confidence = min(c['score'] / 10.0, 1.0)  # Normalize to 0-1
        results.append((c['position'], c['strong'], confidence))

    return results
```

**Pros**:
- Combines multiple signals for better accuracy
- Provides confidence scores
- Can return multiple candidates when ambiguous

**Cons**:
- More complex to implement
- Still not 100% accurate
- Requires tuning of weights/scores

**Expected Accuracy**: ~75-85% overall, higher for content words

### Option 4: Manual Alignment (Gold Standard, Not Scalable)

**Approach**: Manually create alignment files for each verse

**Format**:
```yaml
verse: JHN 1:1
alignments:
- tbta_path: "clauses[0].children[0].children[0]"  # "word" Noun
  macula_positions: [5, 8, 17]  # "Λόγος" appears at positions 5, 8, 17
  primary_strong: "G3056"
- tbta_path: "clauses[1].children[1].children[0]"  # "be" Verb
  macula_positions: [3]
  primary_strong: "G1510"
```

**Pros**:
- 100% accuracy
- Can handle all edge cases
- Serves as training data for ML approaches

**Cons**:
- Extremely time-consuming
- Not scalable to 7,957 verses
- Requires Greek language expertise

### Option 5: Ignore TBTA Word Linking (Pragmatic Alternative)

**Approach**: Don't link at word level; link at verse level only

**Reasoning**:
- TBTA is already verse-scoped
- Strong's data is already available in Macula
- TBTA provides semantic/discourse analysis, not lexical data

**Implementation**:
```python
# In TBTA feature extraction, reference Strong's by verse, not by word
def add_strongs_context(tbta_feature, verse_ref):
    """Add all Strong's numbers from verse as context."""
    macula_data = load_macula(verse_ref)

    # Extract all unique Strong's numbers from verse
    strongs_in_verse = {
        f"G{int(w['lexical']['strong']):04d}": w['lemma']
        for w in macula_data['words']
    }

    # Add to TBTA feature
    tbta_feature['source_language_context'] = {
        'available_strongs': strongs_in_verse,
        'note': 'Verse-level Strong numbers available via Macula dataset'
    }

    return tbta_feature
```

**Pros**:
- Avoids complex/error-prone word-level matching
- Still provides access to Strong's data
- Acknowledges that TBTA and Macula serve different purposes

**Cons**:
- Doesn't create word-specific Strong's links
- Less granular for teaching purposes

## Edge Cases to Handle

### 1. Articles (ὁ, ἡ, τό - G3588)
- **Frequency**: Appears 4+ times in most verses
- **TBTA Treatment**: Often glossed as "-" or omitted
- **Strategy**: Low priority for matching; may skip entirely

### 2. Conjunctions (καὶ - G2532)
- **Frequency**: Appears 2-5 times per verse typically
- **TBTA Treatment**: "and", sometimes implicit/omitted
- **Strategy**: Match by position in clause sequence

### 3. Verbs with Same Lemma (εἰμί - G1510)
- **Frequency**: "was" appears 3 times in JHN 1:1
- **TBTA Variants**: "become", "be", "be" (different senses)
- **Strategy**: Use LexicalSense + context to differentiate

### 4. Compound Expressions
- **Example**: "τὸν Θεόν" (the God) → TBTA may treat as single concept
- **Strategy**: Link to primary content word (noun), note article separately

### 5. Word Order Inversion
- **Example**: Greek "ἦν ὁ Λόγος" vs. TBTA "word was"
- **Strategy**: Don't rely on sequential position matching

### 6. Proper Nouns
- **Example**: Ἰησοῦ (Jesus), Δαυείδ (David)
- **Macula**: `type: proper` in morphology
- **Strategy**: High-confidence matches due to uniqueness

### 7. Particles Without Clear English Equivalent
- **Example**: μέν, δέ (Greek discourse markers)
- **TBTA**: May be omitted or translated as context
- **Strategy**: Mark as "no direct TBTA equivalent"

## Recommended Implementation Strategy

### Phase 1: Verse-Level Context (Immediate)
- Extract all Strong's numbers from Macula for each verse
- Add as reference context to TBTA features
- No word-level linking required
- **Effort**: 1-2 hours
- **Accuracy**: 100% (for verse-level context)

### Phase 2: Noun Linking (Short-term)
- Implement NounListIndex-based matching for nouns
- Provides Strong's for 40-50% of meaningful words
- **Effort**: 4-8 hours
- **Accuracy**: 85-90% for nouns

### Phase 3: Hybrid Algorithm (Medium-term)
- Implement Option 3 (Hybrid Semantic + Position)
- Cover verbs, adjectives, prepositions
- **Effort**: 2-3 days
- **Accuracy**: 75-85% overall

### Phase 4: Manual Review & Refinement (Long-term)
- Review algorithm output for high-frequency verses
- Create override/correction files for important passages
- Train ML model on corrections
- **Effort**: Ongoing
- **Accuracy**: Asymptotically approaching 95%

## File Format Recommendations

### Linking Output Format
```yaml
verse: JHN 1:1
source: tbta-macula-linking
version: 1.0.0
links:
- tbta_constituent: "word"
  tbta_part: Noun
  tbta_noun_index: '1'
  macula_positions: [5, 8, 17]
  strong_numbers:
  - G3056
  lemma: λόγος
  confidence: 0.95
  method: noun_index_match

- tbta_constituent: "be"
  tbta_part: Verb
  tbta_sense: E
  macula_positions: [3]
  strong_numbers:
  - G1510
  lemma: εἰμί
  confidence: 0.80
  method: gloss_match

verse_context:
  all_strongs:
    G1722: ἐν
    G0746: ἀρχή
    G1510: εἰμί
    G3588: ὁ
    G3056: λόγος
    G2532: καί
    G4314: πρός
    G2316: θεός
  total_words: 17
  linked_words: 12
  link_coverage: 0.71
```

## Conclusion

**Best Approach for Initial Implementation**: **Option 5 (Verse-Level Context) + Option 2 (Noun Linking)**

This provides:
1. ✅ Immediate value: All Strong's numbers available per verse
2. ✅ High accuracy: NounListIndex matching is reliable for nouns
3. ✅ Reasonable effort: 1-2 days of development
4. ✅ Extensible: Can add Option 3 later for verbs/other words

**Key Insight**: TBTA and Macula serve complementary purposes. TBTA provides discourse/semantic analysis in English; Macula provides lexical/morphological data in Greek. Linking at verse level honors both purposes while avoiding brittle word-by-word mapping that may not reflect the actual relationship between semantic trees and lexical forms.

## Next Steps

1. **Implement verse-level Strong's extraction** from Macula
2. **Add noun-specific linking** using NounListIndex
3. **Test on sample verses** (JHN 1:1, MAT 1:1, ROM 1:1)
4. **Evaluate accuracy** and refine algorithm
5. **Document linking metadata** in output files
6. **Consider hybrid approach** if noun-only linking is insufficient

## References

- Macula Greek Dataset: https://github.com/Clear-Bible/macula-greek
- TBTA Documentation: `/workspaces/mybibletoolbox-code/bible-study-tools/tbta/`
- Strong's Numbering System: Standard Greek/Hebrew lexicon references
