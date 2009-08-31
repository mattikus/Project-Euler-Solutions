#include <stdbool.h>
#include <stdio.h>

bool isdiv(long answer)
{
  for (int x=2; x < 21; x++) {
    if (answer % x) {
      return false;
    }
  }

  return true;
}

int main()
{
  long answer = 2520;

  while (!isdiv(answer)) {
    answer += 20;
  }

  printf("Problem 5 Answer: %ld\n", answer);
  return 0;
}
