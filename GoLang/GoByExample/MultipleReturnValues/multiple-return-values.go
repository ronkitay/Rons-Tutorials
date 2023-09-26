package main

import "fmt"

func multipleValues() (int, int) {
	return 3, 7
}

func main() {

	a, b := multipleValues()

	fmt.Println(a)
	fmt.Println(b)
	
	_, c := multipleValues()
	fmt.Println(c)
}