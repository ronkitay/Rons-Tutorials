#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# from rons_tutorial_formatting import *
import multiprocessing as MP

# start_block('Multi sum')


def range_sum(start, end, queue):
    print ("start => {} end => {}".format(start, end))
    sum = 0
    for n in range(start, end+1):
        sum += n

    print ("sum = {}".format(sum))
    queue.put(sum)

if __name__ == '__main__':
    max_mum = int(sys.argv[1])
    count = int(sys.argv[2])

    processes = []
    queue = MP.Queue()

    start_value = 0
    delta = max_mum // count
    for i in range(count):
        end = min(start_value + delta + 1, max_mum)
        p = MP.Process(target=range_sum, name="testProc #{}".format(i), args=(start_value, end, queue))
        start_value = end + 1
        end += delta
        processes.append(p)
        p.start()

    total_sum = 0

    for i in range(count):
        total_sum += queue.get()

    print (total_sum)

    for p in processes:
        p.join()

# end_block()
