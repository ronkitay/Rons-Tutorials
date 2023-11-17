package main

import "fmt"

type address struct {
	country string
	city string
	street string
	number int
}

func newAddress(country string) *address {
	address := address{country: country}
	address.city = "Sin City"
	address.street = "Max Payne"
	address.number = 13

	return &address
}

func main() {

	fmt.Println(address{"Sokovia", "Sokovia City", "Main Street", 5})
	fmt.Println(address{country: "Neverneverland", city: "Peter", street: "Pen", number: 18})
	fmt.Println(address{country: "Nowhereland"})
	fmt.Println(&address{country: "Referenceland", city: "Pointerville"})
	fmt.Println(newAddress("Carnage"))

	address := address{country: "Camalot", city: "We already got one!"}
	fmt.Println(address.country)
	
	addressPointer := &address
	fmt.Println(addressPointer.city)
	
	addressPointer.city = "We moved!"
	fmt.Println(address.city)

	cat := struct {
		name string
		doesPurr bool
	} { 
		"Mitzy", 
		true,
	}

	fmt.Println(cat)

}
