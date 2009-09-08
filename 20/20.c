#include <stdio.h>
#include <gmp.h>
#include <string.h>

int ctoi(char x) { return x - '0'; }

int main()
{
  mpz_t n;
  char result[150];
  long answer = 0;

  mpz_init(n);
  mpz_fac_ui(n, 100);
  mpz_get_str(result, 10, n);
  for (int i = 0; i < strlen(result); i++) {
    answer += ctoi(result[i]);
  }
  printf("Problem 20 Answer: %ld\n", answer);
  return 0;
}
