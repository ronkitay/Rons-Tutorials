#!/usr/bin/python
# -*- coding: utf-8 -*-
from timer_decorator import timer
from rons_tutorial_formatting import *

print_block_separator()


# When using 'yield' python will automatically convert this function to an iterator class!
def func(start, end):
    cur = start
    while cur <= end:
        yield cur
        cur += 1

for num in func(1, 100):
    print num

end_block()

start_block()


def fibonacci_with_yield(index):
    a, b = 0, 1

    for i in xrange(0, index):
        yield a
        a, b = b, a+b


@timer
def run_fibonnaci_with_yield():
    ind = 1
    for num_with_yield in fibonacci_with_yield(2000):
        print "%d: %d" % (ind, num_with_yield)
        ind += 1


run_fibonnaci_with_yield()

end_block()
