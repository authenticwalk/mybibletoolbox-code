# Tool 3 Researcher Workflow Guide

**Purpose:** Step-by-step guide for extracting Strong's Web Insights data in production
**Status:** Production-Ready (validated through 5 adversarial experiments)
**Version:** 1.0.0
**Last Updated:** 2025-11-11

---

## Overview

This workflow guides researchers through the systematic process of creating Tool 3 (Strong's Web Insights) data files. Follow these steps for each Strong's number assigned.

**Time Estimates:**
- Standard word: 2-3 hours
- High-coverage word (error corrections, debates): 4-5 hours
- Interdisciplinary word (specialized coverage): 4-5 hours
- Grammatical particle (skip): 30-45 minutes (search + documentation)

---

## Before You Start

### Prerequisites

1. **Read these files first:**
   - `README.md` - Tool 3 overview
   - `schema.yaml` - Output structure
   - `validation/quality-checklist.md` - Validation criteria
   - `EXPERIMENTS-COMPLETE-SUMMARY.md` - Key learnings

2. **Have access to:**
   - Tool 1 (lexicon-core) output for this word
   - `research/expert-blog-inventory.md` - Vetted sources
   - `research/authority-detection.md` - Credentialing framework
   - `templates/` - Error correction, multi-perspective, skip decision templates

3. **Set up workspace:**
   - Create working directory for this word: `work/G####/` or `work/H####/`
   - Have ATTRIBUTION.md ready for new source additions

---

## Step 1: Initial Assessment (15-20 minutes)

### 1.1 Read Tool 1 (Lexicon Core) Output

**CRITICAL:** Always read Tool 1 FIRST to avoid duplication.

```bash
# Read lexicon-core file
cat .data/bible/words/strongs/G####/G####-lexicon-core.yaml
```

**Note:**
- What lexicon data already exists?
- What does Tool 1 already cover thoroughly?
- What gaps might Tool 3 fill?

### 1.2 Preliminary Word Assessment

**Ask these questions:**

1. **Is this word in Tool 3 scope?**
   - ❌ Skip if: Grammatical particle (δέ, γάρ, etc.)
   - ❌ Skip if: Pure function word (no semantic content)
   - ❌ Skip if: Tool 1 is fully sufficient
   - ✅ Include if: Practical insights, modern debates, error corrections, translator challenges exist

2. **What type of word is this?**
   - [ ] Theologically significant (e.g., pneuma, logos, ekklesia)
   - [ ] Common error target (e.g., dynamis/dynamite fallacy)
   - [ ] Translation challenge (e.g., cultural sensitivity, multiple valid renderings)
   - [ ] Rare/specialized (may have discipline-specific coverage)
   - [ ] Standard vocabulary (general coverage expected)

3. **Initial expectation:**
   - High coverage expected? (theological terms, common words)
   - Medium coverage expected? (specialized but accessible)
   - Low coverage expected? (rare, technical, mundane)

**Decision Point:**
- If clearly a grammatical particle → Go to **Step 8 (Skip Decision)**
- Otherwise → Proceed to Step 2

---

## Step 2: Multi-Discipline Web Search (45-60 minutes)

### 2.1 Search Strategy (from Experiment 2 learnings)

**IMPORTANT:** Coverage is discipline-specific. Check ALL relevant disciplines:

1. **Bible Study Platforms:**
   - Bible.org, NetBible.org, BibleHub.com
   - Precept Austin, STEPBible.org
   - Query: `[Greek/Hebrew word] meaning`, `Strong's [number]`

2. **Theological Disciplines:**
   - Systematic theology, biblical theology
   - For theological terms: ecclesiology, pneumatology, etc.
   - For ethics terms: virtue ethics, moral theology
   - Query: `[theological topic] [Greek word]`, `theology of [concept]`

3. **Linguistic Analysis:**
   - billmounce.com, Greek/Hebrew language sites
   - Semantic studies, lexical analysis
   - Query: `[word] Greek semantics`, `[word] etymology fallacy`

4. **Translation Practitioner Resources:**
   - SIL International, Wycliffe, unfoldingWord
   - Field notes, translator guidance
   - Query: `translating [word] [language family]`, `[word] translation challenges`

5. **Specialist Disciplines (when relevant):**
   - Virtue ethics (for ethical terms like eutrapelia)
   - Philosophy (for philosophical concepts)
   - Cultural studies (for culturally sensitive terms)
   - Query: `[concept] virtue ethics`, `[word] philosophical analysis`

### 2.2 Execute Searches

**Minimum:** 10 queries across multiple disciplines

**Document each search:**
```
Query: "[search query]"
Platform: WebSearch / billmounce.com / etc.
Results: [Number of relevant results]
Quality: High / Medium / Low / None
Date: YYYY-MM-DD
```

**Create:** `work/G####/search-log.md`

### 2.3 Initial Results Assessment

**Findings:**
- [ ] 10+ high-quality sources → High coverage
- [ ] 3-9 sources → Medium coverage
- [ ] 1-2 sources → Low coverage (assess if sufficient)
- [ ] 0 sources → Skip decision required

**Decision Point:**
- If 0 relevant sources after exhaustive search → Go to **Step 8 (Skip Decision)**
- If 1-2 sources only: Assess if sufficient for Tool 3 entry
- If 3+ sources → Proceed to Step 3

---

## Step 3: Source Vetting & Authority Assessment (30-45 minutes)

### 3.1 For Each Source Found

**Use:** `research/authority-detection.md` framework

**Check:**
1. **Author Credentials:**
   - Find author bio, faculty page, or "About" section
   - Verify: Ph.D., M.Div., institutional affiliation
   - Document: Highest degree, institution, relevant publications

2. **Authority Level Classification:**
   - **VERY HIGH:** Leading scholars, peer-reviewed monograph authors, research professors
   - **HIGH:** Ph.D. + peer-reviewed publications in relevant field
   - **MEDIUM-HIGH:** Institutional backing (seminary faculty, research institutes)
   - **MEDIUM:** Ph.D. or Th.D. + published works (blog format, not peer-reviewed)
   - **MEDIUM-LOW:** M.Div. + citations + qualified synthesis

3. **Red Flags:**
   - ❌ Anonymous or unverifiable author
   - ❌ No relevant credentials
   - ❌ Sensationalist language
   - ❌ Contradicts standard lexicons without evidence
   - ❌ "Obvious" claims without support

**Create:** `work/G####/sources-vetted.md`

**Format:**
```markdown
## Source 1: [Site Name]

**URL:** [URL]
**Author:** [Name]
**Credentials:** [Ph.D., Institution, Publications]
**Authority Level:** MEDIUM
**Authority Note:** "Expert blog by Greek textbook author, not peer-reviewed"
**Verification Date:** YYYY-MM-DD

**Content Type:** [modern_insight | error_correction | translator_guidance | teaching_help]
**Key Claims:**
- [Claim 1 with evidence]
- [Claim 2 with evidence]

**Assessment:** Include / Exclude / Needs More Verification
```

### 3.2 Authority Distribution Check

**Ideal distribution:**
- At least 1 MEDIUM-HIGH or higher source
- Multiple sources at MEDIUM or above
- Avoid relying solely on MEDIUM-LOW sources

**Minimum for Tool 3:**
- General insights: 1 MEDIUM+ source
- Error corrections: 2 MEDIUM-HIGH+ sources, at least 1 HIGH or VERY HIGH
- Scholarly disagreements: 2+ credentialed scholars with divergent views

---

## Step 4: Content Type Classification (15-20 minutes)

### 4.1 Identify Content Categories

Based on sources found, classify into:

**1. Modern Insights:**
- Linguistic analysis (corpus studies, semantic range, usage patterns)
- Contemporary understanding (recent scholarship, new perspectives)
- Theological insights (Logos Christology, pneumatology, etc.)

**2. Practical Applications:**
- For translators (handling synonyms, register distinctions, cultural factors)
- For preachers (sermon illustrations, teaching points, pedagogical guidance)
- For students (learning aids, memory helps, study questions)

**3. Error Corrections:**
- Common misconceptions (etymological fallacy, semantic anachronism, etc.)
- Prevalence (widespread / moderate / uncommon)
- Expert refutations with evidence

**4. Scholarly Disagreements (from Experiments 1, 5):**
- Interpretive debates (capitalization, reference ambiguity)
- Translation debates (church vs assembly, spirit vs Spirit)
- Theological debates (cessationist vs continuationist, etc.)
- Cultural sensitivities (post-colonial, denominational, contemporary movements)

**5. Teaching Helps:**
- Memory aids
- Study questions
- Cultural notes
- Pedagogical guidance

### 4.2 Decision Point: Special Handling Required?

**If Error Correction content found:**
- → Use `templates/error-correction-template.yaml`
- → Ensure 5-part structure (Error, Classification, Refutation, Validation, Alternative)
- → See Experiment 4 (G1411 dynamis) as model

**If Scholarly Disagreement or Cultural Debate:**
- → Use `templates/multi-perspective-template.yaml`
- → Ensure multi-perspective fairness
- → Apply bias detection tests (Reversal, Respect, Evidence)
- → See Experiments 1 (pneuma) and 5 (ekklesia) as models

**If Discipline-Specific Coverage:**
- → Note discipline context prominently
- → Appropriate framing (e.g., "theological virtue perspective")
- → Don't force general biblical content
- → See Experiment 2 (eutrapelia) as model

---

## Step 5: Data Extraction & Synthesis (2-4 hours)

### 5.1 Extract Content Systematically

**For each source:**

1. **Capture key insights:**
   - What claim is being made?
   - What evidence supports it?
   - What authority backs it?

2. **Document with inline citations:**
   - Format: `content {source-id}`
   - Citation codes from ATTRIBUTION.md
   - If new source: add to ATTRIBUTION.md first

3. **Maintain context:**
   - Don't cherry-pick out of context
   - Preserve nuance and caveats
   - Represent author's position fairly

### 5.2 Synthesis Principles

**DO:**
- ✅ Synthesize multiple sources into coherent insights
- ✅ Note when sources agree or disagree
- ✅ Provide evidence for all claims
- ✅ Use qualitative language ("most", "many", "some")
- ✅ Present multiple perspectives fairly

**DON'T:**
- ❌ Fabricate data
- ❌ Invent statistics ("80% of scholars agree...")
- ❌ Remove important caveats
- ❌ Cherry-pick to support one view
- ❌ Repeat Tool 1 lexicon data without value-add

### 5.3 Special Handling: Error Corrections (5-Part Structure)

**If correcting common error:**

**Part 1: Error Statement**
- State error clearly without mockery
- Include specific claim: "Because dynamis shares roots with 'dynamite'..."
- Note prevalence: widespread | moderate | uncommon

**Part 2: Classification**
- Name the fallacy type: "etymological_fallacy", "semantic_anachronism"
- Alternative names from different scholars (Carson vs Cara terminology)
- Brief definition

**Part 3: Multi-Layered Refutation**
- **Minimum 4 evidence types:**
  1. Linguistic (word formation, semantic analysis)
  2. Diachronic (historical, chronological order)
  3. Contextual (NT usage incompatible with error)
  4. Scholarly consensus (BDAG, LSJ, major lexicons)
  5. Additional (mathematical, comparative, cultural - if available)

**Part 4: Expert Validation (Authority Pyramid)**
- VERY HIGH authority (if available): Carson, leading scholars
- HIGH authority: Ph.D. + peer-reviewed publications
- MEDIUM authority: Expert blogs, textbook authors
- **Minimum:** 2 sources (MEDIUM-HIGH+), at least 1 HIGH or VERY HIGH

**Part 5: Correct Alternative**
- **Principle:** Core methodological principle
- **Methodology:** Step-by-step proper approach
- **Better Analogy:** Memorable alternative (e.g., "dynamo not dynamite")
- **Biblical Usage Pattern:** How word actually functions in NT

**Tone Check:** Gracious and pedagogical throughout
- Acknowledge error is widespread
- Explain WHY wrong, not just THAT wrong
- Teach methodology to avoid similar errors
- Build up correct understanding

**See:** `templates/error-correction-template.yaml` and `experiments/exp4-error-correction/G1411-synthesis.md`

### 5.4 Special Handling: Multi-Perspective Disagreements

**If scholarly disagreement exists:**

**Document All Major Positions:**
- Minimum 2 positions
- Each with: advocates, key arguments, strengths, considerations, sources

**For Each Position:**
- **Advocates:** Name, credentials, authority level
- **Key Arguments:** 3+ arguments with inline citations
- **Strengths:** 2-3 strengths of this view
- **Considerations:** 2-3 limitations or caveats
- **Sources:** URLs, verification dates

**Cultural Considerations:**
- Post-colonial contexts (if relevant)
- Denominational sensitivities
- Contemporary movements
- Affected regions/traditions

**Translator Guidance:**
- **Decision Framework:** Factors to consider (NOT "do this")
- **Contextual Factors:** Audience theology, cultural sensitivity, semantic precision
- **NOT an answer sheet:** Guidance as options, not mandates

**Bias Detection Tests:**
1. **Reversal Test:** Could presentation order reverse without changing implications?
2. **Respect Test:** Would advocates of each view feel fairly represented?
3. **Evidence Test:** Did you present strongest arguments for all positions?

**All 3 tests must pass.**

**See:** `templates/multi-perspective-template.yaml` and experiments 1 (pneuma) and 5 (ekklesia)

---

## Step 6: YAML File Creation (30-45 minutes)

### 6.1 Use Schema as Template

**File Location:** `.data/bible/words/strongs/{num}/{num}-web-insights.yaml`

**Example:** `.data/bible/words/strongs/G1234/G1234-web-insights.yaml`

### 6.2 Populate All Required Sections

**Metadata:**
```yaml
strongs_number: "G1234"
language: "greek"
lemma: "λέγω"
transliteration: "legō"
gloss: "say, speak, tell"

tool:
  name: "strongs-web-insights"
  version: "1.0.0"
  generated_date: "2025-11-11"
```

**Dependency (CRITICAL):**
```yaml
lexicon_core_file: ".data/bible/words/strongs/G1234/G1234-lexicon-core.yaml"
lexicon_core_read: true
lexicon_core_date: "2025-11-10"
```

**Content Sections:**
- `modern_insights:` - Expert analysis, contemporary understanding
- `practical_applications:` - for_translators, for_preachers, for_students
- `error_corrections:` - If applicable, use 5-part structure
- `scholarly_disagreements:` - If applicable, use multi-perspective framework
- `teaching_helps:` - Pedagogical aids

**Metadata:**
- `sources_summary:` - Total sources, authority distribution, source types
- `validation_level_1:` - All CRITICAL criteria
- `validation_level_2:` - All HIGH PRIORITY criteria
- `validation_level_3:` - All MEDIUM PRIORITY criteria
- `data_quality:` - Authority verification method, disciplines searched
- `coverage_notes:` - Honest assessment, discipline context
- `skip_decision:` - If skipped, full documentation

### 6.3 Inline Citation Format

**All content must include inline citations:**

```yaml
content: |
  Modern corpus linguistics shows this word appears in formal discourse
  patterns, contrasting with informal speech markers in Koine Greek {mounce-2023}
```

**Citation codes must match ATTRIBUTION.md**

---

## Step 7: Validation (30-45 minutes)

### 7.1 Self-Validation Checklist

**Use:** `validation/quality-checklist.md`

**Level 1: CRITICAL (Must pass 100%)**

Run through ALL Level 1 criteria:
- [ ] All sources credentialed
- [ ] Authority levels marked
- [ ] Inline citations present
- [ ] No fabricated data
- [ ] Tool 1 read first
- [ ] Content adds value
- [ ] All sources in ATTRIBUTION.md
- [ ] Error corrections complete (if applicable)
- [ ] Scope boundaries respected

**If ANY Level 1 fails → STOP, fix before proceeding**

**Level 2: HIGH PRIORITY (Must pass 80%+)**

Check 9 HIGH PRIORITY criteria:
- [ ] Modern insights expert-based
- [ ] Practical apps grounded
- [ ] Error corrections 5-part complete
- [ ] Gracious tone maintained
- [ ] Multi-perspective fairness
- [ ] Bias detection passed
- [ ] Teaching helps appropriate
- [ ] Multiple sources when available

**If <80% → Revise before proceeding**

**Level 3: MEDIUM PRIORITY (Must pass 60%+)**

Check 8 MEDIUM PRIORITY criteria:
- [ ] Credentials documented
- [ ] Translator guidance field-tested
- [ ] Cross-references present
- [ ] Verification dates recorded
- [ ] Coverage notes clear
- [ ] Discipline-specific coverage noted
- [ ] Cultural sensitivity addressed
- [ ] Scope boundaries respected

**If <60% → Note improvements**

### 7.2 Special Validation

**If Error Correction:**
- [ ] All 5 parts complete
- [ ] 4+ evidence types
- [ ] Authority pyramid (min 2 sources, 1 HIGH/VERY HIGH)
- [ ] Gracious tone throughout

**If Multi-Perspective:**
- [ ] All 3 bias tests passed (Reversal, Respect, Evidence)
- [ ] Minimum 2 positions fairly represented
- [ ] Guidance as options, not mandates

**If Discipline-Specific:**
- [ ] Appropriate framing provided
- [ ] Discipline context clear
- [ ] No forced general content

---

## Step 8: Skip Decision (If Applicable)

### 8.1 When to Skip

**Skip if:**
1. Grammatical particle (δέ, γάρ, etc.)
2. Function word with no semantic content
3. Insufficient expert web coverage (after exhaustive search)
4. Tool 1 is fully sufficient (no practical insights beyond lexicon)

### 8.2 Skip Documentation

**Use:** `templates/skip-decision-template.yaml`

**Required:**
- Skip reason (grammatical_particle | function_word | insufficient_coverage | tool_1_sufficient)
- Skip rationale (detailed explanation)
- Search documentation (minimum 5 queries if insufficient_coverage)
- Scope boundary analysis (Tool 1 vs Tool 3 territory)

**File Location:** `work/G####/skip-decision.yaml`

**No output file created** - skip decision is success, not failure

**See:** Experiment 3 (G1161 de particle) as model

---

## Step 9: Attribution Updates

### 9.1 Check ATTRIBUTION.md

**For each new source used:**

1. **Check if already in ATTRIBUTION.md**
   - Search for site name or author
   - If exists → use existing citation code

2. **If new source:**
   - Add entry to ATTRIBUTION.md
   - Include: copyright notice, citation code, license type, URL
   - Follow ATTRIBUTION.md format

**Required fields:**
```markdown
### [Site Name]

**Citation Code:** {code}
**Copyright:** © [Year] [Owner]
**License:** [Type - e.g., Used with attribution, Fair use, CC BY]
**URL:** [Base URL]
**Purchase/Access:** [Link if applicable]
**Notes:** [Any usage restrictions or attribution requirements]
```

---

## Step 10: Final Review & Commit

### 10.1 Final Review

**Check:**
- [ ] File location correct: `.data/bible/words/strongs/{num}/{num}-web-insights.yaml`
- [ ] All validation passed (Level 1: 100%, Level 2: 80%+, Level 3: 60%+)
- [ ] Inline citations complete
- [ ] ATTRIBUTION.md updated
- [ ] No fabricated data
- [ ] Tool 1 read and referenced

### 10.2 Commit & Push

**Follow Git workflow:**

```bash
# Add file to sparse-checkout if needed
cd .data
git sparse-checkout add bible/words/strongs/G####
cd ..

# Add and commit
git add .data/bible/words/strongs/G####/G####-web-insights.yaml
git add ATTRIBUTION.md  # If updated

git commit -m "feat(strongs-tool3): add web insights for G#### ([word])

- [Number] sources ([authority distribution])
- [Content types: error correction / multi-perspective / standard]
- [Key findings or special notes]

Validation: L1=100%, L2=[%], L3=[%]"

# Push immediately
git push -u origin [branch-name]
```

---

## Quality Standards Summary

### Non-Negotiable (Level 1 - CRITICAL)
1. Verifiable credentials for ALL sources
2. No fabrication whatsoever
3. Inline citations for all claims
4. Authority levels marked clearly
5. Tool 1 integration (read first, no contradictions)
6. Error corrections complete (5-part if applicable)
7. Scope boundaries respected

### Essential Quality (Level 2 - HIGH PRIORITY)
1. Expert-based insights (not opinion)
2. Grounded applications (field-tested preferred)
3. Complete error corrections (5-part structure)
4. Gracious, pedagogical tone
5. Multi-perspective fairness (no bias)
6. Bias detection tests passed
7. Appropriate teaching helps
8. Multiple sources when available

### Quality Enhancement (Level 3 - MEDIUM PRIORITY)
1. Full credential documentation
2. Field-tested translator guidance
3. Cross-references to other tools
4. Verification dates recorded
5. Clear coverage notes
6. Discipline-specific context
7. Cultural sensitivity addressed
8. Scope boundary clarity

---

## Common Pitfalls to Avoid

1. **Not reading Tool 1 first** → Duplication, wasted effort
2. **Single-discipline search** → Missing specialized coverage (see Exp 2)
3. **Forcing content** → Fabrication risk when coverage is insufficient
4. **Unverified credentials** → Authority level cannot be assigned
5. **Biased multi-perspective** → Failing bias detection tests
6. **Harsh error corrections** → Tone failures, not gracious/pedagogical
7. **Incomplete 5-part structure** → Error corrections lack teaching value
8. **Skipping scope assessment** → Including grammatical particles inappropriately
9. **No inline citations** → Cannot verify claims
10. **Ignoring cultural sensitivity** → Missing post-colonial, denominational factors

---

## Time Management

**Estimated times by word type:**

| Word Type | Search | Vetting | Synthesis | Validation | Total |
|-----------|--------|---------|-----------|------------|-------|
| Standard word | 45 min | 30 min | 90 min | 30 min | **2.5-3 hrs** |
| Error correction | 60 min | 45 min | 150 min | 45 min | **4-5 hrs** |
| Multi-perspective | 60 min | 45 min | 180 min | 45 min | **5-6 hrs** |
| Interdisciplinary | 60 min | 45 min | 150 min | 45 min | **4-5 hrs** |
| Skip decision | 30 min | N/A | N/A | 15 min | **45 min** |

**Budget accordingly:**
- 2-3 words per day (standard)
- 1-2 words per day (complex)

---

## Questions & Troubleshooting

### Q: Found only 1 source - proceed or skip?

**A:** Depends on quality and content type:
- If 1 MEDIUM-HIGH+ source with substantial content → Proceed with "limited coverage" caveat
- If 1 MEDIUM-LOW or less → Skip (insufficient)
- If error correction with 1 source → Skip (need minimum 2, prefer 1 HIGH/VERY HIGH)

### Q: Found disagreement but only 1 position has credentialed advocates?

**A:** Don't fabricate second position. Options:
1. Present single position if well-supported, note "limited scholarly engagement"
2. If other view lacks credentials, note as "popular teaching" vs "scholarly consensus"
3. Don't create false balance

### Q: Source is good but author credentials unclear?

**A:** Invest time in verification:
1. Check "About" page, faculty listings, LinkedIn
2. Search for publications, degrees
3. Contact site if necessary
4. If unverifiable → Cannot use (Level 1 failure)

### Q: Discipline-specific coverage but not biblical - include?

**A:** Yes, if:
1. Relevant to word meaning (e.g., virtue ethics for eutrapelia)
2. Properly framed ("theological virtue perspective on...")
3. Sources credentialed in that discipline
4. No fabricated biblical content to "fill gaps"

See Experiment 2 (eutrapelia) as model.

### Q: All sources agree - is this multi-perspective?

**A:** No. Multi-perspective applies when:
1. Genuine scholarly disagreement exists
2. Multiple credible positions with advocates
3. If consensus → document as standard insight (not disagreement)

### Q: Tool 1 already has everything - skip?

**A:** Probably. If Tool 3 would only duplicate Tool 1 without value-add:
- Skip reason: `tool_1_sufficient`
- Rationale: "Lexicon data complete, no modern debates, no error corrections, no translator-specific guidance"

---

## Reference Files

**Before starting any word:**
- [ ] `README.md` - Tool 3 overview
- [ ] `schema.yaml` - Output structure
- [ ] `validation/quality-checklist.md` - Validation criteria

**During research:**
- [ ] `research/expert-blog-inventory.md` - Vetted sources
- [ ] `research/authority-detection.md` - Credentialing framework

**During extraction:**
- [ ] `templates/error-correction-template.yaml` - 5-part structure
- [ ] `templates/multi-perspective-template.yaml` - Fairness framework
- [ ] `templates/skip-decision-template.yaml` - Skip documentation

**For examples:**
- [ ] `experiments/exp4-error-correction/G1411-synthesis.md` - Error correction model
- [ ] `experiments/exp1-scholarly-disagreement/G4151-findings.md` - Multi-perspective model
- [ ] `experiments/exp5-cultural-debate/G1577-guidance-synthesis.md` - Cultural sensitivity model
- [ ] `experiments/exp2-rare-hapax/G2160-assessment.md` - Discipline-specific model
- [ ] `experiments/exp3-scope-boundary/G1161-boundary-assessment.md` - Skip decision model

---

**Remember:** Quality over quantity. Better to skip a word than force content that fails validation.
