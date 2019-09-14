for i in range(int(input())):
    m, n = input().split()
    m, n = int(m), int(n)
    A = []
    for j in range(m):
        A.append(input())
    collision = 0
    for j in range(n):
        count = 0
        for k in range(m):
            if A[k][j] == '1':
                count += 1
        collision += count*(count-1)//2
    print(collision)
