from math import sqrt, floor


def divisors(x):
    divisors = [1]
    for i in range(2, int(floor(sqrt(x)))+1, 1):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x/i)
    return divisors


def amicable(x):
    y = sum(divisors(x))
    return sum(divisors(y)) == x and y != x


def p21(limit=10000):
    amicables = [x for x in range(limit) if amicable(x)]
    return sum(amicables)
