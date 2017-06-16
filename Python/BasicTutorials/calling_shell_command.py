#!/usr/bin/python

from rons_tutorial_formatting import *

import subprocess as SP

print_block_separator("SubProcess.call")

SP.call(["ls", "-lart", "/"], shell=False)

end_block()

start_block("SubProcess.check_output")

ls_la = SP.check_output(["ls", "-la"], shell=False)

print (ls_la)
end_block()
