#!/bin/python3

import math
import os
import random
import re
import sys

def encryption(s):
    key = math.ceil(len(s)**0.5)
    encryp = []
    for i in range(key):
        encryp.append(s[i::key])
    return ' '.join(encryp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
