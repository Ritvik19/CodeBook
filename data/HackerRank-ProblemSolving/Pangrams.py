#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    t = s.lower()
    flag = 0
    test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    for i in test_list:
        if i in t or i == ' ':
            flag = 1

        else:
            flag = 0
            break

    if flag == 1:
        return('pangram')
    else:
        return('not pangram')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
