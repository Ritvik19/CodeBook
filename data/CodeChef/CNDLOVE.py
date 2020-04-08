for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if sum(A) % 2 == 0:
        print('NO')
    else:
        print('YES')