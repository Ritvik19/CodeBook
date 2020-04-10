for t in range(int(input())):
    n = int(input())
    maxtrace = 0
    mat = []
    for i in range(n):
        mat.append([int(x) for x in input().split()])
    
    for i in range(n):
        x = 0
        curSum = 0
        for j in range(i, n):
            y = j
            curSum+=mat[x][y]
            x+=1
        maxtrace = max(maxtrace, curSum)    
    
    for i in range(n):
        y = 0
        curSum = 0
        for j in range(i, n):
            x = j
            curSum+=mat[x][y]
            y+=1
        maxtrace = max(maxtrace, curSum)
    
    print(maxtrace)     