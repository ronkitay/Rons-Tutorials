package main

import (
	"fmt"
	"sync"
)

type Container struct {
	mutex    sync.Mutex
	counters map[string]int
}

func (container *Container) inc(name string) {
	container.mutex.Lock()
	defer container.mutex.Unlock()
	container.counters[name]++
}

func main() {

	container := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var waitGroup sync.WaitGroup

	doIncrement := func(name string, n int) {
		for i := 0; i < n; i++ {
			container.inc(name)
		}
		waitGroup.Done()
	}
	waitGroup.Add(3)
	go doIncrement("a", 1000)
	go doIncrement("a", 2000)
	go doIncrement("b", 5000)

	waitGroup.Wait()
	fmt.Println(container.counters)

}
