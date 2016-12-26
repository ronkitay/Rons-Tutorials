#!/usr/bin/python
# -*- coding: utf-8 -*-
from timer_decorator import timer
from rons_tutorial_formatting import *


class MyRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cur = self.start - 1

    def __iter__(self):
        return self

    def next(self):  # __next__(self) in Python 3.x
        if self.cur >= self.end:
            raise StopIteration()
        self.cur += 1
        return self.cur

print_block_separator()

@timer
def run_filter(range):
    return filter(lambda x: x < 10, range)


print (run_filter(MyRange(1, 1000)))
print (run_filter(MyRange(1, 10000)))
print (run_filter(MyRange(1, 100000)))
print (run_filter(MyRange(1, 1000000)))
# print (run_filter(MyRange(1, 10000000)))  # <-- This will be ~5 sec
# print (run_filter(MyRange(1, 100000000)))  # <-- This will be ~50 sec

end_block()

start_block()


class MyRange2(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRange2Iterator(self.start, self.end)


class MyRange2Iterator(object):
    def __init__(self, start, end):
        self.cur = start - 1
        self.start = start
        self.end = end

    def next(self):  # __next__(self) in Python 3.x
        if self.cur >= self.end:
            raise StopIteration()
        self.cur += 1
        return self.cur


@timer
def run_filter2(range):
    return filter(lambda x: x < 10, range)


print (run_filter2(MyRange2(1, 1000)))
print (run_filter2(MyRange2(1, 10000)))
print (run_filter2(MyRange2(1, 100000)))
print (run_filter2(MyRange2(1, 1000000)))
# print (run_filter2(MyRange2(1, 10000000)))  # <-- This will be ~5 sec
# print (run_filter2(MyRange2(1, 100000000)))  # <-- This will be ~50 sec


end_block()

start_block()


class FibonnaciIterator(object):
    def __init__(self, index):
        self.current_index = 0
        self.target_index = index
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        self.current_index += 1
        if self.current_index >= self.target_index:
            raise StopIteration()
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


@timer
def run_fibonnaci_with_iterator():
    ind = 1
    for num in FibonnaciIterator(20):
        print "%d: %d" % (ind, num)
        ind += 1


run_fibonnaci_with_iterator()

end_block()
