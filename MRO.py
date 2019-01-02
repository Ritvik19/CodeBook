mod = 1000000007
dp = [1,1,3]
for i in range(1, 100000):
    dp.append((dp[-1]*(pow(2,(i+2),mod)-1)%mod)%mod)
for t in range(int(input())):
    n = int(input())
    print(dp[n-1])
