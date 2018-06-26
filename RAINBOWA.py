for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    flag = 0
    for i in range(n//2):
        if A[i] != A[n-i-1]:
            flag = 1
            break
    if set(A) != set([1, 2, 3, 4, 5, 6, 7]):
        flag =1
    if flag == 0:
        print("yes")
    else:
        print('no')
