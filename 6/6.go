package main

import (
  "fmt";
  "math";
)

func main() {
  sum_squares := 1;
  for i := 2; i < 101; i++ {
    sum_squares += int(math.Pow(float64(i), 2))
  }

  square_sums := 0;
  for i := 1; i < 101; i++ {
    square_sums += i
  }
  square_sums = int(math.Pow(float64(square_sums), 2));
  fmt.Println("Problem 6 Answer:", square_sums - sum_squares)
}
