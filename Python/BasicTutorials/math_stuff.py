#!/usr/bin/python
# -*- coding: utf-8 -*-

# Option #1 - import module and use it
# import math

# print math.floor(295.3412312349)
# print math.sqrt(25)
# print math.pow(2, 8)

import time
from math import *
from cmath import pi

print floor(295.3412312349)
print sqrt(25)
print pow(2, 8)
print

print pi
print


def fibonacci_recursive(num):
    if num < 2:
        return 1

    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


start = time.time()
fibonacci_10 = fibonacci_recursive(30)
end = time.time()
print "fibonacci_recursive(10) took %f seconds, result is %d" % (end - start, fibonacci_10)

start = time.time()
fibonacci_24395 = fibonacci_iterative(24395)
end = time.time()
print "fibonacci_iterative(24395) took %f seconds, result is %d" % (end - start, fibonacci_24395)


