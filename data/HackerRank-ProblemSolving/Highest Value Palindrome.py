#!/bin/python3

import math
import os
import random
import re
import sys

def highestValuePalindrome(s, n, k):
    s = list(s)
    palin = list(s)
    l = 0
    r = len(s)-1
    while(l < r):
        if(s[l] != s[r]):
            palin[l] = palin[r] = max(s[l], s[r])
            k -= 1
        l += 1
        r -= 1
    if(k < 0):
        return "-1"
    l = 0
    r = len(s)-1
    while(l <= r):
        if(l == r):
            if(k > 0):
                palin[l] = '9'
        if(palin[l] < '9'):
            if(k >= 2 and palin[l] == s[l] and palin[r] == s[r]):
                k -= 2
                palin[l] = palin[r] = '9'
            elif(k >= 1 and (palin[l] != s[l] or palin[r] != s[r])):
                k -= 1
                palin[l] = palin[r] = '9'
        l += 1
        r -= 1
    return ''.join(palin)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
