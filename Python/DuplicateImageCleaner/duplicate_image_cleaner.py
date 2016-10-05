#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import Queue
from sets import Set
from threading import Thread

root_dir = '/Users/rkitay/Pictures/Sort_From_Home'


def walk(dir_to_walk, queue_to_add_files_to):
    extensions = Set(['jpg', 'jpeg', 'gif', 'png'])
    for root, _, files in os.walk(dir_to_walk):
        for current_file in files:
            file_parts = current_file.lower().split('.')
            extension = file_parts.__getitem__(file_parts.__len__()-1)
            if extension in extensions:
                file_path = os.path.join(root, current_file)
                queue_to_add_files_to.put(file_path)

queue = Queue.Queue()

walk(root_dir, queue)

def do_work(item):
    print "Working on file %s" % item
    pass


def worker():
    while True:
        item = queue.get()
        do_work(item)
        queue.task_done()

for i in range(10):
     t = Thread(target=worker)
     t.daemon = True
     t.start()


queue.join()       # block until all tasks are done


