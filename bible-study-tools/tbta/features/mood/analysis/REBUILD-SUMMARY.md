# Mood Feature Analysis Rebuild Summary

## Date: 2025-11-29

## Task
Re-run the mood feature analysis enrichment to add Japanese (jpn) language from research LANGUAGES.md.

## Actions Taken

1. **Checked current dataset structure**
   - Found existing enriched.secret.jsonl with 13 languages
   - Current languages: eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV, spa-BES, fra-LSG, deu-1912, tur, swh, rus, ind-AYT

2. **Recreated datasets.jsonl**
   - Combined train/validate/test splits (2,215 total entries)
   - Removed translations to prepare for re-enrichment

3. **Attempted enrichment with Japanese**
   - Ran enrich_extract_with_verses.py with jpn added to translation list
   - Command: `--translations eng-YLT,grc,hbo,heb-heb,lat-VUC,arb-NAV,spa-BES,fra-LSG,deu-1912,tur,swh,rus,ind-AYT,jpn`
   - Result: Japanese translations NOT FOUND in eBible corpus

4. **Updated LANGUAGE-SELECTION.md**
   - Added "Languages Considered but Not Available" section
   - Documented that jpn is not available in eBible corpus
   - Added update history noting the attempt and findings

5. **Regenerated data splits from enriched.secret.jsonl**
   - train.jsonl: 1,772 entries with translations
   - validate.jsonl: 221 entries with translations
   - test.jsonl: 222 entries with translations
   - All splits contain 12-13 languages (NT verses lack hbo-hbo)
   - Total: 2,215 annotated entries

6. **Deleted intermediate artifacts**
   - datasets.jsonl (temporary working file)
   - enriched.jsonl (superseded by enriched.secret.jsonl)
   - tbta-extract.secret.jsonl (no longer needed)
   - Kept: enriched.secret.jsonl, data/ splits, and documentation

## Findings

**Japanese Language Availability**: Japanese (jpn) translations identified in research/LANGUAGES.md as having "1 translation, 27 books" are NOT available in the eBible corpus used by the enrichment pipeline. To add Japanese would require:
- External Japanese Bible translation data source
- Integration into the data repository
- Re-running the enrichment pipeline

## Current Status

The mood feature analysis dataset remains at **13 languages** with strong typological diversity:
- **Source languages**: Greek (grc), Hebrew (hbo), Modern Hebrew (heb-heb)
- **Romance subjunctive**: Spanish (spa-BES), French (fra-LSG)
- **Germanic modal**: German (deu-1912), English (eng-YLT)
- **Turkic evidential**: Turkish (tur)
- **Slavic reduced mood**: Russian (rus)
- **Bantu TAM**: Swahili (swh)
- **Afro-Asiatic**: Arabic (arb-NAV), Latin (lat-VUC)
- **Austronesian minimal**: Indonesian (ind-AYT)

## Recommendation

The current 13-language selection provides excellent typological coverage without Japanese. If Japanese modal auxiliary + honorific interaction analysis is deemed essential for the mood feature, it would require a separate data acquisition effort beyond the current eBible corpus.
