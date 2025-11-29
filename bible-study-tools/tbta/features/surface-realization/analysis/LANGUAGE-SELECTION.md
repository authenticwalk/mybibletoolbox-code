# Language Selection for Surface Realization Feature

**Date**: 2025-11-29
**Feature**: Surface Realization
**Purpose**: Enrich dataset with translations that demonstrate pro-drop and pronoun realization patterns

## Selection Criteria

Based on research/LANGUAGES.md, we need languages that:
1. Show different pro-drop typologies (obligatory pronouns, rich-agreement, discourse-based, affix-based)
2. Are available in the eBible corpus
3. Can be verified for identifying constituents in translations

## Core Translations (Required)

| Code | Format | Language | Reason | Coverage |
|------|--------|----------|--------|----------|
| `eng-YLT` | full | English (Young's Literal) | Core + literal translation | OT+NT |
| `grc` | prefix | Greek (source) | Source language | NT (grc-BYZ/SR) |
| `hbo` | prefix | Biblical Hebrew | Source language | OT (hbo-WLC) |
| `heb-heb` | full | Modern Hebrew | Related to source | OT+NT |
| `lat-VUC` | full | Latin Vulgate | Core translation | OT+NT |
| `arb-NAV` | full | Arabic (Van Dyck) | Semitic, pro-drop | OT+NT |

## Feature-Specific Translations

### Tier 1: Obligatory Pronouns (Non-pro-drop)

| Code | Language | Rationale | Validated |
|------|----------|-----------|-----------|
| `fra-LSG` | French (Louis Segond) | Romance but non-pro-drop | Yes |
| `deu-1912` | German (Luther 1912) | Germanic non-pro-drop | Yes |

### Tier 2: Rich-Agreement Pro-drop

| Code | Language | Rationale | Validated |
|------|----------|-----------|-----------|
| `spa-BES` | Spanish (Biblia en Español Sencillo) | Major pro-drop language | Yes |
| `rus` | Russian | Slavic pro-drop (prefix match) | Yes |
| `arb-NAV` | Arabic | Already in core (Semitic pro-drop) | Yes |

### Tier 3: Discourse-Based Pro-drop

| Code | Language | Rationale | Validated |
|------|----------|-----------|-----------|
| `jpn` | Japanese | Radical pro-drop, topic-prominent | Yes |
| `cmn` | Mandarin Chinese | Topic chains, discourse pro-drop | Yes |
| `kor` | Korean | Episode constraints on pro-drop | Yes |

### Tier 4: Subject-Affix Languages

| Code | Language | Rationale | Validated |
|------|----------|-----------|-----------|
| `swa` | Swahili | Bantu subject prefixes | Yes |

### Tier 5: Mixed/Partial Systems

| Code | Language | Rationale | Validated |
|------|----------|-----------|-----------|
| `ind-AYT` | Indonesian (Alkitab Yang Terbuka) | Register-based pro-drop | Yes |

## Final Translation List

**Total**: 15 translation codes (avoiding duplicates)

### Command Format

```bash
--translations eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,fra-LSG,deu-1912,spa-BES,rus,jpn,cmn,kor,swa,ind-AYT
```

## Verification Notes

**Sample verses tested**:
- GEN.001.026 (OT, plural "us" - pro-drop test)
- MAT.004.019 (NT, subject pronouns - pro-drop test)

**Validation results**:
- All core languages have translations available
- Feature-specific languages cover all 5 typological tiers
- No duplicate language codes (only one English, one Arabic, etc.)
- Mix of prefix (grc, hbo, rus, jpn, cmn, kor, swa) and full codes

## Notes on Format

**Full code** (`eng-YLT`): Use when translation covers both OT and NT
**Prefix** (`grc`): Use when OT/NT have different versions - matches first available

The enrichment script will automatically match:
- `grc` → `grc-BRENT` (OT), `grc-BYZ` or `grc-SR` (NT)
- `hbo` → `hbo-WLC` (OT only)
- `rus` → First available Russian translation
- `jpn` → First available Japanese translation
- `cmn` → First available Mandarin translation
- `kor` → First available Korean translation
- `swa` → First available Swahili translation
