for t in range(int(input())):
    n1,n2=input().split()
    l1=list(n1)
    l2=list(n2)
    sum=int(n1)+int(n2)
    for i in range(len(l1)):
        for j in range(len(l2)):
            l1[i],l2[j]=l2[j],l1[i]
            sum1=int("".join(l1))+int("".join(l2))
            if sum1>sum:
                sum=sum1
            l1[i],l2[j]=l2[j],l1[i]
    print(sum)    