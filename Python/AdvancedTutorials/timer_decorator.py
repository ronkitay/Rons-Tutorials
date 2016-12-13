#!/usr/bin/python
# -*- coding: utf-8 -*-
import time


def timer(function_to_measure):
    def measurer(*args):
        start = time.time()
        result = function_to_measure(*args)
        end = time.time()
        print ("Call to {} with arguments {} took {}".format(function_to_measure, str(args), (end - start)))
        return result

    return measurer
