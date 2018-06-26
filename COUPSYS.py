for t in range(int(input())):
    n = int(input())
    discount = [0, 0, 0]
    city = [0, 0, 0]
    for i in range(n):
        c, l, x = map(int, input().split())
        if x > discount[l-1] or (x == discount[l-1] and c < city[l-1]):
            discount[l-1] = x
            city[l-1] = c
    for i in range(3):
        print(discount[i], city[i])
