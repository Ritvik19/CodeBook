def nextbigpos(arr, elem):
    r = len(arr)-1
    l = 0
    ans = len(arr)
    while l <= r:
        mid = (l+r)//2
        if arr[mid] > elem:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return  ans

for t in range(int(input())):
    n = int(input())
    stacks = [0]
    A = list(map(int, input().split()))
    stacks[0] = A[0]

    for i in range(1,n):
        pos = nextbigpos(stacks,A[i])
        if(pos==len(stacks)):
            stacks.insert(pos,A[i])
        elif(pos<len(stacks)):
            stacks[pos]=A[i]

    print(len(stacks), *stacks)
