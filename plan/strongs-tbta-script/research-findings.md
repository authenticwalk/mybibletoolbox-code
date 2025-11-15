# TBTA Integration Research Findings

**Research Date:** 2025-11-15
**Researcher:** Research Agent (Swarm Session: swarm-1763231263160-lofxak0z8)
**Objective:** Analyze TBTA structure and determine linking strategy to Strong's numbers

---

## Executive Summary

**Key Finding:** TBTA data can be linked to Strong's numbers through Macula source text data, which provides word-level Strong's numbers for each position in Greek/Hebrew text.

**Recommended Approach:**
1. Use Macula as the linking layer (contains both Strong's numbers and word positions)
2. Extract TBTA word-level attributes (Part, Person, Number, etc.) from JSON/XML
3. Create aggregated Strong's enrichment showing patterns across all occurrences

**Complexity:** Medium - Requires three-way join (TBTA → Macula → Strong's) but data structures are well-defined

---

## 1. TBTA Data Structure

### 1.1 File Organization

**TBTA GitHub Repository:** https://github.com/AllTheWord/tbta_db_export

**File Naming Convention:**
```
{book:02d}_{chapter:03d}_{verse:03d}_{BookName}.json
{book:02d}_{chapter:03d}_{verse:03d}_{BookName}.xml

Examples:
- 00_001_001_Genesis.json (Genesis 1:1 in JSON format)
- 00_001_001_Genesis.xml  (Genesis 1:1 in XML format)
```

**Coverage:** 11,649 verses across 34 books (~37% of Bible)
- Focus: Narrative and discourse-heavy books (OT pentateuch, historical books, Gospels, Acts)
- Not covered: Most epistles, poetry, prophets (see `tbta-source/COVERAGE.md`)

### 1.2 Data Schema (JSON Format)

**Hierarchical Structure:**
```json
[
  {
    "Part": "Clause",
    "Children": [
      {
        "Part": "NP",  // Noun Phrase
        "Children": [
          {
            "Part": "Noun",
            "Constituent": "God",
            "LexicalSense": "A",
            "NounListIndex": "1",
            "SemanticComplexityLevel": "1",
            "Number": "Singular",
            "Person": "Third",
            "Polarity": "Affirmative",
            "Participant Tracking": "Routine",
            "Surface Realization": "Noun"
          }
        ]
      },
      {
        "Part": "VP",  // Verb Phrase
        "Children": [...]
      }
    ],
    "Discourse Genre": "Climactic Narrative Story",
    "Illocutionary Force": "Declarative",
    "Topic NP": "Most Agent-like"
  }
]
```

**Key Attributes (59 TBTA Features):**

| Category | Attributes | Examples |
|----------|-----------|----------|
| **Word-level** | Part, Constituent, LexicalSense | "Noun", "God", "A" |
| **Grammatical** | Number, Person, Gender | "Singular", "Third", "Masculine" |
| **Semantic** | Polarity, Proximity, Participant Tracking | "Affirmative", "Near", "Routine" |
| **Discourse** | Discourse Genre, Illocutionary Force | "Narrative", "Declarative" |
| **Morphological** | Mood, Aspect, Time | "Indicative", "Unmarked", "Historic Past" |

**Complete Feature List:** See `tbta-source/TBTA-FEATURES.md` for all 59 features

### 1.3 XML Format (Alternative)

**Parallel structure to JSON, attribute-based:**
```xml
<Clause DiscourseGenre="Climactic Narrative Story"
        IllocutionaryForce="Declarative"
        TopicNP="Most Agent-like">
  <NP SemanticRole="Most Agent-like">
    <Noun Number="Singular"
          Person="Third"
          Polarity="Affirmative"
          ParticipantTracking="Routine">God</Noun>
  </NP>
  <VP>...</VP>
</Clause>
```

**Note:** JSON format preferred for programmatic processing due to cleaner nesting structure.

---

## 2. Macula Linking Mechanism

### 2.1 Macula File Structure

**File Location (myBibleToolbox):**
```
.data/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-macula.yaml

Example:
.data/commentary/JHN/001/001/JHN-001-001-macula.yaml
```

**Sample Macula Data:**
```yaml
source: macula-greek
version: 1.0.0
language: grc
verse: JHN 1:1
text: Ἐν ἀρχῇ ἦν ὁ Λόγος...
words:
  - position: 1
    text: Ἐν
    lemma: ἐν
    ids:
      ref: JHN 1:1!1
      wordID: n43001001001
    morphology:
      class: prep
      morph: PREP
    lexical:
      strong: '1722'      # ← Strong's number G1722

  - position: 2
    text: ἀρχῇ
    lemma: ἀρχή
    ids:
      ref: JHN 1:1!2
      wordID: n43001001002
    morphology:
      class: noun
      morph: N-DSF
      gender: feminine
      number: singular
      case: dative
    lexical:
      strong: '746'       # ← Strong's number G746
```

**Key Linking Fields:**
- `position` - Word order within verse (1, 2, 3...)
- `lexical.strong` - Strong's number (without G/H prefix)
- `lemma` - Dictionary form (matches Strong's word)
- `ids.ref` - Verse reference with word position (JHN 1:1!1)

### 2.2 Linking Strategy

**Three-Way Join:**

```
TBTA Word → Macula Word → Strong's Number

Matching Criteria:
1. Verse reference (BOOK.CHAPTER.VERSE)
2. Word position (1, 2, 3... in sequential order)
3. Constituent text (TBTA) ≈ text (Macula)
```

**Algorithm:**
```python
# Step 1: Parse TBTA JSON for verse
tbta_data = load_tbta_json("00_001_001_Genesis.json")
tbta_words = extract_words_in_order(tbta_data)  # Flatten hierarchy

# Step 2: Load Macula data
macula_data = load_yaml(".data/commentary/GEN/001/001/GEN-001-001-macula.yaml")
macula_words = macula_data['words']

# Step 3: Align by position
for i, tbta_word in enumerate(tbta_words):
    macula_word = macula_words[i]

    # Verify alignment (sanity check)
    if normalize(tbta_word['Constituent']) ≈ normalize(macula_word['text']):
        strongs_id = "G" + macula_word['lexical']['strong']

        # Extract TBTA attributes for this Strong's word
        attributes = {
            "Number": tbta_word.get("Number"),
            "Person": tbta_word.get("Person"),
            "Polarity": tbta_word.get("Polarity"),
            "Proximity": tbta_word.get("Proximity"),
            # ... 59 TBTA features
        }

        # Aggregate to Strong's enrichment
        aggregate_to_strongs(strongs_id, attributes, verse_ref)
```

**Challenges:**
1. **Text Normalization:** TBTA uses English glosses ("God"), Macula uses Greek/Hebrew ("θεός")
   - Solution: Use Macula `translation.gloss` field or rely on position matching
2. **Multiple Clauses:** TBTA splits complex sentences into multiple clause trees
   - Solution: Flatten hierarchy and extract words in sequential order
3. **Missing Data:** Not all TBTA verses have Macula coverage
   - Solution: Skip verses where Macula data unavailable (document coverage %)

---

## 3. Existing Script Pattern (extract_feature.py)

### 3.1 Script Purpose

**File:** `/workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py`

**Function:** Extract all verses for a single TBTA feature (e.g., "Clusivity", "Mood") from TBTA repository

**Usage:**
```bash
python extract_feature.py --field Clusivity --max-per-value 2000
```

**Output:** YAML file with verses grouped by feature value:
```yaml
feature: clusivity
extracted: "2025-11-15T18:30:00Z"
tbta_commit: "a1b2c3d"
max_per_value: 2000
value:
  - specific_value: "Inclusive"
    total_verses: 487
    distribution:
      OT: 245
      NT: 242
      Books:
        GEN: 38
        MAT: 52
        ...
    verses:
      - "GEN.001.026"
      - "GEN.003.022"
      - "MAT.028.019"
      ...
```

### 3.2 Key Script Components

**1. TBTA Repository Cloning:**
```python
def clone_tbta_repo():
    """Clone/update TBTA GitHub repository to /tmp/tbta_db_export"""
    subprocess.run(["git", "clone", "--depth=1", TBTA_REPO_URL, TBTA_LOCAL_PATH])
```

**2. Recursive Feature Extraction:**
```python
def extract_field_from_clause(clause_data, field_name):
    """
    Recursively search clause tree for field.
    Handles nested Children arrays.
    """
    values = []

    if field_name in clause_data:
        value = clause_data[field_name]
        if value not in ["Not Applicable", "Unspecified", "."]:
            values.append(value)

    if "Children" in clause_data:
        for child in clause_data["Children"]:
            values.extend(extract_field_from_clause(child, field_name))

    return values
```

**3. LRU Cache (Cap Verses per Value):**
```python
class LRUCache:
    """Limit verses per value to avoid overwhelming output"""
    def __init__(self, max_size=2000):
        self.cache = OrderedDict()
        self.max_size = max_size

    def add(self, value, verse_ref):
        if len(self.cache[value]) > self.max_size:
            self.cache[value].pop(0)  # FIFO
```

**4. Book Name → USFM Mapping:**
```python
BOOK_NAME_MAP = {
    "Genesis": "GEN",
    "Matthew": "MAT",
    "1_Thessalonians": "1TH",
    ...
}
```

### 3.3 Adaptation for Strong's Script

**New Script Requirements:**

| Feature | extract_feature.py | strong-tbta-link.py |
|---------|-------------------|---------------------|
| Input | Single TBTA feature | Strong's number |
| Processing | Extract verses by feature value | Extract word-level attributes |
| Linking | None (verse-level) | Macula (word-level) |
| Output | Verses grouped by value | Attributes aggregated by occurrence |
| Complexity | Low (single data source) | Medium (three-way join) |

**Key Differences:**
1. **Word-level Granularity:** Extract attributes for each word occurrence, not verse-level features
2. **Three-way Join:** TBTA + Macula + Strong's
3. **Attribute Aggregation:** Pattern detection across all occurrences of a Strong's word

---

## 4. Strong's TBTA Hints Tool Context

### 4.1 Tool Objective

**Goal:** Enrich Strong's words with cross-linguistic translation patterns derived from TBTA features

**Example (G2249 ἡμεῖς "we"):**
```yaml
# G2249-tbta-hints.yaml
strongs_id: "G2249"
word: "ἡμεῖς"
gloss: "we"

patterns:
  - feature: "person_clusivity"
    context: "divine speech (Trinity)"
    pattern: "Austronesian languages use exclusive 'kami' (5/5 consistency)"
    examples:
      - lang: "tgl"
        word: "kami"
        verses: ["GEN.001.026", "GEN.003.022", "GEN.011.007"]
    confidence: 0.95

  - feature: "person_clusivity"
    context: "church unity passages"
    pattern: "Austronesian languages use inclusive 'tayo/kita' (4/4 consistency)"
    examples:
      - lang: "tgl"
        word: "tayo"
        verses: ["1CO.012.013", "EPH.004.004"]
    confidence: 0.90
```

### 4.2 Methodology (LLM-Based Logic Tree)

**From:** `/bible-study-tools/strongs-extended/tools/tbta-hints/METHODOLOGY.md`

**5-Step LLM Process:**

1. **Feature Applicability Check**
   - Input: Strong's word (G2249 "we") + TBTA feature (clusivity)
   - Output: Does clusivity apply to pronouns? → Yes (proceed)

2. **Cross-Linguistic Pattern Detection**
   - Input: 900+ translations of G2249 across all occurrences
   - Output: Austronesian languages systematically use "kami" (exclusive) vs "tayo/kita" (inclusive)

3. **Context-Dependent Analysis**
   - Input: Verse contexts (Trinity speech vs church unity vs general)
   - Output: Pattern correlates with theological context (Trinity → exclusive, church → inclusive)

4. **Confidence Calibration**
   - Input: Language count (5), consistency (100%), semantic explanation
   - Output: Confidence = 0.95 (very high)

5. **Evidence Synthesis**
   - Input: All analysis from Steps 1-4
   - Output: YAML with patterns, examples, confidence scores

**Key Insight:** LLM handles pattern detection automatically (no hard-coded rules) → Scales to 14,197 Strong's words

### 4.3 Data Requirements

**What the script needs to provide to the LLM:**

1. **Strong's word metadata:**
   - strongs_id, lemma, gloss, part_of_speech

2. **TBTA feature values across all occurrences:**
   ```yaml
   occurrences:
     - verse: "GEN.001.026"
       tbta_features:
         Person: "First"
         Number: "Plural"
         Participant_Tracking: "Routine"
         # ... all 59 features

     - verse: "GEN.003.022"
       tbta_features:
         Person: "First"
         Number: "Plural"
         # ...
   ```

3. **Translation corpus (from eBible):**
   ```yaml
   translations:
     - verse: "GEN.001.026"
       tgl: "Gumawa tayo ng tao..." (inclusive)
       msa: "Mari kita ciptakan manusia..." (inclusive)
       eng: "Let us make man..."
   ```

**Script Output Format (for LLM processing):**
```yaml
strongs_id: "G2249"
lemma: "ἡμεῖς"
gloss: "we"
part_of_speech: "pronoun"

occurrences:
  - verse: "GEN.001.026"
    context: "Let us make man in our image"
    tbta_features:
      Person: "First"
      Number: "Plural"
      Clusivity: "Inclusive"  # (hypothetical - TBTA doesn't directly label this)
      Participant_Tracking: "Routine"
    translations:
      tgl: "tayo"
      msa: "kita"
      fij: "kedatou"
      eng: "us"

  - verse: "1CO.012.013"
    context: "For we were all baptized into one body"
    tbta_features:
      Person: "First"
      Number: "Plural"
      Participant_Tracking: "Frame Inferable"
    translations:
      tgl: "tayo"
      msa: "kita"
      eng: "we"

# ... repeat for all occurrences
```

---

## 5. Recommended Data Extraction Strategy

### 5.1 Script Architecture

**File:** `src/ingest-data/tbta/link_strongs_tbta.py`

**High-Level Flow:**
```python
def process_strongs_word(strongs_id):
    """
    Extract TBTA features for all occurrences of a Strong's word.

    Steps:
    1. Find all verses containing this Strong's word (via Macula)
    2. For each verse:
       a. Load TBTA data (if available)
       b. Load Macula data
       c. Align words by position
       d. Extract TBTA attributes for this word
       e. Load translation data (eBible)
    3. Aggregate all occurrences
    4. Output YAML for LLM processing
    """

    # Step 1: Find occurrences
    macula_verses = find_verses_with_strongs(strongs_id)
    # Result: ["JHN.001.001", "JHN.001.014", ...]

    # Step 2: Extract data for each occurrence
    occurrences = []
    for verse_ref in macula_verses:
        # Load data sources
        tbta_data = load_tbta_json(verse_ref)
        macula_data = load_macula_yaml(verse_ref)

        if not tbta_data:
            continue  # Skip verses without TBTA coverage

        # Align and extract
        word_position = find_word_position(macula_data, strongs_id)
        tbta_attributes = extract_attributes_at_position(tbta_data, word_position)

        # Get translations
        translations = load_ebible_translations(verse_ref)

        occurrences.append({
            "verse": verse_ref,
            "tbta_features": tbta_attributes,
            "translations": translations
        })

    # Step 3: Output
    output = {
        "strongs_id": strongs_id,
        "occurrences": occurrences
    }

    save_yaml(output, f"output/{strongs_id}-tbta-occurrences.yaml")
```

### 5.2 Key Functions

**1. Find Verses with Strong's Number:**
```python
def find_verses_with_strongs(strongs_id):
    """
    Search Macula files for all verses containing this Strong's word.

    Strategy: Glob all macula.yaml files and grep for strongs_id
    """
    verse_refs = []

    macula_files = glob(".data/commentary/**/*-macula.yaml")
    for macula_file in macula_files:
        data = yaml.safe_load(open(macula_file))

        for word in data['words']:
            if word['lexical']['strong'] == strongs_id.replace('G', ''):
                verse_refs.append(data['verse'])
                break

    return verse_refs
```

**2. Align TBTA Words by Position:**
```python
def extract_attributes_at_position(tbta_data, word_position):
    """
    Flatten TBTA clause tree and extract attributes at word_position.

    TBTA structure:
    - Clause
      - NP
        - Noun (position 1)
      - VP
        - Verb (position 2)

    Need to traverse in document order to match Macula positions.
    """
    words = []

    def traverse(node):
        if node.get('Part') in ['Noun', 'Verb', 'Adjective', ...]:
            words.append(node)  # Leaf word node

        if 'Children' in node:
            for child in node['Children']:
                traverse(child)

    # Traverse all clauses
    for clause in tbta_data:
        traverse(clause)

    # Return attributes for word at position
    if word_position <= len(words):
        return words[word_position - 1]
    else:
        return None
```

**3. Load eBible Translations:**
```python
def load_ebible_translations(verse_ref):
    """
    Load translation data from .data/commentary/{BOOK}/{chap}/{verse}/*-ebible.yaml

    Extract target languages (tgl, msa, fij, etc.)
    """
    book, chapter, verse = parse_verse_ref(verse_ref)
    ebible_file = f".data/commentary/{book}/{chapter:03d}/{verse:03d}/{book}-{chapter:03d}-{verse:03d}-ebible.yaml"

    data = yaml.safe_load(open(ebible_file))

    translations = {}
    for lang_code in ['tgl', 'msa', 'fij', 'ind', 'eng', 'spa']:
        if lang_code in data.get('translations', {}):
            translations[lang_code] = data['translations'][lang_code]['text']

    return translations
```

### 5.3 Output Format

**For each Strong's word, generate:**
```yaml
# G2249-tbta-raw.yaml (intermediate data for LLM)
strongs_id: "G2249"
lemma: "ἡμεῖς"
gloss: "we"
part_of_speech: "personal-pronoun"
testament: "NT"  # Based on occurrence distribution

coverage:
  total_occurrences: 123  # From Macula
  tbta_coverage: 87       # Verses with TBTA data
  coverage_pct: 70.7

occurrences:
  - verse: "GEN.001.026"
    text_en: "Let us make man in our image"
    tbta_features:
      Part: "Pronoun"
      Person: "First"
      Number: "Plural"
      Polarity: "Affirmative"
      Participant_Tracking: "Routine"
      Surface_Realization: "Pronoun"
      # ... (all 59 features where applicable)

    translations:
      tgl: "tayo"
      msa: "kita"
      fij: "kedatou"
      eng: "us"

  # ... repeat for all 87 verses with TBTA coverage

metadata:
  extracted: "2025-11-15T18:30:00Z"
  tbta_commit: "a1b2c3d"
  macula_version: "1.0.0"
  script_version: "1.0.0"
```

---

## 6. Key Challenges and Solutions

### Challenge 1: TBTA-Macula Text Alignment

**Problem:** TBTA uses English glosses ("God"), Macula uses source text ("θεός")

**Solutions:**
1. **Primary:** Position-based alignment (assume sequential order matches)
2. **Validation:** Use Macula `translation.gloss` field to verify:
   ```python
   if tbta_word['Constituent'].lower() == macula_word['translation']['gloss'].lower():
       # Alignment confirmed
   ```
3. **Fallback:** Lemma matching (TBTA LexicalSense → Macula lemma)

**Robustness:** Accept minor misalignments (<5%) due to:
- TBTA clause restructuring
- Idioms (multi-word → single gloss)
- Textual variants

### Challenge 2: Sparse TBTA Coverage

**Problem:** TBTA only covers 37% of Bible (11,649 verses)

**Impact on Strong's Words:**
- High-frequency words (G3588 "the", G2532 "and") → Good coverage (50-70%)
- Low-frequency words (rare verbs) → Poor coverage (<20%)

**Solutions:**
1. **Document coverage percentage** in output:
   ```yaml
   coverage:
     total_occurrences: 487 (from Macula)
     tbta_coverage: 312    (with TBTA data)
     coverage_pct: 64.1
   ```

2. **Prioritize high-value words first:**
   - Top 300 words (70% text coverage)
   - Pronouns, demonstratives, particles (highest TBTA feature relevance)

3. **Mark low-confidence patterns:**
   ```yaml
   confidence: 0.45
   reasoning: "Limited data (only 12 occurrences with TBTA), pattern may not generalize"
   ```

### Challenge 3: Multiple Occurrences per Verse

**Problem:** A Strong's word may appear multiple times in one verse:
```
"I am the way, the truth, and the life" (JHN 14:6)
→ G3588 "the" appears 3 times
```

**Solution:** Track position within verse:
```yaml
occurrences:
  - verse: "JHN.014.006"
    position: 5  # First "the"
    context: "the way"
    tbta_features: {...}

  - verse: "JHN.014.006"
    position: 8  # Second "the"
    context: "the truth"
    tbta_features: {...}
```

### Challenge 4: Hierarchical TBTA Data

**Problem:** TBTA nests words within phrases within clauses:
```json
Clause → NP → Adjective → "holy"
       → NP → Noun → "spirit"
```

**Solution:** Flatten hierarchy in document order:
```python
def flatten_words(clause_data):
    """Extract all word-level nodes in sequential order"""
    words = []

    WORD_PARTS = ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun',
                  'Adposition', 'Conjunction', 'Particle']

    def traverse(node):
        if node.get('Part') in WORD_PARTS:
            words.append(node)
        elif 'Children' in node:
            for child in node['Children']:
                traverse(child)

    traverse(clause_data)
    return words
```

---

## 7. Production Readiness Assessment

### 7.1 Script Feasibility

**Complexity:** Medium (3-way join, hierarchical data)

**Estimated Development Time:**
- Core script: 1-2 days
- Testing/validation: 1 day
- Error handling: 0.5 day
- **Total:** 2-3 days for production-ready script

**Dependencies:**
- Python 3.9+
- Libraries: PyYAML, pathlib, subprocess
- Data sources: TBTA repo (GitHub), Macula files (.data), eBible files (.data)

### 7.2 Data Quality Expectations

**Coverage (Strong's Words):**
- Top 50 words: 60-80% TBTA coverage
- Top 300 words: 40-60% TBTA coverage
- All 14,197 words: 10-30% TBTA coverage (due to TBTA's 37% Bible coverage)

**Accuracy (Alignment):**
- Expected: 95%+ correct word alignment (position-based)
- Validation: Manual spot-check on 20-30 words

**Utility (for LLM):**
- High value: Pronouns, demonstratives (clusivity, proximity, person)
- Medium value: Verbs (aspect, mood, time)
- Low value: Particles, conjunctions (limited TBTA features)

### 7.3 Next Steps

**Phase 1: Proof of Concept (1 week)**
1. Implement core script for single Strong's word (e.g., G2249 "we")
2. Validate alignment accuracy on 10 sample verses
3. Generate sample output for LLM testing
4. Document edge cases and error patterns

**Phase 2: Top 50 Words (2 weeks)**
1. Process top 50 high-value words (pronouns, demonstratives)
2. Refine alignment logic based on PoC learnings
3. Implement error handling (missing data, alignment failures)
4. Generate batch output for LLM integration

**Phase 3: Production (1 month)**
1. Scale to top 300 words
2. Integrate with TBTA Hints LLM workflow
3. Validate pattern extraction accuracy
4. Production deployment

---

## 8. References

**TBTA Documentation:**
- Repository: https://github.com/AllTheWord/tbta_db_export
- Coverage: `/bible-study-tools/tbta/tbta-source/COVERAGE.md`
- Features: `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`

**Macula Documentation:**
- Source: Macula Greek/Hebrew morphology
- Schema: See sample file `/workspaces/mybibletoolbox-code/.data/commentary/JHN/001/001/JHN-001-001-macula.yaml`

**Strong's Extended Tool:**
- Tool overview: `/bible-study-tools/strongs-extended/README.md`
- TBTA Hints methodology: `/bible-study-tools/strongs-extended/tools/tbta-hints/METHODOLOGY.md`
- STAGES workflow: `/bible-study-tools/strongs-extended/tools/STAGES.md`

**Existing Scripts:**
- TBTA feature extractor: `/workspaces/mybibletoolbox-code/src/ingest-data/tbta/extract_feature.py`

---

**Research Status:** Complete
**Next Action:** Implement proof-of-concept script for single Strong's word
**Estimated Timeline:** 3 days (PoC) → 2 weeks (Top 50) → 1 month (Production)
