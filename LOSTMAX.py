for i in range(int(input())):
    N = [int(e) for e in input().split()]
    size = len(N) - 1
    for n in N:
        if n == size  :
            N.remove(n)
            break
    print(max(N))
