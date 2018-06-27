from math import gcd
from functools import reduce

def gcd_list(lst):
    return reduce(gcd, lst)

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if gcd_list(A) == 1:
        print(0)
    else:
        print(-1)
