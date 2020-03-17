#!/bin/python3

import os
import sys


def solve(a, m):
    if a == 0:
        return 'YES'
    elif pow(a, (m - 1) // 2, m) == 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        am = input().split()

        a = int(am[0])

        m = int(am[1])

        result = solve(a, m)

        fptr.write(result + '\n')

    fptr.close()
