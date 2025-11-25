"""Tests for extract_feature.py tool."""

import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from extract_feature import (
    extract_field_from_clause,
    process_json_file,
    extract_feature,
    main
)


class TestExtractFieldFromClause:
    """Tests for extract_field_from_clause function."""

    def test_extract_basic_feature(self, sample_tbta_json):
        """Test basic feature extraction from TBTA JSON."""
        result = extract_field_from_clause(sample_tbta_json[0], "Number")

        assert len(result) > 0
        assert all('constituent' in r for r in result)
        assert all('value' in r for r in result)
        assert all('part' in r for r in result)

    def test_extract_number_feature(self, sample_tbta_json):
        """Test extracting Number feature specifically."""
        result = extract_field_from_clause(sample_tbta_json[0], "Number")

        # Should find Number annotations: "S" for God, "P" for heavens
        assert len(result) >= 2
        labels = [r['value'] for r in result]
        assert 'S' in labels
        assert 'P' in labels

    def test_extract_person_feature(self, sample_tbta_json):
        """Test extracting Person feature."""
        result = extract_field_from_clause(sample_tbta_json[0], "Person")

        assert len(result) >= 1
        assert all(r['value'] == '3' for r in result)

    def test_extract_tense_feature(self, sample_tbta_json):
        """Test extracting Tense feature."""
        result = extract_field_from_clause(sample_tbta_json[0], "Tense")

        assert len(result) >= 1
        assert 'Past' in [r['value'] for r in result]

    def test_extract_with_path(self, sample_tbta_json):
        """Test that hierarchical path is correctly built."""
        result = extract_field_from_clause(sample_tbta_json[0], "Number", path="Clause[0]")

        assert all('path' in r for r in result)
        # Paths should include the initial path
        assert any('Clause[0]' in r['path'] for r in result)

    def test_extract_excludes_unspecified(self, sample_tbta_json_with_unspecified):
        """Test that 'Unspecified' values are excluded."""
        result = extract_field_from_clause(
            sample_tbta_json_with_unspecified[0],
            "Number"
        )

        assert len(result) == 0

    def test_extract_nested_elements(self, sample_tbta_json):
        """Test extraction from nested Children elements."""
        result = extract_field_from_clause(sample_tbta_json[0], "Number")

        # Should extract from both parent and children
        constituents = [r['constituent'] for r in result]
        assert 'God' in constituents
        assert 'the heavens' in constituents

    def test_extract_nonexistent_feature(self, sample_tbta_json):
        """Test extracting a feature that doesn't exist."""
        result = extract_field_from_clause(sample_tbta_json[0], "NonExistentFeature")

        assert len(result) == 0

    def test_extract_empty_element(self):
        """Test extraction from empty element."""
        result = extract_field_from_clause({}, "Number")

        assert len(result) == 0

    def test_extract_preserves_all_fields(self, sample_tbta_json):
        """Test that all required fields are preserved."""
        result = extract_field_from_clause(sample_tbta_json[0], "Number")

        for item in result:
            assert 'constituent' in item
            assert 'value' in item
            assert 'part' in item
            assert 'path' in item
            assert isinstance(item['constituent'], str)
            assert isinstance(item['value'], str)


class TestProcessJsonFile:
    """Tests for process_json_file function."""

    def test_process_valid_file(self, sample_tbta_file):
        """Test processing a valid TBTA file."""
        result = process_json_file(sample_tbta_file, "Number", output_format='jsonl')

        assert len(result) > 0
        assert all('verse' in r for r in result)
        # Should be GEN.001.001
        assert all(r['verse'] == 'GEN.001.001' for r in result)

    def test_process_file_verse_reference(self, sample_tbta_file):
        """Test that verse reference is correctly parsed."""
        result = process_json_file(sample_tbta_file, "Number", output_format='jsonl')

        assert all(r['verse'] == 'GEN.001.001' for r in result)

    def test_process_file_invalid_json(self, malformed_json_file):
        """Test handling of malformed JSON."""
        result = process_json_file(malformed_json_file, "Number", output_format='jsonl')
        # Should return empty list on error
        assert result == []

    def test_process_file_invalid_filename(self, invalid_filename_file):
        """Test handling of invalid filename format."""
        result = process_json_file(invalid_filename_file, "Number", output_format='jsonl')
        # Should return empty list when filename can't be parsed
        assert result == []

    def test_process_file_nonexistent(self, tmp_data_dir):
        """Test handling of nonexistent file."""
        nonexistent = tmp_data_dir / "nonexistent.json"
        result = process_json_file(nonexistent, "Number", output_format='jsonl')
        # Should return empty list on error
        assert result == []

    def test_process_file_different_features(self, sample_tbta_file):
        """Test processing different features from same file."""
        number_result = process_json_file(sample_tbta_file, "Number", output_format='jsonl')
        person_result = process_json_file(sample_tbta_file, "Person", output_format='jsonl')

        assert len(number_result) > 0
        assert len(person_result) > 0
        # Different features should yield different results
        assert number_result != person_result


class TestMainFunction:
    """Tests for main CLI function."""

    def test_main_success(self, tmp_data_dir, sample_tbta_files, capsys):
        """Test successful execution of main function."""
        output_file = tmp_data_dir / "output.jsonl"

        with patch('sys.argv', [
            'extract_feature.py',
            '--source-dir', str(tmp_data_dir),
            '--field', 'Number',
            '--format', 'jsonl',
            '--output', str(output_file)
        ]):
            main()

        assert output_file.exists()

        # Verify output content
        with open(output_file, 'r') as f:
            lines = f.readlines()
            assert len(lines) > 0
            # Each line should be valid JSON
            for line in lines:
                data = json.loads(line)
                assert 'verse' in data
                assert 'label' in data

    def test_main_missing_required_args(self):
        """Test main function with missing required arguments."""
        with patch('sys.argv', ['extract_feature.py']):
            with pytest.raises(SystemExit):
                main()

    def test_main_invalid_source_dir(self, tmp_data_dir):
        """Test main function with invalid source directory."""
        output_file = tmp_data_dir / "output.jsonl"

        with patch('sys.argv', [
            'extract_feature.py',
            '--source-dir', str(tmp_data_dir / "nonexistent"),
            '--field', 'Number',
            '--format', 'jsonl',
            '--output', str(output_file)
        ]):
            with pytest.raises(SystemExit):
                main()

    def test_main_verbose_mode(self, tmp_data_dir, sample_tbta_files):
        """Test main function with verbose logging."""
        output_file = tmp_data_dir / "output.jsonl"

        with patch('sys.argv', [
            'extract_feature.py',
            '--source-dir', str(tmp_data_dir),
            '--field', 'Number',
            '--format', 'jsonl',
            '--output', str(output_file),
            '--verbose'
        ]):
            exit_code = main()

        assert exit_code is None  # main() doesn't return exit code

    def test_main_creates_output_directory(self, tmp_data_dir, sample_tbta_files):
        """Test that main creates output directory if it doesn't exist."""
        output_file = tmp_data_dir / "nested" / "dir" / "output.jsonl"

        with patch('sys.argv', [
            'extract_feature.py',
            '--source-dir', str(tmp_data_dir),
            '--field', 'Number',
            '--format', 'jsonl',
            '--output', str(output_file)
        ]):
            main()

        assert output_file.exists()
        assert output_file.parent.exists()


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_unicode_handling(self, tmp_data_dir):
        """Test handling of Unicode characters in constituents."""
        unicode_json = [{
            "Part": "Clause",
            "Constituent": "Θεός (God) 神",
            "Number": "S",
            "Children": []
        }]

        file_path = tmp_data_dir / "GEN-001-001.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(unicode_json, f, ensure_ascii=False)

        result = process_json_file(file_path, "Number", output_format='jsonl')
        assert len(result) == 1
        assert "Θεός" in result[0]['constituent']

    def test_deeply_nested_structure(self, tmp_data_dir):
        """Test extraction from deeply nested JSON structure."""
        deep_json = [{
            "Part": "Clause",
            "Constituent": "Level 1",
            "Number": "S",
            "Children": [{
                "Part": "Part2",
                "Constituent": "Level 2",
                "Number": "P",
                "Children": [{
                    "Part": "Part3",
                    "Constituent": "Level 3",
                    "Number": "D",
                    "Children": []
                }]
            }]
        }]

        file_path = tmp_data_dir / "GEN-001-001.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(deep_json, f)

        result = process_json_file(file_path, "Number", output_format='jsonl')
        assert len(result) == 3
        labels = [r['label'] for r in result]
        assert set(labels) == {'S', 'P', 'D'}

    def test_empty_children_array(self, tmp_data_dir):
        """Test handling of empty Children arrays."""
        json_data = [{
            "Part": "Clause",
            "Constituent": "Text",
            "Number": "S",
            "Children": []
        }]

        file_path = tmp_data_dir / "GEN-001-001.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)

        result = process_json_file(file_path, "Number", output_format='jsonl')
        assert len(result) == 1

    def test_missing_constituent_field(self, tmp_data_dir):
        """Test handling when Constituent field is missing."""
        json_data = [{
            "Part": "Clause",
            "Number": "S",
            "Children": []
        }]

        file_path = tmp_data_dir / "GEN-001-001.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)

        result = process_json_file(file_path, "Number", output_format='jsonl')
        assert len(result) == 1
        assert result[0]['constituent'] == ''

    def test_large_file_processing(self, tmp_data_dir):
        """Test processing file with many annotations."""
        # Create a large JSON structure
        large_json = []
        for i in range(100):
            large_json.append({
                "Part": f"Clause{i}",
                "Constituent": f"Text {i}",
                "Number": "S" if i % 2 == 0 else "P",
                "Children": []
            })

        file_path = tmp_data_dir / "GEN-001-001.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(large_json, f)

        result = process_json_file(file_path, "Number", output_format='jsonl')
        assert len(result) == 100
