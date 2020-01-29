#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def twoStrings(s1, s2):
    return 'NO' if len(Counter(s1) & Counter(s2)) == 0 else 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
