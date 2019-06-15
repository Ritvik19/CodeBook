a = [1]
for i in range(2,1000001):
    a.append((a[-1]+i+a[-1]*i)%1000000007)
for t in range(int(input())):
    n = int(input())
    print(a[n-1])
