#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def makingAnagrams(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    union = s1 | s2
    intersection = s1 & s2
    return sum((union-intersection).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
