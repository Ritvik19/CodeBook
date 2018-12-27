n = int(input())
perm = list(map(int, input().split()))
visited = [False]*n
cycles = []
for i in range(n):
    if visited[i] == False:
        cycle = []
        cycle.append(i+1)
        j = perm[i]-1
        visited[i] = True
        while i!=j:
            visited[j] = True
            cycle.append(j+1)
            j = perm[j]-1
        cycle.append(i+1)
        cycles.append(cycle)
print(len(cycles))
for cycle in cycles:
    print(*cycle)
