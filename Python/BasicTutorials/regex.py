#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from rons_tutorial_formatting import *

print_block_separator()

match_object = re.search(r"^a.*a$", "a")
if match_object:
    print ("match")

print (re.search(r"^a.*a$", "aa") is not None)

match_object = re.search(r"(\d+).+?(\d+)", "I have 67 dollars and 92 cents!")  # Using .+? makes the .+ be non-greedy
print ("Found '%s' dollars in range [%d -> %d]" % (match_object.group(1), match_object.start(1), match_object.end(1)))
print ("Found '%s' cents in range [%d -> %d]" % (match_object.group(2), match_object.start(2), match_object.end(2)))


def check_if_string_starts_and_ends_with_same_character(some_string):
    match_result = re.search(r"^(.).*\1$", some_string)
    print ("%s starts and ends with the same character = %r" % (some_string, match_result is not None))

check_if_string_starts_and_ends_with_same_character("dsadsadkl;daskd;addd")
check_if_string_starts_and_ends_with_same_character("aa")
check_if_string_starts_and_ends_with_same_character("a")
check_if_string_starts_and_ends_with_same_character("dsadsadkl;daskd;adddz")

end_block()

start_block()


def check_if_num_is_string(some_string):
    match_result = re.search(r"^[-+]?\d+(\.\d+)?( E-?\d+)?$", some_string)
    is_valid_number = match_result is not None
    color_prefix = "\x1b[6;30;42m" if is_valid_number else "\x1b[6;30;41m"
    valid_describer = "a" if is_valid_number else "NOT a"
    print (color_prefix + "%s is %s valid number\x1b[0m" % (some_string, valid_describer))
    # if match_result:
    #     print "Number is %s" % match_result.group(0)

check_if_num_is_string("0")
check_if_num_is_string("1")
check_if_num_is_string("+5")
check_if_num_is_string("-17")
check_if_num_is_string("+98.012")
check_if_num_is_string("-123.456")
check_if_num_is_string("-123.456.1283")
check_if_num_is_string("98.25")
check_if_num_is_string("98.25 E12")
check_if_num_is_string("98.25 E-12")
check_if_num_is_string("98.25 E--12")
check_if_num_is_string("-9892033.2312325 E-12")
check_if_num_is_string("-9892033.2312325 E-")
check_if_num_is_string("-9892033. E2")
check_if_num_is_string("-.2312325 E-12")

end_block()

start_block()

print (re.sub(r"[acf]", "_", "abcdef"))
print (re.sub(r"[acf]", "_", "abcdef", 2))
print (re.sub(r"[acf]", "_", "ABCDEF", 2))
print (re.sub(r"[acf]", "_", "ABCDEF", 2, re.IGNORECASE))

print (re.sub(r"(\d+)", "\\1", "kjsdasds 484395 sdksald jad09430924932 fdFSDFSD $$%$SD 45435 3"))
print (re.sub(r"(\d+)", "\g<1>", "kjsdasds 484395 sdksald jad09430924932 fdFSDFSD $$%$SD 45435 3"))

print (re.split("[aehui]", "If we have some thing strange here I can live with it"))

finditer = re.finditer("(\d+)", "j;j;3j13l777;1j;j12;j312312;j;l3j;l4j1414134j;l4;l1;l421j;ljhjkgk3")
print ("Type of finditer is %s" % type(finditer))
# We can get the "next" from the iterator using 'finditer.next().group(1)' HOWEVER - we DO NOT do it!!!!

for num in finditer:
    print (num.group(1))

end_block()