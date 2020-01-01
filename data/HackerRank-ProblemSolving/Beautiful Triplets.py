#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.


def beautifulTriplets(d, arr):
    gc = 0
    n = len(arr)
    for i in range(n):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc += 1
    return gc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
