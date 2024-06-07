package conn

import (
	"bytes"
	"errors"
	"fmt"
	"io"
	"net"
)

func Connect_to_server() (net.Conn, error) {
	conn, err := net.Dial("tcp", "localhost:12345")
	if err != nil {
		return nil, errors.New("failed to connect to server")
	}
	return conn, nil
}

func Send_data(connection net.Conn, message []byte) error {

	_, err := connection.Write([]byte(message))
	if err != nil {
		fmt.Println("Error sending message:", err)
		return fmt.Errorf("error sending message: %w", err)
	}
	return nil
}

func Recieve_data(connect net.Conn) ([]byte, error) {
	buffer := make([]byte, 1024)
	var result bytes.Buffer
	for {
		n, err := connect.Read(buffer)
		if err != nil {
			if err == io.EOF {
				break
			}
			return nil, fmt.Errorf("error reading from connection: %v", err)
		}

		result.Write(buffer[:n])

		if bytes.Contains(buffer[:n], []byte{'\n'}) {
			break
		}
	}

	return result.Bytes(), nil
}
