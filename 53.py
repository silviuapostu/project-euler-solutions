'''
Combinatoric selections

How many, not necessarily distinct, values of (n take r) combinations,
for 1 ≤ n ≤ 100, are greater than one-million?
'''

from math import factorial

if __name__ == '__main__':
    count = sum([1 for i in range(23, 101) for j in range(0, i)
                if factorial(i)/factorial(j)/factorial(i-j) >= 10**6])
    print(count)
