import socket

def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f'Server listening on {host}:{port}')

    while True:
        # Accept a connection
        connection, client_address = server_socket.accept()
        try:
            print("Connection from", client_address)

            # Receive data
            data = connection.recv(1024)
            if data:
                print("Received:", data.decode())

                # (Optional) Send a response
                connection.sendall(b"Data received\n")
            else:
                break

        finally:
            # Clean up the connection   
            connection.close()

if __name__ == "__main__":
    start_server("localhost", 12345)
