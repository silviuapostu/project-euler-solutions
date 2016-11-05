def fib_list_sum(limit=1000):
    fib = [1, 1]
    sum = 0
    while(fib[-1] < limit):
        fib.append(fib[-1] + fib[-2])
        if (fib[-1] < limit and fib[-1] % 2 == 0):
            sum += fib[-1]
    return sum, fib


# def fib_list_sum_reduce(limit=1000):
#     fib = [1, 1]
#     while (fib[-1] < limit):
#         fib.append(fib[-1] + fib[-2])
#     sum = fib.filter(lambda x: x%2==0).reduce(lambda x,y: x+y)
#     return sum

x,y = fib_list_sum(limit=4000000)
print(x)
