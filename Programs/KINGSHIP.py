for t in range(int(input())):
    n = int(input())
    P = list(map(int, input().split()))
    P = list(sorted(P))
    x = P[0]
    y = sum(P[1:])
    print(x*y)
