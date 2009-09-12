#!/usr/bin/env python

def ispalin(x):
  return str(x)[::-1] == str(x) and str(bin(x))[:1:-1] == str(bin(x))[2:]

print 'Problem 36 Answer:', sum(x for x in xrange(1, 1000000) if ispalin(x))
