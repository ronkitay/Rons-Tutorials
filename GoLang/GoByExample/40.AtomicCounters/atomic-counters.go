package main

// SOURCE: https://gobyexample.com/atomic-counters

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

func main() {

	var counter atomic.Uint64

	var waitGroup sync.WaitGroup

	for i := 0; i < 50; i++ {
		waitGroup.Add(1)

		go func() {
			for c := 0; c < 1000; c++ {
				counter.Add(1)
			}

			waitGroup.Done()
		}()
	}

	for i := 0; i < 5; i++ {
		time.Sleep(1 * time.Microsecond)
		fmt.Println("Counter:", counter.Load())
	}

	waitGroup.Wait()

	fmt.Println("Counter:", counter.Load())
}
