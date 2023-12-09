// https://gobyexample.com/select
package main

import (
	"fmt"
	"time"
)

func main() {
	channel1 := make(chan string)
	channel2 := make(chan string)

	go func() {
		time.Sleep(2 * time.Second)
		channel1 <- "Message for channel #1"
	}()

	go func() {
		time.Sleep(1 * time.Second)
		channel2 <- "Message for channel #2"
	}()

	for i := 0; i < 2; i++ {
		select {
		case message1 := <-channel1:
			fmt.Println("Received:", message1)
		case message2 := <-channel2:
			fmt.Println("Received:", message2)
		}
	}
}
