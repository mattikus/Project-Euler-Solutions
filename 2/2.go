package main

import "fmt"

func main() {
  var (
    x      int = 0;
    y      int = 1;
    answer int;
  )
  for y < 4000000 {
    y, x = y+x, y;
    if y % 2 == 0 {
      answer += y
    }
  }
  fmt.Println("Problem 2 Answer: ", answer);
}
