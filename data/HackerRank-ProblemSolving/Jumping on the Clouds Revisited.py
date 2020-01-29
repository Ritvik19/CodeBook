#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    energyConsumed = 0
    i = 0
    while True:
        i = (i + k) % len(c)
        energyConsumed += 1 + 2*c[i]
        if i == 0:
            break
    return 100 - energyConsumed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
