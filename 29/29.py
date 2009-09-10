#!/usr/bin/env python

print 'Problem 29 Answer:',
print len(set(a**b for a in xrange(2, 101) for b in xrange(2, 101)))
