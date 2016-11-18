# Double-based palindromes
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.


def sum_double_based_palindromes(limit=10**6):
    return sum([x for x in range(limit)
                if str(x) == str(x)[::-1] and bin(x)[2:] == bin(x)[::-1][:-2]])

if __name__ == '__main__':
    print(sum_double_based_palindromes())
