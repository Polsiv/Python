#!/usr/bin/env python3

import tkinter as tk
import socket
import threading
import ssl

def client_thread(client_socket, clients, usernames):
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username
    
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] {username} has entered the chat!\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            if message == "!users":
                client_socket.sendall(f"\n[+] Listing Users: {', '.join(usernames.values())}\n".encode())
                continue

            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break

    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]

def server():
      
    host = "127.0.0.1"
    port = 12345

    usernames = {}
    clients = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Ipv4, TCP:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((host, port))
    server_socket = ssl.wrap_socket(server_socket, keyfile = "server-key.key", certfile = "server-cert.pem", server_side = True) #deprecated
    server_socket.listen()
    
    print(f"\n[+] Server listening on port: {port}")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        print(f"New client connected: {address}")

        thread = threading.Thread(target = client_thread, args = (client_socket, clients, usernames))

        thread.daemon = True 
        thread.start()

if __name__ == "__main__":
    server()