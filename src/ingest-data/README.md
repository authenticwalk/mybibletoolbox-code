# Data Ingestion Scripts

This directory contains scripts for fetching and ingesting data from various Bible resources.

## Directory Structure

Each data source has its own subdirectory:

- `ebible/` - eBible corpus (1000+ translations)
- `strongs/` - Strong's Hebrew and Greek dictionaries
- `macula/` - Macula Hebrew and Greek source language datasets
- `source-languages/` - Combined source language data (uses Macula + Strong's)

## Usage

### eBible Corpus

Fetch translations from the eBible corpus (https://github.com/BibleNLP/ebible):

```bash
python3 -m src.ingest-data.ebible.ebible_fetcher
```

### Strong's Dictionaries

Fetch Strong's Hebrew and Greek dictionary data:

```bash
python3 src/ingest-data/strongs/strongs_fetcher.py
```

### Macula Datasets

Download and cache Macula Hebrew and Greek datasets:

```bash
python3 src/ingest-data/macula/macula_fetcher.py
```

### Source Languages

Fetch combined source language data for a specific verse:

```bash
python3 src/ingest-data/source-languages/source_languages_fetcher.py "JHN 3:16"
```

