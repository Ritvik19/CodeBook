n, x = map(int, input().split())
total = [0]*n
for i in range(x):
    marks = list(map(float, input().split()))
    for j in range(n):
        total[j] += marks[j]
for i in range(n):
    total[i] /= x
for t in total:
    print(t)
