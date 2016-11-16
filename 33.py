# Digit cancelling fractions

from fractions import Fraction
from functools import reduce
from operator import mul


def ordered_diff(a, b):
    # set difference is easier, but doesn't maintain order
    not_in_b = [x for x in a if x not in b]
    not_in_a = [x for x in b if x not in a]
    return not_in_b + not_in_a


def digit_cancelling_fractions():
    fractions = []
    trivials = [
        i * 10 + i for i in range(2, 10)] + [i * 10 for i in range(2, 10)]
    numerator_range = list(set(range(12, 99)) - set(trivials))

    for n in numerator_range:
        n_digits = [n // 10, n % 10]
        denominator_range = list(set(range(n+1, 99)) - set(trivials))
        d_candidates = [i for i in denominator_range
                        if (i // 10 in n_digits) ^ (i % 10 in n_digits)]
        for d in d_candidates:
            if str(d)[::-1] == str(n):
                break
            d_digits = [d // 10, d % 10]
            simple_f = Fraction(*ordered_diff(n_digits, d_digits))
            if Fraction(n, d) == simple_f:
                fractions.append(simple_f)

    f_mul = reduce(mul, fractions)
    return f_mul.denominator


if __name__ == '__main__':
    print(digit_cancelling_fractions())
