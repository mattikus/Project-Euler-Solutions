#!/usr/bin/env python2.6

with open('data.txt') as data:
  print 'Problem 13 Answer:', str(sum(int(line[:11]) for line in data))[:10]
