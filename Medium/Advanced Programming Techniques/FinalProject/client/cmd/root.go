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

type Config struct {
	Problem  string
	Total    int64
	LowLimit int64
	SupLimit int64
	Output   string
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
	// Uncomment the following line if your bare application
	// has an action associated with it:
	Run: func(cmd *cobra.Command, args []string) {

		config := Config{
			Problem:  problem,
			Total:    amount,
			LowLimit: low_limit,
			SupLimit: sup_limit,
			Output:   out_put,
		}

		configJSON, err := json.Marshal(config)
		if err != nil {
			fmt.Println("Error converting to JSON", err)
			return
		}

		connection := conn.Connect_to_server()

		conn.Send_data(connection, configJSON)

		result := conn.Recieve_data(connection)

		fmt.Println(result)

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
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	// rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.client.yaml)")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.
	rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
	rootCmd.Flags().StringVarP(&problem, "problem", "p", "PrimeVerifier", "Problem to solve")
	rootCmd.Flags().Int64VarP(&amount, "amount", "a", 500, "total amount of number")
	rootCmd.Flags().Int64VarP(&low_limit, "low", "l", 0, "low limit for rage")
	rootCmd.Flags().Int64VarP(&sup_limit, "sup", "s", 1000000, "sup limit for range")
	rootCmd.Flags().StringVarP(&out_put, "output", "o", "console", "output mode")

}
