#!/usr/bin/env python3

import socket


def start_client():

    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            message = input("\n[+]Enter your message: ")

            if message == "bye" or not message:
                break
            s.sendall(message.encode())
            data = s.recv(1024) 

            print(f"\n[+] Message from the server: {data.decode()}")


start_client()