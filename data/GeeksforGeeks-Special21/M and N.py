for t in range(int(input())):
    m, n = map(int, input().split())
    print(n) if len(str(m+n)) == len(str(n)) else print(m+n)