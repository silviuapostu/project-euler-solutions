'''
A collection of utility methods for common operations in Project Euler problems
'''

from math import sqrt, floor


def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i < int(floor(sqrt(x)))+1:
        if x % i == 0:
            return False
        i += 1
    return True


def erathos(n):
    '''
    Create an Erathostenes sieve for prime numbers up to n
    '''
    l = list(range(n))
    l[1] = 0
    sqrt = int(round(n**0.5))
    for i in range(2, sqrt + 1):
        if l[i]:
            l[i * i: n: i] = [0] * len(range(i * i, n, i))
    return list(filter(None, l))


def is_pandigital(x):
    if x < 0 or x >= 10**9:
        return False
    digits = list(str(x))
    return ''.join(sorted(digits)) == '123456789'[:len(digits)]
