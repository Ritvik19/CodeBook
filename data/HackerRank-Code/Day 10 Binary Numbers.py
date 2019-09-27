import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    B = bin(n)[2:]
    # print(B)
    count = 0
    counts = []
    face= B[0]
    for b in B:
        if face == '1':
            if b == '1':
                count += 1
            else:
                counts.append(count)
                count = 0
                face = '0'
        else:
            if b == '1':
                count = 1
                face = '1'
    counts.append(count)
    print(max(counts))
