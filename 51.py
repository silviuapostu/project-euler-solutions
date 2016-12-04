'''
Prime digit replacements

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

For a family of size 8, we can employ some optimizations:
* only search for 3-repeated digits, since any other patterns will contain
numbers divisible by 3.
* test only 6 digit primes
* test numbers that have any of {0, 1, 2} as repeating digit
'''

from euler_utils import is_prime, erathos
import string


def valid_pc(x):
    xs = str(x)[::-1]
    return (x > 10**5 and
            (xs.count('0') > 2 or xs.count('1') > 2 or xs.count('2') > 2))


def prime_family():
    primes = erathos(10**6)[4:]  # remove single-digit primes
    primes_c = [p for p in primes if valid_pc(p)]
    for x in primes_c:
            family = []
            for rd in '012':
                # because of the filtering above, we can be certain that the
                # condition below will only be satisfied once
                if str(x)[::-1].count(rd) > 2:
                    family = [int(str(x).replace(rd, d)) for d in '0123456789']
                    family = [fm for fm in family if fm > 10**5]
            prime_family = [x in primes for x in family]
            if sum(prime_family) >= 8:
                return sorted(family)


if __name__ == '__main__':
    print(prime_family()[0])
