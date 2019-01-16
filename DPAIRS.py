n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a = A.index(min(A))
b = B.index(max(B))
for i in range(n):
    if i != a:
        print(i, b)
for i in range(m):
    print(a, i)
