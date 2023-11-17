package main

import "fmt"

type animal struct {
	group string
}

func (a animal) describe() string {
	return fmt.Sprintf("Animal from group %s", a.group)
}

type dog struct {
	animal
	breed string
}

func main() {

	myDog := dog{
		animal: animal{
			group: "dog",
		},
		breed: "poodle",
	}

	fmt.Printf("Dog={group: %s, breed: %s}\n", myDog.group, myDog.breed)

	fmt.Println("Also group:", myDog.animal.group)

	fmt.Println("Describe:", myDog.describe())

	type describer interface {
		describe() string
	}

	var describable describer = myDog

	fmt.Println("Describable dog:", describable.describe())
}
