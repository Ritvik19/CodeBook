#!/bin/python3

import os
import sys


def closestNumber(a, b, x):
    p = pow(a, b)
    mod = p % x
    return int(p + (x - (mod))) if mod > x/2 else int(p - mod)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
