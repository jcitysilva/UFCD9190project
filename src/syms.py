#!/usr/bin/env python3

"""
Project for UFCD 9190: Introduction to Programming Applied to Cybersecurity

(c) João Cidade Silva, 2024 | November 30 .v1

This script identifies and groups duplicate files in a directory based on 
various criteria: file content, name, extension, or regex pattern.
"""

import os
import re
import hashlib
import sys
from pprint import pprint
from docopt import docopt


def main():
    """
    Identifies duplicate files in a directory based on specified criteria.

    Usage:
        {script_name} [-c] [-n] [-e] [-r PATTERN] [DIR_PATH]

    Options:
        DIR_PATH                     Directory to scan [default: .]
        -c, --content                Group files by identical content
        -n, --name                   Group files by identical name
        -e, --extension              Group files by identical extension
        -r PATTERN, --regex=PATTERN  Group files matching a regex pattern
        -h, --help                   Show help
    """
    try:
        # Format the docstring dynamically to inject the script name
        args = docopt(main.__doc__.format(script_name=sys.argv[0]))

        # Ensure at least one option is provided
        if not (
            args["--content"]
            or args["--name"]
            or args["--extension"]
            or args["--regex"]
        ):
            print("\nError: No options provided.")
            print(main.__doc__.format(script_name=sys.argv[0]))
            return

        dir_path = args.get("DIR_PATH", ".")

        # Validate the directory path
        if not os.path.isdir(dir_path):
            print(f"\nError: '{dir_path}' is not a valid directory.")
            return

        # Handle each grouping option
        if args["--content"]:
            show_groups(
                group_files_generic(dir_path, key_func=hash_file), label="BY CONTENT"
            )

        if args["--name"]:
            show_groups(
                group_files_generic(dir_path, key_func=lambda name, _: name),
                label="BY NAME",
            )

        if args["--extension"]:
            show_groups(
                group_files_generic(dir_path, key_func=get_extension),
                label="BY EXTENSION",
            )

        if args["--regex"]:
            regex = args["--regex"]
            show_groups(
                group_files_generic(
                    dir_path,
                    key_func=lambda name, _: name if re.search(regex, name) else None,
                ),
                label=f"BY REGEX (Pattern: {regex})",
            )

    except Exception as e:
        # Catch unexpected errors and display a meaningful message
        print("\nAn error occurred:")
        print(e)
        print(main.__doc__.format(script_name=sys.argv[0]))


def show_groups(duplicates: dict, label: str):
    """
    Displays groups of duplicate files in a readable format.

    Args:
        duplicates (dict): Dictionary where keys are grouping criteria and values are lists of file paths.
        label (str): Label to display for the group type.
    """
    print(f"\n{'=' * 10} {label} {'=' * 10}\n")
    for key, paths in duplicates.items():
        if len(paths) > 1:
            print(f"{key} ({len(paths)} duplicates):")
            pprint(paths)
            print("-" * 50)  # Separator for clarity
    print("\n" + "=" * 50)


def group_files_generic(dir_path: str, key_func) -> dict:
    """
    Generic function to group files by a specific key.

    Args:
        dir_path (str): The directory to search.
        key_func (callable): A function that takes a filename and current directory as input and returns a key.

    Returns:
        dict: A dictionary where keys are the grouping criteria and values are lists of file paths.
    """
    groups = {}
    for curr_dir, _, filenames in os.walk(dir_path):
        for filename in filenames:
            key = key_func(filename, curr_dir)
            if key is not None:  # Skip files that do not match the criteria
                groups.setdefault(key, []).append(os.path.join(curr_dir, filename))
    return groups


def hash_file(filename: str, dir_path: str) -> str:
    """
    Computes the MD5 hash of a file.

    Args:
        filename (str): The name of the file.
        dir_path (str): The directory where the file is located.

    Returns:
        str: The MD5 hash of the file's contents.
    """
    file_path = os.path.join(dir_path, filename)
    try:
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):  # Read file in chunks of 4KB
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None


def get_extension(filename: str, _: str) -> str:
    """
    Extracts the file extension.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The file's extension.
    """
    return os.path.splitext(filename)[1]


if __name__ == "__main__":
    main()
