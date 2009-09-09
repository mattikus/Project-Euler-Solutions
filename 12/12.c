#include <stdio.h>
#include <math.h>

int numdiv(long x)
{
  int divs = 2; // 1 and x
  int root = (int)sqrt(x) + 1;
  for (int i = 2; i <= root; i++) {
    if (x % i == 0) {
      divs += 2; // i and x / i
    }
  }
  return divs;
}

int main(void)
{
  long answer = 0;

  for (long i=1; ;i++) {
    answer += i;
    if (numdiv(answer) > 500) {
      break;
    }
  }
  printf("Problem 12 Answer: %ld\n", answer);
}
