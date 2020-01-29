#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSums(arr):
    s = sum(arr)
    count = 0
    for i in range(len(arr)):
        if 2*count == s-arr[i]:
            return "YES"
        count += arr[i]
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
