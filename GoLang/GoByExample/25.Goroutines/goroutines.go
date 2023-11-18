package main

import (
	"fmt"
	"time"
)

func someFunction(from string) {
	for i := 0; i < 5; i++ {
		fmt.Println(from, ":", i)
	}

}

func main() {

	someFunction("Direct execution")

	go someFunction("Goroutine")

	go func(message string) {
		fmt.Println(message)
	}("Anonymous Goroutine")

	time.Sleep(time.Second)

	fmt.Println("Done")
}
