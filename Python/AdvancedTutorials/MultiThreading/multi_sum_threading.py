#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from Queue import Queue

# from rons_tutorial_formatting import *
import threading as TH

# start_block('Multi sum')


def range_sum(start, end, queue):
    print ("start => {} end => {}".format(start, end))
    sum_of_range = 0
    for n in range(start, end+1):
        sum_of_range += n

    print ("sum_of_range = {}".format(sum_of_range))
    queue.put(sum_of_range)

if __name__ == '__main__':
    max_mum = int(sys.argv[1])
    count = int(sys.argv[2])

    threads = []
    queue = Queue()

    start_value = 0
    delta = max_mum // count
    for i in range(count):
        end = min(start_value + delta + 1, max_mum)
        t = TH.Thread(target=range_sum, name="testThread #{}".format(i), args=(start_value, end, queue))
        start_value = end + 1
        end += delta
        threads.append(t)
        t.start()

    total_sum = 0

    for i in range(count):
        total_sum += queue.get()

    print (total_sum)

    for t in threads:
        t.join()

# end_block()
