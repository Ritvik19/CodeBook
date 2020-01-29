#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    differences = []
    for i in range(1, len(s)):
        differences.append(abs(ord(s[i])-ord(s[i-1])))
    for a, b in zip(differences, differences[::-1]):
        if a != b:
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
