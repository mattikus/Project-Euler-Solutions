package main

import "fmt"

func main() {
	x := 0
	y := 1
	answer := 0

	for y < 4000000 {
		y, x = y+x, y
		if y%2 == 0 {
			answer += y
		}
	}
	fmt.Println("Problem 2 Answer: ", answer)
}
