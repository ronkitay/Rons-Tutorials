#!/usr/bin/python
# -*- coding: utf-8 -*-

name = raw_input("What is your name?")
todo = raw_input("What would you like to do?")

print "Hello {}, I'm happy to {} you.".format(name, todo) # Only from 2.7
print "Hello {0}, I'm happy to {1} you. Please come again {0}!".format(name, todo)
print "Hello %s, I'm happy to %s you." % (name, todo)