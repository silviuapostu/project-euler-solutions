# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

from math import sqrt, floor


def is_prime(x):
    i = 2
    while i < int(floor(sqrt(x)))+1:
        if x % i == 0:
            return False
        i += 1
    return True


def multiplicative_order(a, n):
    k = 2
    while (a**k % n != 1):
        k += 1
    return k


def len_repetend(x):
    return multiplicative_order(10, x)


def max_recurring_cycle(limit=1000):
    '''
    We search for the order of 10 modulo x for all primes
    between 7 and the provided limit. See Wikipedia page for
    mathematical explanation
    https://en.wikipedia.org/wiki/Repeating_decimal
    '''
    max_order, max_order_x = 7, 0
    for x in range(7, limit):
        if is_prime(x):
            x_repetend = len_repetend(x)
            if x_repetend >= max_order:
                max_order, max_order_x = x_repetend, x
    return max_order_x

if __name__ == "__main__":
    print(max_recurring_cycle())
