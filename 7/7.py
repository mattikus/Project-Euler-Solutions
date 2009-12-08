from lib.primes import prime_gen

prime = prime_gen()
for x in xrange(10000): prime.next()
print prime.next()
