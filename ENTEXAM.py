from functools import reduce
for t in range(int(input())):
    n, k, e, m = map(int, input().split())
    marks = []
    for i in range(n):
        marks.append([int(e) for e in input().split()])
    total = []
    for i in range(n-1):
        total.append(reduce(lambda x, y: x+y, marks[i]))
    total = list(reversed(sorted(total)))
    sergey = reduce(lambda x, y: x+y, marks[-1])
    diff = total[k-1] - sergey + 1
    if diff <= 0:
        print(0)
    elif 0 < diff <= m:
        print(diff)
    elif diff > m:
        print("Impossible")
