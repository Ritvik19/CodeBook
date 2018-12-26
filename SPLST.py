for t in range(int(input())):
    a, b, c, x, y = map(int, input().split())
    if (a + b + c) != (x + y) or (a + b + c) - min(a, b, c) < max(x, y):
        print('NO')
    else:
        print('YES')
