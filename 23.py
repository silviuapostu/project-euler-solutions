from math import sqrt, floor
from itertools import cycle


def divisors(x):
    divisors = [1]
    for i in range(2, int(floor(sqrt(x)))+1, 1):
        if x % i == 0:
            divisors.append(i)
            if i*i != x:
                divisors.append(x//i)
    return divisors


def is_abundant(x):
    return sum(divisors(x)) > x


def p23(limit=28123):
    abundants = []
    for i in range(1, limit):
        if is_abundant(i):
            abundants.append(i)
    # count all the multiples of 12, 18, 20 and add them as composed abundants
    z = []
    for a in abundants[3:]:
        if a % 12 == 0 or a % 18 == 0 or a % 20 == 0:
            z.append(a)
    for ix, x in enumerate(set(abundants) - set(z)):
        for y in abundants[ix:]:
            if x+y <= limit and x+y in abundants:
                z.append(x)
                break
    return sum(list(set(range(1, limit+1)) - set(z)))
