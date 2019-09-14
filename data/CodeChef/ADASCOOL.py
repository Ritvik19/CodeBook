for t in range(int(input())):
    n, m = map(int, input().split())
    print('NO' if (n*m)%2 == 1 else 'YES')
