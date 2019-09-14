for i in range(int(input())):
    n = int(input())
    X = [int(e) for e in input().split()]
    Y = [int(e) for e in input().split()]
    sum1 = sum2 = 0
    for j in range(n):
        if j%2 == 0:
            sum1 += X[j]
            sum2 += Y[j]
        else:
            sum1 += Y[j]
            sum2 += X[j]
    print(min(sum1, sum2))
