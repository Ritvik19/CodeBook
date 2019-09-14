for t in range(int(input())):
    n, x, s = map(int, input().split())
    for i in range(s):
        a, b = map(int, input().split())
        if x == a or x == b:
            if x == a:
                x = b
            else:
                x = a
    print(x)
