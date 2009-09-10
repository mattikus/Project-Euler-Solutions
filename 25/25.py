#!/usr/bin/env python

def fibgen():
  x, y, count = 0, 1, 1
  while True:
    yield count, x + y
    x, y, count = x + y, x, count + 1

print "Problem 25 Answer:",
for term, num in fibgen():
  if len(str(num)) >= 1000:
    print term
    exit()
