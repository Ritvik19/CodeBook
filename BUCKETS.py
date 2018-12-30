n, k = map(int, input().split())
balls = []
buck_sum = []
for i in range(n):
    balls.append(list(map(int, input().split())))
    buck_sum.append(sum(balls[-1]))
p = []
for i in range(k):
    p.append(balls[0][i]/buck_sum[0])
for i in range(1, n):
    for j in range(k):
        p[j] = (p[j]*(balls[i][j]+1)/(buck_sum[i]+1)) + ((1-p[j])*(balls[i][j])/(buck_sum[i]+1))
print(*p)
