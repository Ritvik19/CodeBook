for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] % 4 == 0:
            b.append(2)
        elif a[i] % 2 == 0:
            b.append(1)
        else:
            b.append(0)
    total = n*(n+1)//2
    preSum = [0]*3*n
    sum = 0
    preSum[0] += 1
    for i in range(n):
        sum += b[i]
        if sum > 0:
            total -= preSum[sum-1]
        preSum[sum] += 1
    print(total)