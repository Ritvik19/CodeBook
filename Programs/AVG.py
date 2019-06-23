for t in range(int(input())):
    N, K, V = map(int, input().split())
    y =(N+K)*V-sum(list(map(int, input().split())))
    if y>0 and y%K==0:
        print(y//K)
    else:
        print(-1)
