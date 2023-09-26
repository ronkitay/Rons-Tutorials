package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}


func main() {
	result := plus(5, 7)
	fmt.Println("5+7 =", result)

	result = plusPlus(3, 7, 10)
	fmt.Println("3+7+10 =", result)
}