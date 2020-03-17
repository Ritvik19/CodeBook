#!/bin/python3

import os
import sys

from math import factorial


def solve(n, m):
    return (factorial(n+m-1)//(factorial(n)*factorial(m-1))) % 1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
