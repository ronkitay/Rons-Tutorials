#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
from sets import Set

from rons_tutorial_formatting import *
import multiprocessing as MP

start_block('"Distributed" word count')


def count_words(file_name, words, queue):
    print ("Searching for words in {}".format(file_name))

    matched_words = {}

    with open(file_name) as file:
        for line in file:
            for word in re.split(' ', line):
                word = word.strip()
                if word in words:
                    count = 1
                    if word in matched_words:
                        count = matched_words[word] + 1

                    matched_words[word] = count

    queue.put((file_name, matched_words))

if __name__ == '__main__':
    word_file_name = sys.argv[1]
    path_to_search_in = sys.argv[2]

    words = Set()
    with open(word_file_name) as word_file:
        for line in word_file:
            for word in re.split('\b+', line):
                words.add(word.strip())

    print ("Words in words file are: {}".format(words))
    processes = []
    queue = MP.Queue()

    for file_to_search_in in os.listdir(path_to_search_in):

        full_file_path = path_to_search_in + file_to_search_in
        with open(full_file_path) as temp:
            print ("{} = {}".format(file_to_search_in, temp.read()))

        p = MP.Process(target=count_words, name="testProc {}".format(file_to_search_in), args=(full_file_path, words, queue))
        processes.append(p)
        p.start()

    total_sum = 0

    for p in processes:
        p.join()

    while not queue.empty():
        (file_name, words_in_file) = queue.get()
        print "File {} has words {}".format(file_name, words_in_file)

end_block()
