package main

import "fmt"

func intSeq() func() int {
    i := 0
    return func() int {
        i+=2
        return i
    }
}

func main() {

    var nextInt func() int = intSeq()
    fmt.Println(nextInt())
    fmt.Println(nextInt())
    fmt.Println(nextInt())

    newInts := intSeq()
    fmt.Println(newInts())
}