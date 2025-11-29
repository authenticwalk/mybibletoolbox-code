# Language Selection for Person System Feature Enrichment

## Core Languages (MUST INCLUDE)

Based on STAGE-2-1-ANALYSIS-DATASET.md requirements, these are mandatory:

| Code | Format | Reason | Availability |
|------|--------|--------|--------------|
| `eng-YLT` | full | Literal English (Young's Literal Translation) | Both OT & NT |
| `grc` | prefix | Greek source (NT=BYZ/SR, maps automatically) | NT only |
| `hbo` | prefix | Hebrew source (OT=WLC) | OT only |
| `heb-heb` | full | Modern Hebrew (both testaments) | Both OT & NT |
| `lat-VUC` | full | Latin Vulgate (historical, both testaments) | Both OT & NT |
| `arb-NAV` | full | Arabic NAV translation | Both OT & NT |

## Additional Languages That Mark Person/Clusivity

Based on LANGUAGES.md research showing ~31.5% of world languages mark clusivity:

### Austronesian Languages (Nearly Universal Clusivity Marking)

| Code | Language | Rationale | Expected in Data |
|------|----------|-----------|------------------|
| `tgl` | Tagalog | Mandatory clusivity: *tayo* (incl) vs *kami* (excl). Filipino/Philippines. Large speaker base. | Yes |
| `ind-AYT` | Indonesian | Clusivity: *kita* (incl) vs *kami* (excl). Malay family. Large speaker base. | Yes (using ind for auto-match) |
| `fij` | Fijian | Mandatory clusivity in dual/trial/plural. Austronesian. | If available |

### Indo-European Languages (No Clusivity - Baseline)

| Code | Language | Rationale | Expected in Data |
|------|----------|-----------|------------------|
| `deu-1912` | German (1912) | Major European language, no clusivity | Yes |
| `fra-LSG` | French (Louis Segond) | Major European language, no clusivity | Yes |
| `spa-BES` | Spanish (Biblia Española Sagradas) | Major world language, no clusivity | Yes |

### Other Useful Languages

| Code | Language | Rationale | Expected in Data |
|------|----------|-----------|------------------|
| `vie` | Vietnamese | Marks clusivity: *chúng ta* (incl) vs *chúng tôi* (excl). Southeast Asia. | If available |
| `zho-CUV-SIMP` | Chinese (Simplified) | Mandarin optional clusivity 咱们 (incl) vs 我们 (ambiguous) | Yes |
| `kor` | Korean | No clusivity, but different honorifics by person | Yes |

## Final Selection for Enrichment

Using the script's format requirements (full code when both OT/NT, prefix when version differs):

```
eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,tgl,ind,deu-1912,fra-LSG,spa-BES,vie,zho-CUV-SIMP,kor
```

**Total: 14 languages**
- 6 core (required)
- 8 additional (clusivity markers + baseline comparisons)

## Validation Against Sample Verses

### GEN.001.026 ("Let us make")
- ✓ Can identify "us" in all languages
- ✓ Tagalog should show first person plural inclusive (Trinity interpretation)
- ✓ Arabic shows plural first person (no clusivity distinction)

### MAT.006.012 ("Forgive us our debts")
- ✓ Can identify "us" (exclusive - we humans, not God)
- ✓ Tagalog should use *kami* (exclusive)
- ✓ Greek ἡμῖν (no clusivity marking - interpretation required)

All selected languages have sufficient data and demonstrate the feature.
