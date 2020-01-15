#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.


def marsExploration(s):
    count = 0
    for i in range(len(s)):
        pos = i % 3
        if pos == 0 or pos == 2:
            if s[i] != 'S':
                count += 1
        else:
            if s[i] != 'O':
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
