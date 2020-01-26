#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.


def isValid(s):
    freq = [s.count(letter) for letter in set(s)]
    if max(freq)-min(freq) == 0:
        return 'YES'
    elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
        return 'YES'
    elif freq.count(min(freq)) == 1:
        freq.remove(min(freq))
        if max(freq)-min(freq) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
