# Refutation Sources: Where to Find Scholarly Corrections

**Created:** 2025-11-12
**Purpose:** Map authoritative sources for correcting common errors about biblical words

---

## Critical Principle

**NEVER document an error without a scholarly refutation.**

Every community-discussions YAML file must include:
- Error (LOW authority - community source)
- Refutation (HIGH/MEDIUM authority - scholarly source)
- Evidence (facts supporting the correction)

---

## Refutation Source Hierarchy

### HIGH Authority (Prefer These)

**1. Published Lexicons**
- BDAG (Bauer-Danker-Arndt-Gingrich) - Greek
- BDB (Brown-Driver-Briggs) - Hebrew
- LSJ (Liddell-Scott-Jones) - Classical Greek
- Thayer's Greek Lexicon
- **Access:** Via Tool 1 lexicon-core, BibleHub, StudyLight
- **Use:** Etymology, semantic range, usage statistics
- **Authority Marking:** {bdag} {bdb} {lsj} {thayer}

**2. Peer-Reviewed Journals**
- Journal of Biblical Literature (JBL)
- New Testament Studies (NTS)
- Zeitschrift für die alttestamentliche Wissenschaft (ZAW)
- **Access:** Google Scholar, .edu sites, open access
- **Use:** Scholarly debates, diachronic analysis
- **Authority Marking:** {journal-citation}

**3. Academic References**
- Carson, D.A. "Exegetical Fallacies" - classic error taxonomy
- Silva, Moisés "Biblical Words and Their Meaning"
- Barr, James "The Semantics of Biblical Language"
- **Access:** Book excerpts, Google Books, .edu course materials
- **Use:** Systematic treatments of error types
- **Authority Marking:** {carson-fallacies} {silva} {barr}

### MEDIUM Authority (Good Secondary Sources)

**4. Expert Blogs with Citations**
- Bill Mounce (Koine Greek expert, Ph.D.)
- Mike Heiser (Semitic languages, Ph.D.)
- Seminary faculty blogs with credentials
- **Access:** WebSearch with credentialing check
- **Use:** Accessible explanations with scholarly backing
- **Authority Marking:** {blog-author-credentials}

**5. Tool 2 (Scholarly Analysis)**
- If word has scholarly-analysis file
- Check for documented debates, corrections
- **Access:** `./bible/words/strongs/{num}/{num}-scholarly-analysis.yaml`
- **Use:** Pre-researched scholarly insights
- **Authority Marking:** {scholarly-analysis}

**6. Tool 3 (Web Insights)**
- If word has web-insights file with expert sources
- Check error corrections section
- **Access:** `./bible/words/strongs/{num}/{num}-web-insights.yaml`
- **Use:** Expert-level web corrections
- **Authority Marking:** {web-insights-expert}

---

## Search Strategies by Error Type

### For Etymological Fallacies

**Strategy 1: Chronology Check**
- Search: "{claimed origin word} invention date" OR "{word} etymology timeline"
- Verify chronological impossibility
- **Example:** "dynamite invention 1867" + "NT written 1st century" = impossible

**Strategy 2: Etymology Verification**
- Check Tool 1 lexicon-core etymology section
- Search: "{word} etymology" site:.edu OR "{word} etymology" BDAG
- Consult LSJ for Greek, BDB for Hebrew
- **Example:** "dunamis etymology" → δύναμαι (to be able)

**Strategy 3: Explicit Refutation**
- Search: "{word} does not mean {false claim}"
- Search: "{word} etymology fallacy"
- **Example:** "dunamis dynamite fallacy" → multiple scholarly corrections

**Refutation Template:**
```yaml
refutation:
  correction: "{actual etymology from lexicon}"
  chronology: "{timeline showing impossibility if relevant}"
  source: {lexicon or scholarly article}
  evidence: "{lexicon etymology + chronological facts}"
  authority_note: "HIGH - published lexicon"
```

---

### For Anachronisms

**Strategy 1: Semantic Range Check**
- Tool 1 lexicon-core: semantic_range section
- BDAG: check all listed senses
- **Example:** "agape" in BDAG lists 5 senses, not just "unconditional love"

**Strategy 2: Classical vs. NT Comparison**
- LSJ for classical Greek usage
- Compare to Koine/NT usage in Thayer's, BDAG
- Note diachronic shifts vs. modern impositions
- **Example:** LSJ shows χάρις includes physical beauty; not just theological favor

**Strategy 3: Scholarly Treatment**
- Search: "{word} anachronism" OR "{word} does not always mean {modern claim}"
- Carson "Exegetical Fallacies" Chapter 1 (word study fallacies)
- **Example:** "agape unconditional" + "BDAG" → conditional uses documented

**Refutation Template:**
```yaml
refutation:
  correction: "{actual semantic range from lexicon}"
  modern_vs_ancient: "{distinction between modern theology and ancient meaning}"
  source: {lexicon + scholarly article if available}
  evidence: "{lexicon range + counterexamples}"
  authority_note: "HIGH - lexicon semantic range"
```

---

### For False Cognates

**Strategy 1: Etymology Verification**
- Check Tool 1 etymology section
- Search: "{word1} {word2} etymology related"
- Verify in LSJ (Greek) or BDB (Hebrew)
- **Example:** ὀξύς and ὄξος have different roots despite similar spelling

**Strategy 2: Linguistic Literature**
- Search: "{word} cognate" OR "{language1} {language2} cognate"
- Verify cross-language connections with scholarly linguistics
- **Example:** "Greek Hebrew cognate" + word

**Strategy 3: Homonym Distinction**
- Lexicons distinguish homonyms (same spelling, different roots)
- BDAG, LSJ mark homonyms with superscripts (e.g., λύω¹ vs. λύω²)
- **Example:** Check for homonym markers in lexicon

**Refutation Template:**
```yaml
refutation:
  correction: "{actual etymology vs. claimed connection}"
  linguistic_evidence: "{lack of cognate relationship}"
  source: {lexicon etymology section}
  evidence: "{distinct roots documented}"
  authority_note: "HIGH - lexicon etymology"
```

---

### For Over-Specification

**Strategy 1: Lexicon Range Check**
- Verify if claimed specificity is in lexicon definition
- BDAG: check if physical action/specific detail listed
- **Example:** χαρά (joy) - BDAG says "state of gladness," not "jumping"

**Strategy 2: Counterexample Search**
- Find biblical usages contradicting specific claim
- Use concordance or BibleHub search
- **Example:** "love money" (1 Tim 6:10) uses ἀγάπη (not sacrificial)

**Strategy 3: Scholarly Commentary**
- Search: "{word} does not mean {specific claim}"
- Check commentaries on verses using the word
- **Example:** "joy does not mean jumping"

**Refutation Template:**
```yaml
refutation:
  correction: "{actual lexical range without added specificity}"
  counterexamples:
    - verse: "{reference}"
      usage: "{how word used - contradicts specific claim}"
  source: {lexicon}
  evidence: "{broad lexical definition + counterexample}"
  authority_note: "HIGH - lexicon + biblical usage"
```

---

### For Lexical Maximalism

**Strategy 1: Carson's Exegetical Fallacies**
- Chapter 1: "Illegitimate Totality Transfer"
- Documents this exact error pattern
- **Access:** Google Books preview, seminary libraries, course materials

**Strategy 2: Context Determines Sense**
- Show that context selects ONE sense from range
- Use biblical examples showing different senses in different verses
- **Example:** λόγος = "word" (John 1:1) vs. "account" (Matt 12:36)

**Strategy 3: Lexicon Structure**
- Explain that lexicons list RANGE, not simultaneous meanings
- BDAG uses numbered senses (1, 2, 3) as alternatives
- **Example:** BDAG πνεῦμα lists 6 senses; context determines which

**Refutation Template:**
```yaml
refutation:
  correction: "{context determines which sense applies, not all simultaneously}"
  source: {carson-fallacies} OR {lexicon structure}
  evidence: "{examples showing different senses in different contexts}"
  authority_note: "HIGH - scholarly semantic theory"
```

---

### For Theological Projection

**Strategy 1: Distinguish Lexical from Theological**
- Lexical: What word means in Greek/Hebrew
- Theological: How word is used in doctrine
- Show distinction: word can support doctrine without lexically encoding it
- **Example:** Elohim plural supports Trinity, but plural ≠ "Trinity" lexically

**Strategy 2: Historical Development**
- Tool 2 scholarly-analysis: check diachronic section
- When did theological sense emerge?
- Separate biblical word usage from later creedal formulation
- **Example:** Homoousios (Trinity) post-biblical; Elohim pre-dates concept

**Strategy 3: Jewish Interpretation**
- For Hebrew words: check Jewish sources
- Do they see same theology in word? (often no)
- **Example:** Jewish interpretation of Elohim plural = majesty, not Trinity

**Refutation Template:**
```yaml
refutation:
  correction: "{lexical meaning vs. theological usage distinction}"
  historical_development: "{when theological sense emerged}"
  source: {lexicon + historical theology source}
  evidence: "{word's range + theological development timeline}"
  authority_note: "HIGH - lexicon + historical theology"
```

---

### For Selective Definition

**Strategy 1: Full Range Documentation**
- Tool 1 lexicon-core: complete semantic range
- BDAG: all numbered senses
- LSJ: classical range (for Greek)
- BDB: full Hebrew range

**Strategy 2: Multiple Lexicon Comparison**
- Compare BDAG, Thayer's, LSJ, Moulton-Milligan
- Show convergence across lexicons on broader range
- **Example:** All lexicons list χάρις = favor + beauty + gratitude

**Strategy 3: Corpus Evidence**
- Show biblical uses contradicting "ALWAYS" or "NEVER" claims
- Use concordance for counterexamples
- **Example:** λόγος "never means ratio" contradicted by classical usage

**Refutation Template:**
```yaml
refutation:
  correction: "{full semantic range from multiple lexicons}"
  counterexamples:
    - sense: "{excluded sense}"
      evidence: "{where used this way}"
      source: {lexicon}
  source: {multiple lexicons converging}
  evidence: "{range + counterexamples}"
  authority_note: "HIGH - lexicon convergence"
```

---

## Specialized Refutation Resources

### For Etymological Errors

**D.A. Carson - "Exegetical Fallacies" (1984, rev. 1996)**
- Chapter 1: Word-Study Fallacies
- Sections on: Etymology, anachronism, semantic range
- **Access:** Google Books preview, .edu PDFs, seminary libraries
- **Citation Format:** {carson-fallacies p.##}

**Moisés Silva - "Biblical Words and Their Meaning" (1994)**
- Systematic treatment of lexical semantics
- Etymology vs. meaning distinction
- **Access:** Google Books, .edu course materials
- **Citation Format:** {silva-biblical-words p.##}

**James Barr - "The Semantics of Biblical Language" (1961)**
- Classic critique of word-study errors
- Etymology, theological lexicons
- **Access:** Google Books, academic libraries
- **Citation Format:** {barr-semantics p.##}

### For Greek Etymology

**LSJ (Liddell-Scott-Jones) Greek-English Lexicon**
- Authoritative classical Greek etymology
- **Access:** Perseus Digital Library (free), StudyLight
- **Citation Format:** {lsj s.v. {word}}

**BDAG Etymology Sections**
- Each entry has etymology subsection
- **Access:** Via Tool 1, BibleHub, premium lexicon sites
- **Citation Format:** {bdag s.v. {word}}

### For Hebrew Etymology

**BDB (Brown-Driver-Briggs) Hebrew Lexicon**
- Etymology and root analysis
- **Access:** Tool 1, StudyLight, BibleHub
- **Citation Format:** {bdb s.v. {word}}

**Holladay Hebrew Lexicon**
- Modern alternative to BDB
- **Access:** Some .edu sites, Blue Letter Bible
- **Citation Format:** {holladay s.v. {word}}

---

## Search Pattern Templates

### Google Scholar Searches

**Pattern 1: Error + Refutation**
```
"{word}" + "does not mean" + "{false claim}"
"{word}" + "etymology" + "fallacy"
"{word}" + "misconception"
```

**Pattern 2: Scholarly Treatment**
```
"{word}" + "semantic range"
"{word}" + "lexical analysis"
"{word}" + "BDAG" OR "Thayer's" OR "LSJ"
```

**Pattern 3: Historical Linguistics**
```
"{word}" + "diachronic" + "development"
"{word}" + "classical" + "koine"
"{word}" + "LXX" + "septuagint"
```

### .edu Site Searches

**Pattern 1: Course Materials**
```
site:.edu "{word}" + "etymology"
site:.edu "{word}" + "lexicon"
site:.edu "exegetical fallacies"
```

**Pattern 2: Faculty Publications**
```
site:.edu "{word}" + "semantic" + PDF
site:.edu "{word}" + "lexical" + "study"
```

---

## WebFetch Strategies

### Lexicon Sites (HIGH Authority)

**BibleHub Lexicon Pages**
- URL: `https://biblehub.com/greek/{num}.htm` (Greek)
- URL: `https://biblehub.com/hebrew/{num}.htm` (Hebrew)
- Extract: Thayer's, HELPS, Strong's etymology
- **Prompt:** "Extract etymology section and semantic range, focusing on corrections to common misconceptions"

**StudyLight Lexicons**
- URL: `https://www.studylight.org/lexicons/eng/greek/{num}.html`
- Extract: LSJ, Abbott-Smith, Moulton-Milligan
- **Prompt:** "Extract classical usage and any notes on common errors"

### Expert Blog Posts (MEDIUM Authority)

**Bill Mounce's Blog**
- URL: `https://www.billmounce.com/` (search for word)
- Credentials: Ph.D., Koine Greek expert
- **Prompt:** "Extract corrections to popular errors about {word}, noting sources cited"

**Mike Heiser's Blog**
- URL: `https://drmsh.com/` (search for word)
- Credentials: Ph.D., Semitic languages
- **Prompt:** "Extract corrections to common misconceptions, especially etymological"

### Academic Articles

**Google Scholar**
- Search: `"{word}" etymology fallacy` OR `"{word}" semantic misconception`
- Filter: Accessible PDFs
- **Prompt:** "Extract scholarly refutation of popular error about {word}"

---

## Integration with Other Tools

### Check Tool 1 First (Lexicon Core)

**Before searching externally:**
1. Read `./bible/words/strongs/{num}/{num}-lexicon-core.yaml`
2. Check sections:
   - etymology (correct origin)
   - semantic_range (full range vs. selective claim)
   - lexical_convergence (what lexicons agree on)
   - lexical_divergence (documented debates)
3. Use Tool 1 data as PRIMARY refutation source

**If Tool 1 has convergence:** Error contradicts lexical consensus → easy refutation

### Check Tool 2 (Scholarly Analysis)

**For theological projections:**
1. Read `./bible/words/strongs/{num}/{num}-scholarly-analysis.yaml`
2. Check sections:
   - scholarly_debates (legitimate vs. popular confusion)
   - diachronic_analysis (historical development)
   - theological_significance (proper theological connection)
3. Use for distinguishing lexical meaning from theological usage

### Check Tool 3 (Web Insights)

**For documented errors:**
1. Read `./bible/words/strongs/{num}/{num}-web-insights.yaml`
2. Check error_corrections section (if exists)
3. May already have refutation documented

---

## Quality Standards for Refutations

### Minimum Requirements

**1. Authority Level**
- HIGH: Lexicon, peer-reviewed journal, academic book
- MEDIUM: Expert blog with Ph.D. credentials + citations
- Never use LOW authority for refutations

**2. Evidence Type**
- Lexicon definition (contradicts error)
- Usage examples (counterexamples)
- Chronological facts (impossibility)
- Linguistic analysis (etymology)
- Historical development (theological projection)

**3. Citation Format**
- Inline: `{source}` after every claim
- Source must be in ATTRIBUTION.md
- URL or book citation required

**4. Tone**
- Gracious, not dismissive
- Acknowledge why error is tempting
- Provide positive alternative

### Validation Checklist

Before including refutation in YAML:
- [ ] Authority level HIGH or MEDIUM?
- [ ] Evidence provided, not just assertion?
- [ ] Source cited with {inline-citation}?
- [ ] Source in ATTRIBUTION.md?
- [ ] Tone gracious and educational?
- [ ] Alternative framing provided?

---

## Common Refutation Patterns

### Pattern 1: Chronological Impossibility

**Structure:**
1. State claimed connection
2. Provide invention/origin dates
3. Show timeline gap
4. Cite historical source

**Example:**
```yaml
refutation:
  correction: "Dunamis cannot derive from 'dynamite' - chronologically impossible"
  evidence:
    - fact: "NT written 1st-2nd century CE" {biblical-scholarship}
    - fact: "Dynamite invented 1867 by Alfred Nobel" {historical-record}
    - conclusion: "1800+ year gap makes derivation impossible"
  authority_note: "HIGH - historical chronology"
```

### Pattern 2: Lexicon Contradiction

**Structure:**
1. State claimed meaning
2. Quote lexicon definition
3. Show mismatch
4. Provide correct understanding

**Example:**
```yaml
refutation:
  correction: "BDAG defines χαρά as 'state of gladness,' not physical jumping"
  lexicon_definition: "The experience of gladness, joy" {bdag}
  mismatch: "Lexicon does not include physical action of jumping"
  correct_understanding: "Joy = emotional state; may manifest physically but not inherent to word"
  authority_note: "HIGH - BDAG lexicon"
```

### Pattern 3: Counterexample

**Structure:**
1. State "ALWAYS" or "NEVER" claim
2. Provide biblical counterexample
3. Show usage contradicting claim
4. Cite lexicon range

**Example:**
```yaml
refutation:
  correction: "Agapao does not always mean 'sacrificial love'"
  counterexample:
    verse: "1 Timothy 6:10"
    usage: "ῥίζα γὰρ πάντων τῶν κακῶν ἐστιν ἡ φιλαργυρία (love of money)"
    observation: "Loving money is not sacrificial" {llm-cs45}
  lexicon_range: "To love, have affection for (broad range)" {bdag}
  authority_note: "HIGH - biblical usage + lexicon"
```

---

## Success Criteria

**Refutation Sources Research Complete When:**
- ✅ HIGH authority sources mapped
- ✅ MEDIUM authority sources identified
- ✅ Search strategies documented for each error type
- ✅ WebFetch patterns established
- ✅ Integration with Tools 1-3 defined
- ✅ Quality standards clear
- ✅ Common refutation patterns documented
- ✅ Ready to test on G1411 dunamis experiment

---

## Next Steps

1. Test refutation strategies on G1411 δύναμις (dunamis → dynamite)
2. Validate search patterns find authoritative corrections
3. Refine WebFetch prompts based on experiment
4. Update ATTRIBUTION.md with refutation sources used
5. Create schema.yaml incorporating refutation structure

---

**Status:** Complete - Ready for Experimentation Phase
**See Also:** `controversy-patterns.md`, `../schema.yaml`, `../validation/quality-checklist.md`, `/ATTRIBUTION.md`
