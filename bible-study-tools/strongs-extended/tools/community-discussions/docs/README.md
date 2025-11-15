# Community Discussions - Documentation

## Status
✅ PRODUCTION-READY (Research ✅ | Experiments 3/3 ✅ | Validation ✅)

## Overview
Document common misconceptions, popular errors, and controversies about biblical words from community discussions, paired with scholarly refutations. Identifies and corrects widespread errors to prevent misinformation propagation.

**Authority Level:** TWO-TIER STRUCTURE
- Error Documentation: LOW (Stack Exchange, forums, blog comments)
- Error Refutation: HIGH/MEDIUM (peer-reviewed articles, lexicons, expert blogs)

**Timeline:** 7 months production (500 words @ 80 min each, optimized workflow)

## Methodology (3 Steps)
1. **Controversy Discovery** - WebSearch for common questions, misconceptions in community forums
2. **Error Classification** - Categorize type (etymological fallacy, anachronism, theological projection, etc.)
3. **Scholarly Refutation** - Find authoritative corrections with evidence

**Critical Rule:** NEVER document error without scholarly refutation

## Error Type Taxonomy (7 Types)
- **Etymological Fallacies:** False derivations (e.g., "dunamis = dynamite")
- **Anachronisms:** Modern meanings imposed on ancient words
- **False Cognates:** Assuming similar-sounding words are related
- **Over-Specification:** Adding specific meanings not in the text
- **Lexical Maximalism:** Claiming all senses apply simultaneously
- **Theological Projection:** Reading systematic theology into individual words
- **Other:** Edge cases and unique error patterns

## Key Innovations
- **Error-Refutation Pairing:** Every error documented with scholarly correction
- **Prevalence Assessment:** Track how widespread the misconception is
- **Gracious Tone:** Educational approach, not mocking community members
- **Quick Reference Cards:** Fast error lookup for translators/students
- **Related Errors:** Document error clusters and patterns

## Experiments Completed (Adversarial Testing)
1. G1411 (δύναμις, dunamis) - Etymological fallacy (chronological) → "Dunamis = dynamite" refuted
2. G1577 (ἐκκλησία, ekklesia) - Etymological fallacy (root meaning) → "Called out ones" refuted
3. H430 (אֱלֹהִים, Elohim) - Theological projection (sensitive topic) → "Plural proves Trinity" refuted

**Validation Scores:** L1:100% | L2:100% | L3:88% across all experiments

## Coverage Strategy
**Target: ~500 words with documented errors**
- **Known Errors (100):** Well-documented false claims
- **Frequent Questions (200):** Stack Exchange, forum discussions
- **Theological Debates (100):** Legitimate vs. popular confusion
- **Opportunistic (100):** Discovered during other tool work

**Skip (~13,500):** No community discussion, no errors found, lexicon-core sufficient

**Principle:** Only create file if genuine error/controversy exists

## Integration with Other Tools
- **Tool 1 (Lexicon):** Foundation - read first, check for convergence data
- **Tool 2 (Scholarly):** Refutation source for academic corrections
- **Tool 3 (Web Insights):** Refutation source - expert blogs often address errors

## Output Format
`.data/strongs/{num}/{num}-community-discussions.yaml`

Sections: controversies (error → refutation → evidence → classification), common_questions, helpful_cautions

## Complete Documentation
**See:** `/plan/strongs-enrichment-tools/04-community-discussions/` for:
- Full methodology and schema
- 3 completed experiments with validation results (100% L1, 100% L2, 88% L3)
- Research on controversy patterns and refutation sources
- Error type taxonomy and detection strategies
- Quality checklist and validation criteria
- Production workflow optimization (80 min/word target)

This documentation will be migrated here during production deployment.
