# Tool 3: Strong's Web Insights

**Status:** Research Phase Complete
**Priority:** MEDIUM - Supplements core lexicon data with practical applications
**Authority:** MEDIUM to MEDIUM-LOW - Expert blogs and vetted ministry sites
**Coverage:** ~2,000 words with good web resources
**Timeline:** 2 months

---

## Purpose

Extract modern insights, practical applications, and teaching guidance from expert web sources (blogs, structured sites, translator resources) to supplement core lexical data with practitioner-focused content.

**Why This Tool Matters:**
- Bridges academic lexicons and practical ministry
- Captures modern scholarly insights in accessible formats
- Provides translator guidance and preacher illustrations
- Documents expert perspectives not in peer-reviewed journals
- Offers teaching helps and practical applications

**What This Tool Does NOT Do:**
- Duplicate lexicon data (use Tool 1 for that)
- Include peer-reviewed scholarship (use Tool 2 for that)
- Include community forums/discussions (use Tool 4 for that)

---

## Authority Range

**MEDIUM-HIGH:** Institutional sources (Tyndale House, seminary official sites)
**MEDIUM:** Expert blogs by Ph.D. scholars with publications
**MEDIUM-LOW:** Qualified practitioners (M.Div.) who cite sources well

All sources must:
- Have verifiable credentials
- Cite scholarly sources
- Add value beyond basic lexicons
- Be clearly marked with authority level

---

## Methodology Overview

### 3-Step Extraction Process

**Step 1: Source Discovery**
- WebSearch for expert content: `"{strongs} OR {word}" site:{vetted-domain}`
- Check multiple source types: blogs, structured sites, translator resources
- Apply authority detection criteria (see `research/authority-detection.md`)

**Step 2: Content Extraction**
- WebFetch from vetted sources
- Focus on content NOT in Tool 1 (lexicon-core):
  - Modern insights (contemporary scholarly perspectives)
  - Practical applications (for translators, preachers, teachers)
  - Common errors/misconceptions (with corrections)
  - Teaching illustrations (grounded in scholarship)
- Extract author credentials simultaneously

**Step 3: Synthesis & Validation**
- Verify against Tool 1: no contradictions
- Assign authority level: MEDIUM-HIGH, MEDIUM, or MEDIUM-LOW
- Mark clearly in output with inline citations
- Quality check: no fabrication, citations present, value-add confirmed

---

## Research Phase

**Location:** `./research/`

**Documents:**
1. `expert-blog-inventory.md` - Vetted websites, blogs, and translator resources
2. `authority-detection.md` - Systematic criteria for determining source credibility

**Key Research Findings:**

**Vetted Sources (Tier 1-2):**
- STEPBible.org (Tyndale House) - MEDIUM-HIGH
- NetBible.org translator notes - MEDIUM-HIGH
- Bill Mounce's blog (Greek textbook author) - MEDIUM
- Bible.org (Dallas Theological Seminary network) - MEDIUM
- SIL/Wycliffe translation notes - HIGH for practical applications

**Authority Detection Framework:**
- Ph.D. + peer-reviewed pubs + institution = MEDIUM-HIGH
- Ph.D. + publications + independent = MEDIUM
- M.Div. + good citations + track record = MEDIUM-LOW
- Anything below = EXCLUDE from Tool 3

**Coverage Expectations:**
- ~2,000 words will have quality web resources
- Theologically significant words: excellent coverage
- High-frequency words: good coverage
- Rare words: limited or no coverage (expected)

---

## Experimentation Phase

**Location:** `./experiments/`

**5 Experiments Planned:**

### Experiment 1: High-Coverage Word (G26 - ἀγάπη "love")
- **Why:** Theologically central, extensive expert commentary available
- **Test:** Can we find 5+ quality sources? Do they add value beyond lexicons?
- **Expected:** Mounce, Bible.org, WordExplain, SIL notes, NET Bible notes
- **Output:** `experiments/exp1-high-coverage/G26-output.yaml`
- **Validation:** Authority levels assigned correctly? Practical applications present?

### Experiment 2: Medium-Coverage Word (G1343 - δικαιοσύνη "righteousness")
- **Why:** Theologically important but less commonly studied
- **Test:** Can we find 2-3 quality sources? What authority levels?
- **Expected:** Some expert blogs, possibly translator notes
- **Output:** `experiments/exp2-medium-coverage/G1343-output.yaml`
- **Validation:** Quality maintained with fewer sources?

### Experiment 3: Controversial Word (G1411 - δύναμις "power")
- **Why:** Known false etymology (dunamis ≠ dynamite), need error corrections
- **Test:** Can we find expert corrections of common errors?
- **Expected:** Mounce or similar scholar explicitly correcting misconception
- **Output:** `experiments/exp3-controversial/G1411-output.yaml`
- **Validation:** Error + correction + evidence all documented?

### Experiment 4: Translator-Focused Word (H7950 - שֶׁלֶג "snow")
- **Why:** Cultural translation challenge (tropical cultures without snow)
- **Test:** Can we find SIL/Wycliffe translator notes on handling this?
- **Expected:** Practical translation strategies, cultural adaptations
- **Output:** `experiments/exp4-translator-focus/H7950-output.yaml`
- **Validation:** Practical guidance present? Field-tested solutions?

### Experiment 5: Low-Coverage Word (Rare word with <20 occurrences)
- **Why:** Test handling when web resources are scarce
- **Test:** Honest about limited data? No fabrication?
- **Expected:** Perhaps 0-1 sources, explicitly note limited coverage
- **Output:** `experiments/exp5-low-coverage/GXXXX-output.yaml`
- **Validation:** Doesn't force content when sources lacking?

**Each Experiment Produces:**
- Output YAML following schema
- Learnings document (what worked, what needs adjustment)
- Authority verification log

---

## Output Schema

**File Location:** `.data/bible/words/strongs/{num}/{num}.strongs-web-insights.yaml`

**Schema Location:** `./schema.yaml`

**Key Sections:**
- Metadata (Strong's number, tool info, generation date)
- Modern insights (contemporary scholarly perspectives from expert sources)
- Practical applications (for translators, preachers, teachers)
- Error corrections (common misconceptions with expert refutations)
- Teaching helps (illustrations, sermon guidance)
- Quality metadata (authority levels, source verification)

**Inline Citation Pattern:** `{author-year}` OR `{site-identifier}`

---

## Validation Phase

**Location:** `./validation/`

### Quality Checklist (3 levels)

**Level 1: CRITICAL (100% pass required)**
- [ ] All sources have verifiable author credentials OR institutional backing
- [ ] Authority level clearly marked for each insight/application
- [ ] Inline citations: `content {source}` format
- [ ] No fabricated data - all content extracted from real sources
- [ ] Tool 1 (lexicon-core) read FIRST - no contradictions
- [ ] Content adds value beyond lexicon data (not just repeating Thayer's)

**Level 2: HIGH PRIORITY (80%+ pass required)**
- [ ] Modern insights based on expert analysis (not just opinion)
- [ ] Practical applications grounded in evidence or field experience
- [ ] Error corrections documented with: error + refutation + evidence
- [ ] Teaching helps are appropriate and non-sensationalist
- [ ] Multiple sources when available (not just one blog post)

**Level 3: MEDIUM PRIORITY (60%+ pass required)**
- [ ] Author credentials documented in output
- [ ] Translator guidance is field-tested (when applicable)
- [ ] Cross-references to Tool 1 and Tool 2 data (when relevant)
- [ ] Verification date recorded

---

## Subagent Strategy

**Main Agent:** Orchestrate source discovery, extraction, and synthesis

**Phase 1: Source Discovery (Parallel)**
- **Subagent 1:** Search vetted blogs (Mounce, Heiser, etc.)
- **Subagent 2:** Search structured sites (STEPBible, NetBible, Bible.org)
- **Subagent 3:** Search translator resources (SIL, unfoldingWord)
- Each returns: URLs + quick authority assessment

**Phase 2: Content Extraction (Parallel)**
- **Subagent 4-6:** WebFetch from discovered sources
- Extract: insights, applications, error corrections, teaching helps
- Extract: author credentials, citations present
- Each returns: content + authority evidence

**Phase 3: Synthesis (Main Agent)**
- Read Tool 1 output first (avoid duplication)
- Combine data from all sources
- Apply authority detection criteria
- Assign final authority levels
- Generate web-insights.yaml

---

## Integration with Other Tools

### Tool 1 (Lexicon Core) - REQUIRED DEPENDENCY
- **Read Tool 1 FIRST** before extracting web insights
- Tool 3 should ADD to Tool 1, not duplicate
- Focus areas:
  - Modern scholarly perspectives (not in 1800s lexicons)
  - Practical applications (not lexicon focus)
  - Teaching illustrations (grounded in scholarship)
- If web source contradicts Tool 1: flag for human review

### Tool 2 (Scholarly Analysis) - COMPLEMENTARY
- Tool 2: Peer-reviewed scholarship (HIGH authority)
- Tool 3: Expert commentary/blogs (MEDIUM authority)
- Many expert blogs cite Tool 2 sources - capture connections
- Tool 3 can bridge academic content to practical applications

### Tool 4 (Community Discussions) - CLEAR BOUNDARY
- Tool 3: Expert blogs with verifiable credentials
- Tool 4: Community forums (Stack Exchange, Reddit)
- Distinction: Tool 3 requires Ph.D./M.Div. OR institutional backing
- If source lacks credentials → belongs in Tool 4, not Tool 3

### Tool 6 (Translation Patterns) - DATA COMPLEMENT
- Tool 3: Expert translator guidance (prescriptive)
- Tool 6: Corpus analysis patterns (descriptive)
- Both provide translation help, different methods

---

## Coverage Strategy

### High-Priority Words (~500 words)
- Theologically central: love, grace, faith, sin, salvation, righteousness
- Known controversies: dunamis, logos, agape vs phileo
- Common errors: Words with etymological fallacies
- Target: 5+ sources per word

### Medium-Priority Words (~1,000 words)
- High-frequency with practical interest
- Words with good translator resources
- Teaching-focused vocabulary
- Target: 2-3 sources per word

### Low-Priority Words (~500 words)
- Words with at least 1 quality source
- Opportunistic: if good source found, include
- Target: 1 source minimum

### Explicitly Skip
- Rare words with no web coverage (don't force it)
- Words fully covered by lexicons (no value-add)
- Technical grammatical terms (unless special interest)

---

## Implementation Timeline

**Week 1-2: Research Phase** ✅ COMPLETE
- Complete source inventory
- Document authority detection framework
- Validate source vetting criteria

**Week 3-4: Experimentation Phase**
- Run 5 experiments (high, medium, controversial, translator-focus, low coverage)
- Capture learnings
- Refine methodology
- Validate authority detection in practice

**Week 5: Validation Phase**
- Validate experiment outputs against quality checklist
- Refine schema based on learnings
- Document edge cases and handling

**Week 6-9: Production Phase**
- High-priority words: Theologically central, controversial (~500 words)
- Medium-priority words: Good coverage available (~1,000 words)
- Low-priority words: Opportunistic (~500 words)

---

## Success Metrics

**Coverage:**
- 2,000+ words with quality web insights
- 500+ high-priority words with 5+ sources
- 1,000+ medium-priority words with 2-3 sources

**Quality:**
- 100% pass Level 1 validation (authority verified, clearly marked)
- 90%+ pass Level 2 validation (value-add confirmed, grounded insights)
- All authority levels clearly marked and defensible

**Value-Add:**
- Content supplements (not duplicates) Tool 1
- Practical applications present for translator-focused words
- Error corrections documented with evidence
- Teaching helps are appropriate and useful

---

## Key Differentiators from Other Tools

| Aspect | Tool 1 | Tool 2 | Tool 3 | Tool 4 |
|--------|--------|--------|--------|--------|
| **Authority** | HIGH (lexicons) | HIGH (peer-reviewed) | MEDIUM | LOW (community) |
| **Format** | Published lexicons | Academic journals | Expert blogs | Forums |
| **Focus** | Etymology, range | Theological depth | Practical apps | Controversies |
| **Coverage** | All 14,197 words | ~1,000 theological | ~2,000 with resources | ~500 controversial |
| **Credentials** | Published scholars | Ph.D. + peer-reviewed | Ph.D. OR M.Div. | No requirement |

---

## Next Steps

1. ✅ Complete research documents (source inventory, authority detection)
2. Design and run 5 experiments (Week 3-4)
3. Validate experimental outputs (Week 5)
4. Refine schema and methodology based on learnings
5. Begin production phase (Week 6+)

---

**See Also:**
- `research/expert-blog-inventory.md` - Vetted sources and extraction strategies
- `research/authority-detection.md` - Systematic authority evaluation framework
- `/plan/strongs-comprehensive-strategy.md` - Overall Strong's enhancement strategy
- `/plan/strongs-enrichment-sources/IMPLEMENTATION-PLAN.md` - All 7 tools overview
