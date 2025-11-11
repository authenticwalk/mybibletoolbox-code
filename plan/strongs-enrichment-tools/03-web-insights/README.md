# Tool 3: Strong's Web Insights

**Status:** Research Phase Complete
**Authority:** MEDIUM (expert blogs) to MEDIUM-LOW (vetted ministry sites)
**Coverage:** ~2,000 words with good web resources
**Timeline:** 2 months (research ✅ → experiments → validation → production)

---

## Purpose

Extract modern insights, practical applications, and teaching guidance from expert web sources to supplement core lexical data.

**Value Add:**
- Bridges academic lexicons and practical ministry
- Modern scholarly insights in accessible formats
- Translator guidance and preacher illustrations
- Expert perspectives beyond peer-reviewed journals

**Boundaries:**
- NOT lexicon duplication (use Tool 1)
- NOT peer-reviewed scholarship (use Tool 2)
- NOT community forums (use Tool 4)

---

## Authority Levels

| Level | Definition | Examples |
|-------|------------|----------|
| **MEDIUM-HIGH** | Institutional backing | Tyndale House, seminary sites |
| **MEDIUM** | Ph.D. + publications | Bill Mounce, scholar blogs |
| **MEDIUM-LOW** | M.Div. + citations | Qualified practitioner synthesis |

**All sources must:**
- Have verifiable credentials
- Cite scholarly sources
- Add value beyond lexicons
- Be clearly marked with authority level

See `research/authority-detection.md` for detailed framework.

---

## Methodology

### 3-Step Process

**1. Source Discovery**
- WebSearch: `"{strongs} OR {word}" site:{vetted-domain}`
- Check blogs, structured sites, translator resources
- Apply authority detection criteria

**2. Content Extraction**
- WebFetch from vetted sources
- Focus on value-add: modern insights, practical applications, error corrections
- Extract author credentials simultaneously

**3. Synthesis**
- Read Tool 1 first (avoid duplication)
- Assign authority levels
- Validate against quality checklist
- Generate output YAML

See `research/expert-blog-inventory.md` for vetted sources.

---

## Research Phase ✅

### Documents Created

**`research/expert-blog-inventory.md`**
- 11 vetted sources across 4 tiers
- Extraction strategies per source type
- Red flags for exclusion

**`research/authority-detection.md`**
- Systematic credentialing criteria
- Detection patterns (faculty, authors, institutions)
- Decision tree for authority assignment

---

## Experimentation Phase (Next)

### 5 Experiments Designed

| # | Word | Test Focus | Expected Result |
|---|------|------------|-----------------|
| 1 | G26 (agape) | Abundant sources | 5+ sources, methodology validation |
| 2 | G1343 (righteousness) | Moderate coverage | 2-3 sources, quality maintenance |
| 3 | G1411 (dynamis) | Error correction | Dynamite fallacy refutation |
| 4 | H7950 (snow) | Translator guidance | Cultural translation solutions |
| 5 | G4944 (rare word) | Honesty test | Skip if insufficient (integrity) |

See `experiments/EXPERIMENTS-OVERVIEW.md` for details.

---

## Output Schema

**File:** `./bible/words/strongs/{num}/{num}-web-insights.yaml`

**Key Sections:**
- Modern insights (with authority marking)
- Practical applications (translators, preachers, students)
- Error corrections (error + refutation + evidence)
- Teaching helps (grounded in scholarship)
- Cross-references (to Tools 1, 2, 6)

See `schema.yaml` for complete structure.

---

## Validation

**3-Level Quality Checklist:** `validation/quality-checklist.md`

**Level 1 (CRITICAL - 100% pass):**
- Verifiable credentials
- No fabrication
- Inline citations
- Authority marked

**Level 2 (HIGH - 80%+):**
- Expert-based insights
- Grounded applications
- Multiple sources when available

**Level 3 (MEDIUM - 60%+):**
- Documentation completeness
- Cross-references present

---

## Integration

### Tool Dependencies

**Tool 1 (Lexicon Core) - REQUIRED**
- Read Tool 1 FIRST
- Tool 3 supplements (not duplicates)
- Focus on modern insights + applications

**Tool 2 (Scholarly) - COMPLEMENTARY**
- Tool 2: Peer-reviewed (HIGH authority)
- Tool 3: Expert blogs (MEDIUM authority)

**Tool 4 (Community) - BOUNDARY**
- Tool 3: Expert credentials required
- Tool 4: Community forums, no credential requirement

---

## Coverage Strategy

- **High-Priority (~500):** Theologically central, controversies (5+ sources)
- **Medium-Priority (~1,000):** High-frequency, practical (2-3 sources)
- **Low-Priority (~500):** Opportunistic (1+ source)
- **Skip (~12,000):** No web coverage, rely on Tool 1

---

## Success Metrics

- 2,000+ words with quality insights, 95%+ authority verification
- 100% pass Level 1 (critical), 90%+ pass Level 2 (high priority)
- No fabrication, supplements Tool 1, practical applications present

---

## Timeline & Principles

**Weeks 1-2:** Research ✅ | **Weeks 3-4:** Experiments | **Week 5:** Validation | **Weeks 6-9:** Production

**Principles:** Quality over quantity | Clear authority marking | Supplement Tool 1 | Honest coverage

---

## Next Steps

Execute 5 experiments → Validate methodology → Refine based on learnings → Production phase

---

## Related Documents

- `research/expert-blog-inventory.md` - Vetted sources, extraction strategies
- `research/authority-detection.md` - Credentialing framework
- `experiments/EXPERIMENTS-OVERVIEW.md` - All 5 experiment designs
- `experiments/exp1-high-coverage/README.md` - Agape experiment (and others)
- `schema.yaml` - Complete output structure
- `validation/quality-checklist.md` - 3-level validation criteria
- `/plan/strongs-comprehensive-strategy.md` - Overall Strong's strategy
- `/plan/strongs-enrichment-sources/IMPLEMENTATION-PLAN.md` - All 7 tools

---

**Last Updated:** 2025-11-11
**Research Phase:** ✅ COMPLETE
**Ready For:** Experimentation Phase
