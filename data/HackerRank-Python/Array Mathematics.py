import numpy as np
n, m = map(int, input().split())
A = []
for i in range(n):
    A += list(map(int, input().split()))
B = []
for i in range(n):
    B += list(map(int, input().split()))
A = np.array(A).reshape((n,m))
B = np.array(B).reshape((n,m))
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
