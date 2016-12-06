'''
Square root convergents
---
It is possible to show that the square root of two can be expressed as an
infinite continued fraction. In the first one-thousand expansions, how many
fractions contain a numerator with more digits than denominator?

We can derive recursive expressions for the numerators and the denominators
of the fractions representing the expansion terms:
n[k] = 2*n[k-1] + n[k-2], with n[0] = 1 and n[1] = 1
d[k] = 2*d[k-1] + d[k-2], with d[0] = 0 and d[1] = 1
'''

from fractions import Fraction

if __name__ == '__main__':
    n, d, fs = [1, 1], [0, 1], []
    while len(fs) < 1000:
        n.append(2*n[-1]+n[-2])
        d.append(2*d[-1]+d[-2])
        fs.append(Fraction(n[-1], d[-1]))
    print(sum([len(str(f.numerator)) > len(str(f.denominator)) for f in fs]))
