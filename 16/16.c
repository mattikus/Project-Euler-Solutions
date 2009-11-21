#include <gmp.h>
#include <stdio.h>

#define MAX_SIZE 1000
#define CHAR_OFFSET 48

int main(void)
{
  char buf[MAX_SIZE];
  int len;
  int nans = 0;
  mpz_t ans;
  mpz_init_set_si(ans, 2);

  mpz_pow_ui(ans, ans, 1000);
  len = gmp_snprintf(buf, MAX_SIZE, "%Zd", ans);
  for (int i = 0; i < len; i++) { nans += buf[i] - CHAR_OFFSET; }
  printf("Problem 16 Answer: %d\n", nans);

  return 0;
}
