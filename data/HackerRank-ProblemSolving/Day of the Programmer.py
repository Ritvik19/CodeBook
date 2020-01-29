import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year < 1918:
        if year%4 == 0:
            leap = True
        else:
            leap = False
    elif year > 1918:
        if year%400 == 0:
            leap = True
        elif year%4 == 0 and year%100 != 0:
            leap = True
        else:
            leap = False
    else:
        return '26.09.1918'
    return '12.09.'+str(year) if leap else'13.09.'+str(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
