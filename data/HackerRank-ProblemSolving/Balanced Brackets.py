#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    stack = []
    for c in s:
        print(stack)
        if c in ['(', '{', '[']:
            stack.append(c)
        if c in [')', '}', ']']:
            if len(stack) == 0:
                return "NO"
            elif (stack[-1], c) in [('(', ')'), ('{','}'), ('[',']')]:
                stack.pop(-1)
            else:
                return "NO"
    return "YES" if len(stack) == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
