#!/usr/bin/python
# -*- coding: utf-8 -*-

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



