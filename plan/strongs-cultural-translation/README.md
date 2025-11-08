# Strong's Cultural Translation Initiative

**Created:** 2025-11-08
**Status:** Planning Phase
**Owner:** Part of Strong's Word Enhancement comprehensive strategy

---

## Purpose

Document cultural and conceptual translation challenges for Strong's words when the original concept doesn't exist in target cultures. This complements:
- **Lexical Research** (what it means) → `/plan/strongs-enrichment-tools/`
- **TBTA Hints** (how to say it grammatically) → `/plan/tbta-strongs-hints-*.md`

This initiative answers: **"What word/concept should we use when the original doesn't exist in target culture?"**

---

## Three Types of Challenges

### 1. Non-Existent Physical Concepts
**Examples:** Snow (H7950), sheep/lambs (G721/H3532), camels (G2574)
**Problem:** Target culture has never experienced these objects
**Solution Categories:**
- Cultural substitutes (seal pup for lamb in Arctic)
- Descriptive phrases ("frozen rain from sky" for snow)
- Loan words with teaching (transliterate + explanation)

### 2. Untranslatable Abstracts
**Examples:** Agape love (G26), grace (G5485), righteousness (H6666)
**Problem:** Target language lacks semantic equivalent
**Solution Categories:**
- Semantic approximation (find closest match)
- Redemptive analogies (Peace Child approach)
- Compound descriptive phrases
- Loan word with extensive teaching notes

### 3. Cultural Sensitivities
**Examples:** Taboo numbers (666), offensive animals (pigs, dogs), body parts (bowels = compassion)
**Problem:** Direct translation creates offense or misunderstanding
**Solution Categories:**
- Functional equivalents (heart for bowels in emotion contexts)
- Euphemisms when culturally appropriate
- Teaching notes explaining original cultural context

---

## Data Sources

### Primary: 900+ Bible Translations (TBTA Corpus)
- Existing translations show documented solutions
- Cross-linguistic validation across language families
- Evidence of what works/doesn't work in real usage

### Secondary: Translation Notes
- unfoldingWord Translation Notes (CC-BY-SA)
- SIL/Wycliffe case studies
- Academic research on receptor languages

### Tertiary: Scholarly Research
- Don Richardson's "Peace Child" methodology
- Cultural anthropology studies
- Missiological journals

---

## Methodology Overview

See detailed methodology in [research/challenges.md](research/challenges.md)

### 4-Step Process

**Step 1: Identify Core Theological Meaning**
- What truth must be preserved?
- What theological stakes are involved?
- What distortions could arise?

**Step 2: Document Cultural Gap**
- Why doesn't direct translation work?
- What's missing in target culture?
- What dangers exist in alternatives?

**Step 3: Research Solutions**
- Survey existing translations in similar cultures
- Extract patterns across language families
- Document both successful and failed approaches

**Step 4: Provide Translator Guidance**
- Multiple solution strategies documented
- Theological evaluation of each option
- Mitigation strategies for weaknesses
- Clear recommendations with rationales

---

## Output Schema

Each Strong's word with cultural challenges gets a `{number}.strongs-cultural.yaml` file:

```yaml
strongs_number: G721
lemma: ἀρνίον
category: [animal_substitution, sacrificial_imagery]

core_meaning_to_preserve:
  - "Innocence and purity"
  - "Substitutionary sacrifice"
  - "Connection to Passover lamb"

translation_challenges:
  - culture_type: "Arctic (no sheep)"
    problem: "Sheep/lamb unknown; no cultural reference point"
    theological_stakes: "HIGH - Central to atonement theology"

solutions_documented:
  - language: iku (Inuktitut)
    strategy: cultural_substitute
    translation: "nattiq Guutimut" (seal pup of God)
    rationale: "Seals are primary food/sacrifice animal in Inuit culture"
    preserves: [innocence, substitution, sacrifice_imagery]
    loses: [OT_Passover_connection]
    mitigation: "Footnote explaining lamb/Passover background"
    evaluation: "✅ Successful - preserves core theological truth"
    source: "{iku-bible-1991}"

translator_guidance:
  principle: "Substitute culturally appropriate sacrificial animal"
  test_questions:
    - "Is this animal used for food/clothing (economic value)?"
    - "Is this animal young form recognizable (innocence)?"
    - "Does substitution preserve purity/sacrifice imagery?"
  recommended_approach: "cultural_substitute"
  footnote_required: true
```

---

## Current Status

### Completed ✅
- [x] Comprehensive planning document (research/challenges.md)
- [x] Pilot study with 3 sample words (experiments/pilot-samples.md)
  - G26 (agape) - Untranslatable abstract
  - H7950 (snow) - Non-existent physical concept
  - G721 (lamb) - Animal requiring cultural substitution

### Next Steps
1. **Create tool README** following TEMPLATE.md
2. **Test data access** to TBTA translation corpus
3. **Run experiments** on 5-10 high-value words
4. **Design extraction pipeline** for automated pattern detection
5. **Build validation framework** for theological accuracy

---

## Success Criteria

### Quality Standards
- ✅ All solutions from documented real translations (no speculation)
- ✅ Multiple language families represented per word
- ✅ Theological impact assessed for each solution
- ✅ Both successful AND unsuccessful approaches documented
- ✅ Translator guidance grounded in evidence

### Coverage Goals
- **Phase 1:** Top 50 words with highest cultural challenge + theological significance
- **Phase 2:** Expand to 300 most frequent words
- **Phase 3:** Long tail based on priority and community contribution

### Impact Metrics
- Number of cultures with documented solutions
- Language families covered
- Theological validation by scholars/translators
- Real-world adoption by translation teams

---

## Directory Structure

```
strongs-cultural-translation/
├── README.md (this file)
├── research/
│   └── challenges.md (comprehensive methodology - 834 lines)
├── experiments/
│   └── pilot-samples.md (3 complete pilot entries - 1011 lines)
└── validation/
    └── (to be created)
```

**Note:** research/challenges.md and experiments/pilot-samples.md exceed progressive disclosure limits (400 lines for topic files). These should be split into smaller files in a future refactoring.

---

## Related Documents

- **Overview:** `/plan/strongs-comprehensive-strategy.md` - Connects all 3 Strong's initiatives
- **Lexical Research:** `/plan/strongs-enrichment-tools/` - Etymology, scholarly analysis
- **TBTA Hints:** `/plan/tbta-strongs-hints-summary.md` - Grammatical patterns
- **Source Discovery:** `/plan/strongs-enrichment-sources/` - Finding lexicons and articles

---

## Complementary to TBTA Hints

**TBTA Hints provide:** Grammatical/linguistic patterns (HOW to say it)
- Number systems (dual, trial, plural)
- Person/clusivity (inclusive/exclusive we)
- Proximity (demonstrative distance)
- Aspect, mood, semantic roles

**Cultural Challenges provide:** Semantic/conceptual solutions (WHAT to say)
- Non-existent concepts (snow, sheep, bread)
- Untranslatable abstracts (agape, grace, righteousness)
- Cultural sensitivities (taboos, offensive animals)

**Together:** Complete translation guidance combining grammar + semantics + culture

---

## Examples

### Example 1: Translating "snow" (H7950) to Tropical Culture
```yaml
problem: "Tropical culture has never experienced snow"
solution: "white like cloud-water" {haw-bible}
preserves: "Whiteness and purity imagery (Isaiah 1:18)"
```

### Example 2: Translating "Lamb of God" (G721) to Arctic
```yaml
problem: "Arctic culture has no sheep"
solution: "seal pup of God" {iku-bible-1991}
preserves: "Innocence, substitutionary sacrifice"
loses: "Direct OT Passover connection"
mitigation: "Footnote explaining Passover lamb background"
```

### Example 3: Translating "agape" (G26) to Merit-Based Culture
```yaml
problem: "Culture lacks concept of unmerited love"
solution: "sacrificial-choosing-care" {compound-phrase}
teaching_emphasis: "This love is given freely, not earned"
```

---

**Next:** Review `/plan/strongs-comprehensive-strategy.md` for how this fits into the overall Strong's enhancement vision.
