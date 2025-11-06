# Clusivity Analysis - Verse Selection Plan

## INCLUSIVE Clusivity (7 verses)

Verses where "we/us" includes BOTH speaker AND addressee.

| # | Reference | Genre | Context | Why Inclusive | In Sparse-Checkout |
|---|-----------|-------|---------|---------------|-------------------|
| 1 | **Genesis 1:26** | Narrative | God (Trinity) speaking within Godhead | Speaker=God, Addressee=God (Trinity) - both included | ✅ GEN/001 |
| 2 | **Deuteronomy 5:3** | Law | Moses to Israelites about covenant | Moses includes himself with Israel as covenant recipients | ❌ Need DEU/005/003 |
| 3 | **Job 34:4** | Wisdom | Elihu to Job and friends | Invites listeners to join in discernment together | ❌ Need JOB/034/004 |
| 4 | **Psalm 95:1** | Poetry | Psalmist calling congregation to worship | Psalmist joins congregation in singing to God | ❌ Need PSA/095/001 |
| 5 | **Isaiah 2:3** | Prophecy | Nations inviting each other | Nations invite each other to pilgrimage - both groups go | ❌ Need ISA/002/003 |
| 6 | **John 11:15** | Gospel | Jesus to disciples about Lazarus | Jesus + disciples will go together to Lazarus | ❌ Need JHN/011/015 |
| 7 | **Hebrews 10:24** | Epistle | Author exhorting Hebrew Christians | Author includes himself with readers in mutual encouragement | ❌ Need HEB/010/024 |

**Summary**: 1 of 7 currently in sparse-checkout

## EXCLUSIVE Clusivity (7 verses)

Verses where "we/us" includes speaker + others, but NOT the addressee.

| # | Reference | Genre | Context | Why Exclusive | In Sparse-Checkout |
|---|-----------|-------|---------|---------------|-------------------|
| 1 | **Acts 15:25** | Epistle (Narrative) | Apostles writing to churches | "We apostles" excludes church recipients | ❌ Need ACT/015/025 |
| 2 | **Exodus 3:18** | Law/Narrative | Moses/Israelites to Pharaoh | "We Hebrews" excludes Pharaoh (Egyptian) | ❌ Need EXO/003/018 |
| 3 | **Psalm 79:8** | Poetry (Lament) | Psalmist praying to God | Prayer TO God - "us/our" = humans, not God | ❌ Need PSA/079/008 |
| 4 | **Isaiah 6:8** | Prophecy | God's divine council deliberation | "Us" = divine council, not human prophet addressee | ❌ Need ISA/006/008 |
| 5 | **Matthew 6:9** | Gospel (Teaching) | Jesus teaching prayer | "Our Father" - praying TO God excludes God from "our" | ⚠️ Have MAT/005, need MAT/006/009 |
| 6 | **John 3:11** | Gospel (Discourse) | Jesus to Nicodemus | "We speak" (Jesus+witnesses) vs "you" (Nicodemus) - explicit separation | ✅ JHN/003 |
| 7 | **1 Corinthians 1:23** | Epistle | Paul to Corinthian church | "We preach" (apostles) to church - apostolic authority distinction | ❌ Need 1CO/001/023 |

**Summary**: 1 of 7 currently in sparse-checkout (JHN 3:11)

## Sparse-Checkout Commands Needed

```bash
cd .data

# INCLUSIVE verses
git sparse-checkout add commentary/DEU/005/003
git sparse-checkout add commentary/JOB/034/004
git sparse-checkout add commentary/PSA/095/001
git sparse-checkout add commentary/ISA/002/003
git sparse-checkout add commentary/JHN/011/015
git sparse-checkout add commentary/HEB/010/024

# EXCLUSIVE verses
git sparse-checkout add commentary/ACT/015/025
git sparse-checkout add commentary/EXO/003/018
git sparse-checkout add commentary/PSA/079/008
git sparse-checkout add commentary/ISA/006/008
git sparse-checkout add commentary/MAT/006/009
git sparse-checkout add commentary/1CO/001/023

cd ..
```

## Analysis Priority

**Phase 1** (Currently available - start immediately):
1. Genesis 1:26 (Inclusive) ✅
2. John 3:11 (Exclusive) ✅

**Phase 2** (After sparse-checkout expansion):
- Complete remaining 5 inclusive verses
- Complete remaining 5 exclusive verses

## Notes

- **Correction**: Initial agent confusion about Gen 1:26 classification
  - Agent 1 correct: INCLUSIVE (Trinity addressing Trinity)
  - Agent 2 error: Marked as exclusive, but context is divine-to-divine, not divine-to-human
  - Reason for confusion: The verse involves creation of humans, but the "us" refers to intra-Trinitarian speech

- **Genre Distribution** (both lists):
  - ✅ Narrative: Gen 1:26, Exo 3:18, Acts 15:25
  - ✅ Law: Deu 5:3
  - ✅ Wisdom: Job 34:4
  - ✅ Poetry: Psa 95:1, Psa 79:8
  - ✅ Prophecy: Isa 2:3, Isa 6:8
  - ✅ Gospel: Jhn 11:15, Mat 6:9, Jhn 3:11
  - ✅ Epistle: Heb 10:24, 1Co 1:23, Acts 15:25
