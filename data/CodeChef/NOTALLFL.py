for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    pos = [-1]*(k+1)
    ans = 0
    for i in range(n):
        ans = max(ans, i-(pos[arr[i]] + 1))
        pos[arr[i]] = i
    for i in range(1, k+1):
        ans = max(ans, n-(pos[i] + 1))
    print(ans)        