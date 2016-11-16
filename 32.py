# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. Find the sum of all products whose multiplicand/
# multiplier/product identity can be written as a 1 through 9 pandigital.

from functools import reduce


def is_pandigital_triplet(triplet):
    triplet = map(str, triplet)
    s = reduce(lambda x, y: x+y, triplet)
    return ''.join(sorted(s)) == '123456789'


def pandigitals_sum():
    pandigitals = []

    # the only possible factor combinations are:
    # 1-digit x 4-digit numbers
    # 2-digit x 3-digit numbers

    for i in range(2, 100):
        j_start = 1234 if i < 10 else 123
        j_end = 10**4//i
        for j in range(j_start, j_end+1):
            if is_pandigital_triplet([i, j, i*j]):
                pandigitals.append(i*j)

    return sum(list(set(pandigitals)))


if __name__ == '__main__':
    assert is_pandigital_triplet([39, 186, 7254])
    print(pandigitals_sum())
