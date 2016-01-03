#!/usr/bin/python
# -*- coding: utf-8 -*-
import math_stuff

print 7 + 5
print 7 + 5.0
print
print 7 - 5
print 7 - 5.0
print
print 7 * 5
print 7 * 5.0
print
print 7 / 5
print 7 / 5.0
print 7 // 5.0
print
print 7 % 5.0
print
print 7 ** 5
print pow(7,5)
print pow(8,1/3.0) # ∛8=2
print
print math_stuff.sqrt(9)
print math_stuff.sqrt(8)
print
print round(159392.2141851, 3)
print

ten_as_binary = 0b00001010
print ten_as_binary
print "+"
fifteen_as_octal = 0o0017
print fifteen_as_octal
print "+"
hundred_ninty_five_as_hex = 0xc3
print hundred_ninty_five_as_hex
print "="
print hundred_ninty_five_as_hex + ten_as_binary + fifteen_as_octal
