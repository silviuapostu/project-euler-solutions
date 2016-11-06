from math import sqrt


def ndivisors(x):
    divisors = 1
    count = 0
    while x % 2 == 0:
        count += 1
        x = x/2
    divisors = divisors * (count + 1)
    p = 3
    while x != 1:
        count = 0
        while x % p == 0:
            count += 1
            x = x/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


# def ndivisors(x):
#     n = 0
#     for i in range(1, int(sqrt(x))+1):
#         if x % i == 0:
#             n += 2
#         if i*i == x:
#             n -= 1
#     return n


def triangle_divisors(k):
    i = 1
    aux = {}
    while (True):
        if i % 2 == 0:
            aux.setdefault(i//2, ndivisors(i//2))
            aux.setdefault(i+1, ndivisors(i+1))
            n = aux.get(i//2) * aux.get(i+1)
        else:
            aux.setdefault(i, ndivisors(i))
            aux.setdefault((i+1)//2, ndivisors((i+1)//2))
            n = aux.get(i) * aux.get((i+1)//2)
        if n > k:
            return (i * (i+1) // 2)
        i += 1
