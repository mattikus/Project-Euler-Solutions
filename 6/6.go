package main

import "fmt"

func main() {
	sum_squares := 1
	for i := 2; i < 101; i++ {
		sum_squares += i * i
	}

	square_sums := 0
	for i := 1; i < 101; i++ {
		square_sums += i
	}
	square_sums *= square_sums

	fmt.Println("Problem 6 Answer:", square_sums-sum_squares)
}
