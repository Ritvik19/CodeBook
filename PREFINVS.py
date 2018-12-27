s=input()
ans=0
n=len(s)
s=s+'0'
for i in range(n):
    if s[n-i]!=s[n-i-1]:
        ans+=1
print(ans)
