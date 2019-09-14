from math import gcd
for t in range(int(input())):
    n, a, k= map(int, input().split())
    T = 180*(n-2)
    d_num = 2*(T-(a*n))
    d_den = n*(n-1)
    num = a * d_den + (k - 1) * d_num
    den = d_den
    g = gcd(num, den)
    num /= g
    den /= g
    print(int(num), int(den))
