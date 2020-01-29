#!/bin/python3

import math
import os
import random
import re
import sys

def isModifiedKaprekar(n):
    d = len(str(n))
    s = str(n*n)
    r = int(s[-d:])
    try:
        l = int(s[:-d])
    except:
        l = 0
    return r+l == n

def kaprekarNumbers(p, q):
    knum = []
    for i in range(p, q+1):
        if isModifiedKaprekar(i):
            knum.append(i)
    print(*knum) if len(knum) > 0 else print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
