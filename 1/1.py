#!/usr/bin/env python
print 'Problem 1 Answer: ',
print sum(x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0)
