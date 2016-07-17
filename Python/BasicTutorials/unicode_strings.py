#!/usr/bin/python
# -*- coding: utf-8 -*-

print 'Hello\u0020world'
print u'Hello\u0020world'
print ur'Hello\t\u0020world'
print

long_unicode_string = u"""\
This is a very long UNICODE string with some unicode characters like:
* '\u0020'
* '\u0037'
* '\u0182'
* '\uFA19'
* '\uA0B7'
"""

print long_unicode_string

print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')
print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'iso-8859-1')

print '\xc3'
print u'\xc3'

# Chineese
print unicode('\xEA\xB5\xAC\xEC\x9D\x8C\xEC\xA7\x84\xEA\xB2\xBD', 'utf-8')
