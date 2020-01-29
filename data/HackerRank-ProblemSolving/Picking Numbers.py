#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    dic = {}
    for v in a:
        dic[v] = dic.get(v, 0) + 1
        dic[v+1] = dic.get(v+1, 0) + 1
    return max(dic.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
