package main

import (
	"fmt"
	"slices"
)

func main() {

	var s []string
	fmt.Println("Un-Initialized:", s, s == nil, len(s) == 0)
	
	s = make([]string, 3)
	fmt.Println("Empty:", s, "Length:", len(s), "Capacity:" , cap(s))

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"

	fmt.Println("Set:" , s)
	fmt.Println("Get:" , s[2])
	
	fmt.Println("Length:" , len(s))
	
	s = append(s, "d")
	s = append(s, "e", "f")
	
	fmt.Println("Appended:" , s, "Size: ", len(s), "Capacity:", cap(s))
	
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("Copied:" , c, "Size: ", len(c), "Capacity:", cap(c))
	
	l := s[2:5]
	fmt.Println("Slice #1:" , l)

	l2 := s[:5]
	fmt.Println("Slice #2:" , l2)

	l3 := s[2:]
	fmt.Println("Slice #3:" , l3)

	t := []string{"g", "h", "i"}
	fmt.Println("Declared:" , t, "Size: ", len(t), "Capacity:", cap(t))

	t2 := []string{"g", "h", "i"}
    if slices.Equal(t, t2) {
        fmt.Println("t == t2")
    }

	twoD := make([][]int, 3)

	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2 Dimensional:", twoD)

}