import math
import os
import random
import re
import sys

def getTotalX(a, b):
    count = 0
    for i in range(min(a), max(b)+1):
        flag = True
        for _ in a:
            if i%_ != 0:
                flag = False
                break
        for _ in b:
            if _%i != 0:
                flag = False
                break
        count += int(flag)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
