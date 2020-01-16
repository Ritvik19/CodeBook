#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.


def countSort(arr):
    n = len(arr)
    ar = []
    for i in range(n):
        numX, striX = arr[i]
        if i < n//2:
            ar.append((int(numX), '-'))
        else:
            ar.append((int(numX), striX))

    ar.sort(key=lambda tup: tup[0])
    print(*[x[1] for x in ar])


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
