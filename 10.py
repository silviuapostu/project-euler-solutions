def erathos(n):
    '''
    Create an Erathostenes sieve for prime numbers
    '''
    l = list(range(n))
    l[1] = 0
    sqrt = int(round(n**0.5))
    for i in range(2, sqrt+1):
        if l[i]:
            l[i*i: n: i] = [0] * len(range(i*i, n, i))
    return filter(None, l)


def sum_primes(n):
    return sum(erathos(n))
