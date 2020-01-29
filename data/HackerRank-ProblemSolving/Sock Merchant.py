#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    counts = dict()
    for a in ar:
        if a not in counts.keys():
            counts[a] = 0
        counts[a] += 1
    pairs = 0
    for k, v in counts.items():
        pairs += v//2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
