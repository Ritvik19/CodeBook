#!/bin/python3

import os
import sys

from math import gcd
from functools import reduce


def solve(a):
    return 'YES' if reduce(gcd, a) == 1 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a_count = int(input())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
