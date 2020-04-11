for t in range(int(input())):
    n, m = map(int, input().split())
    matrix = [[int(e) for e in input().split()] for i in range(n)]
    flag = 0
    if matrix[0][0] == -1:
        matrix[0][0] = 1
    for i in range(1, n):
        if matrix[i][0] == -1:
            matrix[i][0] = matrix[i-1][0]
        elif matrix[i][0] < matrix[i-1][0]:
            flag = 1
            break
    for j in range(1, m):
        if matrix[0][j] == -1:
            matrix[0][j] = matrix[0][j-1]
        elif matrix[0][j] < matrix[0][j-1]:
            flag = 1
            break
    for i in range(1, n):
        if flag == 1:
            break
        for j in range(1, m):
            if matrix[i][j] == -1:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
            elif matrix[i][j] < matrix[i-1][j] or matrix[i][j] < matrix[i][j-1]:
                flag = 1
                break

    if flag == 1:
        print(-1)
    else:
        for i in range(n):
            print(*matrix[i])
