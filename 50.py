'''
Consecutive prime sum

Which prime, below one-million, can be written as the sum of the
most consecutive primes?
'''

from euler_utils import erathos


def max_window_size(items, target):
    i = 0
    while sum(items[:i]) < target:
        i += 1
    return i


def max_psum(limit):
    primes = erathos(limit)[::-1]
    k = max_window_size(primes[::-1], limit)
    while k > 0:
        psums = [sum(primes[i:i+k]) for i in range(0, len(primes)-k+1)]
        psums = [ps for ps in psums if ps < limit]
        for ps in psums:
            if ps in primes:
                return ps
        k -= 1


if __name__ == '__main__':
    assert max_psum(100) == 41
    assert max_psum(1000) == 953
    print(max_psum(10**6))
