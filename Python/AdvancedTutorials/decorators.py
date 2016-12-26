#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from timer_decorator import timer
from rons_tutorial_formatting import *

print_block_separator()


def logger(old_function):

    def new_function(*args):
        print ("LOG: args = %s" % str(args))
        return old_function(*args)

    return new_function


def func1(s):
    return s.upper()


@logger
def func2(s):
    return s * 3\



@logger
def func3(x, y):
    return "Got coordinates: ({}, {})".format(x, y)


def foo1(function_handler):
    res = function_handler("hello")
    print (res)

foo1(func1)


def foo():
    def yaa():
        print ("Hello from hell!!!")
    yaa()


print (func1("ron"))

end_block()

func1 = logger(func1)

start_block()

print (func1("ron2"))

end_block()

start_block()

print (func2("duplicate this ! "))

end_block()

start_block()

print (func3(7, 12))

end_block()

start_block()


@timer
def slow_function(outer, inner):
    result = list()
    for i in range(1, outer):
        for j in range(1, inner):
            result.append("i,j = {},{}".format(i, j))
            # time.sleep(1)
    return result

my_result = slow_function(300, 400)

print (my_result.__len__())
print (timer(slow_function)(300, 400).__len__())
print (timer(timer(slow_function))(300, 400).__len__())
print (timer(timer(timer(slow_function)))(300, 400).__len__())
print (timer(timer(timer(timer(slow_function))))(300, 400).__len__())

end_block()

