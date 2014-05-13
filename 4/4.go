package main

import (
	"fmt"
	"strconv"
)

func ispalin(x int) bool {
	s := strconv.Itoa(x)
	slen := len(s)
	for i := 0; i < (slen / 2); i++ {
		if !(s[i] == s[(slen-1)-i]) {
			return false
		}
	}
	return true
}

func main() {
	answer := 0
	for i := 100; i < 1000; i++ {
		for j := 999; j > 99; j-- {
			tmp := i * j
			if ispalin(tmp) && tmp > answer {
				answer = tmp
			}
		}
	}
	fmt.Println("Problem 4 Answer:", answer)
}
