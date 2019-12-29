for t in range(int(input())):
    n=int(input())
    l=[0]
    for i in range(n-1):
        if l.count(l[i])==1:
            l.append(0)
        else:
            j=i-1
            k=0
            while l[j]!=l[i]:
                k+=1
                j-=1
            l.append(i-j)
    print(l.count(l[n-1]))