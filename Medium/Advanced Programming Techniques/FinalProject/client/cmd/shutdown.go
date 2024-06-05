/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"client/conn"
	"encoding/json"
	"fmt"

	"github.com/spf13/cobra"
)

var password string

// rootCmd represents the base command when called without any subcommands
var ShutdownCmd = &cobra.Command{
	Use:   "Shutdown cmd",
	Short: "A brief description of your application",
	Long: `A longer description that spans multiple lines and likely contains
examples and usage of using your application. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		config := Config{
			Problem:  "",
			Total:    0,
			LowLimit: 0,
			SupLimit: 0,
			Output:   "",
			Password: password,
			Shutdown: true,
		}

		configJSON, err := json.Marshal(config)
		if err != nil {
			fmt.Println("Error converting to JSON", err)
			return

		}
		connection, err := conn.Connect_to_server()
		if err != nil {
			fmt.Println("Error: Unable to connect to server. Please ensure the server is running and try again!.")
			return
		}

		err = conn.Send_data(connection, configJSON)
		if err != nil {
			fmt.Println("Error sending data:", err)
			return
		}

		result, err := conn.Recieve_data(connection)
		if err != nil {
			fmt.Printf("error receiving data: %v\n", err)
			return
		}

		var response Response

		err = json.Unmarshal(result, &response)

		if err != nil {
			fmt.Printf("error deserializing JSON: %v\n", err)
			return
		}

		for _, item := range response.Response {
			fmt.Println(item)
		}
	},
}

func init() {

	ShutdownCmd.Flags().StringVarP(&password, "shutdown", "d", "", " Shutdown System")

}
