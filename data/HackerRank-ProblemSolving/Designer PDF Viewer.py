#!/bin/python3

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    heights = []
    for w in word:
        heights.append(h[ord(w)-97])
    return max(heights)*len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
