#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

connection = socket.create_connection('127.0.0.1')
connect = connection.connect(12345)

print(connect)
