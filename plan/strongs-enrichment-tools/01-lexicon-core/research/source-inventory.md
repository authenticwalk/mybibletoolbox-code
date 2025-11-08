# Source Inventory: Available Lexicons

**Tool:** strongs-lexicon-core
**Phase:** Research
**Created:** 2025-11-08

---

## Overview

This document inventories ALL available lexicon sources for Strong's word research, organized by location and accessibility.

**Purpose:** Know exactly what data is available where to:
1. Avoid duplication (read base files FIRST)
2. Maximize coverage (extract from all available sources)
3. Mark authority levels (published lexicons = HIGH)

---

## Source 0: Base Strong's Files (PRE-EXISTING)

**Location:** `./bible/words/strongs/{number}/{number}.strongs.yaml`

**CRITICAL:** ALWAYS read this FIRST before extracting from web sources!

### What's Already There

**Fields Present:**
- `strongs_number`: Strong's number (G#### or H####)
- `language`: "greek" or "hebrew"
- `lemma`: Lexical form in original script
- `transliteration`: Romanized form
- `definition`: Base definition {strongs}
- `kjv_usage`: KJV translation(s) {strongs}
- `derivation`: Etymology/root words {strongs}
- `source`: "OpenScriptures Strong's"
- `license`: "CC-BY-SA"

**Pre-Imported Lexicon Data:**

The base files contain imported data from these open-licensed lexicons:
- **BDB** (Brown-Driver-Briggs) - Hebrew lexicon
- **Thayer's Greek-English Lexicon** - NT Greek
- **LSJ** (Liddell-Scott-Jones abridged) - Classical Greek
- **unfoldingWord Translation Words** - Modern open-licensed

**Cross-Reference Codes (when available):**
- `bdag`: Bauer-Danker-Arndt-Gingrich code
- `tdnt`: Theological Dictionary of NT reference
- `louw_nida`: Semantic domain code
- `gk`: Goodrick-Kohlenberger number
- `twot`: Theological Wordbook of OT (Hebrew)
- `lsj`: Liddell-Scott-Jones reference

### Extraction Strategy for Base Files

```python
# Pseudo-code for reading base file
base_file = read_yaml(f"./bible/words/strongs/{number}/{number}.strongs.yaml")

# Extract what's already present
existing_data = {
    'definition': base_file.get('definition'),
    'kjv_usage': base_file.get('kjv_usage'),
    'derivation': base_file.get('derivation'),
    'imported_lexicons': {}  # BDB, Thayer's, LSJ, unfoldingWord if present
}

# Extract cross-reference codes for additional searches
cross_refs = {
    'bdag': base_file.get('bdag'),
    'tdnt': base_file.get('tdnt'),
    'louw_nida': base_file.get('louw_nida'),
    'gk': base_file.get('gk'),
    'twot': base_file.get('twot'),
    'lsj': base_file.get('lsj')
}

# Use cross-refs for web searches
if cross_refs['bdag']:
    search_web(f"BDAG {cross_refs['bdag']}")
if cross_refs['tdnt']:
    search_web(f"TDNT {cross_refs['tdnt']}")
```

### Why Base Files Matter

1. **Avoid Duplication:** Don't re-extract Thayer's if already imported
2. **Cross-Reference Discovery:** Use BDAG/TDNT codes for scholarly article searches
3. **Foundation:** Build on existing data rather than starting from scratch
4. **Quality:** Data already verified and structured

---

## Source 1: BibleHub.com

**URL Pattern:**
- Greek: `https://biblehub.com/greek/{number}.htm`
- Hebrew: `https://biblehub.com/hebrew/{number}.htm`

**Authority:** MEDIUM (aggregator) → HIGH (original lexicons)
**License:** Fair use (aggregator with copyright clearance)

### Available Lexicons

**Greek Words:**
1. **Strong's Exhaustive Concordance** (public domain)
   - Basic definition
   - KJV translation frequency
   - Often already in base file

2. **Thayer's Greek-English Lexicon** (public domain, pre-1895)
   - Comprehensive semantic range
   - Etymology
   - Usage categories (numbered 1, 2, 3...)
   - Often already in base file (check first!)

3. **HELPS Word-studies** (modern, copyright ©)
   - Modern semantic analysis
   - Theological insights
   - Practical applications
   - NOT in base files → extract if available

4. **NAS Exhaustive Concordance** (copyright)
   - Definition from NASB perspective
   - Usage count
   - KJV/NASB translation mapping

**Hebrew Words:**
1. **Strong's Exhaustive Concordance** (public domain)
2. **Brown-Driver-Briggs (BDB)** Hebrew Lexicon (public domain)
   - Often already in base file (check first!)
   - Comprehensive Hebrew lexicon
   - Multiple meaning categories
3. **Gesenius's Lexicon** (public domain, older)

### Additional BibleHub Data

**Usage Statistics Section:**
- Total occurrences count
- Grammatical form breakdown
- Testament distribution (OT/NT)
- **KJV Translation Frequency:**
  - English word: count
  - Ranked by frequency
  - Example: "power" (77×), "mighty work" (11×), etc.

**Related Words Section:**
- Synonyms (other Strong's numbers)
- Root words
- Derived words

**Topical Analysis Section:**
- Biblical themes associated with word
- Cross-references to topical studies

### Extraction Strategy for BibleHub

```python
# Pseudo-code
url = f"https://biblehub.com/greek/{number}.htm"
page = web_fetch(url)

# Extract lexicons (check against base file first!)
if 'Thayer\'s' in page and 'Thayer\'s' not in base_file:
    extract_thayers()  # Full semantic range, etymology

if 'HELPS' in page:
    extract_helps()  # Modern insights, NOT in base file

# Extract usage statistics
usage_stats = {
    'total_occurrences': extract_occurrence_count(),
    'grammatical_forms': extract_form_breakdown(),
    'kjv_translations': extract_kjv_frequency()
}

# Extract related words
related = extract_related_words()  # For relationships tool later
```

### What to Extract vs. Skip

**Extract from BibleHub:**
- ✅ HELPS Word-studies (NOT in base files)
- ✅ Usage statistics (occurrence counts, KJV frequency)
- ✅ Related words (for Tool 5: relationships)
- ✅ Topical analysis sections

**Skip (already in base files):**
- ❌ Strong's basic definition (duplicate)
- ❌ Thayer's (if already imported in base file)
- ❌ BDB (if already imported in base file)

---

## Source 2: StudyLight.org

**URL Pattern:**
- Greek: `https://www.studylight.org/lexicons/eng/greek/{number}.html`
- Hebrew: `https://www.studylight.org/lexicons/eng/hebrew/{number}.html`

**Authority:** MEDIUM (aggregator) → HIGH (original lexicons)
**License:** Fair use (aggregator)

### Available Lexicons

**Greek Words:**
1. **Thayer's Greek-English Lexicon** (public domain)
   - Often already in base file (check first!)

2. **Strong's Concordance** (public domain)
   - Already in base file

3. **Mounce's Concise Greek-English Dictionary** (modern, copyright)
   - Modern NT Greek resource
   - Pedagogical focus
   - NOT in base files → extract if available

4. **Abbott-Smith Manual Greek Lexicon** (public domain/permissive)
   - Scholarly distinctions
   - Synonym analysis
   - NOT typically in base files → extract

5. **LSJ (Liddell-Scott-Jones) Abridged** (public domain)
   - Often already in base file
   - Classical Greek usage
   - Etymology from classical literature

6. **Vocabulary of the Greek New Testament** (Moulton-Milligan)
   - Papyri examples
   - Non-literary Koine usage
   - NOT in base files → extract if available

**Hebrew Words:**
1. **Brown-Driver-Briggs (BDB)** (public domain)
   - Often already in base file (check first!)

2. **Strong's Concordance** (public domain)
   - Already in base file

3. **Gesenius's Hebrew-Chaldee Lexicon** (public domain)

### Unique Value of StudyLight

**Classical Greek Context (LSJ):**
- How word used in Plato, Homer, Aristotle
- Semantic development from Classical → Koine
- Etymology from classical literature

**Papyri Evidence (Vocabulary of Greek NT):**
- Real-world Koine usage (business documents, letters)
- Shows word wasn't just literary/biblical
- Everyday meanings vs. theological meanings

**Scholarly Distinctions (Abbott-Smith):**
- Fine-grained semantic distinctions
- Synonym comparisons
- Technical linguistic notes

### Extraction Strategy for StudyLight

```python
# Pseudo-code
url = f"https://www.studylight.org/lexicons/eng/greek/{number}.html"
page = web_fetch(url)

# Skip lexicons already in base file
skip_if_in_base = ['Thayer\'s', 'Strong\'s', 'LSJ', 'BDB']

# Extract unique lexicons NOT in base
if 'Abbott-Smith' in page:
    extract_abbott_smith()  # Synonym distinctions

if 'Mounce' in page:
    extract_mounce()  # Modern pedagogical

if 'Vocabulary of Greek NT' in page:
    extract_vocabulary_gnt()  # Papyri examples

# For diachronic analysis
if 'LSJ' in page and need_classical_context(word):
    extract_lsj_classical()  # Classical → Koine development
```

### What to Extract vs. Skip

**Extract from StudyLight:**
- ✅ Abbott-Smith (scholarly distinctions)
- ✅ Mounce's (modern perspective)
- ✅ Vocabulary of Greek NT (papyri examples)
- ✅ LSJ classical usage (when doing diachronic analysis)

**Skip (already in base files):**
- ❌ Thayer's (duplicate)
- ❌ Strong's (duplicate)
- ❌ BDB (duplicate for Hebrew)

---

## Source 3: Blue Letter Bible (BLB)

**URL Pattern:**
- Greek: `https://www.blueletterbible.org/lexicon/g{number}/kjv/tr/0-1/`
- Hebrew: `https://www.blueletterbible.org/lexicon/h{number}/kjv/tr/0-1/`

**Authority:** MEDIUM (aggregator) → HIGH (original lexicons)
**License:** Fair use (aggregator)
**Note:** SSL connection issues observed in testing - may need retry logic

### Available Lexicons

**Greek Words:**
1. **Strong's Concordance** (public domain)
   - Already in base file

2. **Thayer's Greek-English Lexicon** (public domain)
   - Often already in base file

3. **TDNT References** (Theological Dictionary of the NT)
   - Reference codes only (not full text)
   - Example: "TDNT 2:286"
   - Cross-reference for scholarly searches

4. **Trench's Synonyms of the New Testament** (public domain)
   - Synonym distinctions
   - When to use word A vs. word B
   - NOT typically in base files → extract

**Hebrew Words:**
- Strong's, Gesenius's, BDB (similar to other sites)
- TWOT references when available

### Unique Value of Blue Letter Bible

**TDNT Reference Codes:**
- Shows which Theological Dictionary volume/page
- Use for scholarly article searches: `"TDNT 2:286"`
- Even without full TDNT text, reference is valuable

**Trench's Synonyms:**
- Explains difference between similar Greek words
- Example: ἀγάπη vs. φιλέω vs. ἔρως (types of love)
- Practical for translators (when to use which synonym)

**Cross-Reference Codes:**
- May show BDAG codes
- May show Louw-Nida domain codes
- Use these for additional web searches

### Extraction Strategy for Blue Letter Bible

```python
# Pseudo-code (note: may need retry logic for SSL issues)
try:
    url = f"https://www.blueletterbible.org/lexicon/g{number}/kjv/tr/0-1/"
    page = web_fetch(url, retry=True)
except SSLError:
    # Known issue - log and continue with other sources
    log_warning(f"BLB SSL error for {number}, skipping")
    return

# Extract unique data NOT in base files
if 'TDNT' in page:
    tdnt_ref = extract_tdnt_reference()  # e.g., "2:286"
    # Store for scholarly searches

if 'Trench' in page:
    extract_trench_synonyms()  # Synonym distinctions

# Cross-reference codes
extract_cross_refs()  # BDAG, Louw-Nida codes for searches
```

### What to Extract vs. Skip

**Extract from BLB:**
- ✅ TDNT reference codes (for scholarly searches)
- ✅ Trench's Synonyms (distinctions between similar words)
- ✅ Cross-reference codes (BDAG, Louw-Nida)
- ✅ Louw-Nida domain codes (semantic domains)

**Skip (already in base files):**
- ❌ Strong's (duplicate)
- ❌ Thayer's (if in base file)

---

## Summary Table: What to Extract Where

| Lexicon/Data | Base File | BibleHub | StudyLight | BLB |
|-------------|-----------|----------|------------|-----|
| **Strong's** | ✅ Skip | ❌ Skip | ❌ Skip | ❌ Skip |
| **Thayer's** | ✅ Check first | ⚠️ Skip if in base | ⚠️ Skip if in base | ⚠️ Skip if in base |
| **BDB (Hebrew)** | ✅ Check first | ⚠️ Skip if in base | ⚠️ Skip if in base | ⚠️ Skip if in base |
| **LSJ (Classical)** | ✅ Check first | ❌ Not available | ⚠️ Skip if in base | ❌ Not available |
| **HELPS Word-studies** | ❌ Not present | ✅ **Extract** | ❌ Not available | ❌ Not available |
| **Abbott-Smith** | ❌ Not present | ❌ Not available | ✅ **Extract** | ❌ Not available |
| **Mounce's** | ❌ Not present | ❌ Not available | ✅ **Extract** | ❌ Not available |
| **Vocabulary of Greek NT** | ❌ Not present | ❌ Not available | ✅ **Extract** | ❌ Not available |
| **Trench's Synonyms** | ❌ Not present | ❌ Not available | ❌ Not available | ✅ **Extract** |
| **Usage Statistics** | ❌ Not present | ✅ **Extract** | ⚠️ Sometimes | ⚠️ Sometimes |
| **TDNT References** | ⚠️ Sometimes | ❌ Not available | ❌ Not available | ✅ **Extract** |
| **Cross-Ref Codes** | ⚠️ Sometimes | ❌ Rarely | ❌ Rarely | ✅ **Extract** |

**Legend:**
- ✅ Extract this data
- ❌ Skip (duplicate or not available)
- ⚠️ Check first (may be in base file)

---

## Extraction Priority Order

### Priority 1: Base Strong's File (ALWAYS FIRST)
1. Read `./bible/words/strongs/{number}/{number}.strongs.yaml`
2. Note what's already present
3. Extract cross-reference codes for additional searches
4. **Do NOT proceed until this is done!**

### Priority 2: BibleHub (Most Comprehensive)
1. Extract HELPS Word-studies (unique modern insights)
2. Extract usage statistics (occurrences, KJV frequency)
3. Note related words (for Tool 5)

### Priority 3: StudyLight (Unique Classical/Papyri)
1. Extract Abbott-Smith (synonym distinctions)
2. Extract Vocabulary of Greek NT (papyri examples)
3. Extract Mounce's (modern pedagogical)
4. Extract LSJ classical usage (only if doing diachronic analysis)

### Priority 4: Blue Letter Bible (Cross-References)
1. Extract TDNT reference codes
2. Extract Trench's Synonyms
3. Extract cross-reference codes (BDAG, Louw-Nida)
4. **Note:** May fail due to SSL issues - non-blocking

---

## Authority Levels

**HIGH Authority (Published Lexicons):**
- Thayer's, BDB, LSJ, Abbott-Smith, Mounce's, Vocabulary of Greek NT, Trench's
- Cite as: `{thayer}`, `{bdb}`, `{lsj-abridged}`, etc.

**MEDIUM Authority (Aggregator Sites):**
- HELPS Word-studies (modern, not public domain but reliable)
- Usage statistics from BibleHub (verified against concordances)
- Cite as: `{helps}`, `{biblehub-lexicon}` with authority note

**Cross-Reference Codes:**
- TDNT, BDAG, Louw-Nida references
- Use for scholarly searches, not as primary data
- Cite as: `{tdnt-ref}`, `{bdag-code}`, etc.

---

## Fair Use Compliance

**Convergence Grouping:**
```yaml
# Correct: List lexicons that agree collectively
etymology:
  derivation_note: "From root δύναμαι (to be able) {thayer} {helps} {biblehub}"
  convergence: "All major lexicons agree on etymology"
```

**Divergence Context:**
```yaml
# Correct: Quote different views in comparative context
divergence:
  classical_usage: "Means 'physical strength' in Plato {lsj}"
  koine_usage: "Shifts to 'miraculous power' in NT {thayer}"
  note: "Semantic shift from Classical to Koine Greek" {llm-cs45}
```

**Do NOT Do:**
```yaml
# WRONG: Full lexicon entry reproduction
thayers_full_entry: "1. strength, power... 2. ability... 3. miracle..."
# This enables reconstruction of copyrighted work!
```

---

## Next Steps

1. Use this inventory when designing extraction methods
2. Create extraction code that reads base files FIRST
3. Skip duplicates, extract unique data only
4. Apply convergence grouping for fair use
5. Mark authority levels clearly

**See Also:**
- `extraction-methods.md` - How to extract from each source
- `convergence-patterns.md` - How to identify agreement/divergence
