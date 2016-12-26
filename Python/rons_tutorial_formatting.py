#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_block_separator(header_message=""):
    if header_message.__len__() > 0:
        header_side_size = (50 - (header_message.__len__() + 2)) / 2
        header = "=" * header_side_size + " " + header_message + " " + "=" * header_side_size
    else:
        header = "=" * 50

    print (header)


def print_gap_between_blocks():
    print ("\n\n")


def start_block(header_message=""):
    print_gap_between_blocks()
    print_block_separator(header_message)


def end_block(add_extra_new_line=False):
    if add_extra_new_line:
        print
    print_block_separator()


