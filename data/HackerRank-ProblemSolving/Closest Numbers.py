#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.


def closestNumbers(arr):
    arr.sort()
    smallest = sys.maxsize
    pairs = []
    for i in range(1, len(arr)):
        diff = abs(arr[i-1] - arr[i])
        if diff < smallest:
            smallest = diff
            pairs = []
            pairs.append(arr[i-1])
            pairs.append(arr[i])
        elif diff == smallest:
            pairs.append(arr[i-1])
            pairs.append(arr[i])
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
