'''
Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''


from euler_utils import erathos
from itertools import permutations, combinations


def prime_perms_seq():
    primes = set([p for p in erathos(10000) if p > 1000])
    pgroups = []
    for p in primes:
        pperms = [int(''.join(pp)) for pp in list(permutations(str(p)))]
        pperms = set(pperms).intersection(primes)
        if len(pperms) > 2:
            pgroups.append(pperms)
            primes = [p for p in primes if p not in pperms]
    ppseq = []
    for pg in pgroups:
        combs = combinations(sorted(list(pg)), 3)
        seq = [c for c in combs if c[2]-c[1] == c[1]-c[0]]
        if len(seq) > 0:
            ppseq.extend(seq)
    return ppseq

if __name__ == '__main__':
    assert (1487, 4817, 8147) in prime_perms_seq()
    print(prime_perms_seq())
