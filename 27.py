# Quadratic primes
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive valuesof n,
# starting with n=0.

from math import sqrt, floor


def is_prime(x):
    i = 2
    while i < int(floor(sqrt(x)))+1:
        if x % i == 0:
            return False
        i += 1
    return True


def n_polynom_primes(a, b):
    i, n = 0, 0
    while True:
        prime_c = i**2 + a*i + b
        if prime_c > 0 and is_prime(prime_c):
            i += 1
            n += 1
        else:
            return n


def max_quadratic_expr_coeff_brutef(coeff_limit=1000):
    q_primes = {}
    for a in range(-coeff_limit+1, coeff_limit):
        for b in range(-coeff_limit, coeff_limit+1):
            q_primes[(a, b)] = n_polynom_primes(a, b)
    (a, b) = max(q_primes, key=q_primes.get)
    return a*b


def max_quadratic_expr_coeff():
    # http://mathworld.wolfram.com/Prime-GeneratingPolynomial.html
    # n^2-79n+1601 = (n-40)^2 + n-40 + 41
    # generically: (n-p)^2+(n-p)+41 = n^2-(2p-1)n+p^2-p+41
    p = 31      # could probably generalize this to solution of quadratic eq
    a = -(2*p-1)
    b = p**2-p+41
    return a*b

if __name__ == "__main__":
    # print(max_quadratic_expr_coeff_brutef())
    print(max_quadratic_expr_coeff())
