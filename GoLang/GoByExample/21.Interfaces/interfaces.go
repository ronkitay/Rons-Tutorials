package main

import (
	"fmt"
	"math"
)

type geometry interface {
	area() float64
	perimeter() float64
}

type rectangle struct {
	height, width float64
}

type circle struct {
	radios float64
}

func (r rectangle) area() float64 {
	return r.height * r.width
}

func (r rectangle) perimeter() float64 {
	return (r.height + r.width) * 2
}

func (c circle) area() float64 {
	return c.radios * c.radios * math.Pi
}

func (c circle) perimeter() float64 {
	return 2 * c.radios * math.Pi
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perimeter())
}

func main() {

	measure(rectangle{1, 1})
	measure(circle{12.5})

}
