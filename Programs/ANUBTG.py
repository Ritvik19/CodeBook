for t in range(int(input())):
    n = int(input())
    C = [int(c) for c in input().split()]
    C = list(reversed(sorted(C)))
    m = n%4
    cost = 0
    if m >1:
        cost += C[n-m] + C[n-m+1]
    elif m == 1:
        cost += C[-1]
    for i in range(0,n-m,4):
        cost += C[i]+C[i+1]
    print(cost)
