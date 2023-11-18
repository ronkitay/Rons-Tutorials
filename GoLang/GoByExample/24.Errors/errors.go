package main

import (
	"errors"
	"fmt"
)

func function1(number int) (int, error) {
	if number == 42 {
		return -1, errors.New("42 is not supported")
	}

	return number + 3, nil
}

type ErrorWithArgument struct {
	argument int
	problem  string
}

func function2(number int) (int, error) {
	if number == 42 {
		return -1, &ErrorWithArgument{number, "42 is not supported"}
	}

	return number + 3, nil
}

func (errorWithArgument ErrorWithArgument) Error() string {
	return errorWithArgument.problem
}

func main() {

	for _, value := range []int{7, 13, 42, 89} {
		if result, error := function1(value); error != nil {
			fmt.Println("Function 1 failed: ", error)
		} else {
			fmt.Println("Function 1 worked: ", result)
		}
	}

	for _, value := range []int{5, 23, 42, 71} {
		if result, error := function2(value); error != nil {
			fmt.Println("Function 2 failed: ", error)
		} else {
			fmt.Println("Function 2 worked: ", result)
		}
	}

	_, theError := function2(42)

	if errorObject, ok := theError.(*ErrorWithArgument); ok { // "Type Assertion"
		fmt.Println("Bad Argument:", errorObject.argument)
		fmt.Println("Reason:", errorObject.problem)
	}

}
