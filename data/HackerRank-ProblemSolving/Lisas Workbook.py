#!/bin/python3

import math
import os
import random
import re
import sys

def workbook(n, k, arr):
    num_special=0
    cur_page=1

    for i in range(len(arr)):
        num_probs_in_chapter=arr[i]
        num_full_pages, leftover_probs = divmod(num_probs_in_chapter, k)

        total_pages = num_full_pages + ( 1 if leftover_probs else 0 )
        problems_in_chapter=iter(range(1, arr[i]+1))

        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]    
            if cur_page in probs_on_page:
                num_special+=1
            cur_page+=1        
    return num_special    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
