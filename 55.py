'''
Lychrel numbers
How many Lychrel numbers are there below 10000?
'''


def lychrel(x):
    i = 0
    while i < 50:
        i += 1
        x += int(str(x)[::-1])
        if str(x) == str(x)[::-1]:
            return False
    return True


if __name__ == '__main__':
    count = 0
    for i in range(1, 10000):
        if lychrel(i):
            count += 1
    print("Total Lychrel numbers below 10000: " + str(count))
