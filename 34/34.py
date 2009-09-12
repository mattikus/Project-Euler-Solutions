#!/usr/bin/env python

from math import factorial

def facmagic(x):
  return x == sum(factorial(int(y)) for y in str(x))

print 'Problem 34 Answer:', sum(x for x in xrange(3,100000) if facmagic(x))

