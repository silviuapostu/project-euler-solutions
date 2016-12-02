'''
Distinct primes factors

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
'''

from euler_utils import prime_factors


def distinct_pf_seq_start(p):
    n, i = 2, 0
    while i < p:
        n += 1
        if len(prime_factors(n)) >= p:
            i += 1
        else:
            i = 0
    return n-p+1


if __name__ == '__main__':
    assert distinct_pf_seq_start(2) == 14
    assert distinct_pf_seq_start(3) == 644
    print(distinct_pf_seq_start(4))
