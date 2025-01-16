#!/usr/bin/env python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1234)

client_socket.connect(server_address)

try:
    message = b"Hello from client"
    client_socket.sendall(message)
    data = client_socket.recv(1024).decode()
    print(f"\[+] Message from the server {data}")


finally:
    client_socket.close()