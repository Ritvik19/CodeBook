import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    birdcount = dict()
    for a in arr:
        if a not in birdcount.keys():
            birdcount[a] = 0
        birdcount[a] += 1
    return list(sorted(sorted(birdcount.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True))[0][0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
