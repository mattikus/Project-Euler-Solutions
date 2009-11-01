#!/usr/bin/env python

first = [ '', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine' ]
teens = [ 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
tens = [ '', 'ten', 'twenty', 'thirty', 'forty',
         'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
answer = 0

def lesshun(x):
    if x < 10:
        return len(first[x])
    elif x < 20:
        return len(teens[x % 10])
    elif x % 10:
        return len(tens[x / 10] + first[x % 10])
    else:
        return len(tens[x / 10])

for x in xrange(1, 1001):
    if x < 100:
        answer += lesshun(x)
    elif x < 1000:
        if x % 100:
            answer += len(first[x / 100] + 'hundredand') + lesshun(x % 100)
        else:
            answer += len(first[x / 100]) + len('hundred')
    else:
        answer += len('onethousand')

print 'Problem 17 Answer:', answer
