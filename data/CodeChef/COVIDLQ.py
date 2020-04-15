for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    last1 = None
    flag = 'YES'
    for i in range(n):
        if A[i] == 1:
            if last1 is not None:
                if i- last1 <=5:
                    flag = 'NO'
                    break
                else:
                    last1 = i
            else:
                last1 = i
    print(flag)                