#!/usr/bin/env python3

import re

pattern = re.compile('[0-9]{3}')

print(f"132 matches pattern = {pattern.match('123')}")
print(f"bla matches pattern = {pattern.match('bla')}")


pattern = re.compile(
    '(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})\.(0|[1-9][0-9]{0,2})')

match = pattern.match('127.0.0.1')
print(
    f"173.211.32.17 matches pattern with groups = {match.group(1)}, {match.group(2)}, {match.group(3)}, {match.group(4)}")

match = pattern.match('82.37.15.98')
print(
    f"82.37.15.98 matches pattern with groups = {match.group(1)}, {match.group(2)}, {match.group(3)}, {match.group(4)}")
