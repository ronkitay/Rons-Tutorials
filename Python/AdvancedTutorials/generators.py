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
    print(num)

end_block()

start_block()


def fibonacci_with_yield(index):
    a, b = 0, 1

    for i in range(0, index):
        print(f"before yield --> {i}")
        yield a
        print(f"after yield --> {i}")
        a, b = b, a+b


@timer
def run_fibonnaci_with_yield():
    ind = 1
    for num_with_yield in fibonacci_with_yield(10):
        print(f"{ind}: {num_with_yield}")
        ind += 1


run_fibonnaci_with_yield()

end_block()

print_block_separator()

start_block()

def complex_generator():
    some_iterable = [ 1 ,7 ,'a', 'kuku']

    yielded_values = []

    for element in some_iterable:
        try:
            value_to_yield = f"yield__{element}"
            yield value_to_yield
            yielded_values.append(value_to_yield)
        except Exception as e:
            print(f"Some errors occured!: {e}")
        finally:
            print(f"it Finally happened: {yielded_values}")

def consume_complex_generator():
    for consumed_value in complex_generator():
        print(consumed_value)


consume_complex_generator()

end_block()