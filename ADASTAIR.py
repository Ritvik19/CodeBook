for t in range(int(input())):
    n, k = map(int, input().split())
    H = list(map(int, input().split()))
    H.insert(0, 0)
    steps_reqd = 0
    for i in range(1, n+1):
        steps_reqd += (H[i]-H[i-1]-1)//k
    print(int(steps_reqd))
