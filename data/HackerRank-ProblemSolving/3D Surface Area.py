#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    area = 0
    neighs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for x in range(H):
        for y in range(W):
            el = A[x][y]
            area += 2
            for dx, dy in neighs:
                try:
                    if -1 in [x+dx, y+dy]:
                        raise IndexError
                    new = el - A[x+dx][y+dy]
                    if new > 0:
                        area += new
                except IndexError:
                    area += el
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
