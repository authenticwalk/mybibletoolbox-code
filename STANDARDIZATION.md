# Format Standardization - eBible/USFM 3.0 Alignment

---

## Purpose

Align our Bible text organization with established standards from:
- **eBible corpus** (BibleNLP): https://github.com/BibleNLP/ebible
- **USFM 3.0 specification**: Standard book codes
- **ISO-639 language codes**: Standard language identification

---

## Standards Adopted

### 1. Book Codes (USFM 3.0)

**Format:**3-letter uppercase codes per USFM 3.0 specification

**Examples:**
- Matthew: `MAT` (not `mt` or `Matt`)
- Genesis: `GEN`
- Revelation: `REV`

**Source:** https://ubsicap.github.io/usfm/identification/books.html

### 2. Language Codes (ISO-639-3)

**Format:** 3-letter lowercase codes per ISO-639-3 standard

**Rationale:** Biblical scholarship uses ISO-639-3 for ancient languages and better granularity

**Common codes:**
```yaml
eng: English
spa: Spanish
fra: French
deu: German (Deutsch)
por: Portuguese
rus: Russian
zho: Chinese
kor: Korean
ara: Arabic
grc: Ancient Greek
heb: Biblical Hebrew
lat: Latin
```

**Note:** We use ISO-639-3 (3 letters) instead of ISO-639-1 (2 letters) because:
- Ancient languages like `grc` (Ancient Greek) have no ISO-639-1 equivalent
- Consistency across modern and ancient languages
- Standard in biblical text repositories

### 3. Directory Structure

**Note:** All data paths are relative to the `mybibletoolbox-data` repository.

**Commentary:** `/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-{tool-name}.yaml`

**Examples:**

**Commentary:**
```
/commentary/MAT/005/003/MAT-005-003-translations.yaml
/commentary/MAT/005/003/MAT-005-003-semantic-clusters.yaml
/commentary/GEN/001/001/GEN-001-001-translations.yaml
```

**Topics:**
```
/topics/BT109/trinity/trinity-{tool}.yaml
/topics/BT130/divine-attributes/omniscience/omniscience-{tool}.yaml
/topics/BT750/salvation/justification/justification-{tool}.yaml
/topics/BT819/eschatology/second-coming/second-coming-{tool}.yaml
```

**Strong's Concordance:**
```
/strongs/G0026/G0026-{tool}.strongs.yaml
/strongs/H0157/H0157-{tool}.strongs.yaml
```

See [Strong's README](../mybibletoolbox-data/strongs/README.md) for complete Strong's Concordance format specification.

**Language-Specific Words:**
```
/languages/grc/words/λογος/grc-λογος-{tool}.yaml
/languages/heb/words/אהב/heb-אהב-{tool}.yaml
/languages/eng/words/love/eng-love-{tool}.yaml
```

**Rationale (Directory Structure):**
- Book code visible in filename (easier to identify files out of context)
- Period separators for chapter.verse (standard in biblical references)
- Hyphen before type descriptor (translations, semantic-clusters, etc.)

---

### 4. Word Normalization Standards

**Purpose:** Store lexical/semantic data for words, organized by root form for easy lookup

**Path:** `/languages/{ISO-639-3}/words/{word}/{ISO-639-3}-{word}-{tool}.yaml`

**Components:**
- `{ISO-639-3}`: ISO-639-3 language code (e.g., `heb`, `grc`, `eng`)
- `{word}`: The word form (root or inflected)
- `{tool}`: The analysis tool that generated this data (e.g., `morphology`, `semantics`, `concordance`)

**Normalization Rules by Language:**

**Hebrew (`heb`):**
- Use lexical form (dictionary entry)
- No gender, number, or state variations
- Examples: `אָהַב` (ahav) not `אֹהֵב` (ohev), `אָהְבָה` (ahavah)

**Greek (`grc`):**
- Use lexical form (nominative singular for nouns, 1st person singular present for verbs)
- No case, gender, number, tense variations
- Examples: `λόγος` (logos) not `λόγου` (logou), `λόγον` (logon)

**English (`eng`):**
- Use base form (infinitive for verbs, singular for nouns)
- Examples: `love` not `loves`, `loving`, `loved`

**Examples:**

```
# Hebrew words (root form)
/languages/heb/words/אהב/heb-אהב-morphology.yaml        # Love (ahav) - morphological analysis
/languages/heb/words/אהב/heb-אהב-semantics.yaml         # Love (ahav) - semantic analysis

# Greek words (root form)
/languages/grc/words/λογος/grc-λογος-morphology.yaml    # Word/logos - morphological analysis
/languages/grc/words/λογος/grc-λογος-semantics.yaml     # Word/logos - semantic analysis

# English words
/languages/eng/words/love/eng-love-concordance.yaml     # Love - concordance data
/languages/eng/words/love/eng-love-semantics.yaml       # Love - semantic analysis
```

**YAML Format:**

```yaml
# Hebrew word example
verse: JOB.038.036
language: heb
word: אָהַב
transliteration: ahav
strongs: H0157
meaning: to love, have affection
related_words:
  - grc/αγαπη
  - eng/love
verses: [JHN.003.016, 1JN.004.008]
tool: morphology
metadata:
  generated_by: tool-name
  generated_date: 2025-11-04

# Greek word example
verse: JHN.001.001
language: grc
word: λόγος
transliteration: logos
strongs: G3056
meaning: word, speech, reason
verses: [JHN.001.001, JHN.001.014]
tool: semantics
metadata:
  generated_by: tool-name
  generated_date: 2025-11-04
```

**Benefits:**
- **Organized**: Language-specific organization under `/languages/`
- **Tool-specific**: Each analysis tool creates separate files
- **Discoverable**: Words organized alphabetically within language directories
- **Cross-referencing**: Easy to link related words across languages

**References for Lemmatization:**

- **Hebrew:** Brown-Driver-Briggs (BDB) Lexicon, Strong's Concordance
- **Greek:** BDAG Lexicon, Strong's Concordance, Thayer's Greek Lexicon
- **Strong's Numbers:** Use as cross-reference (e.g., H0157 for אָהַב, G0026 for ἀγάπη)
- **Strong's Format:** See [Strong's README](../mybibletoolbox-data/strongs/README.md) for complete specification

### 5. Theological Topic Taxonomy

**Standard:** Library of Congress Classification (LCC) codes + human-readable slugs

**Format:** `/topics/{lcc-code}/{slug}/{slug}[-{subsection}]-{tool}.yaml`

**Major LCC Sections for Biblical Topics:**
```
BS: Biblical Studies (texts, interpretation, geography, biblical topics)
BT: Doctrinal Theology (God, Christ, salvation, eschatology)
BV: Practical Theology (prayer, Christian life, worship, ethics)
BX: Denominations and Church History
```

**Example Topics with LCC Codes:**
```
/topics/BS1199/land-of-canaan/land-of-canaan-study.yaml              # Biblical geography
/topics/BT109/trinity/trinity-doctrine.yaml                          # Doctrinal theology
/topics/BT750/salvation/justification/justification-theology.yaml    # Soteriology
/topics/BV210/prayer/prayer-practice.yaml                            # Practical theology
/topics/BV4909/suffering/suffering-pastoral.yaml                     # Christian life topics
```

**YAML Format:**
```yaml
lcc_code: BT109
topic: Trinity
slug: trinity
related_topics: [BT117/holy-spirit, BT130/divine-attributes]
verses: [MAT.28.19, JHN.1.1]
```

**How to Find LCC Codes:**
- Search Westminster Seminary LibGuide: https://wts.libguides.com/c.php?g=1414259
- Use Library of Congress Online Catalog: https://catalog.loc.gov
- Check BISAC codes for cross-reference: https://www.bisg.org/religion

---

### 6. Cross-Referencing Standards

**Purpose:** Consistent format for linking between files (words, topics, verses)

#### Word References

**Format:** `{lang}/{word}`

Use language-prefixed paths when referencing words in any YAML field:

```yaml
# In word files
related_words:
  - grc/αγαπη            # Greek agape
  - heb/אהב              # Hebrew ahav
  - eng/love             # English love
  - grc/λογος            # Greek logos

# In topic or verse analysis files
key_words:
  - grc/πιστις           # faith
  - grc/ελπις            # hope
  - grc/αγαπη            # love
```

**Note:** Full file paths are `/languages/{lang}/words/{word}/{lang}-{word}-{tool}.yaml`

**Benefits:**
- Concise references (no redundant language prefix in reference)
- Language explicit
- Easy to programmatically resolve to full path
- Organized under `/languages/` directory

#### Topic References and Aliases

**Format:** `{lcc-code}/{slug}` - LCC code provides category, slug provides readability

**Standard reference** (no `@`):
```yaml
related_topics:
  - BT750/justification           # Soteriology section
  - BT198/atonement               # Christology section  
  - BV210/prayer                  # Practical theology
```

**Alias reference** (with `@` prefix) - indicates primary definition is elsewhere:
```yaml
# In /topics/BV4627/sin/sin-doctrine.yaml (Practical: Sins & Virtues)
primary_topic: "@BT695/fall-of-man"   # See doctrinal treatment

# In /topics/BT750/atonement/atonement-theology.yaml (Soteriology)
see_also:
  - "@BV210/prayer"                    # Practical application
  - "@BS1199/day-of-atonement"         # Biblical reference
```

**Understanding LCC Codes** (for human reference):
```
BS1199: Biblical Topics (geography, people, events)
BT109:  Trinity
BT130:  Divine Attributes  
BT198:  Christology
BT695:  Creation & Fall
BT750:  Soteriology (Salvation)
BT819:  Eschatology
BV210:  Worship & Prayer
BV4627: Sins & Virtues
BV4909: Suffering & Consolation
```

**Use Cases:**
- `@prefix`: Topic aliased/defined elsewhere
- No prefix: Standard cross-reference
- `primary_topic`: This file redirects to another
- `see_also`: Related topics for further study

**Note:** While LCC codes aren't immediately readable, they're necessary for:
- Precise categorization
- Avoiding slug conflicts
- Standard library compatibility
- The slug makes the actual topic clear

#### Verse References

**Format:** `{BOOK}.{chapter:03d}.{verse:03d}` (zero-padded per Section 1)

```yaml
cross_refs:
  - JHN.3.16
  - ROM.8.28
  - PSA.23.1

related_verses:
  - ref: MAT.5.3
    note: "First beatitude"
  - ref: JHN.11.35
    note: "Jesus wept"
```

### 7. Translation Version Keys (Incremental Format)

**Format:** Incremental specificity as needed: `{lang}` → `{lang}-{version}` → `{lang}-{version}-{year}`

**Principles:**
1. Use minimum specificity needed to uniquely identify the translation
2. Add components only when disambiguation is required
3. Maintain consistency within language families

**Examples:**
```yaml
# Single translation in language (language code only)
ara: "Standard Arabic translation"
heb: "Standard Hebrew text"

# Multiple translations, no version conflict (language + version)
eng-niv: "New International Version"
eng-kjv: "King James Version"
eng-esv: "English Standard Version"

# Same version, different years (language + version + year)
eng-niv-1984: "NIV 1984 edition"
eng-niv-2011: "NIV 2011 edition"
spa-rv-1909: "Reina Valera 1909"
spa-rv-1960: "Reina Valera 1960"
```

**Components (add incrementally as needed):**
1. `lang`: ISO-639-3 language code (3 letters, lowercase) - **REQUIRED**
2. `version`: Translation abbreviation (UPPERCASE: NIV, ESV, KJV, etc.) - add when multiple translations exist
3. `year`: Publication year (4 digits) - add only when same version has multiple editions

**Version Code Standards:**
- Version abbreviations: UPPERCASE (NIV, KJV, ESV, RV, NA28)
- Language codes: lowercase (eng, spa, grc, heb)
- Separator: hyphen (`-`)
- No redundancy: Don't repeat language in version (❌ `eng-engNIV`, ✅ `eng-NIV`)

**Rationale:**
- Minimal format reduces verbosity for unique translations
- Year precision only when needed (NIV 1984 vs 2011 has significant differences)
- Matches eBible corpus naming conventions
- Easy to extend when disambiguation needed

---

### 5. Citation Standards (Inline Source Format)

**Format:** Inline citations immediately after content: `content {source}`

**Principles:**
1. Every translation, fact, or analysis must cite its source
2. Citations appear inline, not as separate fields or lists
3. No fabricated examples - only cite what exists in data files
4. Use standardized source codes from `ATTRIBUTION.md`

**Citation Format by Content Type:**

```yaml
# AI-generated analysis or insights
rationale: "This demonstrates theological emphasis" {llm-cs45}

# Translation citations in examples
- example: "Blessed are the poor in spirit"
  sources: [eng-NIV-2011, eng-ESV]

# Cultural or linguistic notes
cultural_note: "Sino-Tibetan languages use emptiness concept" {llm-cs45}

# Greek/Hebrew source text
source_text: "μακάριοι οἱ πτωχοὶ τῷ πνεύματι" {grc-NA28}
```

**Source Code Structure:**

Incremental format: `{lang}-{version}` → `{lang}-{version}-{year}`

Components:
- `lang`: ISO-639-3 code (3 letters, lowercase) - **REQUIRED**
- `version`: Translation abbreviation (UPPERCASE: NIV, ESV, NA28, etc.)
- `year`: Publication/revision year (4 digits) - **only when multiple editions exist**

**Common Examples:**
```yaml
grc-NA28                   # Greek: Nestle-Aland 28th edition (single edition)
eng-NIV-1984               # English: NIV 1984 (multiple editions exist)
eng-NIV-2011               # English: NIV 2011
eng-ESV                    # English: ESV (single primary edition)
spa-RV-1960                # Spanish: Reina Valera 1960 (multiple editions exist)
llm-cs45                   # AI analysis: Claude Sonnet 4.5
```

**Rules:**
- ✅ Inline format: `content {source}` (curly braces)
- ✅ Immediate placement: Citation directly after the content it supports
- ✅ Array format for multiple sources: `sources: [source1, source2, source3]`
- ❌ NO separate `source:` fields
- ❌ NO newline citations
- ❌ NO fabricated translations
- ❌ NO citations without actual data verification

**Source Authority Levels:**

Per `ATTRIBUTION.md`:
- **High authority**: Biblical text editions (NA28, UBS5, Biblia Hebraica), established translations (NIV, ESV, NASB)
- **Medium authority**: Digital platforms (BibleHub, eBible, Bible Gateway)
- **Low authority**: LLM-generated content (llm-cs45, llm-gpt4) - ALWAYS requires human review

**Rationale:**
- Enables full traceability of all claims
- Prevents fabrication or hallucination
- Maintains academic rigor in analysis
- Clear distinction between authoritative sources and AI-generated content
- Inline format keeps content and citations together
- Incremental specificity (only add year when needed for disambiguation)

**Reference:** See `ATTRIBUTION.md` for complete source codes, authority levels, and citation formats.

---


## References

**Bible Text Standards:**
- **eBible corpus:** https://github.com/BibleNLP/ebible
- **USFM 3.0 book codes:** https://ubsicap.github.io/usfm/identification/books.html
- **ISO-639-3 codes:** https://iso639-3.sil.org/code_tables/639/data
- **BibleHub:** https://biblehub.com (translation source)

**Theological Topic Standards:**
- **Library of Congress Classification (LCC):** https://wts.libguides.com/c.php?g=1414259
- **BISAC Subject Headings (Religion):** https://www.bisg.org/religion
- **Index Theologicus (IxTheo):** https://ixtheo.de/Content/IxTheoClassification


