# partial

import bisect
for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    c = 0
    pre = [0 for k in range(2001)]
    for i in range(1, 2001):
        m = (int(k / i)) + 1
        if(k % i == 0):
            m = m - 1
        x = (int(k / m)) + 1
        if(k % m == 0):
            x = x - 1
        pre[i] = x
    for i in range(1, n + 1):
        brr = [0 for k in range(2001)]
        lis = []
        for j in range(i, n + 1):
            brr[arr[j]] = brr[arr[j]] + 1
            bisect.insort(lis, arr[j])
            size = j - i + 1
            xt = pre[size]
            y = lis[xt-1]
            f = brr[y]
            if brr[f] > 0:
                c = c + 1
    print(c)