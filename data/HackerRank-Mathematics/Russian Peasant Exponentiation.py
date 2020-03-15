#!/bin/python3

import os
import sys


def solve(a, b, k, m):
    if k == 1:
        return a % m, b % m
    else:
        c, d = ((a*a) % m-(b*b) % m) % m, (2*a*b) % m
        x, y = solve(c, d, k//2, m)
        if k % 2:
            e, f = (a*x-b*y) % m, (a*y+b*x) % m
            x, y = e, f
        return x, y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        abkm = input().split()

        a = int(abkm[0])

        b = int(abkm[1])

        k = int(abkm[2])

        m = int(abkm[3])

        result = solve(a, b, k, m)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
