package main

import "fmt"

func sum(numbers ... int) {
	fmt.Print(numbers, " ")
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	fmt.Println(sum)
}

func main() {
	sum(1, 2)
	sum(1, 2, 3)
	
	numbers := []int{1,4,6,9}
	sum(numbers...)
}