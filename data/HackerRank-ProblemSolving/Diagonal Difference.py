import os
import sys

def diagonalDifference(a):
    s1 = s2 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                s1 += a[i][j]
            if i + j == len(a)-1:
                s2 += a[i][j]
    return abs(s1-s2)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
