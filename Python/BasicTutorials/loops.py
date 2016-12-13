#!/usr/bin/python
# -*- coding: utf-8 -*-

from rons_tutorial_formatting import *

print_block_separator()

x = 1
while x < 10:
    print x,
    x += 1

end_block(True)

start_block()

words = ['hello', 'world', 'have', 'a', 'nice', 'day']
for word in words:
    if word.isalpha() and word[0] == 'h':
        print word,
    elif len(word) == 1:
        print word.upper(),
    else:
        shortened_word = word[:-1]
        print shortened_word.title(),
end_block(True)

start_block()

for value_in_range in range(12, 98, 3):
    print value_in_range, ',',

end_block(True)

start_block()

the_range = range(1, 10)
for j in the_range:
    if j > 9:
        print j
        break
    else:
        print "The range `%s` does not contain anything greater than 9" % the_range


print
for j in range(0, 1000, 10):
    if j < 500:
        continue

    print j, ',',

end_block(True)