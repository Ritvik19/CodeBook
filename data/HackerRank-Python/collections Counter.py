from collections import Counter

x = int(input())
X = map(int, input().split())
X = dict(Counter(X))
n = int(input())
money = 0
for i in range(n):
    a, b = map(int, input().split())
    if a in X.keys() and X[a] > 0:
        X[a] -= 1
        money += b
print(money)
