# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.


def is_sum_of_digit_powers(x, pwr=5):
    digits = list(str(x))
    powers = [int(d)**pwr for d in digits]
    return x == sum(powers)


def digit_powers(pwr=5, n_max=254294):
    nums = [x for x in range(n_max, 1, -1) if is_sum_of_digit_powers(x, pwr)]
    return sum(nums)


if __name__ == "__main__":
    # the biggest value of the sum of digit fifth powers is 9**5 * n_digits
    # if n_digits goes beyond 6, the value of the number starts to diverge too
    # much from this max value, thus making equality impossible.
    # we can thus limit ourselves to searching up to 9**5*6 = 254294
    try:
        assert is_sum_of_digit_powers(1634, pwr=4)
        assert is_sum_of_digit_powers(8208, pwr=4)
        assert digit_powers(pwr=4, n_max=9999) == 19316
    except AssertionError:
        print('Failing tests for numbers with 4 digits')
    else:
        print(digit_powers())
