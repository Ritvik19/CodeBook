for i in range(int(input())):
    n = int(input())
    triangle = []
    for j in range(n):
        triangle.append([int(e) for e in input().split()])
    for a in range(n-2,-1,-1):
        for b in range(len(triangle[a])):
            triangle[a][b] += max(triangle[a+1][b], triangle[a+1][b+1])
    print(triangle[0][0])
