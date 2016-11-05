from math import sqrt
def max_prime_factor(x, j=2):
    print("Currently: x=%s, j=%s", % (x,j))
    max_factor = sqrt(x)
    if (x % 2 == 0):
        while (x % 2 == 0):
            x = x/2
        return max_prime_factor(x, 3)
    while (j < max_factor):
        if (x % j == 0):
            return max_prime_factor(x/j, j)
        j += 2
    return j
