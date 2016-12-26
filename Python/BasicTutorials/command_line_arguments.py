#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import io


def get_file_length(file_to_check):
    return get_file_length_with_os_stats(file_to_check)
    # return get_file_length_with_seek_and_tell(file_to_check)


def get_file_length_with_seek_and_tell(file_to_check):
    file_to_check.seek(0, io.SEEK_END)
    file_size = file_to_check.tell()
    file_to_check.seek(0, io.SEEK_SET)
    return file_size


def get_file_length_with_os_stats(file_to_check):
    return os.stat(file_to_check.name).st_size


def validate_is_file(file_name):
    if os.path.isdir(file_name):
        print ("Path {} is a directory, expected a file!".format(file_name))
        exit(2)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print ("Expected <source path> <targer path> but got {} arguments instead.".format(len(sys.argv) - 1))
        exit(1)

    print (sys.platform)

    source_file_name = sys.argv[1]
    target_file_name = sys.argv[2]

    validate_is_file(source_file_name)
    validate_is_file(target_file_name)

    with open(source_file_name, 'r') as source_file:
        source_file_size = get_file_length(source_file)
        with open(target_file_name, 'w') as target_file:
            current_index = source_file_size
            while current_index >= 0:
                source_file.seek(current_index)
                target_file.write(source_file.read(1))
                current_index -= 1

    with open(target_file_name, 'r') as target_file:
        print (target_file.read())