for t in range(int(input())):
    n, k =map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    i = 0
    j = n-1
    flag = 'No'
    while(i<j):
        sums=a[i]+a[j]
        if(sums==k):
            flag = 'Yes'
            break
        elif(sums>k):
            j=j-1
        else:
            i=i+1
    print(flag)
