#!/usr/bin/python
# -*- coding: utf-8 -*-
# import math_stuff

num1 = 7 + 5
print ("7 + 5 = %d (%s)" % (num1, type(num1)))
num2 = 7 + 5.0
print ("7 + 5.0 = %5.7f (%s)" % (num2, type(num2)))

num3 = 7 - 5
print ("7 - 5 = %d (%s)" % (num3, type(num3)))
num4 = 7 - 5.0
print ("7 - 5.0 = %4.2f (%s)" % (num4, type(num4)))

num5 = 7 * 5
print ("7 * 5 = %d (%s)" % (num5, type(num5)))

num6 = 7 * 5.0
print ("7 * 5.0 = %9.3f (%s)" % (num6, type(num6)))

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
