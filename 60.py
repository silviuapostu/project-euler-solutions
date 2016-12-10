'''
Prime pair sets
----
Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.

(HackerRank) We can parametrize the problem in the following way:
Find the sum of all set of K-primes for which any two primes < N concatenate to
produce another prime. Print the sum in sorted order.
3 <= K <= 5
100 <= N <= 20000
'''

from itertools import product
from euler_utils import is_prime, erathos
from functools import reduce

prime_pair_sets = {}


def valid_pair_set(x, N=2*10**4):
    primes = set([i for i in erathos(N) if i > x])
    primes -= {x}
    valids = []
    x = str(x)
    for p in primes:
        if is_prime(int(str(p)+x)) and is_prime(int(x+str(p))):
            valids.append(p)
    return valids


def prime_chain(found, search_space, k=4):
    global prime_pair_sets
    if len(found) >= k:
            print(found)
            return found
    if len(search_space) == 0:
        return {}
    else:
        candidate = min(search_space)
        print("found={}, candidate = {}".format(found, candidate))
        pair_set = prime_pair_sets.setdefault(candidate, set(valid_pair_set(candidate)))
        set_intersection = search_space.intersection(pair_set)
        if len(set_intersection) > 0 or len(search_space) == 1:
            res = prime_chain(found.union({candidate}), set_intersection, k)
            if res != {}:
                return res
            else:
                return prime_chain(found, search_space - {candidate}, k)
        else:
            return prime_chain(found, search_space - {candidate}, k)


if __name__ == '__main__':
    N = 2*10**4
    k = 5
    primes = set(erathos(N))
    print(prime_chain(set(), primes, k))
