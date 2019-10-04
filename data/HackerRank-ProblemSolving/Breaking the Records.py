#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best  = scores[0]
    worst = scores[0]
    beat_b = 0
    beat_w = 0
    for s in scores:
        if s > best:
            best = s
            beat_b += 1
        if s < worst:
            worst  = s
            beat_w += 1
    return beat_b, beat_w

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
