for t in range(int(input())):
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    priceloss = sum([p-k for p in P if p>k])
    print(priceloss)