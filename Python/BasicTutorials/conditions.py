#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *

print_block_separator()

some_variable = True
if some_variable:
    print "some_variable is {0:b}".format(some_variable)
    print "some_variable is {0}".format(some_variable)

another_variable = 7
if another_variable:
    print "another_variable is {0:n}".format(another_variable)

last_variable = 0
if not last_variable:
    print "last_variable is {0}".format(last_variable)

if last_variable or not some_variable:  # Will be false
    print "If was true"
elif last_variable < 0 or some_variable:  # Will be true
    print "Something was true"
else:
    print "Done"

end_block()

start_block()

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print ("list_1 == list_2 => %r" % (list_1 == list_2))
print ("list_1 is list_2 => %r" % (list_1 is list_2))
print ("id(list_1) == id(list_2) => %r" % (id(list_1) == id(list_2)))

end_block()

start_block()

n1 = 10
n2 = 11

print ("n1 = %d, n2 = %d" % (n1, n2))
print ("n1 == n2 => %r" % (n1 == n2))
print ("n1 is n2 => %r" % (n1 is n2))

n2 -= 1

print ("n1 = %d, n2 = %d" % (n1, n2))
print ("n1 == n2 => %r" % (n1 == n2))
print ("n1 is n2 => %r" % (n1 is n2))

n1 -= 1

print ("n1 = %d, n2 = %d" % (n1, n2))
print ("n1 == n2 => %r" % (n1 == n2))
print ("n1 is n2 => %r" % (n1 is n2))

end_block()