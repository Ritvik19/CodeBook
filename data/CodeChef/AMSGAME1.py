from functools import reduce
from math import gcd
for t in range(int(input())):
    n = int(input())
    num = [int(e) for e in input().split()]
    print(reduce(gcd, num))
