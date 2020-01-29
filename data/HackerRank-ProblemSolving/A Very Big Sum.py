import os
import sys

def aVeryBigSum(n, ar):
    sum = 0
    for a in ar:
        sum += a
    return sum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
