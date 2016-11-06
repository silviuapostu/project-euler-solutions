def lattice_route(k):
    L = [1] * k
    for i in range(k):
        for j in range(i):
            L[j] = L[j] + L[j-1]
        L[i] = 2 * L[i - 1]
    return L[k - 1]
