package main

import (
	"fmt"
	"maps"
)

func main() {
	
	theMap := make(map[string]int)
	
	theMap["k1"] = 7
	theMap["k2"] = 13

	fmt.Println("Map: ", theMap)

	value1 := theMap["k1"]
	fmt.Println("value1: ", value1)

	value3 := theMap["k3"]
	fmt.Println("value3: ", value3)

	fmt.Println("Length: ", len(theMap))

	delete(theMap, "k2")
	fmt.Println("After Delete: ", theMap)
	
	clear(theMap)
	fmt.Println("After Clear: ", theMap)

	_, key2IsPresent := theMap["k2"]
	fmt.Println("Present:", key2IsPresent)

	inlineMap := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("Inline Map: ", inlineMap)

	inlineMap2 := map[string]int{"foo": 1, "bar": 2}

	if maps.Equal(inlineMap, inlineMap2) {
		fmt.Println("inlineMap == inlineMap2")
	}
}