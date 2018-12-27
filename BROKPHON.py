for t in range(int(input())):
    n = int(input())
    mis = [0]*n
    msg = list(map(int, input().split()))
    for i in range(1,n):
        if msg[i-1] != msg[i]:
            mis[i-1] = mis[i] = 1
    print(mis.count(1))
