import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    for a in sorted(arr, key=lambda x: x[k]):
        print(*a)
