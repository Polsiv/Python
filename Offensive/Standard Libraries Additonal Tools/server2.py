#!/usr/bin/env python3

import socket
import threading
import pdb 
#pdb debbuging, when the program reaches the breakpint (press L), (p "variable") pritns the variable

class ClientThread(threading.Thread):
    
    def __init__(self, client_sock, client_addr):
        #since we have no clue what the original class is instancing, we call the constuctor
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr
        
        print(f"\n[!] New connected client: {self.client_addr}")

    def run(self):
        message = ''
      
        while True:
                data = self.client_sock.recv(1024)
                message = data.decode().strip()

                #pdb.set_trace() #breakpoint
                if message == 'bye' or not message:
                    break
                
                print(f"\n[+]Message sent from the client {self.client_addr[0]}: {message}")
                self.client_sock.send(data)

        print(f"\n[!] Client: {self.client_addr} Disconnected.")
        self.client_sock.close()


def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    #each level of the sockets relies on different protocols
    #setsockopt arguments:
    #1: Level
    #2: Property to modify
    #3: What
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))

        print("\n[+] Waiting for connections...")

        while True:
            server_socket.listen()
            client_sock, client_addr = server_socket.accept()

            #since Thread is a class and its not prepared for what we gonna do, we can modify its functionallity
            #new_thread = threading.Thread(target = start_server(), args = (client_sock, client_addr))
            
            new_thread = ClientThread(client_sock, client_addr)
            new_thread.start()


if __name__ == "__main__":

    host = "localhost"
    port = 1234
    start_server(host, port)
