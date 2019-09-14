for t in range(int(input())):
    n = int(input())
    A = set(map(int, input().split()))
    print('No') if len(A) == n else print('Yes')
