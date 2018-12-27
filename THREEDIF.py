for t in range(int(input())):
    n1, n2, n3 = sorted(map(int, input().split()))
    print((n1 * (n2-1) * (n3-2))%1000000007)
