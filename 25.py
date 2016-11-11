# first Fibonacci number with n digits. Don't waste memory by storing the whole
# Fibonacci sequence, but only the last two members since we're only testing
# their sum


def n_digit_fibo(n=1000):
    last_fibs = [1, 1, 2]
    ix = 3       # index of Fibo number we're about to test
    while last_fibs[-1] / 10**(n-1) < 1:
        last_fibs[-1] = last_fibs[-2] + last_fibs[-3]
        last_fibs[-3] = last_fibs[-2]
        last_fibs[-2] = last_fibs[-1]
        ix += 1
    return ix-1
