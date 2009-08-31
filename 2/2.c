#include <stdio.h>

int main()
{
  long answer = 0;
  long x = 0, y = 1;
  long tmp = 0;

  for (;;) {
    if (y >= 4000000) {
      break;
    }
    tmp = y;
    y += x;
    x = tmp;
    if (y % 2 == 0) {
      answer += y;
    }
  }

  printf("Problem 2 Answer: %ld\n", answer);
  return 0;
}
