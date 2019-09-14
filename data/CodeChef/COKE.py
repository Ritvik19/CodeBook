for t in range(int(input())):
    n, m, k, l, r = map(int, input().split())
    price = 1000000
    flag = 0
    for i in range(n):
        c, p = map(int, input().split())
        if c > k:
            if l <= max(c-m, k) <= r:
                flag = 1
                price = min(price, p)
        else:
            if l <= min(c+m, k) <=r:
                flag = 1
                price = min(price, p)
    print(price) if flag == 1 else print(-1)
