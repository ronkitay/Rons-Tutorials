package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	time.Sleep(time.Second)

	fmt.Printf("Worker %d done\n", id)
}

func main() {

	var waitGroup sync.WaitGroup

	for i := 1; i <= 5; i++ {
		waitGroup.Add(1)

		workerId := i

		go func() {
			defer waitGroup.Done()
			worker(workerId)
		}()
	}

	waitGroup.Wait()
}
