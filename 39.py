'''
Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Approach: if a+b+c=p and a**2 + b**2 = c**2, then we can determine that:
2*(c*p + a*b) = p**2 => a*b = p*(p/2 - c). Using another factorization,
b = (p**2 - 2*p*a)/(2*p-2*a). We can thus conclude that:

* p is an even integer
* p divides the area of the triangle a*b
* a<b and a<c and without loss of generality a<=b => a < p/3
'''


def int_right_triangles(p=1000):
    p_vals = [i*2 for i in range(1, p//2+1)]
    max_triples = []
    max_p = 0
    for p in p_vals:
        triples = []
        for a in range(1, p//3+1):
            b = p * (p - 2*a) / 2 / (p - a)
            if a*b % p == 0:
                triples.append((a, b, p-a-b))
        if len(triples) > len(max_triples):
            max_triples = triples
            max_p = p

    return max_p


if __name__ == '__main__':
    assert int_right_triangles(120) is 120
    print(int_right_triangles())
