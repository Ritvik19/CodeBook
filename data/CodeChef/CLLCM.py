for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    flag = 'YES'
    for a in A:
        if a % 2 == 0:
            flag = 'NO'
            break
    print(flag)