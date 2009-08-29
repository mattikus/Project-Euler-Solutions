answer = 0
for x in xrange(1000):
  for y in xrange(1000, 99, -1):
    tmp = x * y
    if tmp > answer and str(tmp) == str(tmp)[::-1]: answer = tmp

print "Problem 3 Answer is: ", answer
