for t in range(int(input())):
    n = int(input())
    perm = [int(e) for e in input().split()]
    loc = 0
    abs = 0
    for i in range(n):
        for j in range(i+1, n):
            if perm[i] > perm[j]:
                abs += 1
    for i in range(n-1):
        if perm[i] > perm[i+1]:
            loc += 1
    if loc == abs:
        print("YES")
    else:
        print("NO")
