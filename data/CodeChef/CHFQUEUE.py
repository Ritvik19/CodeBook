n,k = map(int,input().split())
a = list(map(int,input().split()))
chaos=1
st = []
for i in range(n):
    while(len(st)!=0 and a[i]<a[st[-1]]):
        chaos = (chaos * (i - st.pop(-1) + 1))%1000000007
    st.append(i)
print(chaos)