def isdiv(num):
  for x in xrange(2,21):
    if num % x:
      return False
  return True

answer = 2520
while not isdiv(answer):
  answer += 20

print 'Problem 5 Answer:', answer
