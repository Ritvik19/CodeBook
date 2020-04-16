mem={}
pop=[2]
mod=10**9 +7
s=1
for i in range(0,10**5):
	s *= 2
	s = s%mod
	pop.append(s)

for t in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    p = (arr[0]*arr[1])*2
    r = (arr[0]+arr[1])*2
    for i in range(2,N+1):
        p = (p*2 +r*arr[i])%mod
        r += (arr[i]*pop[i])%mod
    print(p)
        