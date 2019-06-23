for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    countp = 0
    countn = 0
    for a in A:
        if a > 0:
            countp += 1
        else:
            countn += 1
    if countn == 0:
        countn = countp
    if countp == 0:
        countp = countn
    print(max(countp, countn), min(countp, countn))
