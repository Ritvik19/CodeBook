for t in range(int(input())):
    x, y, z = map(int, input().split())
    if (x + y + z == 0) or (x + y == z) or (y + z == x) or (z + x == y):
        print('yes')
    else:
        print('no')
