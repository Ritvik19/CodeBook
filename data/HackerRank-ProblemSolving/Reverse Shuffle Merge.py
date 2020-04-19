#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def reverseShuffleMerge(s):
    word = []
    freqs = Counter(s)
    reqs = { k: v/2 for k, v in freqs.items()}  
    avail_skips = { k: v/2 for k, v in freqs.items()} 
    skipped = [] 
    
    for c in reversed(s):
        if reqs[c] == 0:
            continue

        if avail_skips[c] > 0:
            avail_skips[c] -= 1
            skipped.append(c) 

        elif len(skipped) == 0:
            word.append(c)
            
        else:
            i = 0
            skipped.append(c)
            avail_skips[c] -= 1
            min_c = chr(ord('a') - 1)

            while i < len(skipped):
                i = index_of(skipped, find_min_bounded(skipped, i, min_c), i)
                sc = skipped[i]

                if reqs[sc] == 0:
                    min_c = sc
                    continue

                word.append(sc)
                reqs[sc] -= 1
                avail_skips[sc] += 1
                i += 1

                if sc == c:
                    break                

            skipped = skipped[i:]

    return ''.join(word)


def find_min_bounded(arr, start, min_c):
    m = 'z'
    for i in range(start, len(arr)):
        if arr[i] < m and arr[i] > min_c:
            m = arr[i]
    return m


def index_of(arr, v, start):
    for i in range(start, len(arr)):
        if arr[i] == v:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()