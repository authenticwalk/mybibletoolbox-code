# Time Granularity: Research Synthesis

**Feature Definition**: Time granularity captures temporal remoteness—how distant an event is from the discourse moment (now/reference point). Distinct from tense (past/present/future) and aspect (perfective/imperfective), it specifies HOW FAR in the past/future an event occurred.

**Theological Significance**: 15% of biblical contexts are non-arbitrary (crucifixion hours, "third day" resurrection, creation origins, eschatological timing); 85% are stylistically flexible.

---

## 1. TBTA Documentation (`TBTA.md`)

**Complete Value Inventory**: 23-24 character codes organized in three temporal domains:
- **Past** (13 values): P=Present; D/A/a/b/c/d/e/f/g/h/i/q=past distances (immediate to eternity past, unknown)
- **Future** (8 values): E/F/j/k/l/m/n/o/p=future distances (immediate today to year ahead, unknown)
- **Atemporal** (2 values): r=Discourse, T=Timeless

**Gateway Features**: Time applies to **Verbs only** (position 1 of 9-position code). Mood constraints unclear; Aspect co-occurs but independent. Discourse Genre may influence selection (narrative=historic past; teaching=timeless).

**Policy Gaps**: No explicit rule for semantic vs. morphological priority; discourse perspective (modern/original audience/internal story time) unstated; semantic temporal distance marked, not source language morphology.

**Known Issues**: Aspect overgeneralized as "Unmarked" (CRITIQUE.md); no Aktionsart classification; Greek imperatives miscoded as Indicative; coverage complete within 11,649-verse corpus (~37% Bible).

**Discrepancies**:
- **h-value semantics**: "Historic Past" (GitHub) vs "Remote Past/living memory" (DATA-STRUCTURE.md)
- **c-value range**: "3 Days Ago" (GitHub) vs "2-7 days ago" (DATA-STRUCTURE.md)
- **Total values**: "20+" stated vs 23 documented

**Edge Cases**: Timeless vs Present distinction policy absent; Discourse vs Timeless in teaching contexts unclear; flashbacks/anteriority unmarked in documentation; eschatological future encoding absent (archived research included `L` value not in official export).

---

## 2. Language Typology (`LANGUAGES.md`)

**Source Languages**: ❌ **Hebrew & Greek lack explicit temporal remoteness morphology**. Both are aspect-prominent; context determines remoteness, not morphology. Translators must infer temporal distance from context (genealogies, narrative framing, cultural knowledge), then encode it for target languages requiring grammatical marking.

**Language Family Patterns** (1,009 languages analyzed):

| Family | Count | Status | Granularity | Pattern |
|--------|-------|--------|-------------|---------|
| **Niger-Congo (Bantu)** | 89 | ✅ Mandatory | High (4-8) | Hodiernal/hesternal/remote |
| **Austronesian** | 176 | ⚠️ Optional (27%) | Variable | TAM optional, adverb-dependent |
| **Trans-New Guinea** | 141 | ✅ Majority mandatory | Medium-High | Hodiernal/hesternal systems |
| **Indo-European** | 135 | ❌ Optional | Low | Simple past/present/future + adverbs |
| **Quechuan** | 18 | ✅ Mandatory | Medium | **Fused with evidentiality** |
| **Otomanguean** | 69 | ✅ 100% mandatory | Medium | Obligatory TAM |
| **Sino-Tibetan** | 18 | ⚠️ Adverbs mandatory | Medium | Aspect particles + temporal adverbs |
| **Mayan** | 41 | ❌ Optional | Low | Aspect-based, minimal remoteness |

**Root Languages**: 11/13 (Hebrew, Greek, English, Spanish, French, German, Portuguese, Arabic, Russian, Indonesian, Mandarin) lack obligatory temporal remoteness. **Swahili exception**: Mandatory Bantu system.

**Candidate Languages for Stage 2** (10 selected):
1. English (Indo-European, baseline)
2. **Swahili** (Bantu, mandatory, bridge language)
3. Mandarin (aspect + adverbs, bridge)
4. Quechua, Cusco (temporal-evidential fusion)
5. **Tagalog** (Austronesian, aspect-based with temporal adverbs)
6. Amele (Trans-New Guinea, hodiernal)
7. K'iche' (Mayan, aspect-based)
8. Amuzgo (Otomanguean, 100% obligatory)
9. Spanish (Indo-European, bridge)
10. Indonesian (optional TAM)

**Cultural Nuances**: Lunar calendars (Hebrew, Chinese, Islamic); event-based time reckoning (Amazonian languages—no metric units); relative hour systems (biblical "third hour" = variable-length hours); absolute vs. relative tense variation (Russian lacks pluperfect/future perfect).

---

## 3. Scholarly Research (`SCHOLARLY.md`)

**28+ Scholarly Sources** organized in 4 sections:

- **Linguistic Theory** (Comrie, Dahl, Bybee, Klein, Cook, Haspelmath, Reichenbach): Foundational frameworks for aspect vs. tense, temporal remoteness typology, grammaticalization pathways, Reichenbach's E-R-S temporal coordinates.

- **Typological Databases** (WALS, Grambank, 2,467 languages): ~20% of languages mark remoteness distinctions; 99-language WALS sample shows salient non-marking in Southeast Asia; Grambank covers 195 grammatical features including tense/aspect domains.

- **Translation Case Studies**:
  - **Crucifixion Timing** (Mark 15:25 vs John 19:14): Jewish (sunrise-based) vs Roman (midnight-based) hour systems create apparent contradiction. Resolved through different temporal reference frames. Theological stakes: Passover typology, supernatural darkness, divine timing.
  - **"Three Days and Three Nights"** (Matthew 12:40): Hebrew inclusive reckoning (part of day = full day). Corroborated by Esther 4:16-5:1, Genesis 42:17-18, 1 Samuel 30:12-13. Cross-cultural variation: some languages share this idiom, others require footnote.
  - **Papua New Guinea Bible Translation**: Event-based time reckoning (Kaluli) lacked metric calendar/clock concepts. Missionization introduced new vocabulary, creating evidential value for temporal markers. Hybrid solutions blend indigenous seasonal terms with borrowed calendar terms.

- **Key Biblical Passages**: 25+ verses analyzed for temporal precision requirements (Genesis genealogies, Daniel 9 prophetic weeks, Revelation eschatological durations, Passion Week chronology, crucifixion/resurrection timing).

**Findings**: Temporal precision is **non-arbitrary in 15% of contexts** (atonement theology, resurrection apologetics, creation historicity, divine sovereignty, eschatological certainty). Most temporal references (85%) are stylistically flexible (narrative past distinctions, wisdom literature vagueness, travel narrative sequencing).

---

## 4. Theological Classification (`THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`)

**Non-Arbitrary Contexts (15%)**:

**HIGH DOCTRINAL STAKES**:
- **Crucifixion hours** (Mark 15:25, 33-34): 3rd/6th/9th hour precision connects to Passover lamb timing, temple sacrifice schedule. Vague marking loses theological connection.
- **Resurrection "third day"** (1 Cor 15:4): Creedal formula, prophetic fulfillment (Jonah sign). Specific day-count essential for historical verification.
- **Genesis 1:1** ("In beginning"): Historic/primordial past required (not recent past, not timeless myth). Seven-day structure establishes Sabbath theology.
- **Jesus' "hour"** (John 2:4, 12:23): Appointed/eschatological time (not casual future). Demonstrates sovereignty over Passion timing.
- **Second Coming** (Matthew 24:36): Eschatological future + unknown timing (not calculable near/remote future). Prevents date-setting, maintains watchfulness.

**MEDIUM CONTEXTUAL STAKES**:
- **Sabbath/festival timing**: Hodiernal subdivisions required for obedience (twilight for Passover lamb, "between evenings").
- **Prayer hours** (Acts 2:15, 3:1, 10:9): 3rd/6th/9th hours establish daily rhythm of early church, narrative context.
- **Flood chronology** (Genesis 7-8): Precise calendar dates mark historical narrative genre (not mythology).

**Arbitrary Contexts (85%)**:
- General past narratives (remote vs. historic distinction stylistic)
- Vague wisdom literature ("in time," "one day")
- Travel narratives ("after this," "then," "later")
- Timeless/gnomic statements (eternal truths, no temporal change)

---

## Key Discrepancies & Gaps

| Issue | TBTA | Languages | Scholarly | Resolution |
|-------|------|-----------|-----------|-----------|
| Source lang encoding | Not listed | ❌ Neither Hebrew nor Greek marks remoteness morphologically | Confirmed: aspect-prominent, context-dependent | Translators must infer from context |
| Semantic vs morphological | Not stated | N/A | "Semantic temporal remoteness" priority implied by Genesis example | TBTA extracts contextual meaning, not morphology |
| Discourse perspective | Not listed | Not listed | Modern reader perspective (2025) vs. original audience (1st century) | Likely original audience; needs verification |
| Eschatological future | 23 values documented | Mandatory in many families | Special category needed (end-times vs calculable) | Consider adding if not already present |
| Frequency distribution | "Complete" (11,649 verses) | Languages analyzed, not values | Not calculated | Stage 2 analysis needed |

---

## Implications for Algorithm

1. **For high-granularity languages** (Bantu, Trans-New Guinea, Quechuan): Map biblical contexts to appropriate remoteness markers. Critical in 15% theological contexts; flexible in 85%.

2. **For aspect-based languages with temporal adverbs** (Tagalog, Mandarin): Obligatory aspect marking (completed/ongoing/contemplated) combined with optional temporal adverbs. TBTA guides adverb selection; non-arbitrary contexts require explicit temporal adverbs.

3. **For low-granularity languages** (English, Indo-European): Adverbials carry precision ("at the third hour," "on the third day," "in the beginning"). TBTA provides classification, translators add explicit temporal markers.

4. **For languages without obligatory temporal marking**: Temporal choice is optional; translator decides based on theological/contextual priority. Non-arbitrary contexts require precision; arbitrary contexts allow flexibility.

5. **For event-based languages** (Amazonian): May require conceptual shift from metric time to natural/social event cycles. Hybrid solutions blend indigenous and introduced temporal frameworks.

---

**Confidence Levels**: TBTA documentation well-researched (23-value inventory confirmed); language typology data-backed (1,009 language corpus); scholarly analysis comprehensive (28+ sources); theological classification requires peer review (marked unverified where inferred from Scripture).

**Next Stage**: Language translation database (Stage 2) should verify TBTA values in actual corpus, test theological assessments with peer review, validate translation impact claims with field translators working in high-granularity languages.
