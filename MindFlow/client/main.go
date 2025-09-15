package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli"
)

func main() {

	var app = &cli.App{
		Name:    "mindflow",
		Usage:   "A mindflow CLI tool",
		Version: "0.1.0",
		Commands: []cli.Command{
			{
				Name:  "send",
				Usage: "Initialises an empty vilo file",
				Flags: []cli.Flag{
					&cli.StringFlag{Name: "query", Usage: "query in natural language"},
				},
				Action: func(c *cli.Context) error {
					var query = c.String("query")
					resp := SendQuery(query)
					fmt.Println(resp)
					return nil
				},
			},
		},
	}

	log.Fatal(app.Run(os.Args))

}
