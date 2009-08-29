answer = 0
x = 0
y = 1

while True:
  if y >= 4000000: break
  x, y = y, y+x
  if (y % 2 == 0): answer += y

print 'Problem 2 Answer:', answer
