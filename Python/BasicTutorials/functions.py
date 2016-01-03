#!/usr/bin/python
# -*- coding: utf-8 -*-


def function_without_arguments():
    print "In functionWithoutArguments - showing: שלום עולם"

function_without_arguments()
function_without_arguments()
function_without_arguments()
function_without_arguments()


def function_with_1_argument(someString):
    print "In function_with_1_argument({0})".format(someString)

function_with_1_argument("aaaa")
function_with_1_argument(7)
function_with_1_argument(12.566452311)