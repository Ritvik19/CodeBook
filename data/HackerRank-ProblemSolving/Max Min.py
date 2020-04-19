#!/bin/python3

import math
import os
import random
import re
import sys

def maxMin(k, arr):
    arr.sort()
    return min([abs(arr[i+k-1]-arr[i]) for i in range(n-k+1)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
