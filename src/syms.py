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
    # print(args)

    dir_path = args ['DIR_PATH']
    if args['--name']:
        show_groups(group_files_by_name(dir_path))

    if args['--extension']:
        showgroups(group_files_by_ext(dir_path))
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
            ext = os.path.splitext(filename)
            if filename not in groups:
                groups[ex] = []
            groups[ext].append(os.path.join(curr_dir, filename))
        return groups
#:

if __name__ == '__main__':
    main()