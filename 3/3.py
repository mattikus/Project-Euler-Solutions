#!/usr/bin/env python
import math
from lib.primes import prime_gen

if __name__ == "__main__":
    num = 600851475143
    tmp = prime_gen()
    prime = tmp.next()
    bound = math.sqrt(num)
    while prime < bound:
        if num % prime == 0:
            answer = prime
            print answer
        prime = tmp.next()

    print "Problem 3 Answer:", answer
