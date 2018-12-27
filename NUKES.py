a, n, k = map(int, input().split())
dist = []
for i in range(k):
    dist.append(a%(n+1))
    a //= (n+1)
print(*dist)
