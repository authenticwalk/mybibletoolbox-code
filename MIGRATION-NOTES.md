# Ingestion Script Reorganization

## Summary of Changes

All data ingestion scripts have been reorganized into a consistent directory structure under `src/ingest-data/`.

## Files Moved

### 1. Strong's Fetcher
- **From:** `strongs-fetcher.py` (root)
- **To:** `src/ingest-data/strongs/strongs_fetcher.py`
- **Purpose:** Fetches Strong's Hebrew and Greek dictionary data with enhancements

### 2. eBible Fetcher
- **From:** `src/ingest-data/ebible_fetcher.py`
- **To:** `src/ingest-data/ebible/ebible_fetcher.py`
- **Purpose:** Fetches verses from the eBible corpus (1000+ translations)

### 3. Macula Fetcher
- **From:** `src/lib/macula/macula_fetcher.py`
- **To:** `src/ingest-data/macula/macula_fetcher.py`
- **Purpose:** Downloads and caches Macula Hebrew and Greek datasets

### 4. Source Languages Fetcher
- **From:** `src/lib/source_languages_fetcher.py`
- **To:** `src/ingest-data/source-languages/source_languages_fetcher.py`
- **Purpose:** Fetches combined source language data (Macula + Strong's)

## New Directory Structure

```
src/ingest-data/
├── __init__.py
├── README.md
├── ebible/
│   ├── __init__.py
│   └── ebible_fetcher.py
├── macula/
│   ├── __init__.py
│   └── macula_fetcher.py
├── source-languages/
│   ├── __init__.py
│   └── source_languages_fetcher.py
└── strongs/
    ├── __init__.py
    └── strongs_fetcher.py
```

## Processing Libraries (Unchanged)

These remain in `src/lib/` as they are library code used by other scripts:

- `src/lib/macula/macula_processor.py` - Processes Macula XML data
- `src/lib/tbta/tbta_processor.py` - Processes TBTA data

## Usage Examples

### Strong's Dictionary
```bash
python3 src/ingest-data/strongs/strongs_fetcher.py
```

### eBible Corpus
```bash
python3 src/ingest-data/ebible/ebible_fetcher.py
```

### Macula Datasets
```bash
python3 src/ingest-data/macula/macula_fetcher.py
```

### Source Languages
```bash
python3 src/ingest-data/source-languages/source_languages_fetcher.py "JHN 3:16"
```

## Import Path Updates

All import paths in the moved files have been updated to work correctly from their new locations. The scripts support both:
- Direct execution: `python3 src/ingest-data/ebible/ebible_fetcher.py`
- Module import: `from src.ingest_data.ebible import ebible_fetcher`

## Documentation Updates

- `src/ingest-data/README.md` - Updated with new structure and usage examples
- `CLAUDE.md` - Updated git commit examples to reflect new paths

