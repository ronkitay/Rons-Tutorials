#!/usr/bin/python
# -*- coding: utf-8 -*-
import io

from rons_tutorial_formatting import *


# Writing the data


with open('/tmp/temp_file_1', 'w') as some_file:  # Rewrites the file if exists
    some_file.write('1st line\n')
    some_file.writelines(['2nd line\n', '3rd line\n'])

with open('/tmp/temp_file_1', 'a') as some_file:  # Append to the file
    some_file.write('4th line\n')


# Read the data

print_block_separator('readLines')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    print (some_file.readlines())

end_block()
start_block('read - all')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    print (some_file.read())

end_block()
start_block('read - 10 first bytes')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    print (some_file.read(10))

end_block()
start_block('read - skip 23 bytes and get the "tail"')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    some_file.read(23)
    print (some_file.read())

end_block()

start_block('readline')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    line = some_file.readline()

    while line:
        print (line.strip('\n'))
        line = some_file.readline()

end_block()

start_block('file as iterator')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start

    try:
        some_object_iterator = iter(some_file)
        print some_file, 'is iterable'
    except TypeError, te:
        print some_file, 'is not iterable'

    for line in some_file:
        print (line.strip('\n'))

end_block()

start_block('Open file with w+ and re-write a line')

with open('/tmp/temp_file_2', 'w+') as some_file:  # Rewrites the file if exists
    some_file.write('1st line\n')
    some_file.writelines(['2nd line\n', '3rd line\n'])
    some_file.seek(9, io.SEEK_SET)  # Move 9 bytes from the start
    some_file.write('4th line\n')
    some_file.seek(0, io.SEEK_SET)  # Go to start
    print (some_file.read())

end_block()

start_block('Open file with w+ and re-write a line')

with open('/tmp/temp_file_3', 'w+') as some_file:  # Rewrites the file if exists and allows reading as well
    some_file.write('1st line\n')
    some_file.writelines(['2nd line\n', '3rd line\n'])
    some_file.seek(-9, io.SEEK_END)  # Move 9 bytes from the start <-- Works on xNix systems, seems to not work on windows
    some_file.write('4th line\n')
    some_file.seek(0, io.SEEK_SET)  # Go to start
    print (some_file.read())

end_block()

start_block('read + tell')

with open('/tmp/temp_file_1', 'r') as some_file:  # Read from the start
    while some_file.read(1):
        print (some_file.tell())

end_block()

#
# start_block('read + write with different objects')
#
# with open('/tmp/temp_file_3', 'r') as file_for_read:
#     file_for_read.read(7)
#
#     with open('/tmp/temp_file_3', 'w') as file_for_write:
#         file_for_write.write('abc')
#
#     file_for_read.seek(0, io.SEEK_SET)
#     print (file_for_read.read())
#
# end_block()

