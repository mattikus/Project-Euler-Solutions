#!/usr/bin/env python
from math import sqrt

def d(x):
  return sum(i + (x / i) for i in xrange(2, int(sqrt(x)) + 1) if x % i == 0) + 1

if __name__ == "__main__":
  answer = 0
  for a in xrange(1,10000):
    b = d(a)
    answer += a if d(b) == a and a != b else 0
  print "Problem 21 Answer:", answer

