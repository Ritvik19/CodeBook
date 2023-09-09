from bisect import insort
for t in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ctr = 0
    for i in range(n):
        freq = [0] * 2001
        arr, length = [], 0
        for j in range(i, n):
            insort(arr, lst[j])
            freq[lst[j]] += 1
            length += 1
            if freq[freq[arr[(k-1)//(k//length + (k%length != 0))]]]:
                ctr += 1
    print(ctr)