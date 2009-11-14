#include <stdio.h>

int main(void)
{
  int answer = 0;

  for (int i = 1; i < 1000; i++) {
    if (!(i % 3) || !(i % 5)) {
      answer += i;
    }
  }

  printf("Problem 1 Answer: %d\n", answer);
  return 0;
}
