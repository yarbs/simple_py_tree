#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" docstring """
import os


def print_dir_tree(filepath, indent='', step: int = 0):
    if step == 0:
        prefix = f"{indent}|--"
    else:
        prefix = f"|{indent}|--"

    d_file = str(os.path.basename(filepath)).upper()
    print(f"{prefix} {d_file}/")

    indent += '\t'

    with os.scandir(filepath) as entries:
        for entry in entries:
            if entry.is_dir():
                print_dir_tree(entry.path, indent, step+1)
            else:
                print(f"|{indent}|-- {entry.name}")


def main():
    filepath = "/usr/name/your/directory"
    your_filepath = os.path.abspath(filepath)

    print_dir_tree(your_filepath)


if __name__ == '__main__':
    main()
