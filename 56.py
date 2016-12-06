'''
Powerful digit sum
'''

if __name__ == '__main__':
    dsums = ([sum([int(d) for d in str(a**b)])
             for a in range(1, 100) for b in range(1, 100)])
    print(max(dsums))
