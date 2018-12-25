for t in range(int(input())):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    flag = 'NO'
    for a in A:
        if a >= x:
            flag = 'YES'
            break
    print(flag)
