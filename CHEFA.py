for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    p = list(reversed(sorted(p)))
    sum = 0
    for i in range(0,n,2):
        sum += p[i]
    print(sum)
