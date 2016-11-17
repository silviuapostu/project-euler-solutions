# How many circular primes are there under 1 000 000 ?

from collections import deque
from itertools import permutations


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


def cyclic_digit_perms(x):
    d = list(str(x))
    perms = [d[i:] + d[:i] for i in range(1, len(d)+1)]
    return [int(''.join(p)) for p in perms]


def n_circular_primes(limit=10**6):
    primes = erathos(limit)

    # filter out numbers with even digits or that contain the 5 digit
    primes = [i for i in primes
        if not bool(set(str(i)).intersection({'2', '4', '5', '6', '8'}))
        or len(str(i)) == 1]

    circular_primes = []
    for x in primes:
        p = cyclic_digit_perms(x)
        if p == [i for i in p if i in primes]:
            primes = [i for i in primes if i not in p]
            circular_primes += p

    return len(set(circular_primes))


if __name__ == '__main__':
    assert n_circular_primes(100) == 13
    print(n_circular_primes())
