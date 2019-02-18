for t in range(int(input())):
    n, b = map(int, input().split())
    armax = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        if p <= b:
            armax = max(armax, w*h)
    print(armax) if armax > 0 else print('no tablet')
