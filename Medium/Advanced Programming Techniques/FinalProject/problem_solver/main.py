import socket
import requests
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator, i_problem_creator
from util.security import Cryptographer
import json
import logging
import util.log

CRYPT = Cryptographer()
CRYPT.generate_keys()

class Main:

    @staticmethod
    def start_server(host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        logging.info(f'Server listeing on {host} : {port}')
        print(f'Server listening on {host}:{port}')

        flag = True
        while flag:
            connection, client_address = server_socket.accept()
            try:
                print("Connection from", client_address)
                logging.info(f"Connection from {client_address}")
                data = connection.recv(1024)
                if data:

                    decrypted_numbers = json.loads(Main.handle_data(data))

                    data_dict = json.loads(data.decode())

                    if data_dict['Problem'] == "FizzBuzz":
                        creator = fizzbuzz_creator.FizzBuzzCreator()
                        logging.info("FizzBuzz solution performed.")
                    elif data_dict['Problem'] == "PrimeClassifier":
                        creator = prime_creator.PrimeCreator()
                        logging.info("PrimeClassifer solution performed.")
                    elif data_dict['Problem'] == "FibonacciVerifier":
                        creator = fibonacci_creator.FibonacciCreator()
                        logging.info("FibonacciVerifier solution performed.")
                    else: 
                        creator = None
                        logging.error("Problem requested not found.")

                    if creator is not None:
                        results = Main.handle_problem(creator, decrypted_numbers['numbers'])
                        
                        result = {"Results": results}
                        connection.sendall((json.dumps(result) + '\n').encode())
                    else:
                        error_message = {"Results": ["Problem requested not found! "]}
                        connection.sendall((json.dumps(error_message) + '\n').encode())

                    flag = False
                else:
                    break
            finally:
                connection.close()

    @staticmethod
    def get_data_server_public_key():
        response = requests.get('http://127.0.0.1:5000/publickey')
        if response.status_code == 200:
            return response.text
        else:
            logging.error("Failed to get public key")
            raise Exception("Failed to get public key")

    @staticmethod
    def post_encrypted_data(encrypted_data):
        sent_data = {
            'problem_handler_pk': CRYPT.public_key.export_key().decode(),
            'data': encrypted_data
        }
        response = requests.post('http://127.0.0.1:5000/numbers', json=sent_data)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error("Failed to post encrypted data")
            raise Exception("Failed to post encrypted data")

    @staticmethod
    def handle_data(data):
        public_key = Main.get_data_server_public_key()
        encrypted_data = CRYPT.encrypt(data, public_key)
        response_data = Main.post_encrypted_data(encrypted_data)
        decrypted_data = CRYPT.decrypt(response_data['data'])
        return decrypted_data

    @staticmethod
    def handle_problem(creator: i_problem_creator, numbers):
        return creator.problem_to_solve(numbers)

if __name__ == "__main__":
    util.log.log()
    my_main = Main()
    my_main.start_server("localhost", 12345)

    
