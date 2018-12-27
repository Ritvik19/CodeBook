for t in range(int(input())):
    n, m =  map(int, input().strip().split())
    arr = []
    for i in range(n):
        arr.append(input())
    count = 0
    for i in range(n-1):
        for j in range(m-1):
            maxSize = min(n-i, m-j)
            for k in range(1, maxSize):
                if arr[i][j] == arr[i][j+k] and arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i+k][j+k]:
                    count += 1
    print(count)
