#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_block_separator():
    print ("=" * 50)


def print_gap_between_blocks():
    print ("\n\n")


def start_block():
    print_gap_between_blocks()
    print_block_separator()


def end_block(add_extra_new_line=False):
    if add_extra_new_line:
        print
    print_block_separator()


