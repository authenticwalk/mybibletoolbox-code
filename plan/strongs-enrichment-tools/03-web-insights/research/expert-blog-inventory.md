# Expert Blog and Website Inventory

**Tool:** Strong's Web Insights
**Authority Level:** MEDIUM
**Purpose:** Identify vetted expert sources for modern insights and practical applications

---

## Research Questions

1. How to distinguish expert blogs from amateur content?
2. Which websites consistently provide reliable word studies?
3. What credentials indicate expertise?
4. Which sites provide practical translator/preacher guidance?

---

## Vetting Criteria

### Marks of Expertise (Include)
- **Academic credentials:** Seminary degree (M.Div, Th.M, Ph.D), biblical languages training
- **Published works:** Books, journal articles, peer-reviewed contributions
- **Citations present:** Author cites lexicons, scholarly sources
- **Track record:** Consistent quality across multiple articles
- **Institutional affiliation:** Seminary faculty, Bible translation organization
- **Peer recognition:** Cited by other scholars, conference speaker

### Red Flags (Exclude)
- **No credentials listed:** Anonymous or no author bio
- **No source citations:** Claims without supporting evidence
- **Sensationalism:** Clickbait titles, exaggerated claims
- **Commercial focus:** Primary goal is selling products
- **Doctrinal extremism:** Promotes fringe theology without scholarly basis
- **Etymological fallacies:** Makes claims like "dunamis = dynamite"

---

## Vetted Website Inventory

### Tier 1: Structured Lexicon Sites (HIGH-MEDIUM Authority)

**1. WordExplain.com**
- **Focus:** Systematic Greek/Hebrew word studies
- **Authority:** Author credentials visible, citations present
- **Coverage:** Selected theologically significant words
- **Data Available:** Etymology, usage analysis, theological significance
- **Access Method:** WebSearch for "{strongs} site:wordexplain.com"
- **Authority Note:** "MEDIUM - Expert analysis, not peer-reviewed"

**2. STEPBible.org / Tyndale House**
- **Focus:** Academic Bible study tools
- **Authority:** Tyndale House Cambridge (research institute)
- **Coverage:** All Strong's numbers with extended definitions
- **Data Available:** Extended glosses, semantic domains, usage notes
- **Access Method:** Direct URL templating possible
- **Authority Note:** "MEDIUM-HIGH - Academic institution"

**3. NetBible.org Notes**
- **Focus:** Translation notes and textual commentary
- **Authority:** Biblical Studies scholars, names published
- **Coverage:** Verse-level notes (can extract word-specific)
- **Data Available:** Translation decisions, textual variants, word choices
- **Access Method:** Search by verse reference, extract word-specific notes
- **Authority Note:** "MEDIUM-HIGH - Named scholars with credentials"

**4. Bible.org (bible.org)**
- **Focus:** Biblical studies articles and word studies
- **Authority:** Dallas Theological Seminary network
- **Coverage:** Selected words with in-depth studies
- **Data Available:** Practical applications, sermon illustrations, teaching notes
- **Access Method:** WebSearch "{word} site:bible.org"
- **Authority Note:** "MEDIUM - DTS affiliated, varies by author"

### Tier 2: Expert Blogs (MEDIUM Authority)

**5. Dr. Bill Mounce (billmounce.com)**
- **Credentials:** Ph.D., Greek language expert, textbook author
- **Published Works:** "Basics of Biblical Greek" (standard textbook)
- **Focus:** Greek word studies, common mistakes, practical insights
- **Data Available:** Etymology, usage patterns, translation guidance
- **Access Method:** WebSearch "{word} OR {strongs} site:billmounce.com"
- **Authority Note:** "MEDIUM - Expert blog, not peer-reviewed"

**6. Hebrew Word Lessons (various blogs by Hebrew scholars)**
- **Examples:** John H. Walton, Michael Heiser blogs
- **Credentials:** Ph.D. scholars with Hebrew specialization
- **Focus:** Cultural context, ancient Near Eastern background
- **Data Available:** Cultural insights, ANE connections, practical applications
- **Access Method:** WebSearch "{hebrew_word} hebrew scholar blog"
- **Authority Note:** "MEDIUM - Expert opinion, individual perspective"

**7. Greek Word Studies (blogs by Greek scholars)**
- **Examples:** Mike Aubrey (linguistics), Rob Plummer (seminary prof)
- **Credentials:** Ph.D. in NT or linguistics, seminary teaching
- **Focus:** Linguistic analysis, exegetical insights, teaching
- **Data Available:** Semantic analysis, discourse features, practical teaching
- **Access Method:** WebSearch "{greek_word} greek word study blog"
- **Authority Note:** "MEDIUM - Expert analysis, personal blog format"

### Tier 3: Practical Ministry Sites (MEDIUM-LOW Authority)

**8. Precept Austin (preceptaustin.org)**
- **Focus:** Word studies for preachers and teachers
- **Authority:** Ministry-focused, compiles from multiple sources
- **Coverage:** Extensive NT Greek word studies
- **Data Available:** Practical applications, illustrations, teaching notes
- **Caveat:** Secondary source (compiles others' work), verify citations
- **Access Method:** WebSearch "{strongs} site:preceptaustin.org"
- **Authority Note:** "MEDIUM-LOW - Helpful but verify sources"

**9. GotQuestions.org**
- **Focus:** Apologetics and practical questions
- **Authority:** Network of theologians, varies by article
- **Coverage:** Selected words tied to doctrinal questions
- **Data Available:** Practical explanations, apologetic applications
- **Caveat:** Popular level, not technical
- **Access Method:** WebSearch "{word} meaning site:gotquestions.org"
- **Authority Note:** "MEDIUM-LOW - Popular level, clear but basic"

### Tier 4: Translator Resources (HIGH Authority for Practical Applications)

**10. SIL/Wycliffe Translation Notes**
- **Focus:** Practical translation challenges and solutions
- **Authority:** Professional Bible translators with field experience
- **Coverage:** Problem words with cross-cultural issues
- **Data Available:** Translation strategies, cultural adaptations, field notes
- **Access Method:** WebSearch "SIL {word} translation" OR check unfoldingWord
- **Authority Note:** "HIGH for practical - field-tested solutions"

**11. UnfoldingWord Translation Resources**
- **Focus:** Open-licensed translation helps
- **Authority:** Multi-scholar review, open source model
- **Coverage:** Translation words, notes, academy articles
- **Data Available:** Semantic ranges, translation helps, cross-references
- **Access Method:** GitHub repos, search by Strong's number
- **Authority Note:** "MEDIUM-HIGH - Vetted by translation community"

---

## Websites to AVOID (Not Suitable for Tool 3)

### Low Authority / Quality Issues

**❌ Random WordPress Blogs**
- No credentials, no citations, often copied content

**❌ Commercial Concordance Sites (without expert commentary)**
- Just republish Strong's definitions without added value

**❌ Sensationalist "Hidden Meaning" Sites**
- Promote numerology, gematria, conspiracy theories
- Example: "The Hebrew word for X has the same letters as..."

**❌ Outdated or Incorrect Etymology Sites**
- Perpetuate discredited etymologies (dunamis=dynamite)

**❌ AI-Generated Content Farms**
- Proliferating since 2023, often inaccurate
- Detection: generic writing, no specific examples, no citations

---

## Extraction Strategy by Site Type

### For Structured Sites (WordExplain, STEP, NetBible)
```
1. WebSearch to find page: "{strongs} OR {transliteration} site:{domain}"
2. WebFetch with targeted prompt:
   - Extract: Etymology, semantic range, usage statistics
   - Extract: Practical applications (translator/preacher guidance)
   - Extract: Modern insights (how word is understood today)
3. Note authority level in output: "MEDIUM - {site_name}"
4. Inline citations: {site-identifier}
```

### For Expert Blogs (Mounce, Heiser, etc.)
```
1. WebSearch to locate article: "{word} OR {strongs} site:{blog_domain}"
2. Verify author credentials (look for bio, publications)
3. WebFetch with extraction prompt:
   - Extract: Author's insights, not just lexicon summaries
   - Extract: Practical applications, teaching illustrations
   - Extract: Corrections of common errors
4. Note authority: "MEDIUM - Expert blog by {Name}, {Credentials}"
5. Inline citations: {author-year} OR {blog-identifier}
```

### For Translator Resources (SIL, unfoldingWord)
```
1. WebSearch: "SIL {word} translation" OR check unfoldingWord repos
2. WebFetch focusing on:
   - Translation challenges (practical problems)
   - Solutions documented (what worked in field)
   - Cultural considerations
3. Note authority: "HIGH for practical applications - field-tested"
4. Inline citations: {sil} {ufw}
```

---

## Coverage Expectations

### Words with Good Web Coverage (~2,000 words)
- **Theologically significant words:** Love, grace, faith, righteousness, etc.
- **High-frequency words:** He, we, this, say, come, etc.
- **Controversial words:** Words with known debates (dunamis, logos, agape)
- **Practical challenge words:** Words translators ask about

### Words with Limited Web Coverage
- **Rare words (<10 occurrences):** Often no blog posts
- **Technical terms:** Unless theologically significant
- **Mundane vocabulary:** Common words without special interest

---

## Quality Control Checklist

Before including a source in Tool 3 output:

**Level 1: CRITICAL**
- [ ] Author credentials verified (or institutional authority)
- [ ] Citations present in source material (author cites lexicons/scholars)
- [ ] No fabricated or sensationalist claims
- [ ] Authority level clearly marked in output

**Level 2: HIGH PRIORITY**
- [ ] Content adds value beyond basic lexicon data
- [ ] Practical applications grounded in evidence (not speculation)
- [ ] Modern insights based on scholarship (not opinion)
- [ ] Cross-check against Tool 1 (lexicon-core) - no contradictions

**Level 3: MEDIUM PRIORITY**
- [ ] Multiple sources for controversial claims
- [ ] Teaching illustrations are appropriate
- [ ] Translator guidance is field-tested (when applicable)

---

## Integration with Other Tools

### Tool 1 (Lexicon Core) Dependency
- Read Tool 1 output FIRST
- Tool 3 should ADD to Tool 1, not duplicate
- Focus on: modern insights, practical applications, teaching helps
- If web source contradicts Tool 1, flag for review

### Tool 2 (Scholarly Analysis) Relationship
- Tool 2 provides peer-reviewed analysis
- Tool 3 provides expert commentary (one step down in authority)
- Many expert blogs cite scholarly work - capture those connections

### Tool 4 (Community Discussions) Boundary
- Tool 3: Expert blogs with credentials
- Tool 4: Community forums, Stack Exchange, Reddit
- Clear distinction: Tool 3 authors have verifiable expertise

---

## Next Steps

1. **Validate inventory:** Test searches for 5-10 sample words
2. **Document extraction patterns:** Successful WebSearch/WebFetch combinations
3. **Create authority detection guidelines:** Detailed document (next file)
4. **Design experiments:** Test on high-coverage, medium-coverage, and controversial words

---

## Sample Test Words for Research Validation

**High Coverage (should find multiple sources):**
- G26 (ἀγάπη - love)
- G1411 (δύναμις - power)
- G5485 (χάρις - grace)

**Medium Coverage (should find some sources):**
- G4982 (σώζω - save)
- G1343 (δικαιοσύνη - righteousness)

**Controversial (should find error corrections):**
- G1411 (dunamis/dynamite fallacy)
- G4190 (πονηρός - evil, debate about "worthless" vs "malicious")

**Practical Challenge (translator-focused):**
- G26 (agape in cultures with different love categories)
- H7307 (רוּחַ - spirit/wind/breath - translation ambiguity)

---

**Status:** Research phase - inventory complete, ready for validation testing
**Next:** Create authority-detection.md with detailed credentialing criteria
