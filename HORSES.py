for t in range(int(input())):
    n = int(input())
    s = [int(e) for e in input().split()]
    s = sorted(s)
    mn = 10000000000
    for i in range(n-1):
            mn = min(mn, s[i+1]-s[i])
    print(mn)
