for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [A[0]]
    flag = 0
    for i in range(1, n):
        if B[-1] < k:
            flag = i
            break
        B.append(B[-1] + A[i] - k)
    if B[-1] < k and flag == 0:
        flag = n
    if flag != 0:
        print('NO', flag)
    else:
        print('YES')