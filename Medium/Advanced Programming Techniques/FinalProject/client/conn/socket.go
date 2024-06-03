package conn

import (
	"fmt"
	"net"
	"os"
)

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

func Recieve_data(connection net.Conn) []byte {
	buff := make([]byte, 1024)
	n, err := connection.Read(buff)
	if err != nil {
		fmt.Println("Error reading reading respone:", err)
		return nil
	}

	return buff[:n]
}
