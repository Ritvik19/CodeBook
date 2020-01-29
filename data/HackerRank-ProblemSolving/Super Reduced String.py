#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    res = []
    for c in s:
        if res and res[len(res)-1] == c:
            res.pop()
        else:
            res.append(c)    
    res = ''.join(res)
    return res or 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
