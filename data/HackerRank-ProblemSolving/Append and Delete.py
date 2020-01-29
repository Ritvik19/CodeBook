#!/bin/python3

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    commonLength = 0
    for _s, _t in zip(s,t):
        if _s == _t:
            commonLength += 1
        else:
            break
    if len(s)+len(t)-2*commonLength > k:
        return "No"
    if (len(s)+len(t)-2*commonLength)%2==k%2:
        return "Yes"
    if (len(s)+len(t)-k)<0:
        return "Yes"
    return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
