for t in range(int(input())):
    N, M = map(int,input().split())
    X, Y, s = map(int,input().split())
    if X > 0:
        X_rivers = list(map(int,input().split()))
    if Y > 0:
        Y_rivers = list(map(int,input().split()))

    X_prev = 0
    B_sum = 0
    
    for i in range(X):
        B_sum += (X_rivers[i] - X_prev - 1) // s
        X_prev = X_rivers[i]
    B_sum += (N - X_prev) // s

    Y_prev = 0
    A_sum = 0
    
    for j in range(Y):
        A_sum += ((Y_rivers[j] - Y_prev - 1) // s)
        Y_prev = Y_rivers[j]
    A_sum += (M - Y_prev) // s

    print(A_sum * B_sum)