'''
Spiral primes
----
Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed. It is interesting to note that the odd
squares lie along the bottom right diagonal, but what is more interesting is
that 8 out of the 13 numbers lying along both diagonals are prime; that is, a
ratio of 8/13 ≈ 62%. If one complete new layer is wrapped around the spiral
above, a square spiral with side length 9 will be formed. If this process is
continued, what is the side length of the square spiral for which the ratio of
primes along both diagonals first falls below 10%?

Note: the values of the diagonal elements are specified in problem 28, they are
just reversed due to the anticlockwise spiral formation. The bottom right
element need never be tested for primality because it's a square.
The execution time is quite long, it can be shortened by adopting a more
efficient primality test.
'''

from euler_utils import is_prime

if __name__ == '__main__':
    n_primes, k = 3, 1
    while n_primes / (4*k+1) > 0.1:
        k += 1
        prev_max = (k*2-1)**2
        diag_elements = (prev_max+2*k, prev_max+4*k, prev_max+6*k)
        n_primes += sum([1 for i in diag_elements if is_prime(i)])
    print("Spiral side length: " + str(2*k+1))
