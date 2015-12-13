#!/usr/bin/python

intVariable = 10
print "intVariable = {0:10d}".format(intVariable)

floatVariable = 3.145791267
print "floatVariable = {0:10f}".format(floatVariable)

stringVariable = "I have all the time in the world ..."
print "stringVariable = {0:10s}".format(stringVariable)

booleanVariable = True
print "booleanVariable = {0}".format(booleanVariable)

from datetime import datetime
dateVariable = datetime.today()
# https://docs.python.org/2/library/datetime.html
print "dateVariable = {0}".format(dateVariable.strftime("%d-%m-%Y %H:%M:%S"))