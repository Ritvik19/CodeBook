for t in range(int(input())):
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    cost=[]
    for i in range(m):
        cost.append(0)
    for i in range(n):
        cost[f[i]-1] = cost[f[i]-1]+p[i]
        
    mini = 100000000
    for i in range(m):
        if(cost[i]<mini and ((i+1) in f)==True):
            mini=cost[i]
            
    print(mini)