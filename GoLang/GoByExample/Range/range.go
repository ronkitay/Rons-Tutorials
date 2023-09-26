package main

import "fmt"

func main() {

	numbers := []int{2, 3, 4}
	sum := 0

	for _, num := range numbers {
		sum += num
	}

	fmt.Println("Sum: ", sum)

	for index, num := range numbers {
		if num == 3 {
			fmt.Println("Index:", index)
		}
	}

	keysAndValues := map[string]string{"a": "apple", "b": "banana"}
	for key, value := range keysAndValues {
		fmt.Printf("%s -> %s\n", key, value)
	}

	for key := range keysAndValues {
		fmt.Println("Key:", key)
	}

	for index, rune := range "go" {
		fmt.Println(index, rune)
	}
}