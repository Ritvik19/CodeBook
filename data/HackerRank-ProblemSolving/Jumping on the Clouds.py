#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    count = 0
    i = 0
    n = len(c)
    while i < n-1:
        if i < n-2 and c[i+2] == 0:
            i += 1
        if i != n - 1:
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
