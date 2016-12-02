'''
Goldbach's other conjecture

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
'''

from euler_utils import is_prime
from math import sqrt, ceil


def goldbach2():
    n = 35
    while True:
        if not is_prime(n) and n % 2 == 1:
            y = 1
            found = False
            while y <= ceil(sqrt((n-1)/2)) and not found:
                x = n - 2 * y**2
                if is_prime(x):
                    found = True
                y += 1
            if not found:
                return n
        n += 1


if __name__ == '__main__':
    print(goldbach2())
