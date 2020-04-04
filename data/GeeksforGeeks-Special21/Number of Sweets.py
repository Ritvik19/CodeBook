def getDecision(m,n):
    decisions = []
    while m != n:
        if m > n:
            decisions = decisions + (m - n) * ["eat"]
            break
        elif n%2==0:
            n //= 2
            decisions.append("overflow")
        else:
            n += 1
            decisions.append("eat")
    return decisions
    
t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=getDecision(m,n)
    print(*a[::-1])