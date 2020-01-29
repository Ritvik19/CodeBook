#!/bin/python3

import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):
    m = len(c)
    c = sorted(c)
    if (m == 1):
        return max(c[0]-0, n-1-c[0])
    else:
        gaps = []
        for i in range(1, m):
            gaps.append(c[i]-c[i-1])
        return max(c[0]-0, n-1-c[-1], max(gaps)//2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
