n, m = map(int, input().split())
mid = 2*n+1
for i in range(m):
    q = int(input())
    if n+2 <= q <= 3*n:
        print(n - abs(mid-q))
    else:
        print(0)
