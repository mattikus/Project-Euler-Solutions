#!/usr/bin/env python
import itertools

answer = [x for x in itertools.permutations(range(10))][999999]
print "Problem 24 Answer:", ''.join(str(x) for x in answer)
