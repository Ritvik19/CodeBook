n = int(input())
stamps = [int(e) for e in input().split()]
if sum(stamps) == n*(n+1)//2:
    print("YES")
else:
    print("NO")
