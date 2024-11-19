package main

import (
	"fmt"
	"os"
)

func main() {
	// Check if there are any arguments passed (excluding the program name)
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run main.go <arg1> <arg2> ... <argN>")
		return
	}

	// Print out the arguments
	fmt.Println("Arguments passed to the program:")
	for i, arg := range os.Args[1:] {
		fmt.Printf("Argument %d: %s\n", i+1, arg)
	}
}

