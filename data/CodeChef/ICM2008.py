for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == b:
        print('YES')
    elif c == d :
        print('NO')
    else:
        print('YES') if abs(a-b) % abs(c-d) == 0 else print('NO')