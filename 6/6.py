#!/usr/bin/env python

sum_of_squares = sum(x ** 2 for x in xrange(1,101))
square_of_sums = sum(x for x in xrange(1,101)) ** 2
print 'Problem 6 Answer:', square_of_sums - sum_of_squares
