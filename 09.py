from math import sqrt


def is_pyt_triple(a, b, c):
    return 1 if a**2 + b**2 == c**2 else 0


for c in range(1000//2, 0, -1):
    for a in range(c, 0, -1):
        if is_pyt_triple(a, 1000-a-c, c) and a < c:
            print(a * c * (1000-a-c))
            break
