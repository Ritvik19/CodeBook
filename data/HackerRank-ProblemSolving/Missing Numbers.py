#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def missingNumbers(arr, brr):
    brr = Counter(brr)
    arr = Counter(arr)
    return sorted(brr - arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
