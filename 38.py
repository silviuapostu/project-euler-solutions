'''
What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2,...,n) where n > 1

Approach: we know from the given example that there's we shouldn't look beyond
n = 5 to multiply the integer with. We start to look for integers at 9 and
gradually reduce the sequence to multiply with when the concatenated products
are larger than 10**9. We stop when the sequence only contains 1

'''

from euler_utils import is_pandigital
from functools import reduce


def pandigital_multiples():
    n = 5
    pand_max = 0
    x = 9

    while n > 1:
        seq = list(range(1, n+1))
        mults = [x*i for i in seq]
        concat_int = int(reduce(lambda x, y: x+y, [str(m) for m in mults]))
        if concat_int > 10**9-1:
            n -= 1
        else:
            if is_pandigital(concat_int) and concat_int > pand_max:
                pand_max = concat_int
        x += 1

    return pand_max


if __name__ == '__main__':
    print(pandigital_multiples())
