import os
import sys

def gradingStudents(grades):
    newgrades = []
    for g in grades:
        if g > 37:
            if g %5 > 2:
                g += 5-g%5
        newgrades.append(g)
    return newgrades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
