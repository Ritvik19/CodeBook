for t in range(int(input())):
    n = int(input())
    matrix = []
    count1 = 0
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        count1 += matrix[-1].count(1)
    bandwidth = 0
    count1 -= n
    for i in range(n-1,0, -1):
        if count1 > 0:
            count1 -= 2 * i
            bandwidth += 1
    print(bandwidth)
