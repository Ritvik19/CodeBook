for t in range(int(input())):
    profit = []
    for n in range(int(input())):
        s, p, v = map(int,input().split())
        profit.append((p // (s + 1)) * v)
    print(max(profit))