#!/usr/bin/python
# -*- coding: utf-8 -*-


class MyError(BaseException):

    def __init__(self, message):
        super(MyError, self).__init__(message)

try:
    input_string = raw_input("Type a number and see what happens: ")
    num = int(input_string)

    if num > 10:
        raise MyError("bla")
    else:
        raise Exception("blo!")
except MyError as my_error:
    print ("Got exception of type {} with message [{}]".format(type(my_error), my_error))
except (Exception, ValueError) as exception:
    print ("Got exception of type {} with message [{}]".format(type(exception), exception))
finally:
    print ("Done!")



