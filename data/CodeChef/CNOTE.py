res = ["UnluckyChef", "LuckyChef"]
for t in range(int(input())):
    x, y, k, n = map(int, input().split())
    req = x-y
    flag = 0
    for i in range(n):
        p, c = map(int, input().split())
        if p >= req and c<= k:
            flag = 1
    print(res[flag])
