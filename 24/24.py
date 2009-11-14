#!/usr/bin/env python
from math import factorial

def permutation(num, s):
  fac = factorial(len(s) - 1)
  for i in xrange(len(s) - 1):
    tempi = (num / fac) % (len(s) - i)
    temps = s[i + tempi]
    for j in xrange(i + tempi, i, -1):
      s[j] = s[j - 1]
    s[i] = temps
    fac /= (len(s) - (i + 1))
  return ''.join(str(x) for x in s)

print "Problem 24 Answer:", permutation(1000000, range(10))
