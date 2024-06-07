#pylint: disable = E0401, W1203, W0718, W0612, W0719, C0301, R1705, W3101
import socket
import logging
import json
import requests
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator, i_problem_creator
from util.security import Cryptographer
from werkzeug.security import check_password_hash
import util.log
util.log.log()

class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.crypt = Cryptographer()
        self.crypt.generate_keys()

    def start_server(self):
        """ibnitializes the server"""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        logging.info(f'Server listening on {self.host}:{self.port}')
        print(f'Server listening on {self.host}:{self.port}')

        flag = True
        while flag:
            try:
                connection, client_address = self.server_socket.accept()
                print("Connection from", client_address)
                logging.info(f"Connection from {client_address}")
                data = connection.recv(1024)

                if not data:
                    self.send_response(connection, {"Results": ["No data received!"]})
                    continue
                try:
                    data_dict = json.loads(data.decode())
                    if data_dict.get('Shutdown'):
                        flag = self.handle_shutdown(connection, data_dict)
                        continue

                    creator = self.get_problem_creator(data_dict.get('Problem'))
                    if not creator:
                        logging.error("Problem requested not found.")
                        self.send_response(connection, {"Results": ["Problem requested not found!"]})
                        continue

                    decrypted_numbers = json.loads(self.handle_data(data))
                    logging.info(f"{data_dict['Problem']} solution performed.")
                    results = self.handle_problem(creator, decrypted_numbers['numbers'])

                    self.send_response(connection, {"Results": results})

                except Exception as e:
                    logging.error("Failed to handle data: %s", str(e))
                    flag = False
                    self.send_response(connection, {"Results": ["Error handling data: " + str(e)]})

            except socket.timeout:
                logging.error("Timeout occurred while trying to connect to the Flask server. Shutting down the socket server.")
                flag = False

            except ConnectionResetError:
                logging.info(f"Cutting off connection from {client_address}")
                connection.close()

        # Close the socket server after the loop exits
        self.server_socket.close()

    def handle_shutdown(self, connection, data_dict):
        """handles the shut down"""
        if not data_dict.get('Password'):
            self.send_response(connection, {"Results": ["Missing Password!"]})
            return True

        if self.check_password(data_dict['Password']):
            self.send_response(connection, {"Results": ["Connection with Python Socket and Flask server cut off!"]})
            try:
                response = requests.get('http://127.0.0.1:5000/shutdown')
                return False
            except Exception:
                logging.error("Failed to connect to the Flask server for shutdown")
                return False
        else:
            self.send_response(connection, {"Results": ["Incorrect Password!"]})
            return True

    def get_problem_creator(self, problem):
        """returns the problem requested by the client"""

        if problem == "FizzBuzz":
            return fizzbuzz_creator.FizzBuzzCreator()
        elif problem == "PrimeClassifier":
            return prime_creator.PrimeCreator()
        elif problem == "FibonacciVerifier":
            return fibonacci_creator.FibonacciCreator()
        return None

    def send_response(self, connection, message):
        """sends the response to the client"""

        connection.sendall((json.dumps(message) + '\n').encode())

    def get_data_server_public_key(self):
        """Retrieves the public key from data server"""

        try:
            response = requests.get('http://127.0.0.1:5000/publickey')
            if response.status_code == 200:
                return response.text
            else:
                logging.error("Failed to get public key: Received status code %s", response.status_code)
                raise Exception("Failed to get public key")
        except requests.exceptions.ConnectionError as e:
            logging.error("Failed to connect to the Flask server for public key: %s", str(e))
            raise Exception("Flask server is inactive or unreachable") from e

    def post_encrypted_data(self, encrypted_data):
        """sends encrypted data to data server"""

        sent_data = {
            'problem_solver_pk': self.crypt.public_key.export_key().decode(),
            'data': encrypted_data
        }
        try:
            response = requests.post('http://127.0.0.1:5000/numbers', json=sent_data)
            if response.status_code == 200:
                return response.json()
            else:
                logging.error("Failed to post encrypted data: Received status code %s", response.status_code)
                raise Exception("Failed to post encrypted data")
        except requests.exceptions.ConnectionError as e:
            logging.error("Failed to connect to the Flask server to post encrypted data: %s", str(e))
            raise Exception("Flask server is inactive or unreachable") from e

    def handle_data(self, data):
        """handles the data"""

        try:
            public_key = self.get_data_server_public_key()
            encrypted_data = self.crypt.encrypt(data, public_key)
            response_data = self.post_encrypted_data(encrypted_data)
            decrypted_data = self.crypt.decrypt(response_data['data'])
            return decrypted_data
        except Exception as e:
            logging.error("Error handling data: %s", str(e))
            raise

    def handle_problem(self, creator: i_problem_creator, numbers):
        """handles the problem and returns the result"""

        try:
            return creator.problem_to_solve(numbers)
        except Exception as e:
            logging.error("Error solving problem: %s", str(e))
            raise

    def check_password(self, password):
        """checks the password sent by the user"""

        try:
            with open("util/userpassword.txt", encoding='utf-8') as f:
                hashed_password = f.readline().strip()
            return check_password_hash(hashed_password, password)
        except FileNotFoundError as e:
            logging.error("Password file not found: %s", str(e))
            raise Exception("Password file not found") from e
        except Exception as e:
            logging.error("Error checking password: %s", str(e))
            raise
