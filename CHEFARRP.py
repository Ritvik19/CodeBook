def arsp(arr):
    sum = 0
    product = 1
    for a in arr:
        sum += a
        product *= a
    if sum == product:
        return 1
    else:
        return 0

for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    count = 0
    for j in range(n):
        for k in range(n-j):
            count += arsp(A[j:j+k+1])
    print(count)
