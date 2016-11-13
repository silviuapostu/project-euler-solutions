# Number spiral diagonals

# the k-th spiral iteration adds a padding of
# k*8 elements = (2k+1)^2 - (2(k-1)+1)^2 around the current matrix.

# top-right value: max value after padding = (k*2+1)**2
# bottom-left: middle value of added padding range = k**2*4 + 1
# bottom-right, top-left = start value + 1/4 and 3/4 of added padding range
# if we sum all them up => each iteration adds k**2*16 + k*4 + 4


def diagonal_sum(n=1001):
    if n < 2 or n % 2 != 1:
        return "Need an odd number larger than 2!"
    spiral_iterations = (n-1)//2
    diag_sum = 1
    for k in range(1, spiral_iterations+1):
        diag_sum += (k**2*4 + k + 1) * 4
    return diag_sum

if __name__ == "__main__":
    print(diagonal_sum())
