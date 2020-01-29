#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    l = len(s)
    if l % 2 == 1:
        return -1
    else:
        count = 0
        s1, s2 = Counter(s[:l//2]), Counter(s[l//2:])
        for char in s2:
            current = s2[char] - s1.get(char, 0)
            if current > 0:
                count += current
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
