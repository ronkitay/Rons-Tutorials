#!/usr/bin/python
# -*- coding: utf-8 -*-

string1 = 'hello'
string2 = "world"
string3 = str(12)

sentence = "%s %s %s" % (string1, string2, string3)

print sentence.lower()
print sentence.upper()
print sentence.title()
print len(sentence)
print sentence[0] + sentence[1] + sentence[2] + sentence[3] + " --> " + sentence[-8] + sentence[-6] + sentence[-5] + \
      sentence[-4] + sentence[-3]
print

string4 = 'This is a string containing a " in its data'
string5 = "This is a string containing a ' in its data"
string6 = "This is a string containing a \" in its data"
string7 = 'This is a string containing a \' in its data'

print string4
print string5
print string6
print string7

print

string8 = "This is a multiline " \
          "string which is spread accross" \
          "at least 3 lines, while still containing a single" \
          "line of actual text"
print string8

string9 = "This is a multiline\n" \
          "\tstring that is spread over at least\n" \
          "\t\t3 lines while actually containing a new line\n" \
          "\t\t\tvalue"
print string9

string10 = """\
This is another
example of a multiline string
this time without messing with the \\n character
"""
print string10


def show_string_characteristics(the_string):
    print "'%s'.islower() is %s" % (the_string, the_string.islower())
    print "'%s'.istitle() is %s" % (the_string, the_string.istitle())
    print "'%s'.isupper() is %s" % (the_string, the_string.isupper())
    print "'%s'.isalnum() is %s" % (the_string, the_string.isalnum())
    print "'%s'.isalpha() is %s" % (the_string, the_string.isalpha())
    print "'%s'.isdigit() is %s" % (the_string, the_string.isdigit())
    print "'%s'.isspace() is %s" % (the_string, the_string.isspace())
    print "'%s'.islower() is %s" % (the_string, the_string.islower())
    print


show_string_characteristics("Hello World")
show_string_characteristics("Hello world")
show_string_characteristics("hello world")
show_string_characteristics("HELLO WORLD")
show_string_characteristics("TextWithNumbers153523")
show_string_characteristics("TextWithoutNumbers")
show_string_characteristics("   \t   \t   \t\t\t")

string11 = r"This is a raw string, no need to escape things like \n, \t and illegal stuff like \o,\k and others"
print string11

print
print "Say " + "uncle " * 10 + " 10 times"

print
print "this " "is " "strange"

print
string12 = ('hello'
            ' '
            'world')
print string12
print

string13 = "Very long text"
print "A part of '%s' is '%s'" % (string13, string13[5:9])
print "A part of '%s' is also '%s'" % (string13, string13[5:-2])
print "A part of '%s' is also '%s'" % (string13, string13[-4:])
print "A part of '%s' is also '%s'" % (string13, string13[5:])
print "A part of '%s' is also '%s'" % (string13, string13[5:77]) # Does not produce an out-of-bounds error (forgiving API)
# print string13[56] # Uncomment to see it produces an error
print
