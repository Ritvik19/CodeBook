for i in range(int(input())):
    N = int(input())
    P = list(map(int,input().split()))
    P.sort(reverse=True)
    profit = 0
    for i in range(N):
        profit += max(0, P[i]-i)
    print(profit%(10**9+7))   