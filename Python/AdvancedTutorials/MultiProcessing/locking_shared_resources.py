#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *
import multiprocessing as MP

start_block('example for invoking a function in a separate process')


def print_loop(num, lock):
    for i in range(num):
        lock.acquire()
        print ("{}: {}".format(MP.current_process().name, i))
        lock.release()

if __name__ == '__main__':
    processes = []
    l = MP.Lock()
    for i in range(3):
        p = MP.Process(target=print_loop, name="testProc #{}".format(i), args=(400, l))
        processes.append(p)
        p.start()

    # print ("done in process {}".format(MP.current_process().name))

    for i in range(400):
        l.acquire()

        # It is recommended to do the "shared resource" action in a try block and release the lock in 'finally'
        try:
            print ("{}: {}".format(MP.current_process().name, i))
        finally:
            l.release()

    for p in processes:
        p.join()

end_block()
