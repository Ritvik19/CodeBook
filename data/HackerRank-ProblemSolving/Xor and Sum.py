#!/bin/python3

import os
import sys

def xorAndSum(a, b):
    x=int(a,2)
    y=int(b,2)
    p=0
    for i in range(0,314160):
        p+=x^(y<<i)
    return p%((10**9)+7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
