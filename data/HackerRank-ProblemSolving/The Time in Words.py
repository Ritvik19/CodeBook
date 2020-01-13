#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
ones = "one two three four five six seven eight nine".split(" ")

def num_to_word(x):
    if x<10:
        return ones[x-1]
    if x==10:
        return "ten"
    if x<20:
        return "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")[x-11]
    ten = x//10
    one = x%10
    tens = "twenty thirty forty fifty".split(' ')
    if one == 0:
        return tens[ten-2]
    else:
        return tens[ten-2]+' '+ones[one-1]

def timeInWords(h, m):
    if m > 30:
        if m == 59:
            return f"one minute to {num_to_word(h+1 if h!=12 else 1)}"
        elif m == 45:
            return f"quarter to {num_to_word(h+1 if h!=12 else 1)}"
        else:
            return f"{num_to_word(60-m)} minutes to {num_to_word(h+1 if h!=12 else 1)}"
    else:
        if m == 0:
            return f"{num_to_word(h)} o' clock"
        elif m == 1:
            return f"one minute past {num_to_word(h)}"
        elif m==15:
            return f"quarter past {num_to_word(h)}"
        elif m==30:
            return f"half past {num_to_word(h)}"
        else:
            return f"{num_to_word(m)} minutes past {num_to_word(h)}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
