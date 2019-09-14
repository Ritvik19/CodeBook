n, k = map(int, input().split())
mod = 1000000007
kfib = []
sum = 0
for i in range(n):
    if i < k:
        kfib.append(1)
    elif i == k:
        sum = k
        kfib.append(sum)
    else:
        sum = sum+kfib[i-1]-kfib[-k-1]
        kfib.append(sum)
print(kfib[-1]%1000000007)
