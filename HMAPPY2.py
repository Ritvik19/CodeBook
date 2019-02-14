from math import gcd
for t in range(int(input())):
    n, a, b, k = map(int, input().split())
    na, nb, nab = n//a, n//b, (n*gcd(a, b))//(a*b)
    print('Win') if na + nb - 2*nab >= k else print('Lose')
