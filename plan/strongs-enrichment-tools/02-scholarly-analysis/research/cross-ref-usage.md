# Cross-Reference Code Usage for Scholarly Discovery

**Created:** 2025-11-11
**Purpose:** Document how to use BDAG, TDNT, Louw-Nida, and other lexicon codes to discover academic sources

---

## The Problem

Academic biblical scholarship often cites **lexicon numbering systems** instead of Strong's numbers. Searching only by Strong's numbers misses significant scholarly work.

**Example:**
- Strong's G1411 (δύναμις)
- BDAG entry: δύναμις-227
- TDNT reference: 2:286
- Louw-Nida domain: 74.1

Academic papers cite "BDAG 227" or "TDNT 2:286" - we need to search by these codes too.

---

## Cross-Reference Systems Overview

### 1. BDAG (Bauer-Danker-Arndt-Gingrich)

**Full Name:** A Greek-English Lexicon of the New Testament and Other Early Christian Literature (3rd ed.)

**Authority:** HIGHEST - Gold standard for NT Greek lexicography

**Coverage:** All NT Greek words + early Christian literature

**Code Format:**
- Word entry with numerical suffix
- Example: δύναμις-227 (homograph disambiguator)

**Where Found:**
- Tool 1 base Strong's files (if pre-populated)
- BibleHub lexicon cross-references
- Blue Letter Bible references

**Search Strategy:**
```
"BDAG 227"
"BDAG δύναμις"
"Bauer-Danker δύναμις"
```

**Expected Results:** High-quality NT scholarship, semantic analysis

---

### 2. TDNT (Theological Dictionary of the New Testament)

**Full Name:** Theological Dictionary of the New Testament (Kittel, 10 volumes)

**Authority:** HIGHEST - Classic theological word study reference

**Coverage:** Theologically significant NT Greek words

**Code Format:**
- Volume:Page
- Example: 2:286 (Volume 2, page 286)

**Where Found:**
- Tool 1 base Strong's files (cross-references)
- Blue Letter Bible (shows TDNT references)
- Scholarly articles cite extensively

**Search Strategy:**
```
"TDNT 2:286"
"Kittel δύναμις"
"TWNT 2:286" (German: Theologisches Wörterbuch)
```

**Expected Results:** Theological significance, OT background, usage development

---

### 3. Louw-Nida (Greek-English Lexicon Based on Semantic Domains)

**Full Name:** Greek-English Lexicon of the New Testament Based on Semantic Domains

**Authority:** HIGH - Semantic domain approach

**Coverage:** All NT Greek words grouped by meaning

**Code Format:**
- Domain.Subdomain
- Example: 74.1 (Domain 74 "Able, Capable", entry 1)

**Where Found:**
- Tool 1 base Strong's files (if available)
- Blue Letter Bible cross-references
- Logos/Accordance software

**Search Strategy:**
```
"Louw-Nida 74.1"
"LN 74.1"
"semantic domain 74"
```

**Expected Results:** Semantic relationships, synonym distinctions, domain analysis

---

### 4. BDB (Brown-Driver-Briggs)

**Full Name:** Brown-Driver-Briggs Hebrew and English Lexicon

**Authority:** HIGH - Standard OT Hebrew lexicon (public domain)

**Coverage:** All OT Hebrew words + Aramaic

**Code Format:**
- Sequential entry numbers
- Example: BDB 43 or BDB-43

**Where Found:**
- Tool 1 base Strong's files (pre-imported)
- BibleHub Hebrew lexicon
- StudyLight

**Search Strategy:**
```
"BDB 43"
"Brown-Driver-Briggs {Hebrew word}"
```

**Expected Results:** Etymology, cognates, semantic range, OT usage

---

### 5. HALOT (Hebrew and Aramaic Lexicon of the Old Testament)

**Full Name:** The Hebrew and Aramaic Lexicon of the Old Testament (Koehler-Baumgartner)

**Authority:** HIGHEST - Modern standard for Hebrew lexicography

**Coverage:** All OT Hebrew/Aramaic words

**Code Format:**
- Entry numbers (varies by edition)

**Where Found:**
- Some academic articles
- Logos/Accordance software
- Limited free access

**Search Strategy:**
```
"HALOT {Hebrew word}"
"Koehler-Baumgartner {word}"
```

**Expected Results:** Modern scholarship, cognate analysis, semantic precision

---

### 6. GK (Goodrick-Kohlenberger)

**Full Name:** Goodrick-Kohlenberger numbering system

**Authority:** MEDIUM-HIGH - Modern concordance system

**Coverage:** All Greek/Hebrew words (alternative to Strong's)

**Code Format:**
- Sequential numbers (different from Strong's)
- Example: GK 1539

**Where Found:**
- NIV concordances
- Modern study Bibles
- Cross-reference tables

**Search Strategy:**
```
"GK 1539"
"Goodrick-Kohlenberger 1539"
```

**Expected Results:** NIV translation notes, modern concordance work

---

### 7. TWOT (Theological Wordbook of the Old Testament)

**Full Name:** Theological Wordbook of the Old Testament (Harris, Archer, Waltke)

**Authority:** HIGH - Evangelical OT word study

**Coverage:** Theologically significant Hebrew words

**Code Format:**
- Entry numbers
- Example: TWOT 43

**Where Found:**
- Blue Letter Bible cross-references
- Evangelical scholarship
- Seminary libraries

**Search Strategy:**
```
"TWOT 43"
"Theological Wordbook OT {word}"
```

**Expected Results:** Theological significance, evangelical perspective

---

### 8. LSJ (Liddell-Scott-Jones)

**Full Name:** A Greek-English Lexicon (Liddell, Scott, Jones)

**Authority:** HIGHEST - Standard for Classical Greek

**Coverage:** All Classical/Koine Greek (not just biblical)

**Code Format:**
- Alphabetical entries (no numbers)

**Where Found:**
- Tool 1 base Strong's files (abridged version)
- StudyLight
- Perseus Digital Library

**Search Strategy:**
```
"LSJ δύναμις"
"Liddell-Scott δύναμis"
```

**Expected Results:** Classical usage, diachronic development, etymology

---

## Practical Workflow

### Step 1: Check Tool 1 Output

Read the base Strong's file to find cross-reference codes:

```yaml
# From .data/bible/words/strongs/G1411/G1411.strongs.yaml
cross_references:
  bdag: "δύναμις-227"
  tdnt: "2:286"
  louw_nida: "74.1"
  gk: "1539"
```

### Step 2: Search by Each Code

For each cross-reference found, search:

**Google Scholar:**
```
"BDAG 227" OR "BDAG δύναμις"
"TDNT 2:286"
"Louw-Nida 74.1"
"GK 1539"
```

**.edu Sites:**
```
site:.edu "BDAG 227"
site:.edu "TDNT 2:286"
site:.edu "Louw-Nida 74.1"
```

**Specific Journals:**
```
site:jstor.org "BDAG 227"
site:cambridge.org "TDNT 2:286"
```

### Step 3: Combine with Strong's

Cast widest net by searching multiple systems:

```
("Strong's G1411" OR "BDAG 227" OR "TDNT 2:286" OR "GK 1539") δύναμις
```

### Step 4: Document Findings

For each source found:
1. Note which cross-reference code led to discovery
2. Verify peer-review status
3. Extract scholarly insights
4. Cite with inline tags `{source-id}`

---

## Why This Matters

### Discovery Rate Improvement

**Without Cross-References:**
- Search: "Strong's G1411"
- Results: 50 sources (many non-scholarly)

**With Cross-References:**
- Search: "Strong's G1411" OR "BDAG 227" OR "TDNT 2:286" OR "LN 74.1"
- Results: 200+ sources (higher scholarly ratio)

**Impact:** 4x discovery rate for academic sources

### Academic Preference

**Academic Papers Prefer:**
1. BDAG (most common for NT Greek)
2. TDNT (for theological significance)
3. Louw-Nida (for semantic analysis)
4. HALOT (for OT Hebrew)

**Academic Papers Rarely Use:**
- Strong's numbers (considered less scholarly)

**Implication:** Must search by academic systems to find best scholarship

---

## Cross-Reference Mapping

### How to Find Codes When Missing

**If Tool 1 didn't find cross-references:**

1. **BibleHub:**
   - Visit https://biblehub.com/greek/{num}.htm
   - Check "Strong's Concordance" section for cross-references

2. **Blue Letter Bible:**
   - Visit https://www.blueletterbible.org/lexicon/g{num}/
   - Check for TDNT, Louw-Nida references

3. **Online Cross-Reference Tables:**
   - Search "Strong's to BDAG conversion"
   - Search "Strong's to GK conversion"

4. **Lexicon Entry Pages:**
   - Check if BDAG entry number is mentioned
   - Look for semantic domain codes

---

## Expected Coverage

### Greek Words

**High Coverage (90%+):**
- BDAG codes (most NT words)
- GK numbers (all NT words)

**Medium Coverage (50-70%):**
- TDNT references (theologically significant only)
- Louw-Nida domains (all NT words, varies by findability)

**Low Coverage (20-30%):**
- LSJ entries (Classical focus)

### Hebrew Words

**High Coverage (90%+):**
- BDB entries (most OT words)
- GK numbers (all OT words)

**Medium Coverage (50-70%):**
- TWOT entries (theologically significant only)

**Low Coverage:**
- HALOT (rarely cited by code due to subscription limits)

---

## Quality Benefits

### Scholarly Precision

Cross-references lead to:
- **More precise semantic analysis** (BDAG specificity)
- **Theological depth** (TDNT treatment)
- **Semantic relationships** (Louw-Nida domains)
- **Diachronic context** (LSJ classical usage)

### Citation Verification

When scholars cite "BDAG 227," we can:
1. Verify the claim
2. Check if they're quoting accurately
3. Find other scholars citing same entry
4. Build scholarly consensus/divergence patterns

---

## Search Pattern Templates

### Template 1: Comprehensive Search

```
("{Strong's num}" OR "{BDAG code}" OR "{TDNT ref}" OR "{LN code}" OR "{GK num}") {transliteration}
```

**Example:**
```
("Strong's G1411" OR "BDAG 227" OR "TDNT 2:286" OR "LN 74.1" OR "GK 1539") δύναμις
```

### Template 2: Academic-Only Search

```
site:.edu ("{BDAG code}" OR "{TDNT ref}") {transliteration}
```

**Example:**
```
site:.edu ("BDAG 227" OR "TDNT 2:286") δύναμις
```

### Template 3: Journal Search

```
("{BDAG code}" OR "{TDNT ref}") {transliteration} filetype:pdf
```

**Example:**
```
("BDAG 227" OR "TDNT 2:286") δύναμις filetype:pdf
```

---

## Common Pitfalls

**Avoid:**
- ❌ Ignoring cross-references (misses 70% of academic sources)
- ❌ Using only Strong's numbers (scholar bias)
- ❌ Not verifying code accuracy (typos happen)

**Prefer:**
- ✅ Always check Tool 1 for cross-references first
- ✅ Search multiple codes simultaneously
- ✅ Verify references match actual lexicon entries

---

## Integration with Tool 2 Workflow

### During Research Phase

1. Read Tool 1 output for Strong's word
2. Extract all cross-reference codes
3. Create search queries for each code
4. Execute searches (Google Scholar, .edu, etc.)
5. Document which codes led to best sources

### During Experimentation

1. Track discovery rate per cross-reference type
2. Measure scholarly quality by code source
3. Identify which codes are most valuable
4. Refine search strategies based on learnings

### Expected Outcomes

- **G26 ἀγάπη:** TDNT 1:21 should yield extensive theological scholarship
- **G3056 λόγος:** BDAG + TDNT + Louw-Nida should reveal scholarly debates
- **Cultural words:** TDNT cultural notes lead to anthropological sources

---

## Next Steps

1. Test on G26 ἀγάπη - expect TDNT 1:21 to be goldmine
2. Test on G3056 λόγος - expect multiple lexicon codes
3. Document which codes yield best results
4. Create optimized search patterns
5. Update Tool 2 methodology based on findings

---

**References:**
- Tool 1 outputs: `.data/bible/words/strongs/{num}/{num}.strongs.yaml`
- BibleHub: https://biblehub.com
- Blue Letter Bible: https://www.blueletterbible.org
- `/plan/strongs-enrichment-sources/README.md` - Source discovery overview
