from collections import defaultdict
n, m = map(int, input().split())
l1 = []
for i in range(n):
    l1.append(input())
l2 = []
for i in range(m):
    l2.append(input())
d = defaultdict(list)
for i in range(n):
    d[l1[i]].append(i+1)
for i in range(m):
    if l2[i] in d.keys():
        print(*d[l2[i]])
    else:
        print(-1)
