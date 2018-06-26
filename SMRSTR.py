from functools import reduce
for t in range(int(input())):
    n, q = map(int, input().split())
    D = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]
    d = reduce(lambda  x, y: x*y, D)
    op = []
    for i in range(q):
            X[i] //= d
    print(*X)
