#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
print now

print now.year
print now.month
print now.day

print '%04d-%02d-%02d' % (now.year, now.month, now.day)
print '%02d/%02d/%04d' % (now.day, now.month, now.year)
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.day, now.month, now.year, now.hour, now.minute, now.second)
