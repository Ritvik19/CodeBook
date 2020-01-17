#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.


def gameOfThrones(s):
    s = Counter(s).values()
    odds = 0
    for c in s:
        if c % 2 != 0:
            odds += 1
        if odds > 1:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
