for t in range(int(input())):
    count = 0
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    sm = sum(A)
    for a in A:
        if (2*a)+k > sm:
            count += 1
    print(count)
