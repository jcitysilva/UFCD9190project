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
        show_duplicates(search_duplicates_by_name(dir_path))
#:

def search_duplicates_by_name(dir_path) -> dict:
    duplicates = {}
    for curr_dir, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename not in duplicates:
                duplicates[filename] = []
            duplicates[filename].append(os.path.join(curr_dir, filename))
        return duplicates
#:

def show_duplicates(duplicates: dict):
    for filename, paths in duplicates.items():
        if len(paths) > 1:
            print(filename)
            for path in paths:
                print(f'   {path}')
            print()
#:

# res = {
#     'Lab.pdf': ['./Lab.pdf', './dir2/Lab.pdf'],
#     'FahrCelsius2.cs': ['./FahrCelsius2.cs', './dir2/FahrCelsius2'],
#     'Restaurante1.cpp': ['./Restaurante1.cpp', './dir1/subdir1/Restaurante1.cpp']
#     }

if __name__ == '__main__':
    main()