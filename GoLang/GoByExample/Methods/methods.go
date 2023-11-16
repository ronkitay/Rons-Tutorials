package main

import "fmt"

type rect struct {
	width, height int
}

func (r *rect) area() int {
	return r.width * r.height
}

func (r *rect) perimeter() int {
	return (r.width + r.height)*2
}

func main() {

	rectangle := rect{width: 10, height: 7}
	fmt.Println("Area:", rectangle.area())
	fmt.Println("Perimeter:", rectangle.perimeter())

	rectanglePointer := &rectangle
	fmt.Println("Area:", rectanglePointer.area())
	fmt.Println("Perimeter:", rectanglePointer.perimeter())
}
