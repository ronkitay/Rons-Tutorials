#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = 'Ron Kitay'

import gc

# Basic GC in Python is based on reference counters.
# Since Python 2.x the AGC (Automatic GC) that handles circular references


def foo():
    l = []
    l.append(l)
    print l

print ("Garbage collector collected {} objects".format(gc.collect()))
for i in range(10):
    foo()
print ("Garbage collector collected {} objects".format(gc.collect()))

print (gc.get_threshold())
