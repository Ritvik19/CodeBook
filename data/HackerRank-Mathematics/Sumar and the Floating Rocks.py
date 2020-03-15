#!/bin/python3

import os
import sys

from math import gcd


def solve(x1, y1, x2, y2):
    return str(gcd(y2-y1, x2-x1)-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        x1Y1X2Y2 = input().split()

        x1 = int(x1Y1X2Y2[0])

        y1 = int(x1Y1X2Y2[1])

        x2 = int(x1Y1X2Y2[2])

        y2 = int(x1Y1X2Y2[3])

        result = solve(x1, y1, x2, y2)

        fptr.write(str(result) + '\n')

    fptr.close()
