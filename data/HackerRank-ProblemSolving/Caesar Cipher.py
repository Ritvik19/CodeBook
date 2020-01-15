#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.


def caesarCipher(s, k):
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            s = s[:i] + chr(((ord(s[i])-97+k) % 26)+97) + s[i+1:]
        elif 65 <= ord(s[i]) <= 90:
            s = s[:i] + chr(((ord(s[i])-65+k) % 26)+65) + s[i+1:]
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
