# idea: if we maintain the first k first digits fixed (in ascending order)
# we can eliminate (10-k)! numbers that are definitely precedesors in the
# order of lexicographic permutations


from math import factorial
from itertools import cycle


def p24(limit=10**6):
    target = []
    digits = list(range(10))
    while limit > 1:
        digits_iter = iter(digits)
        q = next(digits_iter)
        while (limit > factorial(10-len(target)-1)):
            limit -= factorial(10-len(target)-1)
            q = next(digits_iter)
        digits.remove(q)
        target.append(q)
    target += digits
    return int(''.join([str(i) for i in target]))
