import socket
import requests
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator, i_problem_creator
from util.security import Cryptographer
import json
import logging
import util.log
from werkzeug.security import check_password_hash

CRYPT = Cryptographer()
CRYPT.generate_keys()


class Main:

    @staticmethod
    def start_server(host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)

        logging.info(f'Server listening on {host}:{port}')
        print(f'Server listening on {host}:{port}')

        flag = True
        while flag:
            connection, client_address = server_socket.accept()
            try:
                print("Connection from", client_address)
                logging.info(f"Connection from {client_address}")
                data = connection.recv(1024)

                if not data:
                    Main.send_response(connection, {"Results": ["No data received!"]})
                    continue

                decrypted_numbers = json.loads(Main.handle_data(data))
                data_dict = json.loads(data.decode())

                if data_dict.get('Shutdown'):
                    flag = Main.handle_shutdown(connection, data_dict)
                    continue

                creator = Main.get_problem_creator(data_dict.get('Problem'))
                if not creator:
                    logging.error("Problem requested not found.")
                    Main.send_response(connection, {"Results": ["Problem requested not found!"]})
                    continue

                logging.info(f"{data_dict['Problem']} solution performed.")
                results = Main.handle_problem(creator, decrypted_numbers['numbers'])
                Main.send_response(connection, {"Results": results})

            except ConnectionResetError:
                logging.info(f"Cutting off connection from {client_address}")
                connection.close()

    @staticmethod
    def handle_shutdown(connection, data_dict):
        if not data_dict.get('Password'):
            Main.send_response(connection, {"Results": ["Missing Password!"]})
            return True

        if Main.check_password(data_dict['Password']):
            Main.send_response(connection, {"Results": ["Connection with Python Socket and Flask server cut off!"]})
            try:
                response = requests.get(('http://127.0.0.1:5000/shutdown'))
                return False 
            except requests.exceptions.ConnectionError:
                return False 
        else:
            Main.send_response(connection, {"Results": ["Incorrect Password!"]})
            return True

    @staticmethod
    def get_problem_creator(problem):
        if problem == "FizzBuzz":
            return fizzbuzz_creator.FizzBuzzCreator()
        elif problem == "PrimeClassifier":
            return prime_creator.PrimeCreator()
        elif problem == "FibonacciVerifier":
            return fibonacci_creator.FibonacciCreator()
        return None

    @staticmethod
    def send_response(connection, message):
        connection.sendall((json.dumps(message) + '\n').encode())

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

    @staticmethod
    def check_password(password):
        with open("util/userpassword.txt", encoding='utf-8') as f:
            hashed_password = f.readline().strip()
        return check_password_hash(hashed_password, password)


if __name__ == "__main__":
    util.log.log()
    my_main = Main()
    my_main.start_server("localhost", 12345)
