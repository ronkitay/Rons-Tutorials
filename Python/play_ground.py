#!/usr/bin/python
# -*- coding: utf-8 -*-

not_a_list_yet = [1]

print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)

not_a_list_yet.append(2)

print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)