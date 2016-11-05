def pal(x1, x2, x3):
    return x1 * 100001 + x2 * 10010 + x3 * 1100


def is_pal(n):
    return str(n) == str(n)[::-1]


def lpal():
    for x1 in range(9, 0, -1):
        for x2 in range(9, -1, -1):
            for x3 in range(9, -1, -1):
                n = pal(x1, x2, x3)
                print('testing ' + str(n))
                for x in range(999, 0, -1):
                    if (n % x == 0 and n/x < 1000):
                        print('we found %i as the product of %i and %i' %
                              (n, x, n / x))
                        return n
