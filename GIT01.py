for t in range(int(input())):
    cakes = []
    cost = [0,0]
    n, m = map(int, input().split())
    for i in range(n):
        cakes.append(input())
    for i in range(n):
        for j in range(m):
            if (i+j)%2 == 0:
                if cakes[i][j] == "R":
                    cost[0] += 5
                else:
                    cost[1] += 3
            else:
                if cakes[i][j] == "G":
                    cost[0] += 3
                else:
                    cost[1] += 5
    print(min(cost))    
