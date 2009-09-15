#include <stdio.h>
#include <math.h>

int main(void)
{
  // Crappy simple brute force but executes in less than a third of second
  for (int a = 1; a < 997; a++) {
    for (int b = a + 1; b < 998; b++) {
      for (int c = b + 1; c < 999; c++) {
        if (a + b + c == 1000) {
          if (pow(a, 2) + pow(b, 2) == pow(c, 2)) {
            printf("Problem 9 Answer: %ld\n", a * b * c);
            return 0;
          }
        }
      }
    }
  }
}
