for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    c0 = A.count(0)
    c1 = A.count(2)
    print((c0 * (c0 - 1) // 2) + (c1 * (c1 - 1)) // 2)