#!/usr/bin/python
# -*- coding: utf-8 -*-

# class <class name> (<extended class>)
class Fraction(object):

    # Constructor: def __init__(self, param1, param2 ...)
    # 'self' is the common standard in Python - but any name can be used - it has to be the 1st parameter
    def __init__(self, mone, mechane):
        self.mone = mone
        self.mechane = mechane

    def result(self):
        return float(self.mone) / self.mechane

    # __str__ is the equivalent of 'toString'
    def __str__(self):
        return "%d/%d = %2.2f" % (self.mone, self.mechane, self.result())

    def __gt__(self, other):
        return self.result() > other.result()

    def __le__(self, other):
        return other.__gt__(self)

    def __add__(self, other):  # None mathematical addition operator
        if isinstance(other, Fraction):
            self.mone += other.mone
            self.mechane += other.mechane
        else:
            raise TypeError("2nd parameter has to be a Fraction (or derived), the provided type is {}".format(type(other)))

    # def __lt__(self, other):
    #     print "in lt"
    #     return self.result() < other.result()


f1 = Fraction(2, 3)  # <-- invokes the constructor
f2 = Fraction(4, 5)  # <-- invokes the constructor

print (f1)
print (str(f2))

print f1 > f2
print f1 < f2
print f1.__le__(f2)

f1.__add__(f2)
print (f1)

try:
    f1.__add__("abc")
except TypeError as te:
    print ("Got type error with message: [\x1b[6;30;41m{}\x1b[0m]".format(te.message))



