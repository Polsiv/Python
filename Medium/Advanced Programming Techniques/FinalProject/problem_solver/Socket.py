import socket
import json
import requests
from util.security import Cryptographer
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator, i_problem_creator
from werkzeug.security import check_password_hash

class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.crypt = Cryptographer()
        self.crypt.generate_keys()

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f'Server listening on {self.host}:{self.port}')

        flag = True
        while flag:
            try:
                connection, client_address = self.server_socket.accept()
                print("Connection from", client_address)
                data = connection.recv(1024)

                if not data:
                    self.send_response(connection, {"Results": ["No data received!"]})

                try:
                    decrypted_numbers = json.loads(self.handle_data(data))
                    data_dict = json.loads(data.decode())

                    if data_dict.get('Shutdown'):
                        flag = self.handle_shutdown(connection, data_dict)
                        continue

                    creator = self.get_problem_creator(data_dict.get('Problem'))
                    if not creator:
                        self.send_response(connection, {"Results": ["Problem requested not found!"]})
                        continue

                    results = self.handle_problem(creator, decrypted_numbers['numbers'])
                    self.send_response(connection, {"Results": results})

                except Exception as e:
                    flag = False
                    self.send_response(connection, {"Results": ["Error handling data: " + str(e)]})

            except ConnectionResetError:
                connection.close()

        #close socket server after the loop exits
        self.server_socket.close()


    def handle_data(self, data):
        try:
            public_key = self.get_data_server_public_key()
            encrypted_data = self.crypt.encrypt(data, public_key)
            response_data = self.post_encrypted_data(encrypted_data)
            decrypted_data = self.crypt.decrypt(response_data['data'])
            return decrypted_data
        except Exception as e:
            raise

    def get_problem_creator(self, problem):
        if problem == "FizzBuzz":
            return fizzbuzz_creator.FizzBuzzCreator()
        elif problem == "PrimeClassifier":
            return prime_creator.PrimeCreator()
        elif problem == "FibonacciVerifier":
            return fibonacci_creator.FibonacciCreator()
        return None


    def send_response(self, connection, message):
        connection.sendall((json.dumps(message) + '\n').encode())

    def handle_problem(self, creator: i_problem_creator, numbers):
        try:
            return creator.problem_to_solve(numbers)
        except Exception as e:
            raise

    def get_data_server_public_key(self):
        try:
            response = requests.get('http://127.0.0.1:5000/publickey')
            if response.status_code == 200:
                return response.text
            else:
                raise Exception("Failed to get public key")
        except requests.exceptions.ConnectionError as e:
            raise Exception("Flask server is inactive or unreachable") from e

    def handle_shutdown(self, connection, data_dict):
        if not data_dict.get('Password'):
            self.send_response(connection, {"Results": ["Missing Password!"]})
            return True

        if self.check_password(data_dict['Password']):
            self.send_response(connection, {"Results": ["Connection with Python Socket and Flask server cut off!"]})
            try:
                response = requests.get('http://127.0.0.1:5000/shutdown')
                return False 
            except Exception:
                return False 
        else:
            self.send_response(connection, {"Results": ["Incorrect Password!"]})
            return True

    def post_encrypted_data(self, encrypted_data):
        sent_data = {
            'problem_solver_pk': self.crypt.public_key.export_key().decode(),
            'data': encrypted_data
        }
        try:
            response = requests.post('http://127.0.0.1:5000/numbers', json=sent_data)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("Failed to post encrypted data")
        except requests.exceptions.ConnectionError as e:
            raise Exception("Flask server is inactive or unreachable") from e  

    def check_password(self, password):
        try:
            with open("util/userpassword.txt", encoding='utf-8') as f:
                hashed_password = f.readline().strip()
            return check_password_hash(hashed_password, password)
        except FileNotFoundError as e:
            raise Exception("Password file not found") from e
        except Exception as e:
            raise


