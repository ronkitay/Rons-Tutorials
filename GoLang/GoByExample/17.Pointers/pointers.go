package main

import "fmt"

func zeroByValue(integerValue int) {
	integerValue = 0
}

func zeroByPointer(integerPointer *int) {
	*integerPointer = 0
}

func main()  {
	i := 1
	fmt.Println("Initial value:", i)
	
	zeroByValue(i)
	fmt.Println("After zeroByValue value:", i)

	zeroByPointer(&i)
	fmt.Println("After zeroByPointer value:", i)
	
	fmt.Println("Pointer address value:", &i)
}