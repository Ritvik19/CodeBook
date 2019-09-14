n, q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []
for a, b in zip(A, B):
    C.append(a*b)
for i in range(n):
    l, r = map(int, input().split())
    print(sum(C[l-1:r]))
