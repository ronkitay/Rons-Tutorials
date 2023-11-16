package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	s := "שלום עולם"

	fmt.Println("Len:", len(s))

	for i:=0; i<len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	fmt.Println("Rune count:", utf8.RuneCountInString(s))

	for index, runeValue := range s {
		fmt.Printf("%#U starts at %d\n", runeValue, index)
	}

	for index, width := 0, 0 ; index < len(s); index+=width {
		runeValue, widthOfRune := utf8.DecodeRuneInString(s[index:])
		fmt.Printf("%#U starts at %d\n", runeValue, index)
		width = widthOfRune

		examineRune(runeValue)
	}
}

func examineRune(theRune rune) {
	if theRune == 'ש' {
		fmt.Println("Found the ש")
	} else if theRune == 'ו' {
		fmt.Println("Found the ו")
	}
}