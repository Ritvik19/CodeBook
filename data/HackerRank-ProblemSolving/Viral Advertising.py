#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    m = [2]
    for i in range(n-1):
        m.append(int(3*m[i]/2))
    return sum(m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
