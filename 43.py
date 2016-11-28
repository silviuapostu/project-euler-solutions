'''
Sub-string divisibility

Approach: We compute the lists of possible pandigital sub-strings. They must
have distinct digits.
'''

from math import floor
from functools import reduce


def pad_zero(x):
    return str(x) if x > 99 else '0' + str(x)


def pad_missing_digit(x):
    digits = list('0123456789')
    d = [d for d in digits if d not in list(x)][0]
    return d+x


def dist_d(s):
    digits = list(s)
    return len(digits) == len(set(digits))


def merge_pand_substr(l1, l2):
    l12 = [x+y[-1:] for x in l1 for y in l2 if
           x[-2:] == y[:2] and dist_d(x+y[-1:])]
    return l12


def special_pandigitals():
    primes = [2, 3, 5, 7, 11, 13, 17]
    sub_str = []
    for p in primes:
        s = [pad_zero(p*i) for i in range(1, floor(1000/p)+1) if
             p*i > 9 and dist_d(str(p*i))]
        sub_str.append(s)

    specials = reduce(merge_pand_substr, sub_str)
    return [int(pad_missing_digit(s)) for s in specials]


if __name__ == '__main__':
    l = special_pandigitals()
    assert (1406357289 in l)
    print(sum(l))
