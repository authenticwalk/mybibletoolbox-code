"""Tests for discover_languages.py tool."""

import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
import subprocess

from ..discover_languages import (
    quote_verse,
    parse_translation_id,
    extract_languages,
    main
)


class TestParseTranslationId:
    """Tests for parse_translation_id function."""

    def test_parse_simple_id(self):
        """Test parsing simple translation ID."""
        lang, version = parse_translation_id("eng-NIV")

        assert lang == "eng"
        assert version == "NIV"

    def test_parse_id_with_year(self):
        """Test parsing translation ID with year."""
        lang, version = parse_translation_id("spa-RV-1960")

        assert lang == "spa"
        assert version == "RV-1960"

    def test_parse_id_multiple_hyphens(self):
        """Test parsing ID with multiple hyphens."""
        lang, version = parse_translation_id("eng-New-International-Version")

        assert lang == "eng"
        assert version == "New-International-Version"

    def test_parse_malformed_id(self):
        """Test parsing malformed ID with no hyphen."""
        lang, version = parse_translation_id("malformed")

        # Should handle gracefully
        assert lang == "malformed"
        assert version == "malformed"

    def test_parse_lowercase_conversion(self):
        """Test that language code is converted to lowercase."""
        lang, version = parse_translation_id("ENG-NIV")

        assert lang == "eng"
        assert version == "NIV"

    def test_parse_three_letter_codes(self):
        """Test parsing standard ISO 639-3 codes."""
        test_cases = [
            ("eng-KJV", "eng", "KJV"),
            ("spa-RV", "spa", "RV"),
            ("fra-LSG", "fra", "LSG"),
            ("deu-LUT", "deu", "LUT")
        ]

        for trans_id, expected_lang, expected_version in test_cases:
            lang, version = parse_translation_id(trans_id)
            assert lang == expected_lang
            assert version == expected_version


class TestExtractLanguages:
    """Tests for extract_languages function."""

    def test_extract_single_language(self):
        """Test extracting single language from results."""
        nt_result = {"eng-NIV": "For God so loved..."}
        ot_result = {"eng-NIV": "In the beginning..."}

        languages = extract_languages(nt_result, ot_result)

        assert "eng" in languages
        assert languages["eng"]["testament"] == "both"
        assert languages["eng"]["translations"] == 1
        assert "NIV" in languages["eng"]["versions"]

    def test_extract_multiple_versions_same_language(self):
        """Test extracting multiple versions of same language."""
        nt_result = {
            "eng-NIV": "...",
            "eng-KJV": "...",
            "eng-ESV": "..."
        }
        ot_result = {
            "eng-NIV": "...",
            "eng-KJV": "..."
        }

        languages = extract_languages(nt_result, ot_result)

        assert languages["eng"]["translations"] == 3
        assert set(languages["eng"]["versions"]) == {"NIV", "KJV", "ESV"}

    def test_extract_nt_only_language(self):
        """Test language with NT translation only."""
        nt_result = {"mri-Maori": "..."}
        ot_result = {}

        languages = extract_languages(nt_result, ot_result)

        assert languages["mri"]["testament"] == "nt_only"

    def test_extract_ot_only_language(self):
        """Test language with OT translation only."""
        nt_result = {}
        ot_result = {"heb-WLC": "..."}

        languages = extract_languages(nt_result, ot_result)

        assert languages["heb"]["testament"] == "ot_only"

    def test_extract_multiple_languages(self, sample_translation_results):
        """Test extracting multiple languages."""
        languages = extract_languages(
            sample_translation_results,
            sample_translation_results
        )

        assert "eng" in languages
        assert "spa" in languages
        assert "fra" in languages

        # English has 2 versions
        assert languages["eng"]["translations"] == 2
        # Spanish has 2 versions
        assert languages["spa"]["translations"] == 2

    def test_extract_empty_results(self):
        """Test extraction from empty results."""
        languages = extract_languages({}, {})

        assert len(languages) == 0

    def test_extract_versions_sorted(self):
        """Test that versions are sorted alphabetically."""
        nt_result = {
            "eng-NIV": "...",
            "eng-ASV": "...",
            "eng-KJV": "..."
        }
        ot_result = {}

        languages = extract_languages(nt_result, ot_result)

        # Versions should be sorted
        assert languages["eng"]["versions"] == ["ASV", "KJV", "NIV"]

    def test_extract_deduplicates_versions(self):
        """Test that duplicate versions are deduplicated."""
        nt_result = {"eng-NIV": "..."}
        ot_result = {"eng-NIV": "..."}

        languages = extract_languages(nt_result, ot_result)

        # Should only count NIV once
        assert languages["eng"]["translations"] == 1
        assert languages["eng"]["versions"] == ["NIV"]


class TestQuoteVerse:
    """Tests for quote_verse function."""

    @patch('src.tools.discover_languages.fetch_verse')
    def test_quote_verse_success(self, mock_fetch):
        """Test successful verse quotation."""
        mock_fetch.return_value = {
            "eng-NIV": "For God so loved the world..."
        }

        result = quote_verse("JHN.003.016")

        assert "eng-NIV" in result
        assert "For God so loved" in result["eng-NIV"]
        mock_fetch.assert_called_once()

    @patch('src.tools.discover_languages.fetch_verse')
    def test_quote_verse_failure(self, mock_fetch):
        """Test handling of quote_verse failure."""
        from src.tools.fetch_verse import VerseFetchError
        mock_fetch.side_effect = VerseFetchError("Failed to fetch verse")

        with pytest.raises(RuntimeError, match="Failed to fetch verse"):
            quote_verse("INVALID.000.000")

    @patch('src.tools.discover_languages.fetch_verse')
    def test_quote_verse_invalid_json(self, mock_fetch):
        """Test handling of invalid response."""
        mock_fetch.return_value = None

        with pytest.raises(RuntimeError):
            quote_verse("JHN.003.016")

    @patch('src.tools.discover_languages.fetch_verse')
    def test_quote_verse_empty_result(self, mock_fetch):
        """Test handling of empty results."""
        mock_fetch.return_value = {}

        result = quote_verse("JHN.003.016")
        assert isinstance(result, dict)
        assert len(result) == 0


class TestMainFunction:
    """Tests for main CLI function."""

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_success(self, mock_quote, tmp_data_dir):
        """Test successful language discovery."""
        # Mock 1000+ languages to avoid warning
        nt_translations = {f"lang{i:03d}-V1": f"NT text {i}" for i in range(1, 1001)}
        ot_translations = {f"lang{i:03d}-V1": f"OT text {i}" for i in range(1, 1001)}

        mock_quote.side_effect = [nt_translations, ot_translations]

        output_file = tmp_data_dir / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', str(output_file)
        ]):
            main()

        assert output_file.exists()

        # Verify output format
        with open(output_file, 'r') as f:
            lines = f.readlines()
            assert len(lines) > 0

            # Each line should be valid JSON
            for line in lines:
                data = json.loads(line)
                assert 'lang' in data
                assert 'testament' in data
                assert 'translations' in data
                assert 'versions' in data

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_custom_verses(self, mock_quote, tmp_data_dir):
        """Test main with custom NT and OT verses."""
        # Mock 1000+ languages to avoid warning
        nt_translations = {f"lang{i:03d}-V1": f"NT text {i}" for i in range(1, 1001)}
        ot_translations = {f"lang{i:03d}-V1": f"OT text {i}" for i in range(1, 1001)}

        mock_quote.side_effect = [nt_translations, ot_translations]

        output_file = tmp_data_dir / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--nt-verse', 'ROM.003.023',
            '--ot-verse', 'PSA.023.001',
            '--output', str(output_file)
        ]):
            main()

        # Verify custom verses were used
        assert mock_quote.call_count == 2
        assert mock_quote.call_args_list[0][0][0] == 'ROM.003.023'
        assert mock_quote.call_args_list[1][0][0] == 'PSA.023.001'

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_missing_output_arg(self, mock_quote):
        """Test main with missing output argument."""
        with patch('sys.argv', ['discover_languages.py']):
            with pytest.raises(SystemExit):
                main()

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_creates_output_directory(self, mock_quote, tmp_data_dir):
        """Test that main creates output directory if needed."""
        # Mock 1000+ languages to avoid warning
        nt_translations = {f"lang{i:03d}-V1": f"NT text {i}" for i in range(1, 1001)}
        ot_translations = {f"lang{i:03d}-V1": f"OT text {i}" for i in range(1, 1001)}

        mock_quote.side_effect = [nt_translations, ot_translations]

        output_file = tmp_data_dir / "nested" / "dir" / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', str(output_file)
        ]):
            main()

        assert output_file.exists()
        assert output_file.parent.exists()

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_warning_on_low_count(self, mock_quote, tmp_data_dir, capsys):
        """Test warning when language count is unexpectedly low."""
        # Return very few languages
        mock_quote.side_effect = [
            {"eng-NIV": "NT"},
            {"eng-NIV": "OT"}
        ]

        output_file = tmp_data_dir / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', str(output_file)
        ]):
            with pytest.raises(SystemExit) as exc_info:
                main()

            # Should exit with code 1 due to warning
            assert exc_info.value.code == 1

        captured = capsys.readouterr()
        assert "WARNING" in captured.err

    @patch('src.tools.discover_languages.quote_verse')
    def test_main_keyboard_interrupt(self, mock_quote):
        """Test handling of keyboard interrupt."""
        mock_quote.side_effect = KeyboardInterrupt()

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', 'languages.jsonl'
        ]):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 130


class TestIntegration:
    """Integration tests for the full workflow."""

    @patch('src.tools.discover_languages.quote_verse')
    def test_full_workflow(self, mock_quote, tmp_data_dir):
        """Test complete language discovery workflow."""
        # Mock realistic data with 1000+ languages
        nt_translations = {f"lang{i:03d}-V1": f"NT text {i}" for i in range(1, 1001)}
        ot_translations = {f"lang{i:03d}-V1": f"OT text {i}" for i in range(1, 901)}

        mock_quote.side_effect = [nt_translations, ot_translations]

        output_file = tmp_data_dir / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', str(output_file)
        ]):
            main()

        # Verify output
        with open(output_file, 'r') as f:
            languages = [json.loads(line) for line in f]

        # Should have 1000 languages
        assert len(languages) == 1000

        # Check some have both testaments
        both_count = sum(1 for lang in languages if lang['testament'] == 'both')
        assert both_count == 900  # Languages 1-900 have both

        # Check some are NT only
        nt_only_count = sum(1 for lang in languages if lang['testament'] == 'nt_only')
        assert nt_only_count == 100  # Languages 901-1000 are NT only

    @patch('src.tools.discover_languages.quote_verse')
    def test_error_recovery(self, mock_quote, tmp_data_dir):
        """Test error handling and recovery."""
        mock_quote.side_effect = RuntimeError("Network error")

        output_file = tmp_data_dir / "languages.jsonl"

        with patch('sys.argv', [
            'discover_languages.py',
            '--output', str(output_file)
        ]):
            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1
