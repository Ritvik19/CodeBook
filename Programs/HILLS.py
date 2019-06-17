for t in range(int(input())):
    n, u, d = map(int, input().split())
    hills  = [int(e) for e in input().split()]
    para = 0
    i = 0
    while i<n-1:
        diff = hills[i+1] - hills[i]
        if diff not in range(-d, u+1):
            if diff < -d and para == 0:
                para = 1
            elif diff < -d and para == 1:
                break
            if diff > u:
                break
        i += 1
    print(i+1)
