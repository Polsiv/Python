package conn

import (
	"bytes"
	"fmt"
	"net"
	"os"
)

type Response struct {
	Result []string `json:"result"`
}

func Connect_to_server() net.Conn {
	conn, err := net.Dial("tcp", "localhost:12345")
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		os.Exit(1)
	}
	return conn
}

func Send_data(connection net.Conn, message []byte) {

	_, err := connection.Write([]byte(message))
	if err != nil {
		fmt.Println("Error sending message:", err)
		return
	}
}

func Recieve_data(connect net.Conn) ([]byte, error) {

	buffer := make([]byte, 1024)
	var result bytes.Buffer

	for {
		n, err := connect.Read(buffer)
		if err != nil {
			return nil, fmt.Errorf("error: %v", err)
		}

		result.Write(buffer[:n])

		if bytes.Contains(buffer[:n], []byte{'\n'}) {
			break
		}
	}

	return result.Bytes(), nil

}
