#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom import minidom

document = minidom.parse("sample.xml")

all_elements = document.getElementsByTagName("element")

for element in all_elements:
    name = element.getAttribute('name')
    value = element.firstChild.nodeValue
    print ("%s = %s" % (name, value))
