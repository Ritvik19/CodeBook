n, d = map(int, input().split())
L = []
for i in range(n):
    L.append(int(input()))
L = list(sorted(L))
i = 0
count = 0
while i < n-1:
    if L[i+1] - L[i] <= d:
        count += 1
        i += 1
    i += 1
print(count)
