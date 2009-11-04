#!/usr/bin/env python

def pts(name): return sum(ord(l) - 64 for l in name)
f = open('./names.txt')
names = sorted(f.readline().replace('"','').split(','))
print 'Problem 22 Answer: ',
print sum(x * pts(names[x-1]) for x in xrange(1,len(names)+1))
