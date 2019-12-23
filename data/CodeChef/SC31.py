from functools import reduce

def xor(A, B):
    C = ''
    for a, b in zip(A, B):
        C += '0' if a == b else '1'
    return C

for t in range(int(input())):
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())
    print(reduce(xor, S).count('1'))