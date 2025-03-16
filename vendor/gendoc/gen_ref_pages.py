#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================================================
#
# API Documentation Generator for MkDocs
#
# This script automates the generation of API documentation by scanning Python source files
# and creating corresponding markdown documentation with proper structure and navigation
#
# @filename   gen_ref_pages.py
# @path       vendor\gendoc\gen_ref_pages.py
# @project    PROJECT_NAME
# @encoding   utf-8
#
# @product    PyCharm
# @author     USER
# @email      EMAIL
# @time       2025/03/16 21:58
#
# @version    git
# @record     CURRENT_USER_NAME Create file.
#             CURRENT_USER_NAME Update header comment.
#             CURRENT_USER_NAME description
#
# @license    http://www.opensource.org/licenses/mit-license.html  MIT License
#
# @copyright  Copyright (c) 2025. All rights reserved.
#
#             This software, including its code, documentation, and related materials,
#             is protected by copyright law and international treaties.
#             Unauthorized use, reproduction, or distribution of any part of this software is prohibited.
#
#             ContentForge is a trademark of ContentForge.org.
#             All other trademarks and registered trademarks are the property of their respective owners.
#
#             For permissions, please contact ContentForge.org@hotmail.com.
# =============================================================================================================
from __future__ import print_function, unicode_literals

# =============================================================================================================
# Standard Python Imports
# =============================================================================================================
from pathlib import Path

import mkdocs_gen_files


def ensure_directory(path: Path) -> None:
    """
    Ensure directory exists, create if not present

    Args:
        path: Path object representing the directory to check/create

    Returns:
        None
    """
    path.parent.mkdir(parents=True, exist_ok=True)


def is_valid_python_file(path: Path) -> bool:
    """
    Check if the file is a valid Python file for documentation

    Args:
        path: Path object representing the file to check

    Returns:
        bool: True if the file is valid for documentation, False otherwise

    Note:
        Valid files are:
        - Regular .py files not starting with . or _
        - __init__.py files
    """
    return (
        path.is_file()
        and path.suffix == '.py'
        and not path.name.startswith('.')
        and not path.name.startswith('_')
        or path.name == '__init__.py'
    )


def generate_api_docs():
    """
    Main function to generate API documentation

    This function:
    1. Initializes navigation structure
    2. Scans source directory for Python files
    3. Generates markdown documentation for each valid file
    4. Creates navigation summary

    Raises:
        Exception: If there are errors during documentation generation
    """
    # Initialize navigation object for MkDocs
    nav = mkdocs_gen_files.Nav()

    # Define source and documentation directories
    source_dir = Path("vendor/contentforge")
    docs_dir = Path("docs/reference")

    # Verify source directory exists
    if not source_dir.exists():
        print(f"Warning: Source directory {source_dir} does not exist!")
        return

    # Create documentation directory if needed
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Process all Python files
    try:
        for path in sorted(source_dir.rglob("*.py")):
            # Skip invalid Python files
            if not is_valid_python_file(path):
                continue

            try:
                # Generate module and documentation paths
                module_path = path.relative_to(source_dir).with_suffix("")
                doc_path = path.relative_to(source_dir).with_suffix(".md")
                full_doc_path = docs_dir / doc_path

                # Create navigation structure from path
                parts = tuple(module_path.parts)

                # Skip empty paths
                if not parts:
                    continue

                # Handle special cases
                if parts[-1] == "__init__":
                    # Convert __init__.py to index.md
                    parts = parts[:-1]
                    doc_path = doc_path.with_name("index.md")
                    full_doc_path = full_doc_path.with_name("index.md")
                elif parts[-1] == "__main__":
                    # Skip __main__.py files
                    continue

                # Skip if no valid parts remain
                if not parts:
                    continue

                # Add to navigation structure
                nav[parts] = doc_path.as_posix()

                # Create directory for documentation file
                ensure_directory(full_doc_path)

                # Generate documentation content
                with mkdocs_gen_files.open(full_doc_path, "w") as fd:
                    ident = ".".join(parts)
                    content = [
                        f"# {ident}",
                        "",
                        "## Overview",
                        "",
                        f"::: {ident}",
                        "    options:",
                        "        show_root_heading: true",
                        "        show_source: true",
                        "",
                    ]
                    fd.write("\n".join(content))

                # Set source file for editing
                mkdocs_gen_files.set_edit_path(full_doc_path, path)

            except Exception as e:
                print(f"Error processing file {path}: {str(e)}")
                continue

        # Generate navigation summary
        summary_path = docs_dir / "SUMMARY.md"
        with mkdocs_gen_files.open(summary_path, "w") as nav_file:
            nav_file.write("# API Reference\n\n")
            nav_file.writelines(nav.build_literate_nav())

    except Exception as e:
        print(f"Error generating documentation: {str(e)}")
        raise


# =============================================================================================================
# Script Execution
# =============================================================================================================
if __name__ == "__main__":
    generate_api_docs()
