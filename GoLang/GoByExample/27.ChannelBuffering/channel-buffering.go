package main

import "fmt"

func main() {
	messages := make(chan string, 2)

	messages <- "some"
	messages <- "input"

	fmt.Println(<-messages)
	fmt.Println(<-messages)
}
