#!/usr/bin/env python3

import socket

#create server socket (file descriptor)

#socket.AF_INET (define address family (such as IPV4))
#socket.SOCK_STREAM (TCP CONNECTION)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 1234)

#listening on port 1234
server_socket.bind(server_address)

#create a queue for the clients that attempt to connect to the server  
# (1 connection per)
server_socket.listen(1)

while True:
    
    #only accepts connection, you need the socket from the client so you can communicate with them on a random port

    #client_address: client ip and random port
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024) #bytes
    print(f"\n[+] Data recieved: {data.decode()}")
    print(f"Client information: {client_address}")

    client_socket.sendall(f"Hello there!\n".encode())
    client_socket.close()


    