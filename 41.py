'''
What is the largest n-digit pandigital prime that exists?

Approach: we start by testing pandigitals of n=9 digits in decreasing order,
then decrease n. If we find a prime, we stop searching.
'''

from itertools import permutations
from euler_utils import is_prime


def max_pandigital_prime():
    for i in range(9, 0, -1):
        digits = [str(i) for i in range(1, i+1)]
        perms = list(permutations(digits))
        ints = [int(''.join(p)) for p in perms]
        for x in sorted(ints, reverse=True):
            if is_prime(x):
                return x


if __name__ == '__main__':
    print(max_pandigital_prime())
