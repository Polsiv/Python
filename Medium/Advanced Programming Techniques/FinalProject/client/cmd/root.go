/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"client/conn"
	"encoding/json"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var (
	problem   string
	amount    int64
	low_limit int64
	sup_limit int64
	out_put   string
)

type Response struct {
	Response []string `json:"Results"`
}

type Config struct {
	Problem  string
	Total    int64
	LowLimit int64
	SupLimit int64
	Output   string
	Password string
	Shutdown bool
}

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "client",
	Short: "A brief description of your application",
	Long: `A longer description that spans multiple lines and likely contains
examples and usage of using your application. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		if low_limit < 0 || low_limit > sup_limit || sup_limit < 0 {
			fmt.Println("Error: Low limit should be greater than or equal to 0 and less than or equal to the high limit.")
			return
		}

		config := Config{
			Problem:  problem,
			Total:    amount,
			LowLimit: low_limit,
			SupLimit: sup_limit,
			Output:   out_put,
			Password: "",
			Shutdown: false,
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

		if out_put != "console" {
			file, err := os.Create(out_put)
			if err != nil {
				fmt.Printf("error creating file: %v\n", err)
				return
			}
			defer file.Close()

			for _, item := range response.Response {
				_, err := file.WriteString(item + "\n")
				if err != nil {
					fmt.Printf("error writing to file: %v\n", err)
					return
				}
			}
			fmt.Printf("Results written to file: %s, go check themout!", out_put)
		} else {
			for _, item := range response.Response {
				fmt.Println(item)
			}
		}
	},
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {

	rootCmd.AddCommand(ShutdownCmd)
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	// rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.client.yaml)")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.
	rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
	rootCmd.Flags().StringVarP(&problem, "problem", "p", "PrimeClassifier", "Problem to solve")
	rootCmd.Flags().Int64VarP(&amount, "amount", "a", 10, "total amount of number")
	rootCmd.Flags().Int64VarP(&low_limit, "low", "l", 0, "low limit for rage")
	rootCmd.Flags().Int64VarP(&sup_limit, "sup", "s", 1000, "sup limit for range")
	rootCmd.Flags().StringVarP(&out_put, "output", "o", "console", "output mode")
}
