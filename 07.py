from math import sqrt


def is_prime(x):
    i = 3
    while (i < sqrt(x)):
        if x % i == 0:
            return 0
        i += 1
    return 1


def nth_prime(n):
    primes = [2]
    cprime = 3
    while len(primes) < n:
        if is_prime(cprime):
            primes.append(cprime)
        cprime += 2
    return primes[-1]
