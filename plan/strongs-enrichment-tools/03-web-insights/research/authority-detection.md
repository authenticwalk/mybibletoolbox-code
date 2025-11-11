# Authority Detection Guidelines

**Tool:** Strong's Web Insights
**Purpose:** Systematic method for determining source authority and credibility
**Authority Range:** MEDIUM (expert blogs) to MEDIUM-LOW (vetted ministry sites)

---

## Overview

This document provides detailed criteria for evaluating the authority and reliability of web sources for biblical word studies. The goal is to include sources that add genuine value while clearly marking their authority level so downstream consumers know how to weight the information.

---

## Authority Classification System

### MEDIUM-HIGH Authority
**Definition:** Expert content from institutional sources or highly credentialed individuals

**Indicators:**
- Institutional backing: Tyndale House, seminary-affiliated sites
- Ph.D. credentials in relevant field (NT, OT, linguistics, theology)
- Multiple peer-reviewed publications
- Cited by other scholars in academic work
- Affiliated with recognized biblical scholarship institutions

**Examples:**
- STEPBible.org (Tyndale House Cambridge)
- NetBible.org translator notes (named scholars with credentials)
- Articles by faculty at accredited seminaries

**Usage Note:** "MEDIUM-HIGH - Institutional/academic source, not peer-reviewed"

### MEDIUM Authority
**Definition:** Expert individuals with strong credentials but operating independently

**Indicators:**
- Ph.D. or Th.D. in biblical languages, theology, or linguistics
- Published textbooks or monographs in the field
- Seminary teaching experience (past or present)
- Regular citations of scholarly sources in their writing
- Recognition in the academic community

**Examples:**
- Dr. Bill Mounce (Greek textbook author)
- Dr. Michael Heiser (Hebrew scholar, peer-reviewed publications)
- Seminary professors' personal blogs

**Usage Note:** "MEDIUM - Expert analysis by {Name}, {highest degree}"

### MEDIUM-LOW Authority
**Definition:** Qualified practitioners with ministry credentials who compile/synthesize expert sources

**Indicators:**
- M.Div. or equivalent seminary training
- Consistent citation of scholarly sources
- Track record of quality content
- Ministry experience (pastor, teacher, translator)
- No Ph.D. but demonstrates competence

**Examples:**
- Precept Austin (compiles scholarly sources)
- Ministry sites that cite lexicons and scholars appropriately
- Experienced Bible translators sharing field insights

**Usage Note:** "MEDIUM-LOW - Qualified synthesis, verify citations"

### LOW Authority (EXCLUDE from Tool 3)
**Definition:** Insufficient credentials or quality for inclusion

**Indicators:**
- No verifiable credentials
- No source citations
- Sensationalist claims
- Promotional content
- AI-generated content farms

**Usage Note:** Do not include in Tool 3 output

---

## Detection Methodology

### Step 1: Locate Author Information

**Where to Look:**
- About page
- Author bio at end of article
- Site footer with staff/contributors page
- LinkedIn profile (if linked)
- Seminary/university faculty page

**Red Flag:** No author identified or only pseudonym

### Step 2: Verify Credentials

**Academic Credentials (in order of authority):**
1. **Ph.D./Th.D.** in biblical studies, theology, linguistics, ancient languages
   - Verify: Check university faculty page or LinkedIn
   - Authority: MEDIUM to MEDIUM-HIGH

2. **Th.M./M.Th.** in biblical languages or theology
   - Verify: Seminary alumni pages
   - Authority: MEDIUM (if paired with publications)

3. **M.Div.** from accredited seminary
   - Verify: Seminary website
   - Authority: MEDIUM-LOW (if demonstrates competence)

4. **B.A./B.S.** in biblical studies or none listed
   - Authority: Insufficient for Tool 3 unless other factors

**Professional Credentials:**
- Published books (check Amazon, publisher websites)
- Peer-reviewed articles (check Google Scholar)
- Seminary teaching position (check faculty page)
- Bible translation experience (SIL, Wycliffe, other orgs)
- Conference speaking (SBL, ETS, IBR)

### Step 3: Assess Content Quality

**Positive Indicators:**
- **Citations present:** Author references lexicons, scholars, sources
- **Nuanced argumentation:** Acknowledges different views
- **Technical terminology:** Uses proper linguistic/theological terms
- **Source interaction:** Engages with lexicons, not just repeating them
- **Correction of errors:** Points out common misconceptions with evidence

**Negative Indicators:**
- **No citations:** Just makes claims without support
- **Oversimplification:** "This word ALWAYS means..."
- **Etymological fallacies:** "Because X comes from Y, it means..."
- **Sensationalism:** "Hidden meanings scholars don't want you to know"
- **Commercial focus:** Primary goal is selling books/courses

### Step 4: Cross-Check Against Known Sources

**Validation Tests:**
1. **Lexicon alignment:** Does content align with standard lexicons (Thayer's, BDAG, BDB)?
2. **No contradictions:** Any claims that contradict Tool 1 (lexicon-core)?
3. **Scholarly support:** Are claims supported by established scholarship?
4. **Track record:** Check other articles by same author for consistency

### Step 5: Determine Authority Level

**Decision Tree:**
```
Does source have Ph.D. + peer-reviewed pubs?
├─ YES → Check institutional affiliation
│  ├─ Institution: MEDIUM-HIGH
│  └─ Independent: MEDIUM
└─ NO → Check M.Div./Th.M. + publications
   ├─ YES + good citations → MEDIUM-LOW
   └─ NO OR poor quality → EXCLUDE
```

---

## Specific Detection Patterns

### Pattern 1: Seminary Faculty Member

**Detection:**
- WebSearch: "{author name} seminary" OR "{author name} professor"
- Look for: Faculty page with bio, credentials, publications
- Check: Degree-granting institution (accredited seminary?)

**Authority Assessment:**
- Ph.D. + seminary faculty = MEDIUM to MEDIUM-HIGH
- M.Div. + seminary faculty = MEDIUM-LOW (if demonstrates expertise)
- No advanced degree + faculty = Insufficient (teaching pastors, not scholars)

**Citation Format:** "MEDIUM - {Name}, {Degree}, {Institution}"

### Pattern 2: Published Author

**Detection:**
- WebSearch: "{author name} books" OR check Amazon
- Look for: Textbooks, academic monographs, scholarly books
- Distinguish: Self-published vs. academic press

**Authority Assessment:**
- Textbook author (Zondervan, Baker, etc.) = MEDIUM to MEDIUM-HIGH
- Academic monograph = MEDIUM-HIGH
- Popular-level books = MEDIUM-LOW (unless Ph.D. author)
- Self-published = Insufficient unless other credentials

**Citation Format:** "MEDIUM - {Name}, author of {Book Title}"

### Pattern 3: Institutional Website

**Detection:**
- Check domain: .edu, .ac.uk, or known institution
- Look for: About page describing organization
- Verify: Recognized institution (Tyndale House, Cambridge, DTS, etc.)

**Authority Assessment:**
- Research institute (Tyndale House) = MEDIUM-HIGH
- Seminary-affiliated site = MEDIUM to MEDIUM-HIGH
- Parachurch ministry = MEDIUM-LOW (varies)

**Citation Format:** "MEDIUM-HIGH - {Institution Name}"

### Pattern 4: Translator Practitioner

**Detection:**
- WebSearch: "{author name} Bible translation" OR "{name} SIL" OR "{name} Wycliffe"
- Look for: Translation organization affiliation
- Check: Years of field experience

**Authority Assessment:**
- Ph.D. + field translation = MEDIUM-HIGH
- M.A. + 10+ years field = MEDIUM (for practical applications)
- Short-term translator = MEDIUM-LOW

**Citation Format:** "MEDIUM - {Name}, Bible translator with {Organization}"
**Special Note:** "HIGH for practical translation applications - field-tested"

### Pattern 5: Compilation Sites

**Detection:**
- Look for: "Compiled from...", "Adapted from...", multiple un-cited sources
- Check: Original sources are cited with links
- Verify: Not just copying public domain lexicons

**Authority Assessment:**
- Good compilation (Precept Austin style) = MEDIUM-LOW if sources cited
- Poor compilation (no attribution) = EXCLUDE

**Citation Format:** "MEDIUM-LOW - Compiled from scholarly sources"
**Important:** Always verify and cite the ORIGINAL sources when possible

---

## Red Flags Checklist

### Automatic EXCLUDE Criteria

**❌ Fabrication Indicators:**
- Claims with no citations
- "Scholars have discovered..." without naming scholars
- Made-up statistics or percentages
- Invented etymologies not in standard lexicons

**❌ Sensationalism:**
- "Hidden meaning the church doesn't teach"
- Gematria, numerology claims
- Conspiracy theory connections
- Clickbait titles

**❌ Credential Misrepresentation:**
- Fake degrees (diploma mills)
- Inflated credentials ("theologian" with no degree)
- Anonymous "expert" content

**❌ Commercial Exploitation:**
- Primary goal is selling products
- Information gated behind paywall
- Affiliate link spam

**❌ AI-Generated Content (2023+):**
- Generic, formulaic writing
- No specific examples or citations
- Repetitive phrasing
- Inconsistent or contradictory information

**❌ Outdated Scholarship:**
- Pre-1950s sources only (unless historical)
- Discredited theories presented as fact
- Ignores modern lexical research

---

## Authority Marking in Output

### Format in YAML Output

```yaml
modern_insights:
  - insight: "{actual content}"
    source: "{URL}"
    author: "{Name}"
    credentials: "{Ph.D. in NT Studies, author of 'Biblical Greek Textbook'}"
    authority_level: "MEDIUM"
    authority_note: "Expert analysis, not peer-reviewed"
    institution: "{Optional - if applicable}"
    verification_date: "YYYY-MM-DD"
```

### Authority Level Guidelines

**Use "MEDIUM-HIGH" when:**
- Institutional backing (Tyndale House, seminary official site)
- Ph.D. + multiple peer-reviewed publications
- Widely cited by other scholars

**Use "MEDIUM" when:**
- Ph.D. in relevant field
- Published textbooks or academic books
- Seminary faculty (current or former)
- Strong track record of cited work

**Use "MEDIUM-LOW" when:**
- M.Div. with demonstrated competence
- Compilation sites with good citations
- Experienced practitioners (translators, pastors) without advanced degrees
- Ministry sites that cite scholarly sources appropriately

**Do NOT include:**
- Anything that would be "LOW" authority
- Sources that fail Critical validation criteria

---

## Validation Process

### Before Including Any Source:

**Step 1: Credential Verification (5 minutes)**
- Find author bio
- Verify highest degree
- Check institution/organization

**Step 2: Content Quality Check (3 minutes)**
- Scan for citations
- Check for red flags
- Compare to lexicon data (Tool 1)

**Step 3: Authority Assignment (2 minutes)**
- Apply decision tree
- Choose authority level
- Write authority note

**Step 4: Documentation**
- Record in output YAML
- Note verification method
- Include verification date

### Spot-Check Requirements:

- Every 25th source: Deep verification (check LinkedIn, faculty pages, publications)
- Any source with questionable claims: Full verification before inclusion
- New domain/site: Verify first source thoroughly, then trust if consistent

---

## Examples of Authority Detection

### Example 1: Bill Mounce Blog Post

**Detection Process:**
1. Find author bio: Ph.D. in NT, published "Basics of Biblical Greek"
2. Verify textbook: Standard in seminaries, Zondervan publisher
3. Check citations in article: References lexicons appropriately
4. Authority decision: MEDIUM

**Output:**
```yaml
authority_level: "MEDIUM"
author: "William D. Mounce"
credentials: "Ph.D. in New Testament, author of 'Basics of Biblical Greek'"
authority_note: "Expert analysis by Greek textbook author, not peer-reviewed"
```

### Example 2: Tyndale House STEP Bible

**Detection Process:**
1. Check domain: STEPBible.org → Tyndale House Cambridge
2. Verify institution: Recognized research institute
3. Check content: Multi-scholar collaboration, cited sources
4. Authority decision: MEDIUM-HIGH

**Output:**
```yaml
authority_level: "MEDIUM-HIGH"
institution: "Tyndale House Cambridge"
authority_note: "Academic research institute, multi-scholar collaboration"
```

### Example 3: Precept Austin Compilation

**Detection Process:**
1. Check author: No advanced degree listed
2. Verify content: Compiles from Vine's, lexicons, other sources
3. Check citations: Sources are cited
4. Authority decision: MEDIUM-LOW (useful but secondary)

**Output:**
```yaml
authority_level: "MEDIUM-LOW"
author: "Compiled from multiple scholarly sources"
authority_note: "Helpful synthesis, verify original sources"
verification_note: "Secondary compilation - original sources cited"
```

### Example 4: Random Blog (EXCLUDE)

**Detection Process:**
1. Check author: No credentials listed
2. Verify content: No citations, makes unsupported claims
3. Check quality: "Dunamis means dynamite" (known fallacy)
4. Authority decision: EXCLUDE

**Action:** Do not include in Tool 3 output

---

## Integration with Extraction Workflow

### During WebSearch Phase:
1. Find potential sources
2. Quick authority scan: Does author have credentials?
3. If questionable, skip and try next result
4. If promising, proceed to WebFetch

### During WebFetch Phase:
1. Extract content (insights, applications)
2. Simultaneously extract: author name, credentials, institution
3. Apply authority detection criteria
4. If source fails validation, discard extracted content

### During Synthesis Phase:
1. Assign final authority level
2. Write clear authority note
3. Include in YAML output with full documentation
4. Flag any borderline cases for human review

---

## Quality Assurance

### Self-Check Questions:

Before finalizing any source inclusion, ask:

1. **Can I verify author credentials?** (YES required)
2. **Does content cite sources?** (YES expected for MEDIUM+)
3. **Would I trust this for my own study?** (YES for inclusion)
4. **Is authority level clearly marked?** (ALWAYS)
5. **Does content add value beyond lexicons?** (YES for Tool 3)

### Rejection Criteria:

If ANY of these are true, EXCLUDE:
- Cannot verify author identity
- No credentials found after 5-minute search
- Content contradicts established lexicons without evidence
- Sensationalist or clickbait style
- Primary goal is commercial
- AI-generated content suspected

---

## Next Steps

1. Test authority detection on 5 sample sources (varied authority levels)
2. Document extraction patterns in README
3. Design experiments with known authority ranges
4. Validate that authority marking is clear and consistent

---

**Status:** Research phase complete - authority detection framework established
**Next:** Integrate into Tool 3 README and design experiments
