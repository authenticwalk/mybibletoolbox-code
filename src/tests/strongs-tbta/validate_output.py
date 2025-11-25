#!/usr/bin/env python3
"""
Strong's TBTA Output Validation Script
========================================

Validates output YAML files from the Strong's-TBTA integration script.

Usage:
    python validate_output.py --data-dir .data/strongs
    python validate_output.py --file .data/strongs/G2316/G2316-tbta.yaml
    python validate_output.py --data-dir .data/strongs --verbose
"""

import argparse
import sys
from pathlib import Path
import yaml
import re
from collections import Counter


class ValidationError(Exception):
    """Validation error exception."""
    pass


class OutputValidator:
    """Validator for Strong's TBTA output files."""

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.errors = []
        self.warnings = []
        self.stats = Counter()

    def log(self, message, level="INFO"):
        """Log message if verbose."""
        if self.verbose or level == "ERROR":
            print(f"[{level}] {message}")

    def validate_file_path(self, file_path):
        """
        Validate file path follows STANDARDIZATION.md:
        .data/strongs/(G|H){number:04d}/(G|H){number:04d}-tbta.yaml
        """
        file_path = Path(file_path)

        # Check file exists
        if not file_path.exists():
            raise ValidationError(f"File does not exist: {file_path}")

        # Check extension
        if file_path.suffix != ".yaml":
            self.errors.append(f"Invalid file extension: {file_path.suffix} (expected .yaml)")

        # Check filename pattern
        filename_pattern = r'^([GH]\d{4})-tbta\.yaml$'
        if not re.match(filename_pattern, file_path.name):
            self.errors.append(f"Invalid filename format: {file_path.name}")
            return

        # Extract Strong's number from filename
        strongs_num = file_path.stem.split('-')[0]

        # Check directory name matches
        if file_path.parent.name != strongs_num:
            self.errors.append(
                f"Directory name '{file_path.parent.name}' doesn't match "
                f"filename '{strongs_num}'"
            )

        # Check Strong's number format
        if not re.match(r'^[GH]\d{4}$', strongs_num):
            self.errors.append(f"Invalid Strong's number format: {strongs_num}")

        self.log(f"✓ File path valid: {file_path}", "INFO")

    def validate_yaml_structure(self, file_path):
        """Validate YAML structure and required fields."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            self.errors.append(f"YAML parsing error: {e}")
            return None

        # Check top-level structure
        if not isinstance(data, dict):
            self.errors.append("Root element must be a dictionary")
            return None

        if "nodes" not in data:
            self.errors.append("Missing required 'nodes' field")
            return None

        if not isinstance(data["nodes"], list):
            self.errors.append("'nodes' must be a list")
            return None

        if len(data["nodes"]) == 0:
            self.warnings.append("Empty nodes list")

        self.log(f"✓ YAML structure valid: {len(data['nodes'])} nodes", "INFO")
        return data

    def validate_node(self, node, node_index):
        """Validate individual node structure."""
        required_fields = [
            "Constituent",
            "LexicalSense",
            "Part",
            "SemanticComplexityLevel",
            "Adjective Degree",
            "Aspect",
            "Mood",
            "Polarity",
            "Time",
            "Verses"
        ]

        # Check all required fields present
        for field in required_fields:
            if field not in node:
                self.errors.append(
                    f"Node {node_index}: Missing required field '{field}'"
                )

        # Validate Verses field
        if "Verses" in node:
            if not isinstance(node["Verses"], list):
                self.errors.append(f"Node {node_index}: 'Verses' must be a list")
            elif len(node["Verses"]) == 0:
                self.warnings.append(f"Node {node_index}: Empty Verses list")
            elif len(node["Verses"]) > 100:
                self.errors.append(
                    f"Node {node_index}: Verses list exceeds 100 limit "
                    f"({len(node['Verses'])} verses)"
                )
            else:
                # Validate each verse reference
                for verse_ref in node["Verses"]:
                    if not self.validate_verse_reference(verse_ref):
                        self.errors.append(
                            f"Node {node_index}: Invalid verse reference '{verse_ref}'"
                        )

                self.stats["total_verse_refs"] += len(node["Verses"])

        # Check for invalid attribute values
        invalid_values = ["Not Applicable", ".", "null", ""]
        for field in required_fields:
            if field in node and node[field] in invalid_values:
                self.warnings.append(
                    f"Node {node_index}: Field '{field}' has placeholder value '{node[field]}'"
                )

    def validate_verse_reference(self, ref):
        """
        Validate verse reference format: BOOK-CCC-VVV
        Examples: GEN-001-001, MAT-005-003
        """
        pattern = r'^[A-Z0-9]{3}-\d{3}-\d{3}$'
        return bool(re.match(pattern, ref))

    def validate_file(self, file_path):
        """Validate a single output file."""
        self.log(f"\nValidating: {file_path}", "INFO")
        self.errors = []
        self.warnings = []

        # Validate file path
        self.validate_file_path(file_path)

        # Validate YAML structure
        data = self.validate_yaml_structure(file_path)
        if data is None:
            return False

        # Validate each node
        for i, node in enumerate(data["nodes"]):
            self.validate_node(node, i)

        # Report results
        if self.errors:
            self.log(f"✗ Validation FAILED with {len(self.errors)} errors", "ERROR")
            for error in self.errors:
                self.log(f"  ERROR: {error}", "ERROR")

        if self.warnings:
            self.log(f"⚠ {len(self.warnings)} warnings", "WARN")
            if self.verbose:
                for warning in self.warnings:
                    self.log(f"  WARNING: {warning}", "WARN")

        if not self.errors:
            self.log(f"✓ Validation PASSED", "INFO")
            return True

        return False

    def validate_directory(self, data_dir):
        """Validate all YAML files in directory."""
        data_dir = Path(data_dir)

        if not data_dir.exists():
            self.log(f"Directory does not exist: {data_dir}", "ERROR")
            return False

        # Find all YAML files
        yaml_files = list(data_dir.glob("*/*-tbta.yaml"))

        if not yaml_files:
            self.log(f"No YAML files found in {data_dir}", "WARN")
            return True

        self.log(f"Found {len(yaml_files)} files to validate", "INFO")

        # Validate each file
        passed = 0
        failed = 0

        for yaml_file in yaml_files:
            if self.validate_file(yaml_file):
                passed += 1
            else:
                failed += 1

        # Summary
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Total files: {len(yaml_files)}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Total verse references: {self.stats['total_verse_refs']}")
        print("=" * 60)

        return failed == 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate Strong's TBTA output files",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--data-dir",
        type=Path,
        help="Directory containing Strong's YAML files"
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Validate single file"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    if not args.data_dir and not args.file:
        parser.error("Must specify either --data-dir or --file")

    validator = OutputValidator(verbose=args.verbose)

    if args.file:
        success = validator.validate_file(args.file)
    else:
        success = validator.validate_directory(args.data_dir)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
