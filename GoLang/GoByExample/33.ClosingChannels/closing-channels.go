// https://gobyexample.com/closing-channels
package main

import "fmt"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			jobToDo, channelStillOpen := <-jobs
			if channelStillOpen {
				fmt.Println("Received Job:", jobToDo)
			} else {
				fmt.Println("All Jobs completed")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("Sent Job: ", j)
	}

	close(jobs)
	fmt.Println("Sent All Jobs")

	<-done

	_, channelStillOpen := <-jobs // Useless check - sending jobs would fail after `close(jobs)`
	fmt.Println("Any jobs left?", channelStillOpen)

}
