'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
Find the pair of pentagonal numbers, P_j and P_k, for which their sum and
difference are pentagonal and D = |P_k − P_j| is minimised. Return D
'''

from math import sqrt


def is_pentagonal(Pn):
    n = (sqrt(24*Pn + 1) + 1) / 6
    return n == int(n)


def pentagonal(n):
    return n * (3*n - 1) // 2


def min_diff_pentagonals():
    j = 1
    while True:
        j += 1
        Pj = pentagonal(j)
        for k in range(j, 0, -1):
            Pk = pentagonal(k)
            if is_pentagonal(Pj+Pk) and is_pentagonal(Pj-Pk):
                return Pj-Pk


if __name__ == '__main__':
    print(min_diff_pentagonals())
