#!/usr/bin/python
# -*- coding: utf-8 -*-


some_values = [1, 4, 9, 16, 25]
print some_values[0]
print some_values[-2]
copy_of_values = some_values[:]
some_values[3] = 76
print some_values[-2:]
print some_values[3:-1]
print copy_of_values

print some_values + [36, 49]

some_values.append(1)
print some_values
some_values = some_values + [2, 3, 4]
print some_values

hello_world = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print "1 ==> %s" % hello_world
hello_world[4:5] = []
print "2 ==> %s" % hello_world
hello_world[5:6] = []
print "3 ==> %s" % hello_world
hello_world[-2:] = [' ', 'h', 'e', 'a', 'v', 'e', 'n', '?']
print "4 ==> %s" % hello_world
hello_world.reverse()
print "5 ==> %s" % hello_world

crazy = [[1, 'A', 3.12], [2, 'B', 7.89]]
print crazy
crazy[0] = [3, 'D', 8.56]
print crazy
print crazy[0]
print crazy[0][1]
crazy[0] = 'Hello'
print crazy
print crazy[0]
print crazy[0][1]
