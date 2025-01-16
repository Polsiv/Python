#!/usr/bin/env python3

import socket

def start_udp_server():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\n[+] UDP server  listening on: {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Message sent by client :{data.decode()}")
            print(f"\n[+] CLient info: {addr}")
    
if __name__ == "__main__":
    start_udp_server()