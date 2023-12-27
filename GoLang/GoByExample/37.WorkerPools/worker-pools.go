package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for jobId := range jobs {
		fmt.Println("Worker", id, "started job", jobId)
		time.Sleep(time.Second)
		fmt.Println("Worker", id, "finished job", jobId)
		results <- jobId * 2
	}
}

const NUMBER_OF_JOBS = 5

func main() {
	jobs := make(chan int, NUMBER_OF_JOBS)
	results := make(chan int, NUMBER_OF_JOBS)

	for workerId := 1; workerId <= 3; workerId++ {
		go worker(workerId, jobs, results)
	}

	for job := 1; job <= NUMBER_OF_JOBS; job++ {
		jobs <- job
	}
	close(jobs)

	for result := 1; result <= NUMBER_OF_JOBS; result++ {
		fmt.Printf("Got job result: %d\n", <-results)
	}
}
