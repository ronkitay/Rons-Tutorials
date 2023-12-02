#!/usr/bin/env python3

import sys
import argparse


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--flag', dest="some_flag",
                        action='store_true', help='A flag to turn things on and off')
    parser.add_argument(dest="some_var", type=str,
                        help='The variable which is mandatory')

    arguments = parser.parse_args(args)


if __name__ == '__main__':
    main(sys.argv[1:])
