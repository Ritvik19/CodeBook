#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        for j in b:
            count += b[j]*(b[j]-1)/2
    return int(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
