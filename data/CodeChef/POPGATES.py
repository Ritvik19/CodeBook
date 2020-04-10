for t in range(int(input())):
    n, k = map(int, input().split())
    A = input().split()

    operationCount = 0
    control = 0
    for i in range(n - 1, n - 1 - k, - 1):
        if A[i] == 'H' and not control:
            operationCount += 1
            control = 1
        elif A[i] == 'T' and control:
            operationCount += 1
            control = 0

    count = 0
    if operationCount % 2 == 0:
        for i in range(n - k):
            if A[i] == 'H':
                count += 1
    else:
        for i in range(n - k):
            if A[i] == 'T':
                count += 1
    print(count)