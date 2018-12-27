from functools import reduce
from math import gcd
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    g = reduce(gcd, A)
    if g == 1:
        print(n)
    else:
        print(-1)
