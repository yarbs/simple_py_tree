#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
""" docstring """
import os


def print_dir_tree(filepath: str, file_type_prefix: bool = False) -> None:
    """ Print Directory Tree

    Prints directory tree to stdout for the supplied path and all subdirectories and files

    :param filepath: Filepath to your "root" directory for printing the directory tree
    :param file_type_prefix: prefix with 'f' for file and 'd' for directory
    :return: None, prints to stdout
    """

    def listdir(path: str) -> tuple:
        """ Creates directory listing

        :param path: current working directory path
        :return: directories, files, links for the current working directory
        """
        dirs, files, links = [], [], []
        for name in os.listdir(path):
            path_name = os.path.join(path, name)
            if os.path.isdir(path_name):
                dirs.append(name)
            elif os.path.isfile(path_name):
                files.append(name)
            elif os.path.islink(path_name):
                links.append(name)
        return dirs, files, links

    def walk(root, dirs, files, prefix: str = '', file_type: bool = False):
        """ Walk, Print all files in the working directory

        :param root: current working directory
        :param dirs: subdirectories under current working directory
        :param files: files under current working directory
        :param prefix: prefix to apply when printing directory elements
        :param file_type: boolean on whether to print file type ('f', 'd') as prefix
        :return: None, prints to stdout
        """
        if files:
            if file_type:
                file_prefix = prefix + ('   f--- ' if dirs else ' ') + ''
                dir_prefix, walk_prefix = prefix + '   [d]--- ', prefix + '     f---'

            else:
                file_prefix = prefix + ('   |--- ' if dirs else ' ') + ''
                dir_prefix, walk_prefix = prefix + '   [+]--- ', prefix + '     |---'

        for name in files:
            print(file_prefix + name)

        for name in dirs:
            print(dir_prefix + name.upper())
            path = os.path.join(root, name)

            dirs, files = listdir(path)[:2]
            walk(root=path, dirs=dirs, files=files, prefix=walk_prefix, file_type=file_type)

    filepath_ = os.path.abspath(filepath)
    fp_dirs, fp_files = listdir(filepath_)[:2]
    print(filepath_)

    walk(root=filepath_, dirs=fp_dirs, files=fp_files, file_type=file_type_prefix)


def main():
    fp = os.path.abspath(YOUR_FILE_PATH)
    print_dir_tree(filepath=your_filepath, file_type_prefix=False)


if __name__ == '__main__':
    main()
