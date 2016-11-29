'''
Triangular, pentagonal, and hexagonal

T_285 = P_165 = H_143 = 40755
Find the next triangle number that is also pentagonal and hexagonal.
'''

from math import sqrt


def is_valid_tph(a):
    b = (1 + sqrt(12*a**2 + 12*a + 1)) / 6
    c = (1 + sqrt(4*a**2 + 4*a + 1)) / 4
    return b == int(b) and c == int(c)


def tph_triple():
    i = 286
    while True:
        if is_valid_tph(i):
            return i*(i+1) // 2
        i += 1


if __name__ == '__main__':
    assert is_valid_tph(285)
    print(tph_triple())
