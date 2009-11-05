import calendar
print 'Problem 19 Answer:',
print sum(1 for x in xrange(1901, 2001) for y in xrange(1, 13)
          if calendar.weekday(x, y, 1) == calendar.SUNDAY)
