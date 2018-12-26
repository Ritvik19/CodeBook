for t in range(int(input())):
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    S = list(sorted(S, reverse=True))
    # print(S)
    cutoff = S[k-1]
    count = 0
    for s in S:
        if s >= cutoff:
            count += 1
    print(count)
