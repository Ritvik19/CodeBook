for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    x = A.count(0)
    x += A.count(1)
    print('YES') if x + k >= n else print('NO')
