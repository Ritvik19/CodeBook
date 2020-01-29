#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    count = 0
    topography = 0
    for _ in s:
        if _ == 'D':
            topography -= 1
        else:
            topography += 1
            if topography == 0:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
