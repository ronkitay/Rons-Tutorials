#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *
import AdvancedTutorials.MultiProcessing as MP

start_block('example for invoking a function in a separate process')

def foo(s):
    print ("in proc with '{}' from process {}".format(s, MP.current_process().name))

if __name__ == '__main__':
    p = MP.Process(target=foo, name="testProc", args=("ls /la",))
    p.start()

    p.join()

    print ("done in process {}".format(MP.current_process().name))

end_block()
