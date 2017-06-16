#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket


def talk_to_client(client_socket, soc):
    total_len = 0
    while True:
        text = client_socket.recv(32).strip()
        if text == 'end':
            break
        print ("Received:" + text)
        total_len += len(text)

    client_socket.send(str(total_len))
    client_socket.close()

# family = socket.AF_INET => IPv4
# type = socket.SOCK_STREAM => TCP (the only one supported for this type)
soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

soc.bind(('', 12345))  # Same as binding on 127.0.0.1
soc.listen(3)
while True:
    print ("waiting for a request... ")
    client_socket, client_address = soc.accept()
    talk_to_client(client_socket, soc)
