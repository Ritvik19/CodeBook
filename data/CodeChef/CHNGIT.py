from collections import Counter

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A = Counter(A)
    print(n - A.most_common(1)[0][1])