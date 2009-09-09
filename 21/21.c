#include <stdio.h>
#include <math.h>

int d(int x)
{
  int sumdiv = 1;
  int root = (int)sqrt(x) + 1;
  for (int i = 2; i <= root; i++) {
    if (x % i == 0) {
      sumdiv += (i + (x / i));
    }
  }
  return sumdiv;
}

int main(void)
{
  int answer = 0;
  int j;
  for (int i = 1; i < 10000; i++) {
    j = d(i);
    if (d(j) == i && j != i) {
      answer += i;
    }
  }
  printf("Problem 21 Answer: %d\n", answer);
}
