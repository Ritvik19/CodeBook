def printSpiral(arr, i, j, m, n):
    if i >= m or j >= n:
        return

    for p in range(i, n):
        print(arr[i][p], end=" ")

    for p in range(i+1, m):
        print(arr[p][n - 1], end=" ")

    if (m - 1) != i:
        for p in range(n-2, j-1, -1):
            print(arr[m - 1][p], end=" ")

    if (n - 1) != j:
        for p in range(m-2, i, -1):
            print(arr[p][j], end=" ")

    printSpiral(arr, i + 1, j + 1, m - 1, n - 1)


if __name__ == '__main__':
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    printSpiral(a, 0, 0, 4, 4)
