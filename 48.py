'''
Self powers

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''


def self_powers_sum(n):
    self_pw = [i**i for i in range(1, n+1)]
    return sum(self_pw)


if __name__ == '__main__':
    assert self_powers_sum(10) == 10405071317
    print(str(self_powers_sum(1000))[-10:])
