# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.

# Note: we shouldn't look further than 9! * 7, numbers with 8 digits and more
# can't produce a large enough digit factorial sum even if all digits are 9
# through further inspection, we reduce the upper boundary even more to 1999999

from math import factorial


def equals_digit_factorial_sum(n):
    digits = map(int, list(str(n)))
    return n == sum(map(factorial, digits))


def digit_factorial_sums():
    sums = [i for i in range(3, 2*10**6)
            if equals_digit_factorial_sum(i)]
    return sum(sums)


if __name__ == '__main__':
    assert equals_digit_factorial_sum(145)
    print(digit_factorial_sums())
