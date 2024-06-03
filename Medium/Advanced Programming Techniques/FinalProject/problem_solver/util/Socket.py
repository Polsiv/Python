import socket
import json
import requests
import security as sc

class Socket():

    @staticmethod
    def start_server(host, port):
        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the address and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen(1)
        print(f'Server listening on {host}:{port}')

        flag = True

        while flag:
            # Accept a connection
            connection, client_address = server_socket.accept()
            try:
                print("Connection from", client_address)

                # Receive data
                data = connection.recv(1024)
                if data:
                    data_dict = json.loads(data.decode())
 
                    response = requests.get('http://127.0.0.1:5000/publickey')

                    if response.status_code == 200:

                        encrypted_json = sc.encrypt_data(data, response.text)

                        sent_data = {
                            'socket_pk': sc.get_pk(),
                            'data': encrypted_json 
                            }
           
                        numbers_obtained = requests.post('http://127.0.0.1:5000/numbers', json=sent_data)

                        if numbers_obtained.status_code == 200:
                            pass
                        
                        else: 
                            pass

                    else:
                        pass    
                        
                    # (Optional) Send a response
                    connection.sendall(b"Data received\n")
                    flag = False
                else:
                    break

            finally:
                # Clean up the connection   
                connection.close()

