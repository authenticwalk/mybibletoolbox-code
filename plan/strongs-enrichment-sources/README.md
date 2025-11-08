# Strong's Number Enrichment: Source Discovery Strategies

**Created:** 2025-11-08
**Status:** Planning
**Purpose:** Comprehensive brainstorm of methods to discover lexicons, word study books, scholarly articles, and other sources for enriching Strong's number data while respecting fair use policies.

---

## Executive Summary

Strong's Concordance provides basic definitions for 14,197 Greek and Hebrew words, but translators, pastors, and students need "a book's worth of information" per word: etymology, semantic ranges, scholarly insights, usage patterns, controversies, and cultural context. This document explores multiple strategies for discovering authoritative sources to enrich this data.

**Key Constraint:** All sources must comply with fair use policy (see `/plan/policy/fair-use.md`):
- Focus on convergence grouping (list sources that agree)
- Quote divergence in comparative analysis context
- Always use inline citations
- Never enable programmatic reconstruction of copyrighted works

---

## Strategy 0: Start with Base Strong's Files (ALWAYS FIRST!)

### Critical Foundation

**Location:** `./bible/words/strongs/{number}/{number}.strongs.yaml`

**What's Already There:**
- 14,197 Strong's word files (G0001-G5624 Greek, H0001-H8674 Hebrew)
- Pre-imported open-licensed data from:
  - **BDB** (Brown-Driver-Briggs) - Hebrew lexicon
  - **Thayer's** - Greek lexicon
  - **unfoldingWord** - Translation Words
  - **LSJ** (Liddell-Scott-Jones) - Classical Greek lexicon
- **Cross-reference codes** to other lexicon systems (when available):
  - BDB, BDAG, Louw-Nida, TDNT, GK (Goodrick-Kohlenberger), TWOT, LSJ

**CRITICAL RULE:** Always read the base Strong's file FIRST before doing any research!

**Why This Matters:**
1. Avoid duplicating data already imported
2. Use cross-reference codes for additional searches
3. Build on existing foundation rather than starting from scratch
4. Many scholarly articles cite multiple numbering systems - cross-references unlock broader discovery

**Discovery Method:**
1. Read `./bible/words/strongs/{number}/{number}.strongs.yaml`
2. Note what data is already present
3. Note any cross-reference codes (BDAG, TDNT, Louw-Nida, etc.)
4. Use those codes for web searches: `"BDAG {code}"`, `"Louw-Nida {domain}"`, etc.
5. Only research what's NOT already in the file

**Example:**
```bash
# Always start here:
cat ./bible/words/strongs/G1411/G1411.strongs.yaml

# If it has cross-references like:
# bdag: "δύναμις-227"
# tdnt: "2:286"
# louw_nida: "74.1"

# Then search by those too:
# "BDAG δύναμις-227"
# "TDNT 2:286"
# "Louw-Nida 74.1"
```

---

## Strategy 1: Aggregator Sites with Copyright Clearance

### 1.1 BibleHub.com

**Advantage:** They've already handled copyright negotiations for many lexicons.

**Available Resources:**
- **Thayer's Greek Lexicon** (public domain) - comprehensive NT Greek lexicon
- **HELPS Word-studies** - modern semantic analysis
- **NAS Exhaustive Concordance** - usage statistics
- **Strong's Exhaustive Concordance** (public domain)
- Usage statistics: total occurrences, grammatical form breakdown
- Cross-references to related Strong's numbers

**URL Patterns (from ATTRIBUTION.md):**
- Greek: `https://biblehub.com/greek/{number}.htm`
- Hebrew: `https://biblehub.com/hebrew/{number}.htm`
- Interlinear: `https://biblehub.com/interlinear/{book}/{chapter}-{verse}.htm`

**Discovery Method:**
- Direct URL templating using Strong's number
- Extract convergence patterns from lexicon quotes
- Document usage statistics exactly as shown
- Note cross-references for related word research

**Fair Use Compliance:**
- BibleHub shows excerpts, not full lexicon entries
- We can cite their aggregated data with `{biblehub-lexicon}` attribution
- Focus on convergence patterns rather than full reproduction

---

### 1.2 StudyLight.org

**Advantage:** Offers lexicons not available elsewhere, especially classical Greek resources.

**Available Lexicons (from research):**
- **Thayer's Greek Lexicon** (public domain)
- **Strong's Concordance** (public domain)
- **Mounce's Dictionary** - modern NT Greek reference
- **Abbott-Smith Manual Greek Lexicon** - scholarly distinctions
- **Liddell-Scott-Jones (LSJ)** - classical Greek context (abridged version, public domain)
- **Vocabulary of the Greek NT** - historical development insights
- **Hebrew equivalents** - LXX connections

**URL Pattern:**
- Greek: `https://www.studylight.org/lexicons/eng/greek/{number}.html`
- Hebrew: `https://www.studylight.org/lexicons/eng/hebrew/{number}.html`

**Discovery Method:**
- Direct URL templating
- LSJ particularly valuable for diachronic analysis (Classical → Koine development)
- Abbott-Smith good for synonym distinctions
- Vocabulary of Greek NT for papyri examples

**Fair Use Compliance:**
- Cite as `{studylight-lexicon}` or specific lexicon name
- Document convergence patterns
- Use LSJ for etymology verification

---

### 1.3 Blue Letter Bible (BLB)

**Advantage:** TDNT references, Trench's Synonyms, cross-reference codes.

**Available Resources:**
- **Strong's Concordance** (public domain)
- **Thayer's Greek Lexicon** (public domain)
- **TDNT references** - theological dictionary citations (may not have full text)
- **Trench's Synonyms** - synonym distinctions
- **Cross-reference codes** - links to other numbering systems

**URL Pattern (from ATTRIBUTION.md):**
- Greek: `https://www.blueletterbible.org/lexicon/g{number}/kjv/tr/0-1/`
- Hebrew: `https://www.blueletterbible.org/lexicon/h{number}/kjv/tr/0-1/`

**Discovery Method:**
- Direct URL templating
- Extract TDNT reference codes for further research
- Note Trench's synonym distinctions when available
- Document cross-reference codes (BDAG, Louw-Nida, etc.)

**Caution:**
- May show TDNT references without full content
- Don't fabricate TDNT content - only cite what's actually shown

**Note:** SSL connection failed during initial test - may need retry logic or alternative access method.

---

### 1.4 Bible Gateway

**Advantage:** Large translation database, interlinear tools, commentary access.

**URL Pattern (from ATTRIBUTION.md):**
- `https://www.biblegateway.com/passage/?search={ref}&version={VER}`

**Discovery Method:**
- Search by verse reference, not Strong's number
- Useful for seeing how multiple translations render a specific occurrence
- Convergence/divergence patterns for translation guidance
- May have Strong's number tagging in interlinear view

**Fair Use Compliance:**
- Use for convergence grouping of translation patterns
- Cite as `{biblegateway}`

---

## Strategy 2: Web Search Discovery

### 2.1 Generic Strong's Number Search

**Search Queries:**
- `"Strong's G{number}"` or `"Strong's H{number}"`
- `"Strong's {number}"` (without prefix)
- `"{transliteration} Greek etymology"`
- `"{transliteration} Hebrew etymology"`

**Expected Results:**
- Blog posts analyzing specific words
- Seminary websites with word study resources
- Theological articles citing Strong's numbers
- Study guides and teaching materials

**Discovery Method:**
1. Perform web search with Strong's number
2. Evaluate source authority (seminary > blog > personal website)
3. Extract cited lexicons and scholarly sources
4. Document convergence/divergence patterns
5. Note controversies or common misconceptions

**Fair Use Compliance:**
- Quote blog insights in comparative context
- Mark authority level (high/medium/low)
- Cite as `{source-url}` with authority note

---

### 2.2 Cross-Reference Code Search

**Background:** Many Strong's numbers have cross-references to other lexicon numbering systems (see bible-study-tools/strongs-word-research/README.md:60-74).

**Cross-Reference Systems:**
- **BDB** - Brown-Driver-Briggs (Hebrew)
- **BDAG** - Bauer-Danker-Arndt-Gingrich (Greek)
- **Louw-Nida** - Semantic domain system
- **TDNT** - Theological Dictionary of NT
- **GK** - Goodrick-Kohlenberger numbering
- **TWOT** - Theological Wordbook of OT (Hebrew)
- **LSJ** - Liddell-Scott-Jones (Classical Greek)

**Search Queries:**
- `"BDAG {code}"` - finds scholarly articles citing this lexicon entry
- `"BDB {code}"` - Hebrew lexicon references
- `"Louw-Nida {domain}"` - semantic domain discussions
- `"TDNT {reference}"` - theological dictionary citations
- `"GK {number}"` or `"Goodrick-Kohlenberger {number}"`
- `"TWOT {code}"` - Hebrew theological wordbook

**Discovery Method:**
1. Check if Strong's base file has cross-reference codes
2. If present, search by those codes as well as Strong's number
3. Many scholarly articles cite multiple numbering systems
4. Extract convergence patterns from multiple sources

**Advantage:**
- Academic articles often use BDAG/TDNT/Louw-Nida instead of Strong's
- Casting wider net finds more scholarly sources
- Multiple citation systems increase discovery coverage

---

### 2.3 Academic Site Search

**Search Queries:**
- `"{transliteration} {gloss} biblical" site:.edu`
- `"{transliteration} New Testament usage" site:.edu`
- `"Strong's {number}" site:.edu`
- `"{word} semantic range" site:.edu`

**Expected Results:**
- Seminary course materials
- Linguistic dissertations
- Journal article preprints
- Faculty research pages

**Discovery Method:**
1. Search `.edu` domains for academic authority
2. Look for PDF preprints, course notes, research pages
3. Extract bibliography references for additional sources
4. Note scholarly consensus/divergence patterns

**Fair Use Compliance:**
- Academic insights quoted in scholarly analysis context
- Cite with full URL and author when available
- Mark as high authority (scholarly source)

---

### 2.4 PDF Search

**Search Queries:**
- `"{transliteration} New Testament" filetype:pdf`
- `"Strong's {number}" filetype:pdf`
- `"{word} Greek lexicon" filetype:pdf`
- `"{word} semantic analysis" filetype:pdf`

**Expected Results:**
- Journal article PDFs
- Thesis/dissertation excerpts
- Seminary handouts
- Book previews (limited pages)

**Discovery Method:**
1. Search for PDF-specific results
2. Preview/excerpt pages often available without full access
3. Extract cited lexicons and conclusions
4. Document in bibliography for verification

**Caution:**
- Respect copyright - use only available excerpts/previews
- Don't extract full copyrighted PDFs
- Focus on publicly available academic papers

---

### 2.5 Controversy & Misconception Search

**Search Queries:**
- `"{transliteration} misconception"`
- `"{transliteration} controversy"`
- `"Strong's {number}" error`
- `"{word} not from {false-etymology}"`

**Example:** "dunamis dynamite" controversy

**Discovery Method:**
1. Search for common teaching errors
2. Find scholarly refutations
3. Document both the error and the correction
4. Cite sources for refutation

**Fair Use Compliance:**
- Quote error and refutation in comparative context
- Provide evidence for correction
- Mark authority levels clearly

**Value:** Prevents AI systems from perpetuating common errors.

---

## Strategy 3: Community Discussion Platforms

### 3.1 Biblical Hermeneutics Stack Exchange

**URL:** https://hermeneutics.stackexchange.com

**Search Methods:**
- Search by Strong's number
- Search by transliteration
- Search by English keyword + "Greek" or "Hebrew"

**Available Content:**
- Q&A discussions on word meanings
- Scholarly debates on semantic range
- Tool recommendations for word study
- Cross-references to LXX and Hebrew equivalents

**Discovery Value:**
- Documents areas of scholarly debate
- Identifies common questions/misconceptions
- References to authoritative tools and lexicons
- Links to related academic resources

**Fair Use Compliance:**
- User content is Creative Commons licensed
- Cite as `{bhse-discussion}` with authority level: Low (community)
- Use to document controversies, not as primary authority
- Verify claims from community discussions with lexicons

---

### 3.2 Biblical Language Blogs

**Examples from ATTRIBUTION.md:**
- **Scribal Cafe** - https://scribalcafe.wordpress.com (biblical languages)
- **GotQuestions.org** - https://www.gotquestions.org (theological Q&A)
- **Word Study Tools** - https://wordstudytools.com

**Search Methods:**
- Direct site search: `site:scribalcafe.wordpress.com "{word}"`
- Generic web search brings up relevant posts
- Follow blog categories for systematic coverage

**Discovery Value:**
- Scholars often debunk misconceptions on blogs
- Accessible explanations of complex lexical issues
- Citations to authoritative sources
- Current scholarly discussions

**Fair Use Compliance:**
- Quote insights in comparative context
- Cite as `{source-blog}` with authority level: Medium
- Use to supplement, not replace, lexicon data

---

## Strategy 4: Published Lexicons via Libraries

### 4.1 Public Domain Lexicons

**Fully Available (no restrictions):**

**Greek:**
- **Strong's Exhaustive Concordance** (1890) - public domain
- **Thayer's Greek-English Lexicon** (pre-1895) - public domain
- **Liddell-Scott-Jones (LSJ)** - abridged version public domain
- **Abbott-Smith Manual Greek Lexicon** - check copyright status

**Hebrew:**
- **Brown-Driver-Briggs (BDB)** - public domain
- **Strong's Hebrew dictionary** - public domain

**Discovery Method:**
- These are already available on BibleHub, StudyLight, BLB
- Can be quoted extensively without restriction
- Use as primary authority for semantic ranges

**Sources:**
- OpenScriptures projects (github.com/openscriptures)
- CCEL (Christian Classics Ethereal Library)
- Archive.org (public domain scans)

---

### 4.2 Open License Projects

**unfoldingWord Resources:**
- **translationWords** - github.com/unfoldingWord/translationWords
- Open license (Creative Commons)
- Designed for Bible translators
- Keyed to Strong's numbers

**OpenScriptures:**
- **Strong's database** - github.com/openscriptures/strongs
- **BDB Hebrew Lexicon** - github.com/openscriptures/HebrewLexicon
- Open licenses
- Structured data formats (JSON/XML)

**Discovery Method:**
1. Clone/download open-licensed repositories
2. Import structured data directly
3. Cite as `{source-project}` with license noted
4. Use as supplementary data

**Advantage:** Can be imported wholesale, not just quoted.

---

### 4.3 Copyrighted Lexicons (Fair Use Only)

**Premium Lexicons (limited access):**

**Greek:**
- **BDAG** (Bauer-Danker-Arndt-Gingrich) - $$$, standard NT Greek lexicon
- **TDNT** (Theological Dictionary of NT) - 10 volumes
- **Louw-Nida** - semantic domain lexicon

**Hebrew:**
- **HALOT** (Hebrew and Aramaic Lexicon of OT) - $$$, standard OT lexicon
- **TWOT** (Theological Wordbook of OT)

**Discovery Methods:**

**Via Aggregator Sites:**
- BibleHub may show BDAG excerpts
- BLB may show TDNT reference codes
- Cite what's actually shown, don't fabricate

**Via Academic Libraries:**
- University library guides often cite these lexicons
- Seminary websites may quote excerpts in educational materials
- Extract cited insights with proper attribution

**Via Software Previews:**
- Logos, Accordance, OliveTree may have sample entries
- Use preview content only (respect terms of service)
- Document what's publicly accessible

**Fair Use Compliance:**
- Quote only what's necessary for scholarly analysis
- Never extract full entries
- Focus on convergence patterns
- Use in comparative context with other lexicons
- Mark as high authority
- Cannot be primary source (we don't own them)

---

## Strategy 5: Scholarly Journal Discovery

### 5.1 Open Access Journals

**Search Strategies:**
- Google Scholar: `"{transliteration}" OR "Strong's {number}"`
- Directory of Open Access Journals (DOAJ): search biblical studies
- Academia.edu: search for biblical language papers
- ResearchGate: author-shared preprints

**Expected Resources:**
- Journal of Biblical Literature (some open access)
- Biblical studies journals from seminaries
- Linguistic analysis papers
- Exegetical studies

**Discovery Method:**
1. Search by Strong's number, transliteration, or cross-reference codes
2. Filter for open access / freely available
3. Extract semantic insights and scholarly consensus
4. Document bibliography for source verification

**Fair Use Compliance:**
- Quote insights in scholarly analysis context
- Cite full journal reference
- Mark as high authority (peer-reviewed)

---

### 5.2 Seminary Publications

**Resources:**
- Seminary journals (often have open access policies)
- Faculty publications (may be available on university sites)
- Thesis/dissertation abstracts
- Course materials and syllabi

**Search Methods:**
- Search seminary websites directly
- Use Google Scholar filtered by institution
- Search `.edu` domains for specific seminaries

**Discovery Value:**
- High scholarly authority
- Often focused on practical application
- May address translation challenges directly

---

### 5.3 Bible Translation Organizations

**Organizations:**
- **Wycliffe Bible Translators** - translation resources
- **SIL International** - linguistic research
- **United Bible Societies** - translation handbooks
- **Pioneer Bible Translators** - field insights

**Discovery Methods:**
- Search organizational websites for word study resources
- Look for translator handbooks and guides
- Check for linguistic databases
- Review translation notes repositories

**Expected Resources:**
- Practical translation guidance
- Cross-cultural semantic challenges
- Receptor language examples
- Common translation pitfalls

**Fair Use Compliance:**
- Quote translation insights in educational context
- Cite organizational sources with URL
- Mark authority based on source type

---

## Strategy 6: Specialized Search Approaches

### 6.1 Septuagint (LXX) Research

**Purpose:** Understand how Hebrew words were translated into Greek, which often influences NT Greek word choice.

**Resources:**
- **CCAT/CATSS Parallel Aligned Hebrew-Greek Scriptures** - gold standard
- **Apostolic Bible Polyglot** - interlinear LXX
- BibleHub interlinear (includes LXX)

**Discovery Method:**
1. Find Hebrew Strong's number in OT
2. Look up corresponding LXX Greek word
3. Trace NT usage of that Greek word
4. Document semantic transfer patterns

**Search Queries:**
- `"{Hebrew-word} Septuagint Greek"`
- `"LXX {Hebrew-word}"`
- Site:hermeneutics.stackexchange.com for LXX discussions

**Value:** Explains why NT writers chose specific Greek words.

---

### 6.2 Papyri and Inscriptions

**Purpose:** See how words were used in everyday Koine Greek, not just biblical texts.

**Resources:**
- **Vocabulary of the Greek NT** (Moulton-Milligan) - papyri examples (on StudyLight)
- **DDBDP** (Duke Databank of Documentary Papyri) - searchable
- Inscriptions databases

**Discovery Method:**
- StudyLight's "Vocabulary of Greek NT" entries show papyri usage
- Search DDBDP for word attestations
- Compare biblical vs. non-biblical usage patterns

**Value:** Corrects anachronistic theological readings; shows everyday meanings.

---

### 6.3 Classical Literature

**Purpose:** Trace diachronic development (Classical Greek → Koine → Modern).

**Resources:**
- **LSJ (Liddell-Scott-Jones)** - comprehensive classical Greek lexicon (abridged on StudyLight)
- **Perseus Digital Library** - classical texts with morphological analysis
- **Thesaurus Linguae Graecae** (TLG) - comprehensive Greek corpus (subscription)

**Discovery Method:**
- StudyLight provides LSJ entries
- Perseus for specific classical author usage
- Note semantic shifts from Classical to Koine

**Search Queries:**
- `"{word} classical Greek Plato"`
- `"{word} LSJ definition"`
- `"{word} Homer Septuagint"` (trace development)

**Value:** Etymology verification; prevents false etymologies.

---

### 6.4 Cognate Languages

**Purpose:** Understand Hebrew through related Semitic languages.

**Resources:**
- **Comprehensive Aramaic Lexicon (CAL)** - online, free
- Akkadian dictionaries
- Ugaritic cognates
- Arabic cognates

**Discovery Method:**
- CAL for Aramaic parallels
- Academic articles on cognate analysis
- Etymological notes in BDB often cite cognates

**Search Queries:**
- `"{Hebrew-word} Aramaic cognate"`
- `"{Hebrew-word} Ugaritic"`
- `"{Hebrew-word} Akkadian etymology"`

**Value:** Clarifies difficult Hebrew words through comparative Semitic linguistics.

---

## Strategy 7: Cross-Linguistic Translation Patterns (TBTA Approach)

### 7.1 Extract Patterns from Existing Translations

**Purpose:** Understand how 900+ Bible translations handle each Strong's word across different linguistic features.

**The Idea (from TBTA Strong's hints):**
- For each Strong's word, analyze how it's translated across multiple languages
- Identify patterns: "When language X uses word Y → linguistic feature Z"
- Document convergence: "5/5 Austronesian languages use exclusive form"
- Flag divergence: "Languages split 50/50 on this usage"

**Target Linguistic Features:**
- **Number System** - Dual/Trial number (Hawaiian "lākou" = trial/3 persons)
- **Person/Clusivity** - Inclusive/Exclusive (Tagalog "kami"/"tayo")
- **Proximity** - Demonstrative distance (Japanese これ/それ/あれ)
- **Polarity** - Negative particles
- **Lexical Sense** - Polysemy disambiguation
- **Surface Realization** - Pro-drop patterns

**Example Pattern:**
```yaml
# Strong's G2249: ἡμεῖς (we)
translation_patterns:
  clusivity:
    - context: "divine speech (Trinity)"
      pattern: "5/5 Austronesian languages use exclusive form"
      examples:
        - {lang: "tgl", word: "kami", meaning: "exclusive"}
        - {lang: "msa", word: "kami", meaning: "exclusive"}
        - {lang: "fij", word: "keirau", meaning: "exclusive"}
      confidence: 0.98

    - context: "church unity passages"
      pattern: "8/8 languages use inclusive form"
      examples:
        - {lang: "tgl", word: "tayo", meaning: "inclusive"}
        - {lang: "msa", word: "kita", meaning: "inclusive"}
      confidence: 0.95
```

**Discovery Method:**
1. Access translation corpus (900+ Bible translations)
2. For each Strong's word, extract all translations across languages
3. Group by linguistic feature (clusivity, proximity, number, etc.)
4. Identify convergence patterns (high agreement)
5. Flag ambiguous cases (split decisions)
6. Document with confidence scores

**Value for Translators:**
- Evidence-based guidance: "Most languages with feature X use pattern Y"
- Edge case documentation: Trial number, 4th person, 9-way proximity systems
- Confidence scoring: Strong patterns vs. ambiguous cases
- Cross-linguistic validation

**Sources:**
- eBible corpus: github.com/BibleNLP/ebible (900+ translations)
- Parallel Bible corpora
- Bible translation organization databases

**Related Research:**
- See `/plan/tbta-strongs-hints-*.md` for detailed analysis
- TBTA (The Bible Translator's Assistant) feature prediction
- Focus on top 300 high-frequency words (diminishing returns after that)

---

## Strategy 8: Systematic Cross-Referencing

### 8.1 Related Strong's Numbers

**Method:** For each Strong's number, identify related words:
- Synonyms (different nuances)
- Antonyms (opposite meanings)
- Root words (etymology)
- Derived words (compounds, inflections)

**Discovery Sources:**
- BibleHub shows "related words"
- Thayer's cross-references synonyms
- Trench's "Synonyms of the NT" (on BLB)
- TDNT groups by word families

**Value:**
- Synonym distinctions prevent confusion
- Word families show semantic relationships
- Antonyms clarify by contrast

---

### 8.2 Semantic Domain Grouping

**Method:** Group words by meaning domains rather than etymology.

**Resources:**
- **Louw-Nida** - Greek semantic domain lexicon (expensive but sometimes cited)
- **Semantic Dictionary of Biblical Hebrew (SDBH)** - UBS project
- BibleHub "topical analysis" sections

**Discovery Method:**
- BLB and BibleHub may show Louw-Nida domain codes
- Search for domain discussions: `"Louw-Nida domain {number}"`
- SDBH available online (check UBS website)

**Value:** Understand word in context of related concepts.

---

## Strategy 9: Targeted Resource Recommendations

### 9.1 High-Priority Greek Resources

**For Every Greek Word:**
1. **Thayer's** - public domain, comprehensive, standard (BibleHub, StudyLight, BLB)
2. **HELPS Word-studies** - modern semantic insights (BibleHub)
3. **Strong's** - basic definition, KJV usage (all sites)

**For Classical Context:**
4. **LSJ (abridged)** - classical usage, etymology (StudyLight)
5. **Abbott-Smith** - scholarly distinctions (StudyLight)

**For Papyri Evidence:**
6. **Vocabulary of Greek NT** - everyday Koine usage (StudyLight)

**For Theology:**
7. **TDNT references** - when available (BLB)
8. **Trench's Synonyms** - when available (BLB)

---

### 9.2 High-Priority Hebrew Resources

**For Every Hebrew Word:**
1. **BDB (Brown-Driver-Briggs)** - public domain, standard (BibleHub, StudyLight)
2. **Strong's** - basic definition, KJV usage (all sites)

**For Cognates:**
3. **CAL (Comprehensive Aramaic Lexicon)** - free online

**For Theology:**
4. **TWOT references** - when cited (BLB may show)

**For Modern Resources:**
5. **SDBH (Semantic Dictionary of Biblical Hebrew)** - UBS project

---

## Implementation Priorities

### Phase 1: Foundational Data (Automated)

**Goal:** Extract from reliable, consistent sources with URL patterns.

**Targets:**
1. BibleHub (Greek and Hebrew lexicons, usage stats)
2. StudyLight (additional lexicons, LSJ, Abbott-Smith)
3. Base Strong's files in `./bible/words/strongs/` (read first!)

**Method:** Automated WebFetch with URL templates.

---

### Phase 2: Web Discovery (Semi-Automated)

**Goal:** Cast wide net for scholarly sources and controversies.

**Targets:**
1. Generic web search by Strong's number
2. Cross-reference code search (BDAG, TDNT, Louw-Nida)
3. Academic site search (.edu domains)
4. Controversy search (misconceptions, debates)

**Method:** WebSearch with curated queries, manual filtering.

---

### Phase 3: Community Insights (Manual Review)

**Goal:** Document debates and common questions.

**Targets:**
1. Biblical Hermeneutics Stack Exchange
2. Biblical language blogs
3. Seminary websites

**Method:** Manual search and extraction, marked as lower authority.

---

### Phase 4: Specialized Research (As Needed)

**Goal:** Deep dive for complex or controversial words.

**Targets:**
1. LXX connections
2. Papyri evidence
3. Classical literature
4. Cognate languages

**Method:** Manual research for words needing additional depth.

---

## Quality Control Measures

### Source Authority Ranking

**High Authority (primary sources):**
- Published lexicons (Thayer's, BDB, BDAG, LSJ, TDNT)
- Peer-reviewed journals
- Seminary faculty publications
- Inline with `{thayer}` `{bdb}` `{bdag}` etc.

**Medium Authority (secondary sources):**
- Aggregator sites (BibleHub, StudyLight, BLB)
- Theological blogs by known scholars
- Seminary websites
- Inline with `{biblehub-lexicon}` `{studylight-lexicon}` `{source-name}`

**Low Authority (tertiary sources):**
- Community Q&A (Stack Exchange)
- Personal blogs
- Unverified web content
- Inline with `{bhse-discussion}` `{blog-url}` + note: authority_level: low

---

### Verification Requirements

**For every claim:**
1. Extract data BEFORE analysis (don't work from memory)
2. Cite with inline `{source}` tags
3. Cross-verify controversial claims with multiple sources
4. Mark authority level clearly
5. Add new sources to ATTRIBUTION.md

**For controversies:**
1. Document the claim
2. Provide scholarly refutation
3. Cite evidence for correction
4. Mark authority levels of both claim and refutation

---

## Fair Use Compliance Checklist

For every Strong's number research file:

- [ ] Source-language anchored (Strong's number primary, not just English)
- [ ] Convergence grouping (list lexicons that agree collectively)
- [ ] Divergence in comparative context (quote when scholars disagree)
- [ ] Transformative analysis (add scholarly commentary, not just quotes)
- [ ] Anti-reconstruction (cannot extract any single lexicon programmatically)
- [ ] Complementary use (work enhances but doesn't replace lexicons)
- [ ] Inline citations (every fact tagged with `{source}`)
- [ ] No fabrication (all data extracted from real sources)
- [ ] All sources documented in ATTRIBUTION.md

See `/plan/policy/fair-use.md` for full policy.

---

## Related Planning Documents

This document builds on and complements several other planning efforts:

**Strong's Enrichment:**
- `/plan/strongs-word-research-tools.md` - Original planning for comprehensive word research tool
- `/bible-study-tools/strongs-word-research/README.md` - Tool implementation documentation

**TBTA Strong's Hints (Cross-Linguistic Patterns):**
- `/plan/tbta-strongs-hints-summary.md` - Executive summary of TBTA approach
- `/plan/tbta-strongs-hints-approach.md` - Detailed methodology
- `/plan/tbta-strongs-hints-evaluation.md` - Feature-by-feature analysis
- `/plan/tbta-strongs-hints-llm-enhancement.md` - LLM integration strategies
- `/plan/tbta-comprehensive-review.md` - Complete TBTA feature inventory

**Related Data Sources:**
- `/plan/morphhb-vs-macula.md` - Hebrew morphology data analysis
- `ATTRIBUTION.md` - All source citations and copyright notices
- `plan/policy/fair-use.md` - Fair use policy details

---

## Conclusion

We have **multiple discovery strategies** for enriching Strong's data:

0. **Base Strong's files** - ALWAYS read first! Contains pre-imported lexicons + cross-reference codes
1. **Aggregator sites** (BibleHub, StudyLight, BLB) - already negotiated access
2. **Web search** - Strong's numbers, cross-reference codes, controversies
3. **Community platforms** - Stack Exchange, blogs (marked as lower authority)
4. **Open-licensed projects** - unfoldingWord, OpenScriptures
5. **Academic search** - .edu sites, PDF search, journals
6. **Specialized research** - LXX, papyri, classical literature, cognates
7. **Cross-linguistic patterns** - TBTA approach with 900+ translations
8. **Systematic cross-referencing** - Related words, semantic domains
9. **Targeted recommendations** - Priority resources by language

**Next Steps:**
1. Update tool-experimenter to use these discovery strategies
2. Test on sample Strong's numbers (G1411 dunamis, G0026 agape, H0430 Elohim)
3. Document successful patterns in LEARNINGS
4. Iterate based on quality review

**Key Success Factor:** Cast wide net, verify with multiple sources, mark authority levels, cite everything inline.
