for t in range(int(input())):
    n, k = map(int, input().split())
    B = list(map(int, input().split()))
    flag = 1
    w = 0
    for i in range(n):
        if B[i] > k:
            flag = 0
            break
        elif w + B[i] <= k:
            w += B[i]
        else:
            w = B[i]
            flag += 1
    if flag == 0:
        print("-1")
    else:
        print(flag)