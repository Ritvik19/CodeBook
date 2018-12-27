n = int(input())
A = list(map(int, input().split()))

B = []
for i in range(n):
    x = A[i]
    for j in range(i, n):
        x = min(x, A[j])
        B.append(x)

q = int(input())
for i in range(q):
    k = int(input())
    print(B.count(k))
