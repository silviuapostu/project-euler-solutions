'''
Coded triangle numbers

Approach: we calculate the score of every word. If max_score is the maximum
of these scores, then we generate a sequence of triangle numbers up to the
ceiling of n = (sqrt(1+8*max_score) - 1) / 2
'''

from math import sqrt, ceil


def score(s):
    scores = [ord(c) - ord('A') + 1 for c in list(s)]
    return sum(scores)


def n_triangle_words():
    words = open('p042_words.txt').read().split(',')
    w_scores = [score(w[1:-1]) for w in words]
    n_max = ceil((sqrt(1 + 8*max(w_scores)) - 1) / 2)
    triangles = [n * (n+1) // 2 for n in range(1, n_max+1)]
    return sum([True for ws in w_scores if ws in triangles])


if __name__ == '__main__':
    assert score('SKY') is 55
    print(n_triangle_words())
