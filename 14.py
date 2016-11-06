def chain(x):
    chain = [x]
    while (x > 1):
        if x % 2 == 0:
            x //= 2
        else:
            x = 3*x+1
        chain.append(x)
    return chain


def collatz():
    max_chain = 0
    for i in range(9*10**5, 10**6, 1):
        c = chain(i)
        if len(c) > max_chain:
            max_chain = len(c)
            p = i
    return p
