#!/usr/bin/env python

for x in xrange(1,998):
  for y in xrange(x+1, 999):
    for z in xrange(y+1, 1000):
      if x + y + z == 1000:
        if x ** 2 + y ** 2 == z ** 2:
          print 'Problem 9 Answer:', x * y * z
          exit()

