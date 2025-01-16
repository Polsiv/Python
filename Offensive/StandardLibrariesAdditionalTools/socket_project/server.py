#!/usr/bin/env python3

import os
import socket

def start_server():
    
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"\n[*] Listeing on {host}:{port}")

        s.listen(1)

        conn, addr = s.accept()

        with conn:
            print(f"\n[+] New client connected: {addr}")
            
            while True:
                data = conn.recv(1024).decode()

                if not data:
                    break
                
                data = data.replace("\n", "")
                cur_u = os.getlogin()
                conn.sendall(f"Hi {data}!, this is {cur_u}!\n".encode())


if __name__ == "__main__":
    start_server()





