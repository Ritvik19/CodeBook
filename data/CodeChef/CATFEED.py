for t in range(int(input())):
    n, m = map(int, input().split())
    cnt = [0]*n
    flag = 0
    M = list(map(int, input().split()))
    for x in M:
        ch = 0
        for i in range(1, n+1):
            if i != x:
                ch |= (cnt[x-1] > cnt[i-1])
        flag |= ch
        cnt[x-1] += 1

    print('NO') if flag else print('YES')