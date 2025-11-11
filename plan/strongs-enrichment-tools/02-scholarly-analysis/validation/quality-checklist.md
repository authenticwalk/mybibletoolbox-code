# Tool 2: Scholarly Analysis Quality Checklist

**Purpose:** Validation criteria for scholarly analysis outputs
**Authority Standard:** HIGH - Tier 1-2 sources only (peer-reviewed or equivalent)

---

## Level 1: CRITICAL (Must Pass 100%)

**Fabrication Prevention:**
- [ ] Zero fabrication - all claims from documented sources
- [ ] No LLM-generated theology - must cite scholars
- [ ] No invented scholarly debates
- [ ] No fake citations or sources

**Citation Standards:**
- [ ] Inline citations for EVERY claim `{source-id}`
- [ ] All inline citations have ATTRIBUTION.md entries
- [ ] Citations match actual source content (spot-check 10%)
- [ ] No percentages or numerical predictions without source

**Authority Requirements:**
- [ ] ALL sources are Tier 1 (HIGHEST) or Tier 2 (HIGH)
- [ ] No Tier 3+ sources used (expert blogs → Tool 3, community → Tool 4)
- [ ] Author credentials verified (PhD, seminary faculty)
- [ ] Peer-review status verified OR equivalent (PhD dissertation, SBL paper)

**Fair Representation:**
- [ ] Scholarly debates present ALL major views (not just preferred)
- [ ] Evidence provided for each scholarly position
- [ ] Opposing views not misrepresented or strawmanned
- [ ] Consensus status accurately reported

**Source Documentation:**
- [ ] All new sources added to ATTRIBUTION.md
- [ ] Full bibliographic information (author, title, year, venue, pages)
- [ ] DOI or URL included when available
- [ ] Authority tier marked (1 or 2)

---

## Level 2: HIGH PRIORITY (80%+ Pass Rate Required)

**Theological Significance:**
- [ ] Importance level justified (not just asserted)
- [ ] Key themes explained with scholarly support
- [ ] Doctrinal relevance documented from peer-reviewed sources
- [ ] At least 3 scholarly sources cited for theological importance

**Cultural & Historical Context:**
- [ ] 1st century context documented (NT) OR ancient Near East (OT)
- [ ] Social practices cited from scholarly sources
- [ ] Archaeological/historical evidence when available
- [ ] Comparison with contemporary non-biblical usage

**Diachronic Analysis:**
- [ ] Classical → Koine semantic development documented
- [ ] Semantic shifts explained with scholarly support
- [ ] At least 2 time periods covered (Classical + Koine minimum)
- [ ] Sources cited for each period

**Scholarly Insights:**
- [ ] Specific observations (not generic statements)
- [ ] Field of study noted (NT studies, linguistics, etc.)
- [ ] Significance explained
- [ ] Date of scholarship noted (prefer recent when available)

**Source Quality:**
- [ ] Minimum 5 scholarly sources per word (Tier 1-2)
- [ ] At least 50% Tier 1 (HIGHEST - peer-reviewed journals)
- [ ] Multiple fields represented (theology, linguistics, history)
- [ ] Recent scholarship included (within 20 years)

**Cross-References:**
- [ ] BDAG/TDNT/Louw-Nida codes used for discovery (if available)
- [ ] Builds on Tool 1 (lexicon-core) foundation
- [ ] Adds depth beyond Tool 1 (not redundant)

---

## Level 3: MEDIUM PRIORITY (60%+ Pass Rate Required)

**Scholarly Debates:**
- [ ] Multiple views documented when debates exist
- [ ] Proponents named for each view
- [ ] Consensus status assessed
- [ ] Synthesis provided

**Intertextual Connections:**
- [ ] OT connections documented when relevant
- [ ] LXX usage noted for NT Greek words
- [ ] Greco-Roman parallels when culturally significant
- [ ] Dead Sea Scrolls when relevant

**Translation Guidance:**
- [ ] Translation challenges identified
- [ ] Scholarly solutions documented
- [ ] Receptor language issues noted when relevant

**Controversies & Misconceptions:**
- [ ] Popular errors documented when widespread
- [ ] Scholarly refutation with evidence
- [ ] Significance explained

**Metadata:**
- [ ] Source distribution recorded (Tier 1 vs Tier 2 count)
- [ ] Fields represented listed
- [ ] Cross-reference codes used documented
- [ ] Extraction notes for challenges

---

## Validation Process

### Pre-Extraction

**1. Verify Word Qualifies for Tool 2:**
- [ ] Theologically significant? (if not, Tool 1 may be sufficient)
- [ ] Scholarly literature expected? (grammatical words may have little)
- [ ] Priority level? (focus on top 1,000 theological words)

**2. Review Tool 1 Output:**
- [ ] Read lexicon-core output for foundation
- [ ] Note cross-reference codes (BDAG, TDNT, Louw-Nida)
- [ ] Identify gaps Tool 2 should fill

### During Extraction

**3. Source Discovery:**
- [ ] Search by cross-reference codes (not just Strong's)
- [ ] Use journal-access strategies (Google Scholar, .edu sites)
- [ ] Verify authority for each source (Tier 1-2 only)
- [ ] Document all sources immediately in ATTRIBUTION.md

**4. Content Extraction:**
- [ ] Quote in scholarly analysis context (fair use)
- [ ] Use inline citations for every claim
- [ ] Represent debates fairly (all major views)
- [ ] Distinguish between scholarly consensus and minority views

**5. Quality Checks:**
- [ ] Verify no Tier 3+ sources used
- [ ] Check for fabrication (all claims sourced?)
- [ ] Ensure fair representation (debates balanced?)
- [ ] Confirm citations match sources (spot-check)

### Post-Extraction

**6. Run Full Validation:**
- [ ] Level 1: 100% pass required (critical items)
- [ ] Level 2: 80%+ pass required (high priority)
- [ ] Level 3: 60%+ pass required (medium priority)

**7. Authority Verification:**
- [ ] All sources are Tier 1 or Tier 2
- [ ] Author credentials verified for 100% of sources
- [ ] Peer-review status confirmed for 100% of sources
- [ ] No expert blogs or community sources

**8. Citation Audit:**
- [ ] Every claim has inline citation
- [ ] All inline citations in ATTRIBUTION.md
- [ ] Spot-check 10% of citations match sources
- [ ] No orphaned citations (citation without ATTRIBUTION entry)

**9. Theological Review:**
- [ ] Represents major theological traditions fairly
- [ ] No theological bias (unless sourced from scholar)
- [ ] Controversial claims have strong evidence
- [ ] LLM only for synthesis, not theology

**10. Documentation:**
- [ ] Validation results recorded
- [ ] Pass/fail per level documented
- [ ] Any issues noted for methodology improvement
- [ ] Learnings captured for future experiments

---

## Spot-Check Protocol

**For each output, randomly select:**

**10% of Claims:**
- [ ] Verify claim matches cited source
- [ ] Check source is correctly categorized (Tier 1 or 2)
- [ ] Confirm no misrepresentation

**10% of Citations:**
- [ ] Look up source in ATTRIBUTION.md
- [ ] Verify bibliographic information accurate
- [ ] Check source is accessible (URL works, DOI valid)

**10% of Author Credentials:**
- [ ] Verify PhD claimed (check university website)
- [ ] Confirm institutional affiliation
- [ ] Check peer-review status of venue

---

## Common Failure Patterns

### Tier 1: CRITICAL Failures (Must Fix)

**Fabrication:**
- ❌ Claims without sources
- ❌ Invented scholarly debates
- ❌ Paraphrased "scholarship" from LLM memory
- ✅ FIX: Extract from actual sources, cite everything

**Wrong Authority:**
- ❌ Expert blogs used (Tier 4 → save for Tool 3)
- ❌ Stack Exchange discussions (Tier 5 → save for Tool 4)
- ❌ Study Bible notes (Tier 4, also copyright issues)
- ✅ FIX: Use only Tier 1-2 sources

**Unfair Representation:**
- ❌ Only citing scholars who agree with one view
- ❌ Misrepresenting opposing views
- ❌ Ignoring major scholarly positions
- ✅ FIX: Present all major views, cite evidence for each

### Tier 2: HIGH Priority Failures (Should Fix)

**Insufficient Depth:**
- ❌ Only 2-3 sources for theological word
- ❌ No cultural/historical context
- ❌ Missing diachronic analysis
- ✅ FIX: Research more thoroughly, use cross-ref codes

**Tool 1 Redundancy:**
- ❌ Repeating what Tool 1 already covered
- ❌ Not adding scholarly depth
- ❌ Just restating lexicon definitions
- ✅ FIX: Focus on what Tool 1 didn't cover (debates, theology, culture)

**Citation Gaps:**
- ❌ Claims without inline citations
- ❌ Generic "scholars say" without naming
- ❌ Missing ATTRIBUTION.md entries
- ✅ FIX: Add inline citations, complete ATTRIBUTION.md

---

## Success Metrics

### Per-Word Targets

**For Theologically Central Words (G26 ἀγάπη, G4102 πίστις, etc.):**
- Sources: 10-15 Tier 1-2 sources
- Theological significance: Fully documented
- Scholarly debates: Multiple views represented
- Cultural context: Comprehensive
- Validation: 100% Level 1, 90%+ Level 2, 80%+ Level 3

**For Moderately Theological Words:**
- Sources: 5-10 Tier 1-2 sources
- Theological significance: Well documented
- Scholarly debates: Major views represented
- Cultural context: Adequate
- Validation: 100% Level 1, 80%+ Level 2, 70%+ Level 3

**For Minimally Theological Words:**
- Consider: Is Tool 2 needed? Tool 1 may be sufficient
- Sources: 3-5 Tier 1-2 sources if proceeding
- Focus: Specific scholarly insights, not full analysis

### Overall Tool 2 Quality Targets

- **Authority:** 100% Tier 1-2 sources (zero Tier 3+)
- **Validation:** 100% Level 1 pass rate across all words
- **Source Quality:** 50%+ Tier 1 (HIGHEST) sources
- **Coverage:** Top 1,000 theological words completed
- **Theological Fairness:** Multiple traditions represented when relevant
- **Fair Use:** 100% compliance (scholarly quoting in context)

---

## Decision Points

### After Experiment 1 (G26 ἀγάπη)

**If passes all levels:**
- ✅ Proceed to Experiment 2 (G3056 λόγος)

**If Level 1 failures:**
- ❌ STOP - Fix critical issues before continuing
- Review authority standards
- Improve source verification process

**If Level 2 failures >20%:**
- ⚠️ Refine extraction methodology
- Improve search strategies
- Add more scholarly sources

### After Experiment 2 (G3056 λόγος)

**If both experiments pass:**
- ✅ Methodology validated
- Begin production phase
- Scale to top 100 theological words

**If inconsistent results:**
- ⚠️ Investigate word-specific factors
- Identify patterns in success/failure
- Refine methodology based on patterns

---

## Next Steps

1. Create validation spreadsheet for tracking
2. Run Experiment 1: G26 ἀγάπη
3. Complete full validation (all 3 levels)
4. Document pass/fail rates
5. Identify methodology improvements
6. Run Experiment 2: G3056 λόγος
7. Final validation and methodology finalization

---

**References:**
- authority-ranking.md - Source authority tiers
- journal-access.md - How to find Tier 1-2 sources
- cross-ref-usage.md - Using codes for discovery
- schema.yaml - Output structure requirements
- SCHEMA.md - Project-wide standards
- REVIEW-GUIDELINES.md - Project validation levels
