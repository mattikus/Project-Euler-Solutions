#!/usr/bin/env python

from math import sqrt

def isabund(x):
  return (sum(y+(x/y) for y in xrange(2, int(sqrt(x))+1) if not x%y)+1 > x)

nums = set(range(1, 28123))
abund = [x for x in xrange(12, 28123) if isabund(x)]
sums = set(x + y for pos, x in enumerate(abund) for y in abund[pos:])
print 'Problem 23 Answer:', sum(nums - sums)
