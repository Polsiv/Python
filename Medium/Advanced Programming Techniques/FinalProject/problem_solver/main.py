import socket
import requests
import json
import logging
from factory import fibonacci_creator, fizzbuzz_creator, prime_creator, i_problem_creator
from util.security import Cryptographer
from werkzeug.security import check_password_hash
import util.log

CRYPT = Cryptographer()
CRYPT.generate_keys()

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
                send_response(connection, {"Results": ["No data received!"]})
                continue

            try:
                decrypted_numbers = json.loads(handle_data(data))
                data_dict = json.loads(data.decode())

                if data_dict.get('Shutdown'):
                    flag = handle_shutdown(connection, data_dict)
                    continue

                creator = get_problem_creator(data_dict.get('Problem'))
                if not creator:
                    logging.error("Problem requested not found.")
                    send_response(connection, {"Results": ["Problem requested not found!"]})
                    continue

                logging.info(f"{data_dict['Problem']} solution performed.")
                results = handle_problem(creator, decrypted_numbers['numbers'])
                send_response(connection, {"Results": results})
                
            except Exception as e:
                logging.error("Failed to handle data: %s", str(e))
                send_response(connection, {"Results": ["Error handling data: " + str(e)]})

        except ConnectionResetError:
            logging.info(f"Cutting off connection from {client_address}")
            connection.close()

def handle_shutdown(connection, data_dict):
    if not data_dict.get('Password'):
        send_response(connection, {"Results": ["Missing Password!"]})
        return True

    if check_password(data_dict['Password']):
        send_response(connection, {"Results": ["Connection with Python Socket and Flask server cut off!"]})
        try:
            response = requests.get('http://127.0.0.1:5000/shutdown')
            return False 
        except requests.exceptions.ConnectionError:
            logging.error("Failed to connect to the Flask server for shutdown")
            return False 
    else:
        send_response(connection, {"Results": ["Incorrect Password!"]})
        return True

def get_problem_creator(problem):
    if problem == "FizzBuzz":
        return fizzbuzz_creator.FizzBuzzCreator()
    elif problem == "PrimeClassifier":
        return prime_creator.PrimeCreator()
    elif problem == "FibonacciVerifier":
        return fibonacci_creator.FibonacciCreator()
    return None

def send_response(connection, message):
    connection.sendall((json.dumps(message) + '\n').encode())

def get_data_server_public_key():
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

def post_encrypted_data(encrypted_data):
    sent_data = {
        'problem_handler_pk': CRYPT.public_key.export_key().decode(),
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

def handle_data(data):
    try:
        public_key = get_data_server_public_key()
        encrypted_data = CRYPT.encrypt(data, public_key)
        response_data = post_encrypted_data(encrypted_data)
        decrypted_data = CRYPT.decrypt(response_data['data'])
        return decrypted_data
    except Exception as e:
        logging.error("Error handling data: %s", str(e))
        raise

def handle_problem(creator: i_problem_creator, numbers):
    try:
        return creator.problem_to_solve(numbers)
    except Exception as e:
        logging.error("Error solving problem: %s", str(e))
        raise

def check_password(password):
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

if __name__ == "__main__":
    util.log.log()
    start_server("localhost", 12345)