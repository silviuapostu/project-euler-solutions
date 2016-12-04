'''
Permuted multiples: find the smallest positive integer, x, such that
2x, 3x, 4x, 5x, and 6x, contain the same digits
'''


def min_pm():
    i = 0
    while True:
        i += 1
        multiples = [i*f for f in range(2, 7)]
        eq_digits = [sorted(str(m)) == sorted(str(i)) for m in multiples]
        if False not in eq_digits:
            return i


if __name__ == '__main__':
    print(min_pm())
