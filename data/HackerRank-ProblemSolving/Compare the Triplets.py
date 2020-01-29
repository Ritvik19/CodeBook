import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice = bob = 0
    if a0 > b0:
        alice += 1
    elif a0 < b0:
        bob += 1
    if a1 > b1:
        alice += 1
    elif a1 < b1:
        bob += 1
    if a2 > b2:
        alice += 1
    elif a2 < b2:
        bob += 1
    return(alice, bob)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
