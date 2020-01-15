#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.


def biggerIsGreater(s):
    for i in range(len(s)-1)[::-1]:
        if ord(s[i]) < ord(s[i+1]):
            for j in range(i+1, len(s))[::-1]:
                if ord(s[i]) < ord(s[j]):
                    lis = list(s)
                    lis[i], lis[j] = lis[j], lis[i]
                    return ("".join(lis[:i+1]+lis[i+1:][::-1]))
    return "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
