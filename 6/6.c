#include <stdio.h>
#include <math.h>


int main(void) {
  
  long sum_squares = 0;
  for (int x=1; x<101; x++) {
    sum_squares += powl(x, 2); 
  }
  long squared_sums = 0;
  for (int x=1; x<101; x++) {
    squared_sums += x;
  }
  squared_sums = powl(squared_sums, 2);

  printf("Problem 6 Answer: %ld\n", squared_sums - sum_squares);
}
