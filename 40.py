'''
Champernowne's constant

Given the irrational number 0.123456789101112131415161718192021...

If d_n represents the nth digit of the fractional part, find the value of:
d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''

from functools import reduce


def champernowne_nth_digit(n):
    i, n_digits = 0, 0
    while n_digits <= n:
        i += 1
        digit_add = 9 * 10**(i-1) * i
        n_digits += digit_add

    low = n_digits - digit_add + 1
    iix = (n - low) // i
    ints = list(range(10**(i-1), 10**i))
    return int(str(ints[iix])[(n - low) % i])


def champernowne_cst_product():
    factors = [champernowne_nth_digit(10**i) for i in range(7)]
    return reduce(lambda x, y: x*y, factors)


if __name__ == '__main__':
    assert champernowne_nth_digit(12) is 1
    print(champernowne_cst_product())
