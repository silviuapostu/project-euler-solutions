'''
Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

Note: a truncatable prime of more than 3 digits cannot contain even digits
'''

from euler_utils import is_prime


def is_truncatable_prime(x, dir=0):
    d = list(str(x))
    truncs = []
    if dir == 0:
        truncs = [d[i:] for i in range(len(d))]
    else:
        truncs = [d[:i] for i in range(1, len(d) + 1)]
    truncs = [int(''.join(t)) for t in truncs]
    return False not in [is_prime(t) for t in truncs]


def is_t_eligible(x):
    if x < 100:
        return True
    else:
        even_digits = {'0', '2', '4', '6', '8'}
        if len(even_digits.intersection(set(str(x)))) > 0:
            return False
    return True


def sum_truncatable_primes():
    t_primes = []
    i = 22
    while len(t_primes) < 11:
        if (is_t_eligible(i) and
            is_truncatable_prime(i, dir=0) and
            is_truncatable_prime(i, dir=1)):
            t_primes.append(i)
        i += 1

    return sum(t_primes)

if __name__ == '__main__':
    print(sum_truncatable_primes())
