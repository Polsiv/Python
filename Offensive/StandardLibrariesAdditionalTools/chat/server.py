#!/usr/bin/env python3 
import socket


def start_chat_server():
    host = "localhost"
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #TIME_WAIT

    server_socket.bind((host, port))
    server_socket.listen(1)

    print("\n[+] Server is ready!")
    conn, addr = server_socket.accept()

    print(f"\n[+] Connection stablished with: {addr}")

    while True:
        client_message = conn.recv(1024).decode().strip()
        print(f"\n[+] Client message: {client_message}")

        if client_message == "bye" or not client_message:
            break

        server_message = input(f"\n[+] Message to send: ")
        conn.send(server_message.encode())

    conn.close() 

start_chat_server()