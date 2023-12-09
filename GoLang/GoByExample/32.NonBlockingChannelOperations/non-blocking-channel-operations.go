// https://gobyexample.com/non-blocking-channel-operations
package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)
	select {
	case message := <-messages:
		fmt.Println("Received message", message)
	default:
		fmt.Println("No message received...")
	}

	message := "hi"
	select {
	case messages <- message:
		fmt.Println("Sent message", message)
	default:
		fmt.Println("No message sent...")
	}

	select {
	case message := <-messages:
		fmt.Println("Received message", message)
	case signal := <-signals:
		fmt.Println("Received signal", signal)
	default:
		fmt.Println("No activity...")
	}
}
