for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    ans = 0
    for a, b in zip(A, B):
        ans += min(a, b)
    print(ans)