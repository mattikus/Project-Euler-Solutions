#include <stdio.h>

int main(void)
{
  long answer = 0;
  long x = 0, y = 1;
  long tmp = 0;

  while (y <= 4000000) {
    tmp = y;
    y += x;
    x = tmp;
    if (y % 2 == 0) {
      answer += y;
    }
  }

  printf("Problem 2 Answer: %ld\n", answer);
}
