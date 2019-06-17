from math import gcd
for t in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    l = A[0]*A[1]//gcd(A[0], A[1])
    for i in range(n):
        for j in range(i+1,n):
            if A[i]*A[j]//gcd(A[i], A[j]) < l:
                l = A[i]*A[j]//gcd(A[i], A[j])
    print(l)
