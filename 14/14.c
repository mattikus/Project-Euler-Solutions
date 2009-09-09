#include <stdio.h>

long doseq(long n)
{
  int steps = 1;

  while (n > 1) {
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = (n * 3) + 1;
    }

    steps++;
  }
  return steps;
}

int main(void)
{
  long answer = 0;
  long tmp;
  long oldtmp = 0;

  for (long i=1; i < 1000000; i++) {
    tmp = doseq(i);
    if (tmp > oldtmp) {
      answer = i;
      oldtmp = tmp;
    }
  }
  printf("Problem 14 Answer: %ld\n", answer);
}
