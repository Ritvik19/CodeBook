def findK(arr, m, n, q):
    k, l = 0, 0
    lis = []
    while k < m and l < n:
        for i in range(l, n):
            lis.append(arr[k][i])
        k += 1
        for i in range(k, m):
            lis.append(arr[i][n-1])
        n -= 1
        if(k < m):
            for i in range(n-1,l-1,-1):
                lis.append(arr[m-1][i])
            m -= 1
        if(l < n):
            for i in range(m-1,k-1,-1):
                lis.append(arr[i][1])
            l += 1
    return lis[q-1]

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findK(matrix, n[0], n[1], n[2]))