n, s, m = map(int, input().split())
dp = [0, s]
for i in range(2, n+1):
    dp.append((dp[i-1]*s +m - dp[(i+1)//2]) % m)
print(dp[-1])
