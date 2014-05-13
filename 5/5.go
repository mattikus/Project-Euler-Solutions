package main

import "fmt"

func isdiv(i int) bool {
	for j := 2; j < 21; j++ {
		if i%j != 0 {
			return false
		}
	}
	return true
}

func main() {
	answer := 2520
	for !isdiv(answer) {
		answer += 20
	}
	fmt.Println("Problem 5 Answer:", answer)
}
