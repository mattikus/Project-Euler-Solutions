def prime_gen():
    primes = []
    x = 2
    while True:
        if 0 not in [x % i for i in primes]:
            yield x
            primes.append(x)
        x += 1
