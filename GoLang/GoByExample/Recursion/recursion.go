package main

import "fmt"

func factorial(number int) int {
	if (number == 0) {
		return 1
	}
	return number * factorial(number-1)
}

func main() {
	fmt.Println(factorial(7))

	var fibonnaci func(number int) int

	fibonnaci = func(number int) int {
		if (number < 2) {
			return number
		}
		return fibonnaci(number-1) + fibonnaci(number-2)
	}

	fmt.Println(fibonnaci(7))
}