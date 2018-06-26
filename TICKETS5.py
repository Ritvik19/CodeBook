def ticket(arr):
    if A[0] == A[1]:
        return "NO"
    n = len(arr)
    i, j = 2, 3
    flag = 0
    while i < n:
        if A[i] != A[i-2]:
            flag = 1
            break
        i += 2
    while j < n:
        if A[j] != A[j-2]:
            flag = 1
            break
        j += 2
    if flag == 0:
        return "YES"
    else:
        return "NO"
for t in range(int(input())):
    A = input()
    print(ticket(A))
