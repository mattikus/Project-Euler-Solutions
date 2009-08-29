#include <stdbool.h>
#include <string.h>
#include <stdio.h>

bool check_palin(int input)
{
  int len;
  char *begin, *end;
  char palin[20];

  sprintf(palin, "%d", input); //wish i had itoa in c99
  len = strlen(palin) - 1;
  begin = &palin[0];
  end = &palin[len];

  for (; len >= 0; --len) {
    if ( *begin++ != *end--) {
      return false;
    }
  }

  return true;
}

int main()
{
  int tmp = 0;
  int answer = 0;

  for (int x = 100; x < 1000; x++) {
    for (int y = 999; y > 99; y--) {
      tmp = x * y;
      if (check_palin(tmp) == true) {
        if (tmp > answer)
          answer = tmp;
      }
    }
  }

  printf("Problem 3 Answer: %d\n", answer);
  return 0;
}
