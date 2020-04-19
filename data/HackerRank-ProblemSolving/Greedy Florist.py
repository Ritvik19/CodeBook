#!/bin/python3

import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    c.sort(reverse=True)
    l = len(c)
    cost = 0
    for i in range(l):
        cost += (int(i/k)+1)*c[i]
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
