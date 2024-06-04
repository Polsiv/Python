import socket
import json
import requests
from security import Cryptographer

CRYPT = Cryptographer()

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
                   #data_dict = json.loads(data.decode())
 
                    response = requests.get('http://127.0.0.1:5000/publickey')

                    if response.status_code == 200:
                       
                        CRYPT.generate_keys()
                        encrypted_json = CRYPT.encrypt(data, response.text)
                        sent_data = {
                            'problem_handler_pk': CRYPT.public_key.export_key().decode(),
                            'data': encrypted_json 
                            }
           
                        data_obtained = requests.post('http://127.0.0.1:5000/numbers', json = sent_data)

                        if data_obtained.status_code == 200:

                            obtained_data = data_obtained.json()
                            decrypted_numbers = CRYPT.decrypt(obtained_data['data'])
                      

                        else: 
                            print("Error")

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

