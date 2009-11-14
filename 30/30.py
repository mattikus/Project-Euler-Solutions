#!/usr/bin/env python

def sumpowers(x):
  return x if sum(int(i)**5 for i in str(x)) == x else 0

print 'Problem 30 Answer:', sum(sumpowers(x) for x in xrange(2,200000))
