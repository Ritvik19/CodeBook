#!/bin/python3

import math
import os
import random
import re
import sys

def camelcase(s):
    count = 1
    for _ in s:
        if 'A' <= _ <= 'Z':
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
