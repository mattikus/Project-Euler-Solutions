#!/usr/bin/env python

def pts(name): return sum(ord(l) - 64 for l in name)
names = sorted(open('names.txt').readline().replace('"','').split(','))
print 'Problem 22 Answer: ',
print sum(x * pts(names[x-1]) for x in xrange(1,len(names)+1))
