for t in range(int(input())):
    n = int(input())
    W = [int(w) for w in input().split()]
    min = n
    for i in range(n):
        if min-i < W[i]:
            min = W[i] + i
    print(min)
