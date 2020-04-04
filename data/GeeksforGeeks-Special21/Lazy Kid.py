def can_sort(arr,n):
    if n is 1:
        return True
    i = 1
    while(i < n and arr[i-1] < arr[i]):
        i += 1
    if i == n:
        return True
    j = i
    while(arr[j] < arr[j-1]):
        if(i > 1 and arr[j] < arr[i-2]):
            return False
        j += 1
        if j == n:
            return True
    k = j
    if (arr[k] < arr[i-1]):
        return False
    while(k > 1 and k < n):
        if(arr[k] < arr[k-1]):
            return False
        k += 1
    return True

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    arr=[]
    for i in range(n):
        arr.append(int(line[i+1]))
    if(can_sort(arr,n)):
        print('Yes')
    else:
        print('No')
