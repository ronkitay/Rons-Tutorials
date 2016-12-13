#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *

import re

print_block_separator()


# is_greater_than_2 is the same as 'lambda val: val > 2'
def is_greater_than_2(val):
    return val > 2

some_values = [1, 2, 3, 4, 5]
print ("Values are = %s" % some_values)

filtered_results = filter(lambda val: val > 2, some_values)
print ("Filtered (with lambda) Values are = %s" % filtered_results)

filtered_results = filter(is_greater_than_2, some_values)
print ("Filtered (without lambda) Values are = %s" % filtered_results)

mapped_values = map(lambda val: "%d => %s" % (val, chr(val - 1 + ord('a'))), some_values)
print ("Mapped (with lambda) Values are = %s" % mapped_values)

values_plus_ten = [ val + 10 for val in some_values ]
print values_plus_ten

end_block()

start_block()

list_of_lists = [[1, 2, 3], [4, 5, 6, 7], [8]]

lists_of_middles = [l[len(l)/2] for l in list_of_lists]
print lists_of_middles

lists_of_middles = map(lambda sub_list: sub_list[len(sub_list)/2], list_of_lists)
print lists_of_middles

lists_of_middles = map(lambda sub_list1, sub_list2: (sub_list1[len(sub_list1)/2], sub_list2[len(sub_list2)/2]), list_of_lists, list_of_lists[::-1])
print lists_of_middles

print (map(lambda a, b: "%d_%s" % (a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['a', 'b', 'c', 'd']))

end_block()

start_block()

my_list = ["abc def", "kkk", "aa bb cc", "hi all", "bye"]
print (my_list)


# filtered_my_list = filter(lambda string: len(re.findall(r"(\s+)", string)) == 1, my_list)
filtered_my_list = filter(lambda string: re.split(r"\s+", string).__len__() == 2, my_list)
print (filtered_my_list)

reversed_my_list = map(lambda sentence: re.sub(r"(.+?)(\s+)(.+)", "\\3 \\1", str(sentence)), filtered_my_list)
print(reversed_my_list)

end_block()
