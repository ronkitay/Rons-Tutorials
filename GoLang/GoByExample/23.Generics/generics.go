package main

import "fmt"

func MapKeys[KEY comparable, VALUE any](theMap map[KEY]VALUE) []KEY {
	result := make([]KEY, 0, len(theMap))

	for key := range theMap {
		result = append(result, key)
	}

	return result
}

type List[TYPE any] struct {
	head, tail *element[TYPE]
}

type element[TYPE any] struct {
	next  *element[TYPE]
	value TYPE
}

func (list *List[TYPE]) Push(value TYPE) {
	newElement := element[TYPE]{value: value}
	if list.head == nil {
		list.head = &newElement
		list.tail = &newElement
	} else {
		list.tail.next = &newElement
		list.tail = &newElement
	}
}

func (list *List[TYPE]) GetAll() []TYPE {
	var elements []TYPE

	for element := list.head; element != nil; element = element.next {
		elements = append(elements, element.value)
	}

	return elements
}

func main() {

	var someMap = map[int]string{1: "2", 2: "4", 4: "8"}

	fmt.Println("Keys:", MapKeys(someMap))

	_ = MapKeys[int, string](someMap)

	list := List[int]{}

	list.Push(10)
	list.Push(13)
	list.Push(23)

	fmt.Println("List:", list.GetAll())
}
