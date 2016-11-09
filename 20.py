from math import factorial


def factorial_digit_sum(n):
    n_fact = factorial(n)
    digits = list(str(n_fact))
    digits = map(int, digits)
    return sum(digits)
