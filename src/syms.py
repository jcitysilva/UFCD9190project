#!/usr/bin/env python3

"""
Project for UFCD 9190: Introduction to programming applied to cybersecurity

(c) João Cidade Silva, 2024
"""

import os
import pprint

from docopt import docopt

def main ():
    doc = """
Returns all duplicated files in the given folder.

Usage:
    syms.py [-c] [-n] [-e] [-r PATTERN] [DIR_PATH]

Options:
    DIR_PATH         Start directory [default: .]
    -c, --content      Search files with the same binary content
    -n, --name      Search files using the same name
    -e, --extension
    -r PATTERN, --regex=PATTERN
"""

    args = docopt(doc)
    dir_path = args.get('DIR_PATH', '.')

    if not dir_path:
        dir_path = '.'

    if args['--name']:
        print("BY NAME")
        show_groups(group_files_by_name(dir_path))
        print("_________________________________________________________________________")

    if args['--extension']:
        print("BY EXTENSION")
        show_groups(group_files_by_extension(dir_path))
        print("_________________________________________________________________________")
#:

def show_groups(duplicates: dict):
    for filename, paths in duplicates.items():
        if len(paths) > 1:
            print(filename)
            for path in paths:
                print(f'   {path}')
            print()
#:

def group_files_by_name(dir_path) -> dict:
    groups = {}
    for curr_dir, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename not in groups:
                groups[filename] = []
            groups[filename].append(os.path.join(curr_dir, filename))
        return groups
#:

def group_files_by_extension(dir_path) -> dict:
    groups = {}
    for curr_dir, _, filenames in os.walk(dir_path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext not in groups:
                groups[ext] = []
            groups[ext].append(os.path.join(curr_dir, filename))
        return groups
#:

if __name__ == '__main__':
    main()