from math import gcd
from functools import reduce
for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    x = reduce(gcd, A)
    if x > 1:
        print(x)
    else:
        print(-1)
