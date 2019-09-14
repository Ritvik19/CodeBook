for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    count = n
    temp = 0
    for i in range(1,n):
        if A[i-1] <= A[i]:
            temp += 1
        else:
            count += (temp)*(temp+1)//2
            temp = 0
    if temp != 0:
        count += (temp)*(temp+1)//2
    print(count)
