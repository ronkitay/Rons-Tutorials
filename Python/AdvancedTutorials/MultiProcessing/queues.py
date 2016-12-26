#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *
import multiprocessing as MP

start_block('communicating between processes')

num = 12


def calc(q):
    global num
    num += 1
    q.put(num)

if __name__ == '__main__':
    processes = []
    queue = MP.Queue()
    for i in range(3):
        p = MP.Process(target=calc, name="testProc #{}".format(i), args=(queue, ))
        processes.append(p)
        p.start()

    for i in range(400):
        num_from_proc = queue.get()
        print (num_from_proc)

    for p in processes:
        p.join()

end_block()
