#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv


not_a_list_yet = [1]

print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)

not_a_list_yet.append(2)

print "not_a_list_yet is of type {0}, Its content is {1}".format(not_a_list_yet.__class__, not_a_list_yet)


f = open('/tmp/ron.csv','w')
csv_header_writer = csv.DictWriter(f, ['time', 'ip', 'url'], "")
csv_header_writer.writeheader()

d = dict()
d["time"] = 'aaa'
d["ip"] = 'bbb'
d["url"] = 'ccc'

csv_header_writer.writerow(d)



csv_writer = csv.writer(f)
csv_writer.writerow(['hello', 'world', 'this is\na strange thing'])

f.close()